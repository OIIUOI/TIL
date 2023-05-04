이벤트엔 버블링 이외에도 **‘캡처링(capturing)’** 이라는 흐름이 존재합니다. 실제 코드에서 자주 쓰이진 않지만, 상황에 따라 필요할 수도 있으니 간단하게 살펴봅시다.

먼저, 표준 [DOM 이벤트](https://www.w3.org/TR/DOM-Level-3-Events/)에서 정의한 이벤트 흐름에는 3가지 단계가 있습니다.

1.  캡처링 단계: 이벤트가 하위 요소로 전파되는 단계
2.  타깃 단계: 이벤트가 실제 타깃 요소에 전달되는 단계
3.  버블링 단계: 이벤트가 상위 요소로 전파되는 단계

**버블링 단계**는 이미 지난 시간에 배웠죠? **타깃 단계**는 이벤트 객체의 `target` 프로퍼티가 되는 요소에 등록되어있던 이벤트 핸들러가 동작하는 단계인데, 쉽게 생각해서 **가장 처음 이벤트 핸들러가 동작하게 되는 순간**이라고 생각하시면 됩니다.

자, 그럼 이제 **캡쳐링**에 대해서 좀 더 알아볼까요?

# 캡쳐링

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>JS with Codeit</title>
  </head>
  <body>
    <div id="content">
      <h1 id="title">오늘 할 일</h1>
      <ol id="list">
        <li class="item">자바스크립트 공부</li>
        <li class="item">독서</li>
      </ol>
    </div>
    <script src="index.js"></script>
  </body>
</html>

```

만약 위 코드에서 **자바스크립트 공부**를 클릭한다면, 버블링은 `li`태그 부터, `ol`태그, `div`태그, `body`태그, `html`태그, `document`, `window` 객체로 이벤트가 전파가 된다는 거 알고 계시죠? **캡쳐링**은 **이벤트가 발생하면 가장 먼저, 그리고 버블링의 반대 방향으로 진행되는 이벤트 전파 방식**입니다.

아래 이미지를 한번 보세요.

![캡쳐링](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3807&directory=%E1%84%8F%E1%85%A2%E1%86%B8%E1%84%8E%E1%85%A7%E1%84%85%E1%85%B5%E1%86%BC.png&name=%E1%84%8F%E1%85%A2%E1%86%B8%E1%84%8E%E1%85%A7%E1%84%85%E1%85%B5%E1%86%BC.png)

이벤트가 발생하면 가장 먼저 `window` 객체에서부터 `target` 까지 이벤트 전파가 일어납니다. (캡쳐링 단계) 그리고 나서 타깃에 도달하면 타깃에 등록된 이벤트 핸들러가 동작하고, (타깃 단계) 이후 다시 `window` 객체로 이벤트가 전파됩니다. (버블링 단계)

이런 과정을 통해 각 요소에 할당된 이벤트 핸들러가 호출되는데요.

캡쳐링 단계에서 이벤트를 발생시켜야 하는 일은 매우 드문 경우입니다. 보통 타깃 단계에서 `target`에 등록된 이벤트 핸들러가 있으면 해당 이벤트 핸들러가 먼저 동작한 이 후에 버블링 단계에서 각 부모 요소에 등록된 이벤트 핸들러가 있으면 그 때 해당 이벤트 핸들러가 동작하는 것이 일반적인데요.

하지만 상황에 따라서는 캡쳐링 단계에서 부모 요소의 이벤트 핸들러를 동작시켜야 할 수도 있겠죠? 캡쳐링 단계에서 이벤트 핸들러를 동작시키려면, `addEventListener`에 세번째 프로퍼티에 `true` 또는 `{ capture:true }`를 전달하면 됩니다. 아래 코드를 실행해서 각 태그들을 클릭해 보세요.

-   HTML
-   CSS

```html
<!DOCTYPE html>
<html lang="ko">
  <head>
    <meta charset="UTF-8">
    <title>Codeit Acid Rain</title>
    <link rel="stylesheet" href="style.css">
  </head>
  <body>
    <div>DIV
      <ul>UL
        <li>LI</li>
      </ul>
    </div>  
    <script>
      for (let elem of document.querySelectorAll('*')) {
        elem.addEventListener("click", e => alert(`캡쳐링 단계: ${elem.tagName}`), true);
        elem.addEventListener("click", e => alert(`버블링 단계: ${elem.tagName}`));
      }
    </script>
  </body>
</html>

```

결과 확인

앞서 언급한 것처럼 캡쳐링은 흔하게 접할 만한 상황이 아니기 때문에 일부러 간략하게만 다뤘습니다.

혹시나 캡쳐링과 함께 자바스크립트의 이벤트에 더 궁금한 부분이 있다면 아래 링크를 참고해 주세요!

-   [표준 DOM 이벤트](https://www.w3.org/TR/DOM-Level-3-Events/)
-   [자바스크립트의 이벤트 순서](https://www.quirksmode.org/js/events_order.html#link4)
-   [addEventListner에 캡쳐링 단계 적용하기](https://developer.mozilla.org/ko/docs/Web/API/EventTarget/addEventListener)
