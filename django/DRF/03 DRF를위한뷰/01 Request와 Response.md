`@api_view()`는 Django 기반의 함수형 뷰를 DRF 기반의 함수형 뷰로 변경하는 데코레이터 함수입니다. 대표적으로 `HttpRequest` 대신 `Request`를, `HttpResponse` 대신 `Response`를 사용하게 해 주는데요

movies/views.py

```python
@api_view(['GET', 'POST'])
def movie_list(request):
    if request.method == 'GET':
        movies = Movie.objects.all()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        data = request.data
        serializer = MovieSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

```

그런데, DRF에서만 사용되는 `Request`와 `Response`는 정확하게 어떤 기능을 하는 걸까요? `POST`와 `GET`요청을 처리하는 과정을 통해 자세히 살펴보겠습니다.

# `POST`  요청 처리 과정

DRF에서 `POST` 요청은 `Request` 객체에 담겨서 전달됩니다. 그 과정에서 JSON 형태로 들어온 데이터를 파이썬 딕셔너리 형태로 변환해 줍니다.

예를 들어, 아래와 같은 데이터를 생성하는 `POST` 요청이 들어왔다고 할게요.

```json
{
    "name":"프리즌",
    "opening_date":"2017-03-23",
    "running_time":125,
    "overview":"밤이 되면 죄수들이 밖으로 나가 대한민국 완전범죄를 만들어내는 교도소  그 교도소의 권력 실세이자 왕으로 군림하는 익호(한석규).  그 곳에 검거율 100%로 유명한 전직 경찰 유건(김래원)이 뺑소니, 증거인멸, 경찰 매수의 죄목으로  입소하게 되고, 특유의 깡다구와 다혈질 성격으로 익호의 눈에 띄게 된다.  익호는 유건을 새로운 범죄에 앞세우며 점차 야욕을 내보이는데 …  세상을 움직이는 놈들은 따로 있다  감옥 문이 열리면 큰 판이 시작된다!"
}

```

  

`Request` 객체에 담겨서 전달된 요청의 결과를 `request.data`로 확인해 보겠습니다.

```python
@api_view(['GET', 'POST'])
def movie_list(request):
    print(request.data)
    print(type(request.data))
    # ...

```

```
# request.data 결과
{
    'name':'프리즌', 
    'opening_date':'2017-03-23', 
    'running_time':125, 
    'overview':'밤이 되면 죄수들이 밖으로 나가 대한민국 완전범죄를 만들어내는 교도소  그 교도소의 권력 실세이자 왕으로 군림하는 익호(한석규).  그 곳에 검거율 100%로 유명한 전직 경찰 유건(김래원)이 뺑소니, 증거인멸, 경찰 매수의 죄목으로  입소하게 되고, 특유의 깡다구와 다혈질 성격으로 익호의 눈에 띄게 된다.  익호는 유건을 새로운 범죄에 앞세우며 점차 야욕을 내보이는데 …  세상을 움직이는 놈들은 따로 있다  감옥 문이 열리면 큰 판이 시작된다!'
}

# type(request.data) 결과
<class 'dict'>

```

데이터가 파이썬 딕셔너리 형태로 바뀌었네요. 이렇게 `Request`는 JSON 형식으로 들어온 데이터를 파싱해서 파이썬 딕셔너리 형태로 변환해 줍니다.

여기에서 '파싱'이란 데이터를 추출하여 가공하기 쉬운 상태로 바꾸는 것을 의미하는데요. JSON 문자열에서 키와 값을 추출하여 파이썬에서 다루기 쉬운 파이썬 딕셔너리 형태로 만든거죠.

파이썬 딕셔너리로 변환된 데이터는 시리얼라이저를 통해 파이썬 객체 형태로 변경됩니다.

movies/views.py

```python
serializer = MovieSerializer(data=data)
serializer.save()

```

movies/serializers.py

```python
class MovieSerializer(serializers.Serializer):
    # ...
    def create(self, validated_data):
        return Movie.objects.create(**validated_data)

```

시리얼라이저가 JSON 데이터를 바로 파이썬 객체로 바꾸는 게 아니라, 중간에 `Request`를 통해 먼저 JSON 데이터를 파이썬 딕셔너리로 바꿔 주는 과정이 있는 것이죠.

# `GET`  요청 처리 과정

DRF에서 `GET` 방식의 요청이 들어오면 조회한 결과값은 `serializer`라는 변수에 담기는데요. `serializer.data`를 통해 저장된 데이터를 확인해 볼게요.

movies/views.py

```python
@api_view(['GET', 'POST'])
def movie_list(request):
    movies = Movie.objects.all()
    serializer = MovieSerializer(movies, many=True)
    print(serializer.data)
    # ...

```

```
# serializer.data 결과
[
  {
    'id': 1,
    'name': '프리즌', 
    'opening_date': '2017-03-23', 
    'running_time': 125, 
    'overview': '밤이 되면 죄수들이 밖으로 나가 대한민국 완전범죄를 만들어내는 교도소  그 교도소의 권력 실세이자 왕으로 군림하는 익호(한석규).  그 곳에 검거율 100%로 유명한 전직 경찰 유건(김래원)이 뺑소니, 증거인멸, 경찰 매수의 죄목으로  입소하게 되고, 특유의 깡다구와 다혈질 성격으로 익호의 눈에 띄게 된다.  익호는 유건을 새로운 범죄에 앞세우며 점차 야욕을 내보이는데 …  세상을 움직이는 놈들은 따로 있다  감옥 문이 열리면 큰 판이 시작된다!'
  },
  
  ...
]

```

각 영화는 파이썬 딕셔너리 형태로 출력됩니다. 이렇게, 시리얼라이저는 파이썬 객체 형태로 저장된 데이터를 파이썬 딕셔너리 형태로 변환해 줍니다.

해당 데이터가 응답으로 전달될 때에는 JSON 형태로 다시 변환돼야 합니다. 그 작업을 `Response`가 처리합니다.

```python
return Response(serializer.data, status=status.HTTP_201_CREATED)

```

응답이 전달될 때는 시리얼라이저에서 파이썬 객체를 파이썬 딕셔너리 형식으로 변환하고, `Response`에서 딕셔너리 형태의 데이터를 JSON으로 바꿔 주고 있네요.

`Request`와 `Response`가 동작하는 방식을 정리하면 아래와 같습니다.

![24-1](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5847&directory=24-1.png&name=24-1.png)

![24-2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5847&directory=24-2.png&name=24-2.png)
