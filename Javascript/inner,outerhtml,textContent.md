지난 시간에 살펴본 요소 노드의 프로퍼티들을 한 번 더 복습하고 넘어갑시다!

```html
<!DOCTYPE html>
<html lang="ko">
<head>
  <meta charset="UTF-8">
  <title>JS with Codeit</title>
</head>
<body>
  <div id="content">
    <h2 id="title-1">Cat-1</h1>
    <ul id="list-1">
      <li>Ragdoll</li>
      <li>British Shorthair</li>
      <li>Scottish Fold</li>
      <li>Bengal</li>
      <li>Siamese</li>
      <li>Maine Coon</li>
      <li>American Shorthair</li>
      <li>Russian Blue</li>
    </ul>
    <h2 id="title-2">Cat-2</h1>
    <ul id="list-2">
      <li>Sphynx</li>
      <li>Munchkin</li>
      <li>Persian</li>
      <li>Norwegian Forset</li>
      <li>Turkish Angora</li>
      <li>Bombay</li>
      <li>Selkirk Rex</li>
      <li>Munchkin</li>
    </ul>
  </div>
  <script src="index.js"></script>
</body>
</html>

```

# 1. element.innerHTML

-   요소 노드 내부의 HTML 코드를 문자열로 리턴해 줍니다. (내부에 있는 줄 바꿈이나 들여쓰기 모두 포함합니다.)

```js
const myTag = document.querySelector('#list-1');

// innerHTML
console.log(myTag.innerHTML);

```

![innerHTMLouterHTMLtextContent](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent&name=innerHTMLouterHTMLtextContent)

-   요소 안의 정보를 확인할 수도 있지만, 내부의 HTML 자체를 수정할 때 좀 더 자주 활용됩니다. (내부에 있던 값을 완전히 새로운 값으로 교체하기 때문에 주의해서 사용해야해요!)

```js
const myTag = document.querySelector('#list-1');

// innerHTML
console.log(myTag.innerHTML);
myTag.innerHTML = '<li>Exotic</li>';
console.log(myTag.innerHTML);

```

![innerHTMLouterHTMLtextContent-2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent-2&name=innerHTMLouterHTMLtextContent-2)

# 2. element.outerHTML

-   요소 노드 자체의 전체적인 HTML 코드를 문자열로 리턴해줍니다. (내부에 있는 줄 바꿈이나 들여쓰기 모두 포함합니다.)

```js
const myTag = document.querySelector('#list-1');

// outerHTML
console.log(myTag.outerHTML);

```

![innerHTMLouterHTMLtextContent-3](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent-3&name=innerHTMLouterHTMLtextContent-3)

-   `outerHTML`은 새로운 값을 할당할 경우 요소 자체가 교체되어 버리기 때문에 주의해야 합니다.

```js
const myTag = document.querySelector('#list-1');

// outerHTML
console.log(myTag.outerHTML);
myTag.outerHTML = '<ul id="new-list"><li>Exotic</li></ul>';

```

![innerHTMLouterHTMLtextContent-4](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent-4&name=innerHTMLouterHTMLtextContent-4)

# 3. element.textContent

-   요소 안의 내용들 중에서 HTML 태그 부분은 제외하고 텍스트만 가져옵니다. (내부에 있는 줄 바꿈이나 들여쓰기 모두 포함합니다.)

```js
const myTag = document.querySelector('#list-1');

// textContext
console.log(myTag.textContent);

```

![innerHTMLouterHTMLtextContent-5](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent-5&name=innerHTMLouterHTMLtextContent-5)

-   새로운 값을 할당하면  `innerHTML`과 마찬가지로 내부의 값을 완전히 새로운 값으로 교체 합니다.

```js
const myTag = document.querySelector('#list-1');

// textContext
console.log(myTag.textContent);
myTag.textContent = 'new text!';

```

![innerHTMLouterHTMLtextContent-6](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent-6&name=innerHTMLouterHTMLtextContent-6)

-   하지만  `textContent`는 말그대로 텍스트만 다루기 때문에, 특수문자도 그냥 텍스트로 처리한다는 점, 꼭 기억해주세요!

```js
const myTag = document.querySelector('#list-1');

// textContext
console.log(myTag.textContent);
myTag.textContent = '<li>new text!</li>';

```

![innerHTMLouterHTMLtextContent-7](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3789&directory=innerHTMLouterHTMLtextContent-7&name=innerHTMLouterHTMLtextContent-7)
