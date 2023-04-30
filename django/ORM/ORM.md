# ORM

## Shell

```shell
python manage.py shell
```

## 데이터 추가하기 (Create)

데이터를 추가하기 위해서는 import를 이용해서 먼저 사용할 Model을 불러 와야 합니다.

```python
from {app_name}.models import {model}
```

그 다음 불러온 모델을 이용해서 데이터를 추가하면 되는데 여기에 두가지 방법이 있습니다.

### Create

먼저 Create는 데이터 객체를 생성하고 데이터베이스에 반영하는 과정을 한 번에 할 수 있습니다. 생성과 동시에 실제 데이터베이스에 반영이 되는거죠.

```python
data_model = {model}.objects.create( {field_name}=value, ... )
# example
# food = Food.objects.create(price=10000)
```

### Save

save를 이용하면 데이터 객체를 생성하는 타이밍과 실제로 데이터베이스에 반영하는 과정을 
분리할 수 있습니다. 아래 코드는 위에서 사용한 Create와 똑같은 기능을 수행합니다.

```python
data_model = {model}( {field_name}=value, ... )
data_model.save()
# example 
# food = Food(price=10000)
#   food.save()
```

## 데이터 조회하기 (Read)

데이터를 데이터베이스로 부터 읽어오는 것은 Django Model Manager인 objects를 통해서 할 수 있습니다. 읽어 온 데이터는 Queryset 이라고 하는 데이터 결과 객체에 들어가며 Queryset은 파이썬의 리스트처럼 사용할 수 있습니다.

### 모든 데이터 조회하기

데이터 모델의 모든 데이터를 가져오기 위해서는 all()을 사용합니다.

```python
data = {model}.obejcts.all()
```

### 하나의 데이터 조회하기

하나의 데이터를 가져오기 위해서는 **get()**을 사용합니다. 이때 특정 필드를 전달 인자로 넣어 데이터를 가져오거나 아래에서 설명하는 조건 키워드를 함께 사용할 수 있습니다. get은 하나의 데이터를 조회할 때 라는것을 기억해주세요. 만약 get을 사용했을때 조회 결과가 여러개라면 에러를 내게 됩니다.

```python
data = {model}.objects.get(field=value)
```

### 조건에 맞는 여러 데이터 조회하기

조건에 맞는 여러 데이터를 조회할 때는 **filter()**를 사용합니다. 필드를 전달 인자로 넣어 해당 필드 조건에 해당하는 모든 데이터를 가져오거나 아래에서 설명하는 조건 키워드를 함께 사용할 수 있습니다.

```python
data = {model}.objects.filter(field=value)
```

### 정렬해서 데이터 조회하기

데이터를 특정 필드에 따라 정렬해서 조회하고 싶을 때는 **order_by()**를 사용합니다. 이때 두 개 이상의 필드를 함께 사용해서 정렬할 수 있으며 **'-'**를 사용해서 내림차순으로 정렬할 수 있습니다.

```python
data = {model}.objects.order_by('field_1', '-field_2')
# field_1을 기준으로 오름차순으로 정렬하고 
# 그 결과를 다시 field_2를 기준으로 내림차순으로 정렬합니다.
```

### 데이터의 개수 세기

데이터의 개수를 셀 때는 **count()**를 사용합니다.

```python
rows = {model}.objects.count()
```

### 특정 조건을 제외한 데이터 조회하기

특정 조건을 제외한 데이터를 조회하고 싶을 때는 **exclude()**를 사용해 보세요.

```python
data = {model}.objects.exclude(field=value)
# 특정 field가 value인 데이터를 제외한 모든 데이터를 조회합니다.
```

### 체인으로 연결해서 조회하기

여러가지 데이터 조회를 체인처럼 연결해서 사용할 수 있습니다. 아래에서 배우는 조건 키워드도 모두 한 번에 엮어서 사용할 수 있습니다.

```python
data = {model}.objects.filter(price=10000).order_by('name')
# 가격(price)이 10,000원인 데이터를 이름(name)으로 정렬해서 조회합니다.
```

```python
data = {model}.objects.filter(price=10000)
data = data.order_by('name')
# 이렇게 적어도 위와 똑같은 명령을 수행합니다. 
```

그러면 체인으로 엮는 방법과 풀어서 아래처럼 쓰는 방법 중에 무엇이 더 좋을까요? 사실 둘 중 어떤 방법을 사용해도 괜찮지만 아래처럼 여러번 나누어 사용하는 것을 추천합니다. Django의 ORM은 매우 강력해서 여러분이 생각하는 거의 대부분의 형태로 구현할 수 이게 해줍니다. 하지만 그러한 강력함 때문에 작성할 때 책임이 따릅니다. 모든 코드는 명확하게 작성할 수록 좋은데 ORM을 통해서 데이터 조회를 하다보면 복잡한 조회를 요구할 때가 많습니다. 복잡한 쿼리를 작성하다보면 체인으로 연결해서 한줄에 작성하는 경우가 많은데 이렇게 복잡한 조회 과정을 하나의 체인으로 묶는것을 지양해야합니다. 그 이유는 첫째로, 체인으로 한 번에 묶는다고 더 빠른 속도로 동작하지 않기 때문이고 두번째로 코드의 가독성이 매우 떨어지기 때문입니다. Django의 ORM은 기본적으로 지연연산(lazy evaluation)으로 이루어집니다. 지연 연산은 우리가 정말로 연산이 필요하기 전까지 연산을 수행하지 않는 것을 말합니다. 그러니까 한 줄로 적는 것과 여러줄 나누어 적는 것이 모두 똑같이 동작한다는 것이죠. 그렇기 때문에 우리는 한 줄로 복잡한 연산을 작성할 필요가 없이 여러 줄로 나누어 적을 수 있고 이런 방식은 코드의 가독성을 매우 높여줍니다.

## 필드 조건 옵션 (Field Lookups)

Queryset 연산을 할 때 사용할 수 있는 여러 필드 조건 옵션입니다. 필드명 뒤에 `__` 를 쓰고 사용할 옵션 인자를 적어 주면 됩니다. 아래의 조건 옵션 말고도 더 많은 옵션 들이 있습니다. 아래의 공식 문서를 참고하세요. [필드 조건 옵션 공식문서 바로 가기](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups)

| lookup       | 설명                                             | 예시                                                                                                                                                        |
| ------------ | ---------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------- |
| __contains   | 대소문자를 구분하여 문자열 포함 여부 확인                        | Post.objects.get(title__contains='Codeit')                                                                                                                |
| __icontains  | 대소문자를 구분하지 않고 문자열 포함 여부 확인                     | Post.objects.get(title__icontains='Codeit')                                                                                                               |
| __in         | 반복 가능한 객체 안에서의 포함 여부를 확인                       | Post.objects.filter(id__in=[1, 2, 3])                                                                                                                     |
| __gt         | 초과 여부 확인 (Greater than)                        | Post.objects.filter(id__gt=4)                                                                                                                             |
| __gte        | 이상 여부 확인 (Greater than or equal to)            | Post.objects.get(id__gte=4)                                                                                                                               |
| __lt         | 미만 여부 확인 (Less than)                           | Post.objects.get(id__lt=4)                                                                                                                                |
| __lte        | 이하 여부 확인 (Less than or equal to)               | Post.objects.get(id__lte=4)                                                                                                                               |
| __startswith | 대소문자를 구분하여 해당 문자열로 시작하는지 여부 확인                 | Post.objects.filter(title__startswith='code')                                                                                                             |
| __istatswith | 대소문자를 구분하지 않고 해당 문자열로 시작하지 여부 확인               | Post.objects.filter(context__istartswith='code')                                                                                                          |
| __endswith   | 대소문자를 구분하여 해당 문자열로 끝나는지 여부 확인                  | Post.objects.filter(title__endswith='code')                                                                                                               |
| __iendswith  | 대소문자를 구분하지 않고 해당 문자열로 끝나는지 여부 확인               | Post.objects.filter(title_iendswith='code')                                                                                                               |
| __range      | range로 제시하는 범위 내에 포함되는지 확인<br>(시작과 끝 범위 모두 포함) | import datetime start_date = datetime.date(2021, 1, 1) end_date = datetime.date(2021, 3, 1) Post.objects.filter(dt_created__range=(start_date, end_date)) |
| __isnull     | 해당 필드가 Null 인지 여부를 확인                          | Post.objects.filter(context__isnull=True)                                                                                                                 |

## 데이터 수정하기

데이터를 수정하기 위해서는 수정할 데이터 객체를 가져온 다음 원하는 필드를 수정하고 save()를 호출하여 데이터베이스에 반영하면 됩니다.

```python
data = {model}.objects.get(id=1)
data.name = 'Woojae'
data.save()
```

## 데이터 삭제하기

데이터를 삭제하기 위해서는 삭제할 데이터 객체를 가져온 다음 delete()를 호출하면 됩니다.

```python
data = {model}.objects.get(id=3)
data.delete()
```

모델에 대해 더 많은 내용이 궁금하다면 아래 Django 문서를 참고하세요! [Making queries | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/queries/##) 데이터 추가하기 (Create)

데이터를 추가하기 위해서는 import를 이용해서 먼저 사용할 Model을 불러 와야 합니다.

```python
from {app_name}.models import {model}
```

그 다음 불러온 모델을 이용해서 데이터를 추가하면 되는데 여기에 두가지 방법이 있습니다.

### Create

먼저 Create는 데이터 객체를 생성하고 데이터베이스에 반영하는 과정을 한 번에 할 수 있습니다. 생성과 동시에 실제 데이터베이스에 반영이 되는거죠.

```python
data_model = {model}.objects.create( {field_name}=value, ... )
# example
# food = Food.objects.create(price=10000)
```

### Save

save를 이용하면 데이터 객체를 생성하는 타이밍과 실제로 데이터베이스에 반영하는 과정을 
분리할 수 있습니다. 아래 코드는 위에서 사용한 Create와 똑같은 기능을 수행합니다.

```python
data_model = {model}( {field_name}=value, ... )
data_model.save()
# example 
# food = Food(price=10000)
#   food.save()
```

## 데이터 조회하기 (Read)

데이터를 데이터베이스로 부터 읽어오는 것은 Django Model Manager인 objects를 통해서 할 수 있습니다. 읽어 온 데이터는 Queryset 이라고 하는 데이터 결과 객체에 들어가며 Queryset은 파이썬의 리스트처럼 사용할 수 있습니다.

### 모든 데이터 조회하기

데이터 모델의 모든 데이터를 가져오기 위해서는 all()을 사용합니다.

```python
data = {model}.obejcts.all()
```

### 하나의 데이터 조회하기

하나의 데이터를 가져오기 위해서는 **get()**을 사용합니다. 이때 특정 필드를 전달 인자로 넣어 데이터를 가져오거나 아래에서 설명하는 조건 키워드를 함께 사용할 수 있습니다. get은 하나의 데이터를 조회할 때 라는것을 기억해주세요. 만약 get을 사용했을때 조회 결과가 여러개라면 에러를 내게 됩니다.

```python
data = {model}.objects.get(field=value)
```

### 조건에 맞는 여러 데이터 조회하기

조건에 맞는 여러 데이터를 조회할 때는 **filter()**를 사용합니다. 필드를 전달 인자로 넣어 해당 필드 조건에 해당하는 모든 데이터를 가져오거나 아래에서 설명하는 조건 키워드를 함께 사용할 수 있습니다.

```python
data = {model}.objects.filter(field=value)
```

### 정렬해서 데이터 조회하기

데이터를 특정 필드에 따라 정렬해서 조회하고 싶을 때는 **order_by()**를 사용합니다. 이때 두 개 이상의 필드를 함께 사용해서 정렬할 수 있으며 **'-'**를 사용해서 내림차순으로 정렬할 수 있습니다.

```python
data = {model}.objects.order_by('field_1', '-field_2')
# field_1을 기준으로 오름차순으로 정렬하고 
# 그 결과를 다시 field_2를 기준으로 내림차순으로 정렬합니다.
```

### 데이터의 개수 세기

데이터의 개수를 셀 때는 **count()**를 사용합니다.

```python
rows = {model}.objects.count()
```

### 특정 조건을 제외한 데이터 조회하기

특정 조건을 제외한 데이터를 조회하고 싶을 때는 **exclude()**를 사용해 보세요.

```python
data = {model}.objects.exclude(field=value)
# 특정 field가 value인 데이터를 제외한 모든 데이터를 조회합니다.
```

### 체인으로 연결해서 조회하기

여러가지 데이터 조회를 체인처럼 연결해서 사용할 수 있습니다. 아래에서 배우는 조건 키워드도 모두 한 번에 엮어서 사용할 수 있습니다.

```python
data = {model}.objects.filter(price=10000).order_by('name')
# 가격(price)이 10,000원인 데이터를 이름(name)으로 정렬해서 조회합니다.
```

```python
data = {model}.objects.filter(price=10000)
data = data.order_by('name')
# 이렇게 적어도 위와 똑같은 명령을 수행합니다. 
```

그러면 체인으로 엮는 방법과 풀어서 아래처럼 쓰는 방법 중에 무엇이 더 좋을까요? 사실 둘 중 어떤 방법을 사용해도 괜찮지만 아래처럼 여러번 나누어 사용하는 것을 추천합니다. Django의 ORM은 매우 강력해서 여러분이 생각하는 거의 대부분의 형태로 구현할 수 이게 해줍니다. 하지만 그러한 강력함 때문에 작성할 때 책임이 따릅니다. 모든 코드는 명확하게 작성할 수록 좋은데 ORM을 통해서 데이터 조회를 하다보면 복잡한 조회를 요구할 때가 많습니다. 복잡한 쿼리를 작성하다보면 체인으로 연결해서 한줄에 작성하는 경우가 많은데 이렇게 복잡한 조회 과정을 하나의 체인으로 묶는것을 지양해야합니다. 그 이유는 첫째로, 체인으로 한 번에 묶는다고 더 빠른 속도로 동작하지 않기 때문이고 두번째로 코드의 가독성이 매우 떨어지기 때문입니다. Django의 ORM은 기본적으로 지연연산(lazy evaluation)으로 이루어집니다. 지연 연산은 우리가 정말로 연산이 필요하기 전까지 연산을 수행하지 않는 것을 말합니다. 그러니까 한 줄로 적는 것과 여러줄 나누어 적는 것이 모두 똑같이 동작한다는 것이죠. 그렇기 때문에 우리는 한 줄로 복잡한 연산을 작성할 필요가 없이 여러 줄로 나누어 적을 수 있고 이런 방식은 코드의 가독성을 매우 높여줍니다.

### 조건 키워드

모든 데이터 조회는 조건 키워드를 함께 사용하여 조회할 수 있으며 **{field_name}__{keyword}={condition}** 형태로 사용합니다. 아래는 몇가지 조건 키워드의 예시입니다.

**__exact, __iexact**

__exact는 대소문자를 구분해서 조건과 정확히 일치 하는지를 체크하며
__iexact는 대소문자를 구분 하지 않고 일치하는 지를 체크합니다.

```python
data = {model}.objects.filter(name__iexact='chicken')
# 음식의 이름(name)이 'chicken'인 데이터를 모두 조회합니다.
# 단, 대소문자를 구분하지 않습니다.
```

**__contains, __icontains**

지정한 문자열을 포함 하는지를 체크합니다. 
마찬가지로 __icontains는 대소문자를 구분하지 않고 체크합니다.

```python
data = {model}.objects.filter(name__contains='chicken')
# 음식의 이름(name)에 'chicken'이 포함된 모든 데이터를 조회합니다.
# 단, 대소문자를 구분합니다. (__contains)
```

**__range**

지정한 범위 내에 포함 되는지 체크합니다.

날짜, 숫자 문자 등 모든 데이터의 범위를 사용할 수 있으며 파이썬의 range와 비슷합니다.

```python
data = {model}.objects.filter(price__range=(1000,5000))
# 가격(price)이 1000원~5000원인 모든 데이터를 조회합니다.
```

```python
import datetime
start_date = datetime.date(2020,8,12)
end_date = datetime.date(2020,9,12)
data = {model}.objects.filter(pub_date__range=(start_date,end_date))
# 생성일(pub_date)이 2020-08-12~2020-09-12인 모든 데이터를 조회합니다.
```

이밖에도 많은 조건 키워드가 있습니다.

**__lt , __gt, __lte, __gte**

미만 (less-than), 초과 (greater-than)
이하 (less-than-or-equal), 이상(greater-than-or-equal)인 데이터를 조회합니다.

```python
data = {model}.objects.filter(age__gt=25)
```

**__in**

주어진 리스트 안에 존재하는 자료를 조회합니다.

```python
data = {model}.objects.filter(age__in=[21,25,27])
```

**__id=1**

![](assets/2023-04-29-16-19-09-image.png)![](assets/2023-04-29-16-19-34-image.png)

```python
Review.objects.filter(author__id=1)
Review.objects.filter(author__nickname="asdf")
```

이러한 조건 키워드를 조회와 함께 사용하면 복잡한 조회도 SQL없이 구현할 수 있습니다. 이 밖에도 몇가지 조건키워드가 더 있는데 여기서 모든 조건 키워드를 나열하지 않았습니다. '로직을 작성하다가 이런 조건 키워드가 있으면 좋겠는데' 하는 생각이 들때 공식 문서를 참고해서 찾아보세요. [QuerySet API reference | Django documentation | Django](https://docs.djangoproject.com/en/2.2/ref/models/querysets/#field-lookups)

---

## 데이터 수정하기

데이터를 수정하기 위해서는 수정할 데이터 객체를 가져온 다음 원하는 필드를 수정하고 save()를 호출하여 데이터베이스에 반영하면 됩니다.

```python
data = {model}.objects.get(id=1)
data.name = 'Woojae'
data.save()
```

## 데이터 삭제하기

데이터를 삭제하기 위해서는 삭제할 데이터 객체를 가져온 다음 delete()를 호출하면 됩니다.

```python
data = {model}.objects.get(id=3)
data.delete()
```

모델에 대해 더 많은 내용이 궁금하다면 아래 Django 문서를 참고하세요! [Making queries | Django documentation | Django]([Making queries | Django documentation | Django](https://docs.djangoproject.com/en/2.2/topics/db/queries/))

# Django Model API

Django에서 Model을 정의하면 ORM을 통해 데이터베이스와 소통할 수 있는 API를 제공합니다. 여기서는 우리가 사용하는 Model API를 정리하고 조금 더 자세히 살펴보겠습니다.

## API란?

우리가 앞에서 데이터베이스를 조작할 때 사용했던 아래와 같은 모든 명령어들이 바로 API 입니다.

```
<model>.objects.all() # 모든 데이터 가져오기
<model>.objects.get() # 조건에 맞는 데이터 1개 가져오기
```

API란 Application Programming Interface의 약자로 어플리케이션에서 시스템의 기능을 제어할 수 있도록 만든 인터페이스를 말합니다. 쉽게 말하면 어떤 기능을 쉽게 사용할 수 있도록 만든 체계라고 할 수 있는데요, 예를 들어 여러분이 식당에 가면 주문을 받는 직원이 있죠? 우리는 해당 직원을 통해서 먹고 싶은 음식을 주문하고 전달 받아서 맛있게 먹으면 됩니다. 직접 요리사에게 먹고 싶은 음식에 대해 설명하거나 만드는 법을 알려줄 필요가 없죠. 여기서 직원에 해당하는 것이 바로 API 입니다.

## Queryset

Queryset은 Django Model의 데이터가 담겨있는 목록으로 파이썬의 리스트와 비슷한 형태를 가지고 있습니다. 우리는 이러한 Queryset을 얻기 위해서 아래와 같은 'objects'를 이용합니다. 이 'objects'는 'Model Manager'라고 하는데 Model과 데이터베이스 간에 연산을 수행하는 역할을 합니다. 이 'objects'를 통해 데이터베이스와 연산해서 얻은 여러 모델 데이터가 담겨 있는 것이 바로 Queryset 인거죠.

```
<model>.objects.all() # <model>의 모든 데이터 Queryset 가져오기 
```

## Queryset API

자, 어려운 내용은 잠시 내려두고 쉽게 말해서 Queryset은 데이터베이스로 부터 가져온 여러개의 model 데이터 입니다. 우리는 이러한 Queryset을 우리가 원하는 조건에 맞게 만들 수 있으면 되는거죠.

Queryset을 반환 하는 API

| API        | 설명                                          | 예시                                            |
| ---------- | ------------------------------------------- | --------------------------------------------- |
| all()      | 해당 모델 테이블의 모든 데이터 조회                        | Post.objects.all()                            |
| filter()   | 특정 조건에 맞는 모든 데이터 조회                         | Post.objects.filter(content__contains='coke') |
| exclude()  | 특정 조건을 제외한 모든 데이터 조회                        | Post.objects.exclude(title__contains='code')  |
| order_by() | 특정 조건으로 정렬된 데이터 조회<br>(-를 붙이면 오름차순으로 정렬)    | Post.objects.order_by('-dt_created')          |
| values()   | Queryset에 있는 모든 모델 데이터의 정보를 사전형으로 갖는 리스트 반환 | Post.objects.all().values()                   |

하나의 데이터 객체를 반환하는 API

| API             | 설명                                                                        | 예시                                                                       |
| --------------- | ------------------------------------------------------------------------- | ------------------------------------------------------------------------ |
| get()           | 조건에 맞는 하나의 데이터 조회                                                         | Post.objects.get(id=1)                                                   |
| create()        | 하나의 데이터를 생성하고 해당 모델 데이터를 반환                                               | Post.objects.create(title='Learning Django', context='Codeit Django')    |
| get_or_create() | 조건에 맞는 데이터를 조회하고 해당 데이터가 없다면 새로 생성 후 생성된 모델 데이터를 반환                       | Post.objects.get_or_create(title='Learning Python', context='It's good’) |
| latest()        | 주어진 필드 기준으로 가장 최신의 모델 데이터를 반환                                             | Post.objects.latest('dt_created')                                        |
| first()         | 쿼리셋의 가장 첫번째 모델 데이터를 반환, 정렬하지 않은 쿼리셋이라면 pk를 기준으로 정렬 후 반환, 만약 데이터가 없다면 None | Post.objects.order_by('title').first()                                   |
| last()          | 연산된 쿼리셋의 가장 가지막 모델 데이터를 반환,<br>만약 데이터가 없다면 None                           | Post.objects.order_by('title').last()                                    |

그 외 API

| API      | 설명                                                                     | 예시                                                                                                                                        |
| -------- | ---------------------------------------------------------------------- | ----------------------------------------------------------------------------------------------------------------------------------------- |
| exists() | 연산된 쿼리셋에 데이터가 있다면 True 반환                                              | Post.objects.get(pk=812).exists()                                                                                                         |
| count()  | 쿼리셋의 데이터 개수를 정수로 반환                                                    | Post.objects.all().count()                                                                                                                |
| update() | 데이터를 수정할 때 사용<br>(여러 데이터 또는 여러 필드를 한 번에 수정 가능),<br>수정된 데이터의 개수를 정수로 반환 | Post.objects.filter(dt_created__year=2021).update(context='codeit')<br>→ 생성일이 2021년인 모든 포스트 데이터들의 context를 'codeit'으로 바꾸고 변경된 데이터의 개수를 리턴 |
| delete() | 데이터를 삭제할 때 사용                                                          | post = Post.objects.get(pk=1) post.delete()                                                                                               |
