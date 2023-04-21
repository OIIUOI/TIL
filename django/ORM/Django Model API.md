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
