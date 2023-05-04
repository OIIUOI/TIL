![1-1](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5824&directory=1-1.png&name=1-1.png)

# DRF(Django REST Framework)

눈에 보이는 화면을 다루는 영역을 프론트엔드, 눈에 보이지 않는 데이터와 로직을 처리하는 영역을 백엔드라고 하는데요. Django는 프론트엔드와 백엔드를 모두 처리해 주는 풀스택 프레임워크였죠? 먼저 배워본 분들이라면 아실 텐데요(혹시 모르신다면 [관련 토픽](https://www.codeit.kr/topics/getting-started-with-django?pathType=CAREER&pathSlug=python-fullstack-developer)을 먼저 수강하시기 바랍니다).

하지만, 웹이 발전하면서 점점 더 복잡한 기능들이 필요해졌고, Django만으로 그런 기능들을 다 개발하는 게 어려워졌습니다. 특히, 프론트엔드의 복잡한 기능들을 개발하는 게 힘들어졌죠. 그래서, 프론트엔드와 백엔드를 각각의 전용 프레임워크로 따로 개발하는 게 더 좋은 방식이 되었습니다.

이런 흐름에서 등장한 게 바로 Django REST Framework입니다. 줄여서 DRF라고 많이 부르는데요. DRF는 Django를 백엔드 개발에만 사용하도록 해 줍니다.

# DRF의 역할: 직렬화

프론트엔드는 데이터를 백엔드에 요청하고, 백엔드는 요청에 맞게 처리하여 데이터를 반환합니다. 웹이 동작하는 기본 방식인데요. 그 과정에서 사용하는 데이터 형식이 서로 달라 문제가 됩니다.

예를 들어볼게요. Django는 백엔드에서 데이터를 처리할 때 파이썬 객체 형식을 사용합니다. 하지만, 프론트엔드에서는 보통 JSON 형식을 많이 사용하죠?(JSON에 대한 자세한 설명이 필요하다면 [링크](https://developer.mozilla.org/ko/docs/Learn/JavaScript/Objects/JSON)를 참조해 주세요).

이런 차이 때문에, 백엔드와 프론트엔드의 통신을 위해선 먼저 데이터 형식이 통일돼야 합니다. 그 과정을 **직렬화(Serialization)**와 **역직렬화(Deserialization)**라고 합니다.

직렬화는 서버에 파이썬 객체로 저장된 데이터를 JSON 형태로 바꿔 주는 것입니다. 반대로 역직렬화는 JSON 형태의 데이터를 파이썬 객체로 바꿔 주는 것이죠. DRF가 바로 이 작업을 해 줍니다.

아래는 직렬화와 역직렬화 과정을 표현한 이미지인데요. 데이터의 형태가 어떻게 바뀌고 있는지 잘 살펴보시기 바랍니다.

![1-2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5824&directory=1-2.png&name=1-2.png)

# DRF와 Django의 관계

Django는 응답으로 데이터와 HTML, CSS 코드를 함께 반환합니다. 그래서, Django의 응답만으로 하나의 웹 페이지가 완성될 수 있죠.

하지만, DRF는 HTML과 CSS 코드를 반환하지 않습니다. 대신, 요청에 따라 처리된 데이터만 프론트엔드에 전달합니다. 이 부분이 Django와 DRF의 가장 큰 차이입니다.

![1-3](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5824&directory=1-3.png&name=1-3.png)

이 부분을 제외하면 많은 부분이 유사합니다. 예를 들어, DRF는 Django의 모델과 ORM 문법을 그대로 사용합니다.

또, URL 설계 방식도 동일한데요. Django에서 URL을 생성할 때 `urls.py` 파일에 사용하고 싶은 이름을 정의하고 뷰와 연결했었죠? DRF도 마찬가지입니다.

DRF가 Django를 기반으로 하기 때문에 유사한 부분이 정말 많습니다. 그래서, Django를 배우신 분들이라면 쉽게 사용할 수 있습니다.
