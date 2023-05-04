# 비표준 속성 활용하기

## 1. 선택자로 활용

가장 간단하게는 아래와 같이 `querySelector`로 태그를 선택할 때 css 선택자를 활용해서 태그를 선택하는 데에 활용할 수도 있습니다.

```js
const fields = document.querySelectorAll('[field]');
console.log(fields);

```

![비표준속성다루기](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3829&directory=%E1%84%87%E1%85%B5%E1%84%91%E1%85%AD%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5&name=%E1%84%87%E1%85%B5%E1%84%91%E1%85%AD%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5)

## 2. 값을 표시할 태그를 구분할 때 활용

비표준 속성은 객체 형태의 데이터가 있을 때, 각 프로퍼티 값들이 들어갈 태그를 구분하는데 활용할 수도 있습니다.

```js
const fields = document.querySelectorAll('[field]');
const task = {
  title: '코드 에디터 개발',
  manager: 'CastleRing, Raccoon Lee',
  status: '',
};

for (let tag of fields) {
  const field = tag.getAttribute('field');
  tag.textContent = task[field];
}

```

![비표준속성다루기-2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3829&directory=%E1%84%87%E1%85%B5%E1%84%91%E1%85%AD%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5-2&name=%E1%84%87%E1%85%B5%E1%84%91%E1%85%AD%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5-2)

## 3. 스타일이나 데이터 변경에 활용

`getAttribute` 메소드를 활용해서 속성값을 가져오고, `setAttribute` 메소드를 활용해서 속성값을 설정해주는 원리로 이벤트를 통해 실시간으로 스타일을 변경하거나 데이터를 변경하는데 활용할 수 있습니다.

때로는 `class`를 다루는 것보다 `setAttribute`로 비표준 속성을 변경하는게 스타일을 다루기에 오히려 편리한 경우도 있습니다.

```js
const fields = document.querySelectorAll('[field]');
const task = {
  title: '코드 에디터 개발',
  manager: 'CastleRing, Raccoon Lee',
  status: '',
};

for (let tag of fields) {
  const field = tag.getAttribute('field');
  tag.textContent = task[field];
}

const btns = document.querySelectorAll('.btn');
for (let btn of btns) {
  const status = btn.getAttribute('status');
  btn.onclick = function () {
    fields[2].textContent = status;
    fields[2].setAttribute('status', status);
  };
}

```

![비표준속성다루기-3](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3829&directory=%E1%84%87%E1%85%B5%E1%84%91%E1%85%AD%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5-3&name=%E1%84%87%E1%85%B5%E1%84%91%E1%85%AD%E1%84%8C%E1%85%AE%E1%86%AB%E1%84%89%E1%85%A9%E1%86%A8%E1%84%89%E1%85%A5%E1%86%BC%E1%84%83%E1%85%A1%E1%84%85%E1%85%AE%E1%84%80%E1%85%B5-3)

# 좀 더 안전하게, dataset 프로퍼티

다양한 방식으로 활용되는 비표준 속성에는 한 가지 문제가 있습니다. 비표준 속성을 사용해 코드를 작성했을 때 시간이 지나서 나중에 그 속성이 표준으로 등록되면 문제가 발생할 수 있다는 건데요. HTML은 아직까지도 개발자들의 요구를 반영하기 위해 계속해서 발전하는 언어입니다. 그래서 이런 경우 예기치 못한 부작용이 발생할 수 있는 것이죠.

예를 들어서, 만약 `glitter`라는 비표준 속성을 만들어서 `glitter` 속성값이 `true`면 마우스를 올렸을 때 주변에 별이 반짝이는 애니메이션이 동작하도록 프로그램를 설계했다고 가정해봅시다. 그런데 갑자기 `glitter`라는 속성이 `true`일 때 태그가 계속 깜빡거리는 기능을 하는 표준으로 생겨나버리면 우리가 처음에 설계한 방식대로 동작하지 않을 수 있겠죠?

그래서 비표준 속성을 사용하기 위해 미리 약속된 방식이 존재하는데요. 바로 `data-*` 속성입니다.

`data-`로 시작하는 속성은 모두 dataset이라는 프로퍼티에 저장되는데요. 예를 들어서 `data-status`라는 속성이 있다면, `element.dataset.status`라는 프로퍼티에 접근해서 그 값을 가져올 수 있는 것이죠.

그래서 본문의 코드도 아래와 같이 고치고,

-   HTML
-   CSS

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <title>JS with Codeit</title>
</head>

<body>
  <p>할 일 : <b data-field="title"></b></p>
  <p>담당자 : <b data-field="manager"></b></p>
  <p>상태 : <b data-field="status"></b></p>
  <div>
    상태 변경: 
    <button class="btn" data-status="대기중">대기중</button>
    <button class="btn" data-status="진행중">진행중</button>
    <button class="btn" data-status="완료">완료</button>
  </div>
  <script src="index.js"></script>
</body>

</html>

```

결과 확인

자바스크립트 코드도 다음과 같이 고쳐주면,

```js
const fields = document.querySelectorAll('[data-field]');
const task = {
  title: '코드 에디터 개발',
  manager: 'CastleRing, Raccoon Lee',
  status: '',
};

for (let tag of fields) {
  const field = tag.dataset.field;
  tag.textContent = task[field];
}

const btns = document.querySelectorAll('.btn');
for (let btn of btns) {
  const status = btn.dataset.status;
  btn.onclick = function () {
    fields[2].textContent = status;
    fields[2].dataset.status = status;
  };
}

```

조금 더 안전하게 비표준 속성을 활용할 수 있습니다.

# 동작확인하기

아래 코드를 실행해서 상태변경 버튼을 클릭해 보세요!

-   HTML
-   CSS

```html
<!DOCTYPE html>
<html lang="ko">

<head>
  <meta charset="UTF-8">
  <title>JS with Codeit</title>
</head>

<body>
  <p>할 일 : <b data-field="title"></b></p>
  <p>담당자 : <b data-field="manager"></b></p>
  <p>상태 : <b data-field="status"></b></p>
  <div>
    상태 변경: 
    <button class="btn" data-status="대기중">대기중</button>
    <button class="btn" data-status="진행중">진행중</button>
    <button class="btn" data-status="완료">완료</button>
  </div>
  <script>
    const fields = document.querySelectorAll('[data-field]');
    const task = {
      title: '코드 에디터 개발',
      manager: 'CastleRing, Raccoon Lee',
      status: '',
    };

    for (let tag of fields) {
      const field = tag.dataset.field;
      tag.textContent = task[field];
    }

    const btns = document.querySelectorAll('.btn');
    for (let btn of btns) {
      const status = btn.dataset.status;
      btn.onclick = function () {
        fields[2].textContent = status;
        fields[2].dataset.status = status;
      };
    }
  </script>
</body>

</html>

```

결과 확인

# 마무리

사실 비표준 속성을 활용하는 것은 개발자의 선택적인 부분입니다. 반드시 비표준 속성을 활용해야만 하는 상황은 아마 없을지도 모릅니다. 하지만 상황에 따라서 비표준 속성이 필요할 수도 있고 혹은 비표준 속성을 활용하는 것이 조금 더 효율적일 수도 있으니 다양한 상황들을 고려해서, 만약 비표준 속성을 활용해야 한다면 `data-*`형태와 `dataset`프로퍼티를 사용하는 것이 조금 더 안전하다는 점도 꼭 잊지 말고 기억해두시면 좋을 것 같습니다.
