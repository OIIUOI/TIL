# Data Modeling



유저 모델을 유저 모델과 프로필 모델로 나누는 방법을 알려드릴게요. 데이터를 잃지 않으려면 데이터 마이그레이션을 활용해야 하는데요. 과정을 정리하자면 아래와 같습니다.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled.png&name=Untitled.png)

테이터를 잃지 않으려면 모델을 한 번에 나누는 게 아니라 일단 프로필 모델로 데이터를 옮기고, 유저 모델에서 프로필 필드를 지워줘야 합니다. 한 단계씩 살펴볼게요.

## 1. 프로필 모델 생성하기

models.py

```python
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')

    intro = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.email

class Profile(models.Model):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')

    intro = models.CharField(max_length=60, blank=True)

    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

프로필 모델을 정의하고 유저 모델에 있는 프로필 필드를 복사한 다음, `OneToOneField`로 일대일 관계를 형성해 줍니다. (유저 모델에 있는 프로필 필드는 남겨 둡니다.)

그리고 마이그레이션을 해 줍니다.

```python
python manage.py makemigrations --name "profile"
```

```python
python manage.py migrate
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(1).png&name=Untitled+%281%29.png)

## 2. 프로필 데이터 옮기기

이제 프로필 모델이 생겼으니까 데이터를 유저 모델에서 프로필 모델로 옮겨주는 마이그레이션을 만들어 줍니다.

```python
python manage.py makemigrations --empty coplate --name "migrate_profile_data"
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(2).png&name=Untitled+%282%29.png)

이렇게 빈 마이그레이션 파일을 일단 만들어 주고, 아래와 같은 내용을 작성할 수 있습니다.

0008_migrate_profile_data.py

```python
from django.db import migrations

def user_to_profile(apps, schema_editor):
    User = apps.get_model('coplate', 'User')
    Profile = apps.get_model('coplate', 'Profile')
    for user in User.objects.all():
        Profile.objects.create(
            nickname = user.nickname,
            profile_pic = user.profile_pic,
            intro = user.intro,
            user = user,
        )

class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0007_profile'),
    ]

    operations = [
        migrations.RunPython(user_to_profile),
    ]
```

`user_to_profile` 함수는 모든 유저를 돌면서, 각 유저의 프로필 정보를 새로운 프로필 오브젝트에 저장해 줍니다. (프로필을 생성하는 코드가 정확히 이해 안 되셔도 괜찮습니다. 나중에 자세히 배울 거에요!) 프로필 모델의 `user` 필드도 현재 유저로 설정해 주고요. 그리고 `RunPython`을 통해 이 함수를 실행시켜 줍니다.

마이그레이션을 적용하면 데이터가 복사됩니다.

```python
python manage.py migrate
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(3).png&name=Untitled+%283%29.png)

## 3. 유저 모델에서 프로필 필드 지우기

이제 마지막 스탭이 남았는데요. 유저 모델에서 프로필 필드를 지워주는 겁니다.

models.py

```python
class User(AbstractUser):
    def __str__(self):
        return self.email
```

이렇게 프로필 필드를 다 지워주고 `AbstractUser`에 해당하는 필드만 남겨둡니다. 필드를 지우고 다시 한번 `makemigrations`를 하면 되는데요. 실제로 해 보면 어떤 오류가 납니다.

```python
python manage.py makemigrations --name "delete_user_profile_fields"
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(4).png&name=Untitled+%284%29.png)

이건 forms.py 파일 때문에 나는 오류인데요. `forms.py` 파일에는 이런 코드가 있습니다.

forms.py

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'intro',
        ]
        widgets = {
            'intro': forms.Textarea,
        }
```

유저 모델의 `nickname`, `profile_pic`, `intro` 필드를 사용하는데 이런 필드를 방금 유저 모델에서 지워줬기 때문에 오류가 나는 거죠. 필드들을 코멘트 처리해 주면 오류가 나지 않습니다.

forms.py

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            # 'nickname',
            # 'profile_pic',
            # 'intro',
        ]
        widgets = {
            # 'intro': forms.Textarea,
        }
```

당연히 유저 모델을 지금처럼 나누면 폼 말고도 고쳐야 하는 부분이 많은데요. 예를 들어 유저의 닉네임은 이제 `user.nickname` 대신 `user.profile.nickname` 이렇게 접근해야 합니다. 하지만 지금은 그냥 마이그레이션 부분에만 집중하고, 나중에 다시 유저 모델이 하나인 상태로 돌려놓을게요.

다시 마이그레이션을 해 보면 이번엔 잘 될 겁니다.

```python
python manage.py makemigrations --name "delete_user_profile_fields"
```

```python
python manage.py migrate
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(5).png&name=Untitled+%285%29.png)

파이썬 쉘을 켜서 데이터가 잘 옮겨졌는지 확인해 보겠습니다.

```python
python manage.py shell
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(6).png&name=Untitled+%286%29.png)

이렇게 유저 한 명을 가져와서 `nickname`, `profile_pic`, `intro` 필드에 접근하려고 하면 존재하지 않는 필드(속성)이라고 나옵니다.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(7).png&name=Untitled+%287%29.png)

대신 프로필 오브젝트를 돌면서 각 필드를 출력해 보면 프로필 데이터가 잘 나오는 걸 확인하실 수 있습니다.

## 4. 다시 유저 모델 하나로 돌아가기

모델을 성공적으로 나눴는데요. 다시 유저 모델 하나인 상태로 돌아가려면 어떻게 해야 할까요? 이전 마이그레이션으로 돌아가면 되겠죠? 6번 마이그레이션으로 돌아가면 되는데, 아래 커맨드를 실행하면 오류가 납니다.

```python
python manage.py migrate coplate 0006
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(8).png&name=Untitled+%288%29.png)

데이터 마이그레이션을 되돌리는 함수를 정의해 주지 않았기 때문이죠.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(9).png&name=Untitled+%289%29.png)

9번 마이그레이션을 되돌리면 다시 유저 모델에 프로필 필드가 생기는데요, 8번 마이그레이션을 되돌릴 때는 프로필 모델에 있는 정보를 유저 모델로 복사해 줘야 합니다. 그리고 7번 마이그레이션을 취소하면 프로필 모델이 삭제되겠죠?

`0008_migrate_profile_data.py` 파일에 함수를 추가해 주겠습니다.

0008_migrate_profile_data.py

```python
from django.db import migrations

def user_to_profile(apps, schema_editor):
    User = apps.get_model('coplate', 'User')
    Profile = apps.get_model('coplate', 'Profile')
    for user in User.objects.all():
        Profile.objects.create(
            nickname = user.nickname,
            profile_pic = user.profile_pic,
            intro = user.intro,
            user = user,
        )


def profile_to_user(apps, schema_editor):
    User = apps.get_model('coplate', 'User')
    Profile = apps.get_model('coplate', 'Profile')
    for profile in Profile.objects.all():
        user = profile.user
        user.nickname = profile.nickname
        user.profile_pic = profile.profile_pic
        user.intro = profile.intro
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0007_profile'),
    ]

    operations = [
        migrations.RunPython(user_to_profile, profile_to_user),
    ]
```

이번엔 `profile_to_user`라는 함수를 정의해 줬는데요. 각 프로필 오브젝트를 돌면서, 해당하는 유저의 프로필 필드를 채워주는 함수입니다. 이 함수를 `RunPython` operation의 두 번째 파라미터로 넘겨줬고요. 마이그레이션을 적용할 때는 `user_to_profile` 함수가 실행되고, 마이그레이션을 취소할 때는 `profile_to_user` 함수가 실행되는 겁니다.

다시 마이그레이션을 되돌려 봅시다.

```python
python manage.py migrate coplate 0006
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(10).png&name=Untitled+%2810%29.png)

이번에는 마이그레이션이 잘 취소됐습니다. 코드도 다시 되돌려 놓을게요.

models.py

```python
class User(AbstractUser):
    nickname = models.CharField(
        max_length=15, 
        unique=True, 
        null=True,
        validators=[validate_no_special_characters],
        error_messages={'unique': '이미 사용중인 닉네임입니다.'},
    )

    profile_pic = models.ImageField(default='default_profile_pic.jpg', upload_to='profile_pics')

    intro = models.CharField(max_length=60, blank=True)

    def __str__(self):
        return self.email
```

유저 모델을 이렇게 돌려놓고, 프로필 모델은 지워줍니다. 그리고 forms.py 파일에서 코멘트 처리된 부분도 돌려놓으면 되겠죠?

forms.py

```python
class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = [
            'nickname',
            'profile_pic',
            'intro',
        ]
        widgets = {
            'intro': forms.Textarea,
        }
```

그럼 파이썬 쉘로 원상태가 복구됐는지 확인해 보겠습니다.

```python
python manage.py shell
```

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(11).png&name=Untitled+%2811%29.png)

우선 프로필 모델을 임포트하려고 하면 이렇게 오류가 납니다. 프로필 모델이 삭제됐기 때문이죠. 대신 각 유저를 돌며서 유저에 대한 정보를 출력해 보면 프로필 정보가 잘 저장돼있는 걸 확인하실 수 있습니다.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5222&directory=Untitled%20(12).png&name=Untitled+%2812%29.png)

프로필 정보가 다시 프로필 모델에서 유저 모델로 옮겨졌습니다.

이제 마이그레이션 7, 8, 9번은 사용하지 않으니까 마이그레이션 파일들(`0007_profile.py`, `0008_migrate_profile_data.py`, `0009_delete_user_profile_fields.py`)을 지워주시면 됩니다.



## 일대다 관계 (1:N)

```python
class MyModel(models.Model):
    ...    
    field_name = models.ForeignKey(<to_model>, on_delete=<option>, ...)
```

일대다 관계는 가장 흔히 발생하는 관계입니다. 장고에서 일대다 관계를 정의할 때는 `ForeignKey` 필드를 사용하는데요. ‘다’에 해당하는 쪽에 `ForeignKey` 필드를 추가하면 됩니다. 예를 들어 ‘유저’가 ‘리뷰’를 작성한다는 관계는 한 명의 유저가 여러 리뷰를 작성할 수 있고, 하나의 리뷰는 한 명의 작성자가 있기 때문에 일대다 관계인데요. ‘다’ 쪽인 `Review` 모델에 `ForeignKey` 필드를 추가해 주면 됩니다.

```python
class Review(models.Model):
    ...
    author = models.ForeignKey(User, on_delete=models.CASCADE)
```

자주 사용하는 `on_delete` 옵션은 세 가지가 있습니다.

1. `models.CASCADE`: 특정 유저가 삭제되면 그 유저를 참조하고 있는 리뷰도 모두 삭제됩니다.
2. `models.PROTECT`: 유저를 참조하고 있는 리뷰가 하나라도 있으면 유저를 삭제하지 못하게 합니다.
3. `models.SET_NULL`: 특정 유저를 삭제하면, 그 유저를 참조하고 있던 리뷰들의 `author` 값이 모두 `NULL`로 설정됩니다. (사용하려면 `ForeignKey` 필드에 `null=True`로 설정해 줘야 합니다.)

## 일대일 관계 (1:1)

```python
class MyModel(models.Model):
    ...
    field_name = models.OneToOneField(<to_model>, on_delete=<option>, ...)
```

장고에서 일대일 관계를 정의할 때는 `OneToOneField`를 사용합니다. 일대일 관계를 보면 한 모델이 다른 모델에 ‘속해’있는 경우가 많은데요.

- 유저-프로필 관계에서는 프로필이 유저에게 속해있습니다.
- 사람-여권 관계에서는 여권이 사람에게 속해있습니다.
- 레스토랑-장소 관계에서는 레스토랑이 장소에 속해있습니다.

이런 경우 속해있는 쪽 (프로필, 여권, 레스토랑)에 `OneToOneField`를 추가하면 됩니다. 하지만 명백히 한쪽이 다른 쪽에 속해있지 않을 경우에는 어떤 모델에 `OneToOneField`를 추가하든지 상관없습니다.

유저-프로필 관계의 경우 아래와 같이 관계를 형성할 수 있겠죠?

```python
class Profile(models.Model):
    ...
    user = models.OneToOneField(User, on_delete=models.CASCADE)
```

## 다대다 관계 (M:N)

```python
class MyModel(models.Model):
    ...    
    field_name = models.ManyToManyField(<to_model>, ...)
```

장고에서 다대다 관계를 정의할 때는 `ManyToManyField`를 사용합니다. `ManyToManyField`는 여러 오브젝트를 가리키기 때문에 `on_delete` 옵션이 없습니다 (’참조하고 있는 오브젝트’를 정의할 수가 없습니다). `ManyToManyField`는 어느 모델에 추가하든 크게 상관없습니다. 예를 들어 어떤 온라인 쇼핑몰의 물품(`Product`)은 여러 컬렉션`Collection`)에 있을 수 있고, 컬렉션은 여러 물품을 포함할 수 있는데요. 물품-컬렉션 관계는 다대다 관계고 아래와 같이 정의할 수 있습니다.

```python
class Product(models.Model):
    ...

class Collection(models.Model):
    ...
    products = models.ManyToManyField(Product)
```

그리고 `ManyToManyField`는 `null` 옵션이 없다는 점도 기억해 주세요. `ManyToManyField`는 처음에는 비어있고, 필드에 오브젝트를 하나씩 추가하는 형태이기 때문에 필드가 항상 비어있을 수 있다고 가정합니다.

## 자신과 관계를 맺을 때는?

모델 자신과 관계를 맺을 때도 있는데요. 예를 들어,

- 유저가 유저를 팔로우 하는 경우 (다대다)
- 두 유저가 친구가 되는 경우 (다대다)
- 댓글에 댓글을 다는 경우 (일대다)

이런 경우에는 관계를 맺을 모델 `<to_model>`에 `'self'`를 넣어줍니다.

이 중에서도 다대다 관계는 조금 특별한데요. 관계가 대칭일 수도 있고, 비대칭 관계일 수도 있기 때문입니다. 유저 A가 B를 팔로우 한다고 B가 A를 팔로우 하는 건 아니겠죠? 그렇기 때문에 팔로우는 비대칭 관계입니다. 하지만 A와 B가 친구이면 B와 A도 당연히 친구이기 때문에 친구 관계는 대칭 관계인 거죠. 대칭 여부는 `symmetrical` 옵션을 통해 전달해 줍니다.

```python
# 팔로우
class User(AbstractUser):
    ...
    following = models.ManyToManyField('self', symmetrical=False)

# 친구
class User(AbstractUser):
    ...
    friends = models.ManyToManyField('self', symmetrical=True)

# 댓글
class Comment(models.Model):
    ...
    parent_comment = models.ForeignKey('self') # symmetrical은 다대다 관계에서만 사용합니다.
```

## 제네릭 관계

```python
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey


class MyModel(models.Model):
    ...
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    content_object = GenericForeignKey('content_type', 'object_id')
```

특정 모델 하나랑 관계를 맺는 것이 아니고 여러 모델과 관계 일반적인 관계를 맺고 싶을 때는 제네릭(Generic) 관계를 사용합니다. ‘좋아요’는 리뷰에도 누를 수 있고, 댓글에도 누를 수 있고, 나중에는 어쩌면 다른 오브젝트에도 누를 수 있겠죠? 그래서 좋아요와 좋아요 대상 사이에는 제네릭 관계를 사용합니다.

제네릭 관계는 `ContentType`과 오브젝트의 id를 저장하는데요. 모델 종류와 오브젝트의 id를 저장하면 어떤 모델과도 관계를 형성할 수 있겠죠?

매번 `ContentType`과 오브젝트 id를 사용해서 연결된 오브젝트에 접근하려면 너무 번거롭기 때문에 `GenericForeignKey`라는 걸 사용할 수 있습니다. 일반 `ForeignKey`처럼 필드를 통해서 연결된 오브젝트에 접근할 수 있는 거죠. `GenericForeignKey`를 생성할 때 `ContentType` 필드와 오브젝트 id 필드를 파라미터로 넘겨줘야 하는데, `content_type`과 `object_id`라는 이름을 사용했다면 이 부분을 비워놔도 됩니다.

예:

```python
class Like(models.Model):
    ...
    content_type = models.ForeignKey(ContentType, on_delete=models.CASCADE)

    object_id = models.PositiveIntegerField()

    liked_object = GenericForeignKey()
```



## Meta Option

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-18-01-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-18-22-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-18-53-image.png)

```python
class Review(models.Model):
    ...
    dt_create = models.DateTimeField(auto_now_add=True)
    ...
    class Meta:
        ordering = ['-dt_created']
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-21-02-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-21-28-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-21-44-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-23-07-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-23-21-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-23-44-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-24-08-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-24-23-image.png)



# ModelAdmin

**admin.py**

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-30-41-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-32-34-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-32-52-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-33-28-image.png)



## Inline

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-34-01-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-34-15-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-34-37-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-34-59-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-18-35-19-image.png)
