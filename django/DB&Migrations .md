![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-04-44-07-image.png)

# None-relational DB & Relational DB

‘릴레이션(Relation)’은 ‘테이블’을 뜻하는데요. 릴레이셔널 데이터베이스는 데이터를 테이블에 저장하고 논 릴레이셔널(non-relational) 데이터베이스는 테이블에 저장하지 않습니다. 그럼 논 릴레이셔널 데이터베이스는 데이터를 어떻게 저장할까요?

사실 하나의 방법이 정해져있지는 않는데요. 가장 많이 사용하는 방법 중 하나는 문서(document) 형태로 데이터를 저장하는 겁니다. 데이터를 문서 형태로 저장하는 데이터베이스를 document-oriented database라고도 부릅니다. 문서도 다양한 형식이 있는데 그중에 JSON 형식이 가장 보편적입니다. 우리가 이전에 봤던 리뷰를 테이블에 저장하지 않고 JSON 문서 형태로 저장한다면 아래와 같습니다.

```json
{
    "id": 1,
    "title": "코스버거에 다녀오다!",
    "restaurant_name": "코스버거",
    "restaurant_link": "https://place.map.kakao.com/m/698951184",
    "rating": 4,
    "image1":, "review_pics/burger.png"
    "image2": "", 
    "image3": "", 
    "content": "버거랑 감자튀김 다 맛있었어요! 콜라는 역시 제로콕!",
    "dt_created": "2021-12-17T08:25:14.111Z", 
    "dt_updated": "2021-12-18T13:53:40.521Z",
    "author": 5,
}
```

JSON 형식은 딕셔너리와 비슷한데요. Key는 필드 이름이고 value는 필드값이 되는 거죠. `author` 필드의 값은 작성자 id입니다. 문서 형태의 장점은 데이터 형식을 자유롭게 정할 수 있다는 건데요. 예를 들어 `author` key의 값에 더 많은 정보를 저장할 수도 있습니다.

```json
{
    "id": 1,
    "title": "코스버거에 다녀오다!",
    "restaurant_name": "코스버거",
    "restaurant_link": "https://place.map.kakao.com/m/698951184",
    "rating": 4,
    "image1":, "review_pics/burger.png"
    "image2": "", 
    "image3": "", 
    "content": "버거랑 감자튀김 다 맛있었어요! 콜라는 역시 제로콕!",
    "dt_created": "2021-12-17T08:25:14.111Z", 
    "dt_updated": "2021-12-18T13:53:40.521Z",
    "author": {
        "id": 5,
        "email", "joy@example.com",
        "nickname": "조이",
        "profile_pic": "profile_pics/63b9ab1491ca84853ac6cf8b91fc5ce8b966361124882af6c70d8d7184005ea1.jpeg",
    },
}
```

리뷰를 보여줄 때는 주로 작성자의 닉네임과 프로필 사진도 같이 보여주겠죠? 위처럼 데이터를 저장하면 이 정보를 한 문서에서 바로 가져올 수 있습니다. 반면 테이블 구조를 생각해 보면 작성자의 id를 가지고 유저 테이블로 가서, id에 해당하는 유저를 찾고, 거기서 닉네임과 프로필 사진을 가져와야 합니다.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5198&directory=ch1_01.png&name=ch1_01.png)

문서 형태가 테이블 형태보다 필요한 정보를 더 빨리 가져올 수 있겠죠?

하지만 위에서 본 것처럼 리뷰 데이터에 유저 정보까지 저장하면 안 좋은 점도 있습니다. 바로 데이터가 중복된다는 건데요. (문서) 데이터베이스 어딘가에는 유저도 저장돼있을 겁니다.

```json
{
    "id": 5,
    "password": "...",
    "last_login": "2021-12-15T07:01:56.949Z",
    "is_superuser": false,
    "email", "joy@example.com",
    ...
    "nickname": "조이",
    "profile_pic": "profile_pics/63b9ab1491ca84853ac6cf8b91fc5ce8b966361124882af6c70d8d7184005ea1.jpeg",
    "intro": "",
}
```

이렇게 말이죠. 여기에도 유저 정보가 있고, 리뷰에도 유저 정보가 있는데, 예를 들어 닉네임을 수정하려면 유저 정보가 있는 모든 곳을 찾아서 잘 바꿔줘야 합니다. Relational 데이터베이스는 이렇게 데이터가 중복되는 걸 보통 허용하지 않고 특정 데이터는 한 곳에서만 관리하기 때문에 데이터의 일관성을 보장할 수 있습니다.

릴레이셔널 데이터베이스는 SQLite3, MySQL, PostgreSQL 같은 프로그램을 통해서 사용할 수 있다고 했는데요. 논 릴레이셔널 데이터베이스에도 여러 데이터베이스 프로그램이 있습니다. 대표적으로 MongoDB, Cassandra 같은 것들이 있는데 아마 들어보셨을 수도 있을 겁니다.

그리고 릴레이셔널 데이터베이스는 모두 SQL을 사용한다는 공통점이 있었는데요. 논 릴레이셔널 데이터베이스는 SQL을 사용하지 않기 때문에 논 릴레이셔널 데이터베이스를 NoSQL(non-SQL) 데이터베이스라고 자주 부릅니다. NoSQL 데이터베이스들이 공통적으로 사용하는 하나의 언어는 없고 데이터베이스 프로그램마다 다릅니다. 이 [링크](https://docs.mongodb.com/manual/tutorial/query-documents/)에서는 MongoDB에서 데이터를 조회하는 예시를 보실 수 있습니다.

이번 레슨에서는 논 릴레이셔널(non-relational), 또는 NoSQL 데이터베이스에 대해 알아봤는데요. 릴레이셔널 데이터베이스의 장점은 데이터의 일관성, 그리고 SQL을 통한 복잡한 데이터 조회 기능이라면 NoSQL 데이터베이스의 장점은 퍼포먼스(데이터 조회 속도)와 데이터 형식의 자유도입니다. 그래서 NoSQL 데이터베이스는 ‘빅 데이터’ 또는 구조가 없는 데이터(unstructured data), 예를 들면 오디오, 비디오 데이터를 저장할 때 많이 사용합니다. 하지만 이런 경우가 아니라면 NoSQL 데이터베이스를 사용해도 데이터 조회 속도의 차이는 미세하고 오히려 데이터의 일관성을 관리하기가 굉장히 어려워지기 때문에 릴레이셔널 데이터베이스를 많이 사용합니다. 우리도 이번 토픽에서 릴레이셔널 데이터베이스를 사용할 거고요.

# Migrations

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-09-23-image.png)

```bash
python manage.py makemigrations
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-10-19-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-10-35-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-10-55-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-11-10-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-12-00-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-12-19-image.png)

```bash
python manage.py migrate
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-13-46-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-14-09-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-14-21-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-14-50-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-15-08-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-05-15-21-image.png)

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-06-26-22-image.png)

```bash
python manage.py showmigrations
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-06-27-43-image.png)

```bash
python manage.py showmigrations app_name
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-06-35-13-image.png)

```python
python manage.py showmigrations app_name 0006
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-06-40-52-image.png)

```python
python manage.py makemigrations app_name
```

![](C:\Users\jin47\AppData\Roaming\marktext\images\2023-04-25-06-39-10-image.png)

```python
python manage.py makemigrations --name "nameyouwant"
```



![](assets/2023-04-25-06-50-18-image.png)

![](assets/2023-04-25-06-50-32-image.png)

```python
python manage.py showmigrations app_name 0004
```



<img src="assets/2023-04-25-06-53-10-image.png" title="" alt="" width="224"><img src="assets/2023-04-25-06-53-29-image.png" title="" alt="" width="372">

<img title="" src="assets/2023-04-25-06-54-07-image.png" alt="" width="442">

<img src="assets/2023-04-25-06-57-34-image.png" title="" alt="" width="473">

<img title="" src="assets/2023-04-25-06-56-01-image.png" alt="" width="495">

![](assets/2023-04-25-06-58-06-image.png)

![](assets/2023-04-25-06-58-21-image.png)



![](assets/2023-04-25-06-59-18-image.png)

```python
python manage.py showmigrations app_name zero
```



## Migrations dependency

<img src="assets/2023-04-25-07-02-32-image.png" title="" alt="" width="228"><img title="" src="assets/2023-04-25-07-02-48-image.png" alt="" width="396">

![](assets/2023-04-25-07-03-32-image.png) **=** ![](assets/2023-04-25-07-04-12-image.png)

![](assets/2023-04-25-07-04-47-image.png)



![](assets/2023-04-25-07-06-00-image.png)![](assets/2023-04-25-07-06-17-image.png)

![](assets/2023-04-25-07-06-51-image.png)

마이그레이션 간의 디펜던시를 그림으로 그린 걸 **디펜던시 그래프**라고 하는데요.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5209&directory=Untitled%20(6).png&name=Untitled+%286%29.png)

디펜던시 그래프를 보면 어떤 디펜던시가 있는지, 마이그레이션이 어떤 순서로 적용되거나 취소되는지 파악할 수 있습니다.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5209&directory=gif3.gif&name=gif3.gif)

예를 들어 coplate 1번을 처음 적용한다면, 디펜던시를 먼저 적용해 주고 coplate 1번을 적용하고요.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5209&directory=gif4.gif&name=gif4.gif)

coplate 1번을 취소한다면 coplate 1번에 의존하고 있는 애들을 먼저 취소한 다음 coplate 1번을 취소해 줍니다.



## 데이터 마이그레이션이란?

마이그레이션은 주로 테이블 구조를 짜는 데에 사용하지만 데이터를 다루는 데에도 사용합니다. 마이그레이션을 통해 데이터를 삽입하거나 수정하거나 삭제하는 거죠. 이렇게 데이터를 다루는 마이그레이션을 데이터 마이그레이션이라고 하는데요. 데이터 마이그레이션은 주로 테이블 구조에 맞게 데이터를 옮겨줘야 할 때 사용합니다. 그냥 테이블에 데이터를 넣을 때, 예를 들어 테이블을 만들고 나서 테이블에 초기 데이터를 넣을 때도 데이터 마이그레이션을 사용할 수는 있지만, 그럴 때는 장고 fixture 같은 다른 수단을 사용하는 게 더 편할 겁니다.

### 데이터 마이그레이션을 사용하기에 좋은 예시

`User` 모델에 이메일 도메인을 저장하는 `email_domain` 컬럼을 만든다고 할게요.

![](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5216&directory=Untitled%20(21).png&name=Untitled+%2821%29.png)

그러면 데이터 마이그레이션을 사용해서 새로 생성된 `email_domain` 컬럼에 값을 채워넣어 줄 수 있습니다. 데이터 마이그레이션 과정을 복습해 보면서 어떻게 하는지 살펴볼게요.

### 데이터 마이그레이션 과정

models.py

```python
class User(AbstractUser):
    ...

    email_domain = models.CharField(max_length=30, null=True)
```

이렇게 `email_domain` 필드를 추가하고 마이그레이션을 했다고 할게요. (마이그레이션 0006_user_email_domain.py라고 하겠습니다.) 이 컬럼을 채워주는 새로운 마이그레이션을 만들어 볼 겁니다.

먼저 비어있는 마이그레이션 파일을 만들어 줍니다.

```python
python manage.py makemigrations --empty coplate --name "populate_email_domain"
```

`--empty` 옵션을 사용해서 비어있는 마이그레이션 파일을 만들 수 있습니다.

0007_populate_email_domain.py

```python
from django.db import migrations

class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0006_user_email_domain'),
    ]

    operations = [
    ]
```

이런 파일이 생성됩니다. 이제 이 파일을 채워 넣으면 되는데요. 이렇게 채워 넣을 수 있습니다.

0007_populate_email_domain.py

```python
from django.db import migrations

def save_email_domain(apps, schema_editor):
    User = apps.get_model('coplate', 'User')
    for user in User.objects.all():
        user.email_domain = user.email.split('@')[1]
        user.save()

class Migration(migrations.Migration):

    dependencies = [
        ('coplate', '0006_user_email_domain'),
    ]

    operations = [
        migrations.RunPython(save_email_domain, migrations.RunPython.noop),
    ]
```

`save_email_domain`이 `email_domain` 컬럼에 데이터를 채워 넣는 함수인데요, 데이터 마이그레이션 함수는 보통 `apps`와 `schema_editor`를 파라미터로 받습니다. 그리고 모델을 가져올 때는 꼭 `apps.get_model('coplate', 'User')` 이런 식으로 가져온다는 것 기억해 주세요. models.py 파일에 있는 모델은 지금 어떤 상태일지 모르기 때문에 마이그레이션 히스토리를 보고 현시점에 맞는 유저 모델을 가져오는 겁니다.

`operations` 부분을 보시면 `RunPython`이라는 게 있는데요. 말 그대로 파이썬 코드를 실행하는 operation(작업)입니다. 마이그레이션을 적용할 때는 `save_email_domain` 함수를 실행하고, 마이그레이션을 취소할 때는 `migrations.RunPython.noop`이라는 걸 실행하는데, 이건 아무것도 안 하는 함수입니다. `RunPython`에 두 번째 파라미터를 넘거주지 않으면 마이그레이션을 되돌릴 수 없기 때문에 아무것도 안 하는 함수라도 넘겨준 겁니다. 어차피 0006번을 취소하면 `email_domain` 컬럼이 삭제되기 때문에 마이그레이션을 되돌릴 때는 아무것도 할 필요가 없겠죠?

```python
python manage.py migrate coplate 0007
```

이렇게 하면 `email_domain` 컬럼이 생기고 안에 데이터가 채워지고,

```python
python manage.py migrate coplate 0005
```

이렇게 하면 `email_domain` 컬럼이 삭제됩니다.
