# DRF 설치하기

DRF 학습을 위한 실습 환경을 구성해 보겠습니다. 먼저 실습 환경 구성을 위해 pyenv와 pyenv-virtualenv가 필요한데요. 설치가 안된 분들은 아래 레슨들을 먼저 참고해 주세요.

- [macOS](https://www.codeit.kr/learn/3555)
- [Windows](https://www.codeit.kr/learn/3556)

다음으로 파이썬 3.9 버전(3.8 버전 이상이면 괜찮습니다)으로 가상 환경을 생성하고, Django 4.0 버전과 DRF 3.13.1 버전을 설치해 주세요.

터미널

```bash
> pyenv install 3.9.11                                   # 파이썬 3.9.11 버전 설치
> pyenv virtualenv 3.9.11 venv                           # venv라는 가상 환경 생성
> mkdir movie_api                                        # 프로젝트를 위한 디렉토리(폴더) 생성
> cd movie_api                                           # 디렉토리 안으로 이동
> pyenv local venv                                       # venv 가상 환경 적용
> pip install django==4.0 djangorestframework==3.13.1    # Django 4.0, DRF 3.13.1 설치
> django-admin startproject movie_api                    # 해당 위치에 Django 프로젝트 생성
```

DRF를 사용하기 위해서는 `settings.py`에 있는 `INSTALLED_APPS`에 `rest_framework`를 추가해야 합니다.

movie_api/settings.py

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'rest_framework'
]
```

# 모델 생성

이번 토픽에서는 영화 관련 정보들을 관리하는 API를 만들면서 DRF를 배워볼 건데요. 가장 기본이 될 `movies` 앱과 모델을 만들어 보겠습니다. 모델을 생성하고, 데이터베이스에 마이그레이션하고, 테스트용 데이터를 넣는 것까지 해 볼게요.

먼저 프로젝트 디렉토리로 이동하고 `movies` 앱을 만듭니다.

터미널

```bash
> cd movie_api
> python manage.py startapp movies
```

새롭게 만든 앱을 `INSTALLED_APPS`에 등록해 줄게요.

movie_api/settings.py

```python
INSTALLED_APPS = [
    # ...
    'django.contrib.staticfiles',
    'rest_framework',
    'movies'
]
```

다음으로, 영화에 대한 기본 정보를 담을 수 있는 `Movie` 모델을 생성할게요. `Movie` 모델에는 `name`(이름), `opening_date`(개봉일), `running_time`(상영 시간), `overview`(간략한 소개 문구) 필드가 존재합니다.

movies/models.py

```python
from django.db import models

class Movie(models.Model):
    name = models.CharField(max_length=30)
    opening_date = models.DateField()
    running_time = models.IntegerField()
    overview = models.TextField()
```

작성한 모델을 실제 데이터베이스에 적용하기 위해 마이그레이션 하겠습니다. 또, 간단한 테스트 데이터도 넣어줄게요.

- [movies.json](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5826&directory=movies.json&name=movies.json) 다운로드

위 링크로 파일을 다운받아 `manage.py`가 존재하는 폴더에 넣어 주세요.

![3-1](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=5826&directory=3-1.png&name=3-1.png)  

다음으로, 테스트 데이터를 넣어 주겠습니다.

터미널

```bash
> python manage.py makemigrations
> python manage.py migrate
> python manage.py loaddata movies.json  
```

해당 과정에 사용된 `loaddata`는 JSON 형식의 파일로부터 데이터를 받아 Django 데이터 베이스에 입력해 주는 명령어입니다.
