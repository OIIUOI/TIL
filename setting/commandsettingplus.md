# 커맨드 라인 추가 설정하기

## 커맨드 라인을 꼭 더 이쁘게 써야 하나요?

그렇지 않습니다. 이전 강의에서 개발 환경 구성을 모두 마쳤다면 아래 내용은 온전히 '선택'의 영역입니다. macOS와 WSL의 기본 커맨드 라인 유틸리티는 기본적으로 검정 바탕에 흰색 글자 인데 추가적인 설정을 통해서 가독성을 높이고 더 편리하게 사용할 수 있습니다. 아래 설치 과정 중 특별한 구분이 없으면 Windows(WSL), macOS 모두 호환됩니다.

## 01. Zsh Shell

Shell은 운영체제와 커널(Kernel)사이를 연결해주는 역할을 하는 프로그램으로 사용자의 명령어를 해석해서 운영체제가 동작할 수 있도록 합니다. 이러한 Shell이 여러 종류가 있는데 그 중에서 거의 모든 운영체제가 기본으로 선택하는 것이 Bash Shell 이고 Bash Shell의 기능을 대부분 가지고 있으면서 더 많은 기능이 포함된 것이 바로 Zsh Shell입니다.

### 1.1 Shell 확인하기

맨 처음 WSL에 우분투(Ubuntu)를 설치하면 기본적으로 Bash Shell이 설치되어 있고 만약 macOS라면 10.15 이전 버전은 Bash Shell이, 그 이상 버전이라면 Zsh Shell이 기본적으로 설치되어 있습니다. 아래 명령어를 입력하면 현재 사용 중인 Shell을 확인할 수 있습니다. **현재 Zsh Shell을 사용하고 있다면 바로 02. Oh-My-Zsh 설정으로 넘어가 주세요.**

```bash
echo $SHELL
```

### 1.2 Zsh Shell 설치하기 for WSL Ubuntu

아래 명령어를 입력해서 zsh를 설치합니다.

```bash
sudo apt-get install zsh
```

여기에서 'y'를 입력해서 진행합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled.png&name=Untitled.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled.png&name=Untitled.png)

설치가 끝났다면 기본 shell을 zsh로 변경합니다.

```bash
chsh -s `which zsh`
```

WSL을 재실행 하면 아래와 같은 화면을 볼 수 있는데 0을 눌러서 진행합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%201.png&name=Untitled+1.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%201.png&name=Untitled+1.png)

다시 WSL을 재실행하고 사용 중인 Shell을 확인해보면 zsh shell로 변경된 것을 확인할 수 있습니다.

```bash
echo $SHELL
```

### 1.3 Zsh Shell 설치하기 for macOS

앞서 환경 설정 할때 homebrew를 이용했었죠? zsh도 homebrew를 이용해서 쉽게 설치할 수 있습니다.

```bash
brew install zsh
```

## 02. Oh-My-Zsh

Oh My Zsh는 Zsh의 여러가지 설정을 다루는 플러그인으로 Zsh를 더 쉽고 편하게 사용할 수 있게 해줍니다. 아래 명령어를 입력해서 설치합니다. 이때 macOS라면 기본 Shell을 zsh shell로 변경하기 위해 사용자의 비밀번호를 물어보는 과정이 추가 됩니다.

```bash
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
```

모든 설치가 끝나면 이렇게 이전과는 다른 조금 더 이쁜 커맨드 라인 화면을 볼 수 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%202.png&name=Untitled+2.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%202.png&name=Untitled+2.png)

## 03. Zsh 테마 변경 및 설정

### 3.1 테마 변경하기

이번에는 zsh에 테마를 입혀서 조금 더 가시성이 좋게 만들어 볼게요. VSCode를 홈 경로(~)에서 실행합니다.

```bash
cd ~
code .
```

그다음 왼쪽의 폴더 트리에서 .zshrc 파일을 클릭합니다. `.zshrc` 파일은 zsh의 여러 설정을 해주는 부분입니다. 여기에ㅓ 11번째 줄 근처를 보면 `ZSH_THEME`이라는 부분이 있습니다. zsh의 테마를 적어주는 부분인데 기본적으로 'robbyrussell' 테마가 적용되어 있습니다. 여기에 
변경하고자 하는 테마의 이름을 입력하면 되는데 우리는 기본으로 내장되어있는 'agnoster' 테마로 변경해 주겠습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%203.png&name=Untitled+3.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%203.png&name=Untitled+3.png)

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%204.png&name=Untitled+4.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%204.png&name=Untitled+4.png)

그 다음 커맨드 라인 프로그램을 재시작하면 아래와 같이 변경된 테마를 볼 수 있습니다. 만약 이전의 초기 테마로 돌아가고 싶다면 `robbyrussell`을 입력해서 돌아갈 수 있습니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%205.png&name=Untitled+5.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=Untitled%205.png&name=Untitled+5.png)

이 밖에도 아래 Github에 나와있는 여러가지 테마를 적용할 수 있습니다. [External themes · ohmyzsh/ohmyzsh Wiki · GitHub](https://github.com/ohmyzsh/ohmyzsh/wiki/External-themes)

### 3.2 pyenv 설정하기

홈 디렉토리(~)로 이동한 후 vscode를 실행해주세요.

```bash
cd ~
code .
```

그리고 왼쪽 폴더 트리에서 .bashrc를 클릭하고 맨 아래를 보면 우리가 pyenv를 설정 해준 부분이 있죠? 이 부분은 `.bashrc` 즉 bash shell에 설정을 해준 것 이므로 `.zshrc` 그러니까 zsh shell에도 설정해주어야 합니다.
아래 세 줄을 복사해서 .zshrc 파일의 맨 아래쪽에 붙여넣어 주세요.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-20__6.43.07_copy.png&name=_2020-09-20__6.43.07_copy.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-20__6.43.07_copy.png&name=_2020-09-20__6.43.07_copy.png)

그다음 다시 커맨드 라인 프로그램을 실행하고 아래 명령어를 이용해서 우리가 설정해 주었던 파이썬 환경 목록이 제대로 나오는지 확인합니다.

```bash
pyenv versions
```

## 04. 재미있는 Zsh 플러그인

### 4.1 zsh-syntax-highlighting

이름에서도 알 수 있듯이 명령어를 자동으로 하이라이팅해 주는 기능이 있는 플러그인입니다. 아래 명령어를 한 줄씩 입력해서 설치한 후 재실행을 해보면 여러 가지 색으로 명령어가 구분되는 것을 확인 할 수 있습니다.

```bash
cd ~
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git
```

```bash
echo "source ${(q-)PWD}/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh" >> ${ZDOTDIR:-$HOME}/.zshrc
```

### 4.2 autojump

autojump는 내가 이전에 이동 했었던 경로를 기억해두었다가 해당 디렉토리 이름만으로 Jump 하듯 이동할 수 있게 해주는 플러그인 입니다. 예를들어 이전에 cd /codeit/django/costaurant/new 라는 경로로 이동한적이 있다면 jump의 약자인 j를 사용해서 `j new` 라는 명령어 만으로 같은 경로로 이동할 수 있습니다.

- WSL Ubuntu에서 설치하기

```bash
cd ~
git clone https://github.com/wting/autojump.git
```

```bash
cd autojump
./install.py or ./uninstall.py
```

설치를 하고 나면 화면 아래쪽에 .zshrc에 다음의 두 라인을 추가하라는 안내가 나옵니다. 여러분 화면의 다음 두 줄을복사합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.34.51_copy.png&name=_2020-09-21__4.34.51_copy.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.34.51_copy.png&name=_2020-09-21__4.34.51_copy.png)

```bash
cd ~
code .
```

VSCode를 실행하고 .zshrc의 맨 아래쪽에 복사한 두 줄을 다음과 같이 붙여 넣습니다. 그리고 WSL을 재실행 하면 모든 설치가 완료됩니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.37.59_copy.png&name=_2020-09-21__4.37.59_copy.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.37.59_copy.png&name=_2020-09-21__4.37.59_copy.png)

- macOS에서 설치하기

autojump 역시 homebrew를 이용해서 설치가 가능합니다.

```bash
brew install autojump
```

설치가 끝났다면 홈 경로(~)에서 VSCode를 실행하고

```bash
cd ~
code .
```

아래로 내려서 plugins 항목에 다음과 같이 git 옆에 autojump를 추가합니다. 이때 콤마가 아니라 아래와 같이 띄어쓰기로 구분해야 합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.44.51_copy.png&name=_2020-09-21__4.44.51_copy.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.44.51_copy.png&name=_2020-09-21__4.44.51_copy.png)

그 다음 터미널을 재실행 하면 설치가 완료 됩니다.

### 4.3 zsh-autosuggestions

마지막으로 소개할 플러그인은 zsh-autosuggestions으로 내가 이전에 타이핑 했던 명령어를 기반으로 명령어를 추천해주는 플러그인 입니다. 아래 명령어를 각각 입력해서 플러그인을 다운로드 합니다.

```bash
cd ~
git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
```

완료 되었다면 VSCode로 .zshrc를 열고

```bash
cd ~
code .
```

plugins 항목에 아래처럼 zsh-autosuggestions를 추가합니다. 이때 콤마가 아닌 띄어쓰기로 각 플러그인을 구분해야 합니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.51.40_copy.png&name=_2020-09-21__4.51.40_copy.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.51.40_copy.png&name=_2020-09-21__4.51.40_copy.png)

그 다음 사용하고 있는 커맨드 라인 유틸리티를 재실행하면 모든 설치가 완료됩니다. 이제 아래와 같이 명령어를 입력하면 내가 이전에 입력했었던 히스토리를 토대로 입력할 명령어를 흐리게 추천해 줍니다.

![https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.55.22_copy.png&name=_2020-09-21__4.55.22_copy.png](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3632&directory=_2020-09-21__4.55.22_copy.png&name=_2020-09-21__4.55.22_copy.png)

이 밖에도 zsh shell에서 사용할 수 있는 여러 가지 플러그인이 있습니다.
검색과 설정을 통해서 여러분만의 커맨드 라인 환경을 구성해보세요 :)
