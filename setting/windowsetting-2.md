이번 레슨에서는 이 두 가지를 이용해서 가상 환경을 구성하고 `django`를 설치해보도록 하겠습니다.
저는 맥에서 강의를 진행하지만 이전 레슨에서 윈도우에서도 맥과 똑같이 할 수 있도록 환경을 구성했습니다.
맥에서 터미널에 입력하는 모든 명령어는 WSL를 이용해서 입력하면 됩니다.

이제 내가 어떤 OS를 사용하는지에 관계없이 하나의 개발 환경을 구성할 수 있게 된 거죠.



# 1. pyenv 를 이용한 파이썬 설치

(1) 처음 우리가 같이 해볼 것은 파이썬 설치입니다.

"어? 저는 이미 다른 버전의 파이썬이 설치되어 있는데요." 하시는 분들도 괜찮습니다. 
지금 어떠한 파이썬이 설치되어 있는지에 관계없이 새로운 환경을 만들어서 사용할 겁니다.

그럼 터미널 또는 WSL을 켜고 `pyenv`를 이용해서 파이썬을 설치해보겠습니다.
먼저 우리가 설치할 수 있는 파이썬의 버전을 볼까요?

```bash
pyenv install --list
```

따라서 입력해보세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_1.png&name=setting_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_1.png&name=setting_1.png)

엄청 많죠?
이 모든 버전이 현재 우리가 사용할 수 있는 파이썬 버전들입니다.

이 중에서 선택해서 설치하면 되는데 꼭 한 가지만 설치할 필요는 없습니다. 원하는 버전의 파이썬을 모두 설치하고 마음대로 바꿔쓸 수 있거든요.
그러니까 우리는 `3.7.13` 버전과 `3.8.13` 버전 두 개를 설치해보도록 하겠습니다.

```bash
pyenv install 3.7.13
```

따라서 입력해보세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_3.png&name=setting_3.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_3.png&name=setting_3.png)

`3.7.13` 버전의 파이썬이 설치가 되었다면 이번에는 `3.8.13` 버전도 설치해주세요.

```bash
pyenv install 3.8.13
```

(2) 설치가 모두 끝났다면 우리가 설치한 파이썬을 보도록 하겠습니다.

```bash
pyenv versions
```

따라서 입력해보세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_4_1.png&name=setting_4_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_4_1.png&name=setting_4_1.png)

그러면 이렇게 우리가 설치한 파이썬을 모두 볼 수 있습니다.

# 2. pyenv-virtualenv 를 이용한 가상환경 생성

(1) 이제 여러 버전의 파이썬도 준비가 되었으니까 가상 환경을 구성해볼까요?
먼저 가상 환경을 하나 생성하도록 하겠습니다.

같이 입력해보세요.

1. `pyenv virtualenv` 를 입력하고
2. 이어서 파이썬의 버전과 생성할 가상 환경의 이름을 입력합니다.

```bash
pyenv virtualenv 3.7.13 django-envs
```

우리는 `3.7.13` 버전의 파이썬으로 `django-envs` 라는 이름의 가상 환경을 만들어볼게요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_5.png&name=setting_5.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_5.png&name=setting_5.png)

이렇게 하면 가상 환경이 생성이 됩니다.
만약 가상 환경을 잘못 만들어서 삭제하고 싶다면 `pyenv uninstall` 그다음 가상 환경의 이름을 사용하면 됩니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_6_1.png&name=setting_6_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_6_1.png&name=setting_6_1.png)

(2) 자 그러면 다시 파이썬 환경 목록을 볼까요?
이처럼 우리가 생성해 준 `django-envs`가 생긴 것을 볼 수 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_7_1_1.png&name=setting_7_1_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_7_1_1.png&name=setting_7_1_1.png)

그런데 잘 보면 `3.7.13/envs/django-envs`와 `django-envs` 두 가지가 있죠?
이름만 있는 것과 이 이름의 가상 환경이 어떤 버전의 파이썬으로 만들어졌는지를 보여주는 두 가지가 항상 같이 나오게 됩니다.

참고로 이름만 있는 `django-envs` 는 ['심볼릭 링크'](https://ko.wikipedia.org/wiki/%EC%8B%AC%EB%B3%BC%EB%A6%AD_%EB%A7%81%ED%81%AC)를 의미합니다.
심볼릭 링크는 우리가 Windows 나 macOS에서 어떤 파일이나 디렉토리에 쉽게 접근하기 위해 바탕화면에 만드는 '바로 가기'와 같다고 생각하시면 됩니다. `django-envs` 는 `3.7.13/envs/django-envs` 의 '바로 가기'인 셈이죠.

결국 같은 가상 환경을 가리키므로 `django-envs` 나 `3.7.13/envs/django-envs` 중 어떤 걸 적용하셔도 상관 없습니다.



# 3. pyenv로 설치한 파이썬 적용 및 django 2.2 설치

(1) 이제 생성한 가상 환경을 적용해볼게요.

우리가 설치했던 파이썬 기본 환경인 `3.7.13`과 `3.8.13`이 있고 가상 환경 `django-envs`가 있죠?

가상 환경을 적용할 때 두 가지 방법이 있습니다.
바로 `global`과 `local`인데요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_8.png&name=setting_8.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_8.png&name=setting_8.png)

먼저 **global**은 우리 컴퓨터 전역에 적용하는 것으로 `global`로 설정하면 따로 지정해 주지 않아도 항상 `global`로 설정한 파이썬 환경을 사용합니다.

다음으로 **local**은 특정 디렉토리 내에서만 사용하도록 적용하는 것인데요. `local`로 지정한 디렉토리에서는 `global`로 적용된 환경을 무시하고 `local`로 적용된 환경을 사용합니다.

그러니까 `global`로 `3.8.13`를 지정하고 특정 디렉토리에 `3.7.13`로 `local`을 적용하면
그 디렉토리 안에서는 `3.7.13` `local` 버전이 사용된다는 거죠.
그리고 디렉토리의 하위 디렉토리에도 자동으로 `local` 항목이 적용됩니다.

같이 해보면 조금 더 이해하실 수 있을거에요.

(2) 그러면 바로 해볼게요.

먼저 적용할 항목은 **global**입니다. `global`은 시스템 전역에서 사용할 환경을 지정해 주는 것이라고 했죠?

우리는 현재 선택지가,

- `3.7.13` 버전
- `3.8.13` 버전
- 그리고 새로 만들어주었던 `django-envs`

위 세가지가 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_9_1.png&name=setting_9_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_9_1.png&name=setting_9_1.png)

이 중에서 우리는 컴퓨터 전역에 `3.8.13` 버전의 파이썬을 적용하겠습니다.
따라서 입력해보세요.

```bash
pyenv global 3.8.13
```

이러면 `global` 설정이 적용이 된 것입니다.

잘 적용되었는지 확인해볼까요?
현재 적용되어 있는 파이썬 환경을 보려면 `pyenv versions`를 입력해서
옆에 있는 별사탕(*) 표시를 보시면 됩니다.



![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_10_1.png&name=setting_10_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_10_1.png&name=setting_10_1.png)

지금 보면 사용하는 환경이 `3.8.13`라고 나오죠?
이제 이 컴퓨터 어디에서 파이썬을 실행해도 따로 `local` 설정을 해주지 않으면 `3.8.13`를 기본 환경으로 사용합니다.

(2) 다음은 **local** 설정입니다.

`local`은 특정 디렉토리에 가상 환경을 지정해 주는 것인데
우리는 앞에서 생성했던 `codeit-django` 디렉토리에 적용해보도록 하겠습니다. `codeit-django` 디렉토리 안쪽으로 이동해 주세요.

```bash
cd codeit-django
```

먼저 아무런 설정을 하지 않고 현재 사용하는 파이썬 환경을 봐볼까요?

`pyenv versions`를 입력해서 보거나 또는 그냥 `pyenv version`을 입력해보세요.
그럼 바로 현재 적용되어 있는 파이썬 환경이 나옵니다.
보면 우리가 아무것도 해주지 않아도 전역으로 지정해둔 `3.8.13` 가상 환경이 적용되어 있습니다.



![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_11.png&name=setting_11.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_11.png&name=setting_11.png)

그러면 이제 이 디렉토리에 `django-envs` 가상 환경을 `local`로 적용해보도록 하겠습니다.

따라서 입력해보세요.

```bash
pyenv local django-envs
```

그리고 다시 `pyenv version`을 입력해보면 적용되어 있는 환경이 바뀐 것을 볼 수 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_12.png&name=setting_12.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_12.png&name=setting_12.png)

만약 이 디렉토리를 나가면 어떻게 될까요?

`cd ..`을 이용해서 상위 디렉토리로 이동한 다음 `pyenv version`으로 확인을 해보면 이렇게 우리가 `global`로 적용해 주었던 환경이 적용되어 있죠?
그리고 다시 `codeit-django`로 들어가면 `django-envs` 환경이 저장되어 있는 것을 볼 수 있습니다.



![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_13.png&name=setting_13.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_13.png&name=setting_13.png)

`pyenv`는 가상 환경을 켜고 끌 필요 없이 한번 설정을 해두면 해당 디렉토리로 이동했을 때 자동으로 가상 환경이 적용됩니다.
매우 편리하죠?

파이썬 가상 환경을 만들고 적용하는 법,
그리고 `global` 설정과 `local` 설정의 차이 모두 이해가 되셨나요?

# 3. django 설치

(1) 그럼 이제 `django`를 설치해 봅시다.

지금처럼 `django-envs` 환경이 적용되어 있는 상태에서 우리가 앞으로 사용할 `django`를 설치해보겠습니다.

여기서 한 가지 알아두셔야 할 점은 `codeit-django` 디렉토리에 `django`를 설치하는 것이 아니라 **django-envs 환경에 django를 설치하는 것입니다.**

그러면 다시 `django` 설치로 돌아와서 우리는 `django 2.2` 버전을 사용할 거니까 따라서 입력해보세요.

```bash
pip3 install django==2.2
```





![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_14.png&name=setting_14.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_14.png&name=setting_14.png)

설치가 끝났다면 설치가 잘 되었는지 확인해볼까요?
따라서 입력해보세요.

```bash
django-admin --version
```



![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_15.png&name=setting_15.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_15.png&name=setting_15.png)



화면에 보이는 것처럼 `2.2`가 잘 출력되는지 확인합니다.

여기서 한 가지 더 지금 설치된 파이썬 패키지 목록을 한번 볼까요? `pip3 list`를 입력하면 설치되어 있는 파이썬 패키지와 버전을 볼 수 있습니다.



![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_16.png&name=setting_16.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_16.png&name=setting_16.png)



보면 우리가 설치한 `django`와 django가 필요한 몇 가지 패키지가 설치되어 있는데요.
여기서 `cd ..` 명령을 통해 하나 상위 디렉토리로 이동해서 다시 한번 `pip3 list`로 파이썬 패키지 목록을 보면 우리가 설치했던 `django`가 없습니다.

왜냐하면 지금 적용되어 있는 환경은 `global` 환경으로, `global`로 지정해둔 `3.8.13` 환경이기 때문입니다.



![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_17.png&name=setting_17.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3557&directory=setting_17.png&name=setting_17.png)



이렇게 각각의 환경은 독립적으로 구성됩니다.

자 여기까지 해서 `django` 설치를 모두 마쳤는데요.
어떠신가요?
조금 복잡했죠?

개발 환경을 처음 구성하는 과정은 사실 누구에게나 쉽지 않습니다.
그러니까 이번 레슨을 끝까지 따라오셨다면 정말 큰일 하나를 하신 거예요.














