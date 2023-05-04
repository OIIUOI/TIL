지금까지 백엔드 개발을 위한 DRF 사용법을 배워 봤습니다. 이제는 프론트엔드와 백엔드를 나눠서 멋진 웹 사이트를 만들 수 있게 됐는데요.

하지만 실제로 프론트엔드와 백엔드를 각각 개발해서 프로젝트를 진행하다 보면 CORS 에러가 발생할 수 있습니다. 이 에러가 무엇인지, 어떻게 해결할 수 있는지 한번 알아볼게요.

# CORS란?

CORS란 Cross-Origin Resource Sharing의 약자로, 우리말로 직역하면 **교차 출처 리소스 공유**라는 뜻입니다. 의미 그대로 서로 다른 출처에서 리소스를 공유하는 것을 CORS라고 합니다.

그런데, ‘출처’라는 게 무엇일까요? 이에 대하여 알아보기 위해 이번 토픽에서 배운 영화 리스트 조회 URL을 한번 확인해 볼게요.

영화 리스트 조회 URL의 구조를 살펴보면 프로토콜, 호스트, 포트, 패스가 존재합니다. 아래 이미지에 각각 해당하는 부분을 표시해 놨는데요.

![35-1](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5858&directory=35-1.png&name=35-1.png)

이 중에서 프로토콜, 호스트, 포트를 합쳐서 출처(Origin)라고 부릅니다.

![35-2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5858&directory=35-2.png&name=35-2.png)

CORS는 출처가 다른 자원들을 공유한다는 뜻으로, 한 출처에 있는 자원에서 다른 출처에 있는 자원에 접근하도록 하는 개념입니다.

그런데 CORS를 위해서는 별도의 설정이 필요합니다. 필요한 설정을 하지 않은 채 서로 다른 출처에서 리소스를 공유하려고 하면 에러가 발생할 수 있습니다.

예를 들어서, 그동안 저희가 백엔드 개발을 하면서 사용했던 URL의 출처는 `http://localhost:8000/`이었죠? 그런데 프론트엔드의 출처는 일반적으로 `http://localhost:3000/`이 많이 사용됩니다. 이렇게 서로의 출처에 차이가 있지만 별도의 설정을 하지 않았기 때문에, 백엔드와 프론트엔드를 바로 연결하려고 하면 문제가 생깁니다. 이러한 문제를 CORS 에러라고 합니다.

# DRF에서 CORS 처리하기

그렇다면 DRF에서 CORS를 처리하기 위한 설정에 대해 한번 알아볼게요. 먼저, Django에서 CORS 에러를 해결하기 위해 필요한 라이브러리를 설치합니다. 터미널에 아래 코드를 입력해 주세요.

터미널

```bash
pip install django-cors-headers

```

  

다음으로, `settings.py` 파일을 수정해 줄게요. 아래와 같이 작성해 주세요.

movie_api/settings.py

```python
INSTALLED_APPS = [
    ...,
    'corsheaders',
]

MIDDLEWARE = [
    # 최상단에 작성
    'corsheaders.middleware.CorsMiddleware',
        ...,
]

CORS_ALLOWED_ORIGINS = [ 
    'http://localhost:3000', 
]

```

`CORS_ALLOWED_ORIGINS` 목록에 API 요청을 허용하고 싶은 출처(예를 들어 `http://localhost:3000`)를 입력하면 됩니다
