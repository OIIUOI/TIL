# Javascript

id select = #idname

class select = .classname



# 1. 자바스크립트로 태그 선택하기

| 메소드                                      | 의미                     | 결과                                |
| ---------------------------------------- | ---------------------- | --------------------------------- |
| document.getElementById('id')            | HTML id속성으로 태그 선택하기    | id에 해당하는 태그 하나                    |
| document.getElementsByClassName('class') | HTML class속성으로 태그 선택하기 | class에 해당하는 태그 모음(HTMLCollection) |
| document.getElementsByTagName('tag')     | HTML 태그 이름으로 태그 선택하기   | tag에 해당하는 태그 모음(HTMLCollection)   |
| document.querySelector('css')            | css 선택자로 태그 선택하기       | css 선택자에 해당하는 태그 중 가장 첫번째 태그 하나   |
| document.querySelectorAll('css')         | css 선택자로 태그 선택하기       | css 선택자에 해당하는 태그 모음(NodeList)     |

# 2. 유사 배열이란?

- 배열과 유사한 객체 ex) HTMLCollection, NodeList, DOMTokenList, ...

## 특징

1. 숫자 형태의 indexing이 가능하다.
2. `length` 프로퍼티가 있다.
3. 배열의 기본 메소드를 사용할 수 없다.
4. `Array.isArray(유사배열)`의 리턴값은 `false`다.

# 3. 이벤트와 이벤트 핸들링, 그리고 이벤트 핸들러

- 이벤트 : 웹 페이지에서 발생하는 대부분의 일(사건)들
   ex) 버튼 클릭, 스크롤, 키보드 입력, ...

- 이벤트 핸들링 : 자바스크립트를 통해 이벤트를 다루는 일

- 이벤트 핸들러 : 이벤트가 발생했을 때 일어나야하는 구체적인 동작들을 표현한 코드. **이벤트 리스너(Event Listener)**라고도 부른다.

# 4. 이벤트 핸들러를 등록하는 2가지 방법

## 4-1. 자바스크립트로 해당 DOM 객체의 onclick 프로퍼티에 등록하기

```js
const btn = document.querySelector('#myBtn');

btn.onclick = function() {
  console.log('Hello Codeit!');
};
```

## 4-2. HTML 태그의 onclick 속성에 바로 표시하기

```html
<button id="myBtn" onclick="console.log('Hello Codeit!')">클릭!</button>
```

이번 레슨은 어땠나요?
