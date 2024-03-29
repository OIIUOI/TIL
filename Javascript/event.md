﻿
# EVENT
## 마우스 이벤트
|이벤트 타입|설명|
|--|--|
|mousedown|마우스 버튼을 누르는 순간|
|mouseup|마우스 버튼을 눌렀다 떼는 순간|
|click|왼쪽 버튼을 클릭한 순간|
|dblclick|왼쪽 버튼을 빠르게 두 번 클릭한 순간|
|contextmenu|오른쪽 버튼을 클릭한 순간|
|mousemove|마우스를 움직이는 순간|
|mouseover|마우스 포인터가 요소 위로 올라온 순간|
|mouseout|마우스 포인터가 요소에서 벗어나는 순간|
|mouseenter|마우스 포인터가 요소 위로 올라온 순간 (버블링이 일어나지 않음)|
|mouseleave|마우스 포인터가 요소에서 벗어나는 순간 (버블링이 일어나지 않음|

### mouseenter, mouseover
마우스 이벤트 타입에는 `mouseover, mouseout`과 비슷한 `mouseenter`와 `mouseleave`라는 타입이 있습니다.

이름에서도 알 수 있듯이 `mouseenter`는 `mouseover`처럼 **마우스 포인터가 요소 바깥에서 안쪽으로 들어갈 때**, `mouseleave`는 `mouseout`처럼 **마우스 포인터가 요소 안쪽에서 바깥으로 나갈 때** 발생하는데요.

그럼 `mouseover, mouseout`과 어떤 차이가 있을까요?
#### 1. 버블링이 일어나지 않는다.

`mouseenter`와 `mouseleave`는 **버블링이 일어나지 않습니다.**

위 코드 결과에서 `mouseover` 타입으로 이벤트 핸들러가 등록된 `div#box1`요소(왼쪽)에서 마우스를 움직여 보세요.

당연히 해당 요소 바깥에서 안쪽으로 마우스 커서가 이동할 때도 이벤트가 발생하지만, **버블링과 이벤트 위임**의 원리로 자식요소인 `b.title` 부분으로 마우스 커서가 이동할 때도 이벤트가 발생합니다.

하지만 `mouseenter` 타입으로 이벤트 핸들러가 등록된 `div#box2`요소(오른쪽)에서는 해당 요소 바깥에서 안쪽으로 마우스 커서가 이동할 때만 이벤트 핸들러가 동작하는 모습을 확인할 수 있습니다.

#### 2. 자식 요소의 영역을 계산하지 않는다.

`mouseenter`와 `mouseleave`는 **자식 요소의 영역을 계산하지 않습니다.**

다시 `mouseover` 타입으로 이벤트 핸들러가 등록된 `div#box1`요소(왼쪽)에서 마우스를 움직여 봅시다.

버블링에 의해 자식 요소로 마우스 커서가 이동할 때도 이벤트 핸들러가 동작하지만, 자식 요소에서 다시 `div#box1`요소로 마우스 커서가 이동할 때도 이벤트 핸들러가 동작하죠? `mouseover`는 자식 요소의 영역을 구분하기 때문입니다.

반면, `mouseenter`는 자식 요소의 영역을 구분하지 않기 때문에 `mouseenter` 타입으로 이벤트 핸들러가 등록된 `div#box2`요소(오른쪽)에서는 자식 요소에서 이벤트 핸들러가 동작하지 않는 것뿐만 아니라 자식 요소의 영역에 들어갔다 나올 때도 이벤트 핸들러가 동작하지 않는 모습을 볼 수 있습니다.

#### 정리

`mouseover/mouseout`과 비교하면서 `mouseenter/mouseleave`에 대해 살펴봤는데요. 간단하게 정리하면, **이벤트가 자식 요소에 영향끼치는지**가 둘의 가장 큰 차이라고 할 수 있습니다.

그래서 이벤트 핸들러가 자식 요소에까지 영향을 끼치게 하고싶은 경우에는 `mouseover/mouseout`을, 자식 요소에는 영향을 끼치지 않고 해당 요소에만 이벤트 핸들러를 다루고자 한다면 `mouseenter/mouseleave`를 활용하면 좋겠죠?

---
## 키보드 이벤트
|이벤트 타입|설명|
|--|--|
|keydown|키보드의 버튼을 누르는 순간|
|keypress|키보드의 버튼을 누르는 순간 ('a', '5' 등 출력이 가능한 키에서만 동작하며, Shift, Esc 등의 키에는 반응하지 않음)|
|keyup|키보드의 버튼을 눌렀다 떼는 순간|

## 포커스 이벤트
|이벤트 타입|설명|
|--|--|
|focusin|요소에 포커스가 되는 순간|
|focusout|요소로부터 포커스가 빠져나가는 순간|
|blur|요소로부터 포커스가 빠져나가는 순간 (버블링이 일어나지 않음)|

## 스크롤 이벤트
|이벤트 타입|설명|
|--|--|
|scroll|스크롤 바가 움직일 때|

## 윈도우 창 이벤트
|이벤트 타입|설명|
|--|--|
|resize|윈도우 사이즈를 움직일 때 발생|

# 프로퍼티
## 1. 공통 프로퍼티

아래의 프로퍼티들은 이벤트 타입과 상관없이 모든 이벤트 객체들이 공통적으로 가지고 있는 프로퍼티입니다.
|프로퍼티|설명|
|--|--|
|type|이벤트 이름 ('click', 'mouseup', 'keydown' 등)|
|target|이벤트가 발생한 요소|
|currentTarget|이벤트 핸들러가 등록된 요소|
|timeStamp|이벤트 핸들러가 등록된 요소|
|currentTarget|이벤트 발생 시각(페이지가 로드된 이후부터 경과한 밀리초)|
|bubbles|버블링 단계인지를 판단하는 값|

## 2. 마우스 이벤트

마우스와 관련된 이벤트의 경우에는 아래와 같은 이벤트 객체의 프로퍼티들을 가지고 있습니다.
|프로퍼티|설명|
|--|--|
|button|누른 마우스의 버튼 (0: 왼쪽, 1: 가운데(휠), 2: 오른쪽)|
|clientX, clientY|마우스 커서의 브라우저 표시 영역에서의 위치|
|offsetX, offsetY|마우스 커서의 이벤트 발생한 요소에서의 위치|
|screenX, screenY|마우스 커서의 모니터 화면 영역에서의 위치|
|altKey|이벤트가 발생할 때 alt키를 눌렀는지|
|ctrlKey|이벤트가 발생할 때 ctrl키를 눌렀는지|
|shiftKey|이벤트가 발생할 때 shift키를 눌렀는지|
|metaKey|이벤트가 발생할 때 meta키를 눌렀는지 (window는 window키, mac은 cmd키)|

### 1. clientX, clientY

`client` 프로퍼티는 말 그대로 **클라이언트 영역 내에서 마우스의 좌표 정보**를 담고있는데요. **클라이언트 영역이란 이벤트가 발생한 순간에 브라우저가 콘텐츠를 표시할 수 있는 영역**을 뜻합니다.

clientX : 브라우저가 표시하는 화면 내에서 마우스의 X좌표 위치를 담고 있습니다. clientY : 브라우저가 표시하는 화면 내에서 마우스의 Y좌표 위치를 담고 있습니다.

`client` 값은 **그 순간 보여지는 화면을 기준으로 계산**하기 때문에 스크롤 위치와는 무관하게 **항상 보여지는 화면의 좌측 상단의 모서리 위치를 (0, 0)으로 계산**합니다.

### 2. offsetX, offsetY

`offset` 프로퍼티는 **이벤트가 발생한 target이 기준**이 됩니다.

offsetX : 이벤트가 발생한 `target` 내에서 마우스의 X좌표 위치를 담고 있습니다. offsetY : 이벤트가 발생한 `target` 내에서 마우스의 Y좌표 위치를 담고 있습니다.

`offset` 값도 **이벤트가 발생한 대상을 기준으로 계산**하기 때문에 스크롤 위치와는 무관하게 **항상 대상의 좌측 상단의 모서리 위치를 (0, 0)으로 계산**합니다.

### 3. pageX, pageY

page 프로퍼티는 **전체 문서를 기준**으로 마우스 좌표 정보를 담고 있습니다. 그렇기 때문에 스크롤로 인해서 보이지 않게된 화면의 영역까지 포함해서 측정한다는 점이 앞의 두 프로퍼티와의 차이점 입니다.

pageX : 전체 문서 내에서 마우스의 X좌표 위치를 담고 있습니다. pageY : 전체 문서 내에서 마우스의 Y좌표 위치를 담고 있습니다.

자칫 `client` 값과 혼동하기 쉬우니 잘 구분해 두시는 것이 좋습니다.

### 그림으로 정리하기

그림으로 정리하면 좀 더 이해하기 쉬울테니 참고해 두시면 좋을 것 같아요!

![clientpageoffset](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3817&directory=clientpageoffset&name=clientpageoffset)





## 3. 키보드 이벤트

키보드와 관련된 이벤트의 경우에는 아래와 같은 이벤트 객체의 프로퍼티들을 가지고 있습니다.

|프로퍼티|설명|
|--|--|
|key|누른 키가 가지고 있는 값|
|code|누른 키의 물리적인 위치|
|altKey|이벤트가 발생할 때 alt키를 눌렀는지|
|ctrlKey|이벤트가 발생할 때 ctrl키를 눌렀는지|
|shiftKey|이벤트가 발생할 때 shift키를 눌렀는지|
|metaKey|이벤트가 발생할 때 meta키를 눌렀는지 (window는 window키, mac은 cmd키)|


이 프로퍼티들은 자주 사용되는 프로퍼티일 뿐 이벤트 객체의 모든 프로퍼티가 아닙니다. 혹시 이벤트 객체의 더 많은 프로퍼티들이 궁금하시다면 아래 링크를 참고해 보세요!

-   [이벤트](https://developer.mozilla.org/en-US/docs/Web/API/Event)
-   [마우스 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/MouseEvent)
-   [키보드 이벤트](https://developer.mozilla.org/en-US/docs/Web/API/KeyboardEvent)



