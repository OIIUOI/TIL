![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting.png&name=windows_setting.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting.png&name=windows_setting.png)

# 1. VSCode 설치

(1) VSCode 공식 사이트([https://code.visualstudio.com/](https://code.visualstudio.com/))로 이동해서 프로그램을 다운로드합니다.

# 2. WSL 설치

(1) WSL을 설치하기 앞서서 먼저 숨겨져있는 윈도우 기능을 켜줘야 합니다.

1. '검색창'을 클릭하고 'windows 기능'이라고 검색해 주세요.
2. 그다음 'windows 기능 켜기/끄기'로 들어갑니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_4_1.png&name=windows_setting_4_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_4_1.png&name=windows_setting_4_1.png)

(2) 나오는 화면에서 **Linux용 Windows 하위 시스템 항목**에 체크를 하고 확인을 눌러서 설정해 주세요.
처음 설정할 때는 재부팅이 필요합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_5_1.png&name=windows_setting_5_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_5_1.png&name=windows_setting_5_1.png)

(3) 재부팅이 되었다면 이제 WSL을 설치해봅시다.

다시 '검색창'을 클릭하고 store를 입력하여 마이크로소프트 스토어로 들어갑니다.
그리고 스토어 검색창에 'ubuntu'라고 검색해 주세요.
아래 보이는 **ubuntu 18.04 LTS** 버전을 클릭합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_6_1.png&name=windows_setting_6_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_6_1.png&name=windows_setting_6_1.png)

(4) '설치'를 눌러서 진행하시면 되는데 만약 마이크로소프트 계정이 있다면 로그인을 해주셔도 되고 그냥 닫아도 설치가 진행됩니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_7.png&name=windows_setting_7.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_7.png&name=windows_setting_7.png)

(5) 잠시 후에 설치가 다 되었다면 '검색창'을 클릭하여 ubuntu라고 검색하시면 설치한 **Ubuntu 18.04 LTS** 프로그램이 보입니다.
앞으로 우리가 자주 쓸 예정이니까 편하게 쓸 수 있도록 시작 화면이나 작업 표시줄에 고정해 주세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_8.png&name=windows_setting_8.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_8.png&name=windows_setting_8.png)

(6) 이제 설치가 되었으니까 초기 설정을 해주도록 할게요.
'ubuntu 18.04 LTS'를 클릭해서 실행합니다. 처음에 실행하면 나머지 설치 과정이 필요합니다.
잠시 기다려주세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_9.png&name=windows_setting_9.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_9.png&name=windows_setting_9.png)

우리가 사용할 username과 비밀번호를 입력하라는 메시지가 나올 것입니다.
비밀번호는 타이핑을 해도 보이지 않으니까 입력을 하고 엔터를 치면 됩니다. **비밀번호를 잘 기억해주세요.**

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_10_1.png&name=windows_setting_10_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_10_1.png&name=windows_setting_10_1.png)

(7) 이번에는 복사 후 WSL에 붙여넣기를 편리하게 하기 위한 설정을 해주겠습니다.
WSL 내에서는 우리가 흔히 복사, 붙여넣기 할 때 사용하던 `Ctrl + C`, `Ctrl + V` 를 사용할 수 없기 때문입니다.

ubuntu 창의 노란색 박스 영역에 마우스 커서를 가져다 놓은 후 마우스 오른쪽 버튼을 클릭하여 '속성'을 클릭해줍니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_11_1.png&name=windows_setting_11_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_11_1.png&name=windows_setting_11_1.png)

그 다음 **Ctrl + Shift + C/V를 복사(C)/붙여넣기로 사용**을 체크 후 확인을 클릭합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_12_1.png&name=windows_setting_12_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_12_1.png&name=windows_setting_12_1.png)

이렇게 설정을 해주면 WSL 내에서 `Ctrl + Shift + C` 로 복사를, `Ctrl + Shift + V` 로 붙여넣기를 할 수 있습니다.

(8) 이제 ubuntu 업데이트 및 기본 패키지 설치를 해주겠습니다.
ubuntu도 하나의 OS니까 업데이트도 해야 하고 사용할 프로그램도 설치해 줘야겠죠?

업데이트를 진행하기 위해 아래에 있는 코드를 복사해서 붙여넣기 한 후 실행해주세요.

```bash
sudo apt-get update
```

방금 설정을 해주었기 때문에 복사 후 `Ctrl + Shift + V` 로 붙여넣기 하면 되겠죠?

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_13.png&name=windows_setting_13.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_13.png&name=windows_setting_13.png)

아래 명령은 한 번에 여러줄을 복사 후 붙여넣기 하여 실행하고 설치가 다 될때까지 기다려주세요.

```bash
sudo apt-get install -y make build-essential \
libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev \
wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev git python-pip sqlite3
```

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_14.png&name=windows_setting_14.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_14.png&name=windows_setting_14.png)

(9) 다 되었으면 디렉토리를 하나 만들어볼까요?

1. `mkdir`을 쓰고 `codeit-django`라고 생성할게요.
2. 그다음 `cd` 명령어를 이용해서 생성한 디렉토리로 이동합니다.

만약 이러한 커맨드가 익숙하지 않으시다면 선수과목인 [[유닉스 커맨드라인]](https://www.codeit.kr/paths/skill/unix-command-line)을 먼저 수강하고 오시는 것을 추천드립니다.

여기까지 되었다면 이제 따라 써보세요.

```bash
code .
```

그러면 지금 화면처럼 VSCode 서버가 설치됩니다.
잠시 기다려서 설치를 완료해 주세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_15.png&name=windows_setting_15.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_15.png&name=windows_setting_15.png)

설치가 완료되면 다음과 같이 WSL: UBUNTU에서 실행된 `CODEIT-DJANGO` 디렉토리에서 VSCode가 실행된 것을 볼 수 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16.png&name=windows_setting_16.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16.png&name=windows_setting_16.png)

상당히 편리하죠?
ubuntu에서 동작하는 디렉토리 또는 파일이지만 마치 윈도우에서 개발하듯 사용할 수 있습니다.

하지만 아래 스크린 샷과 같이 [WSL: UBUNTU-18.04] 와 같은 형태가 보이지 않을 수 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16_1_1.png&name=windows_setting_16_1_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16_1_1.png&name=windows_setting_16_1_1.png)

문제 해결을 위해 왼쪽의 **확장프로그램(Extensions)** 아이콘을 클릭하고 **wsl** 을 검색합니다. 검색 결과 중에 Microsoft 사의 **WSL- Remote** 를 Install 을 클릭하여 설치합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16_2_2.png&name=windows_setting_16_2_2.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16_2_2.png&name=windows_setting_16_2_2.png)

설치가 완료되면 Visual Studio Code 를 종료한 후 다시 WSL 에서 `code .` 을 실행합니다. 설치 후 스크린 샷처럼 나오면 잘 해결된 것입니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16_1.png&name=windows_setting_16_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_16_1.png&name=windows_setting_16_1.png)

# 3. pyenv, pyenv-virtualenv 설치

(1) 이번에는 파이썬 관리 패키지인 `pyenv`를 설치해보겠습니다.
가상 환경을 구성해 주는 `pyenv-virtualenv`도 `pyenv`를 설치하면 함께 설치됩니다.

설치 명령어는 아래에서 복사한 후 터미널에서 붙여넣기(`Ctrl + Shift + V`)하고 엔터키를 입력해주세요.

```bash
curl https://pyenv.run | bash
```

잠시 기다리면 설치가 모두 완료됩니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_17_1.png&name=windows_setting_17_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_17_1.png&name=windows_setting_17_1.png)

(2-1) WSL 을 처음 설치하시고 지금까지 진행하셨다면 **Bash Shell** 을 사용하고 계실 겁니다.

아래 명령을 입력해보세요.

```bash
echo $SHELL
```

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_18_1.png&name=windows_setting_18_1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_18_1.png&name=windows_setting_18_1.png)

만약 아래와 같이 `zsh` 가 출력된다면 해당 설정을 건너 띄고 [(2-2)](https://www.codeit.kr/learn/3556#two-dash-two) 로 넘어가주세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_18_2.png&name=windows_setting_18_2.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_18_2.png&name=windows_setting_18_2.png)

`bash` 라면 아래 유의사항을 참고하셔서 각 코드 블록 안에 있는 명령을 복사하여 터미널에 붙여넣어(`Ctrl + Shift + V`) 실행해주세요.

- 첫 코드 블록 안에 있는 명령문은 여러 줄로 되어있는데, **전체**를 복사하여 붙여넣어 주세요.
- 그다음 코드 블록 안에 있는 명령문은 **한 줄씩** 복사 후 붙여넣어 주세요.

**| pyenv 설정하기 for bash**

```bash
sed -Ei -e '/^([^#]|$)/ {a \export PYENV_ROOT="$HOME/.pyenv"a \export PATH="$PYENV_ROOT/bin:$PATH"a \' -e ':a' -e '$!{n;ba};}' ~/.profile
```

```bash
echo 'eval "$(pyenv init --path)"' >>~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.bashrc

echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bashrc
```

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_18.png&name=windows_setting_18.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_18.png&name=windows_setting_18.png)

(2-2) 기존에 WSL 을 사용하고 계신 분 중에는 **Zsh Shell** 을 사용하고 계실 수도 있습니다.

Zsh Shell 에서 설정을 위해 아래 코드 블록 안의 명령을 **한 줄씩** 복사 후 터미널에 붙여넣기 해서 실행해주세요

**| pyenv 설정하기 for zsh**

```
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zprofile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zprofile
echo 'eval "$(pyenv init --path)"' >> ~/.zprofile

echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.profile
echo 'eval "$(pyenv init --path)"' >> ~/.profile

echo 'eval "$(pyenv init -)"' >> ~/.zshrc
echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.zshrc
```

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_19.png&name=windows_setting_19.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_19.png&name=windows_setting_19.png)

여기까지 잘 따라오셨다면 ubuntu 를 완전히 종료 후 다시 실행시킵니다. 
그리고 아래 명령어를 입력하여 실행해보세요

```bash
pyenv --version
```

다음과 같이 pyenv의 버전이 나온다면 설치가 잘 된 것입니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_20.png&name=windows_setting_20.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3556&directory=windows_setting_20.png&name=windows_setting_20.png)

이렇게 해서 이번 시간에 우리는 앞으로 코드를 편집할 **VSCode**, 파이썬의 버전을 관리할 **pyenv**, 파이썬 가상 환경을 관리할 **pyenv-virtualenv** 를 설치했습니다.

이어서 다음 레슨에서는 우리가 설치한 `pyenv`, `pyenv-virtualenv`를 이용해서 파이썬 가상 환경을 구성하고 `django`를 설치해보도록 하겠습니다.
