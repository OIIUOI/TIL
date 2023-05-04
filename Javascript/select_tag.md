

지금까지 `id`와 `class` 속성을 이용해서 JavaScript로 HTML 태그를 선택하는 방법에 대해 알아봤는데요. `document.getElementsByTagName('태그이름')`메소드를 활용하면 태그 이름으로 태그를 선택할 수 있습니다.

```js
const btns = document.getElementsByTagName('button');

```

이렇게 하면 HTML 문서 내에 있는 모든 `button` 태그를 선택하게 됩니다.

![태그이름으로태그선택하기](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3827&directory=%E1%84%90%E1%85%A2%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%84%85%E1%85%B3%E1%86%B7%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9%E1%84%90%E1%85%A2%E1%84%80%E1%85%B3%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5&name=%E1%84%90%E1%85%A2%E1%84%80%E1%85%B3%E1%84%8B%E1%85%B5%E1%84%85%E1%85%B3%E1%86%B7%E1%84%8B%E1%85%B3%E1%84%85%E1%85%A9%E1%84%90%E1%85%A2%E1%84%80%E1%85%B3%E1%84%89%E1%85%A5%E1%86%AB%E1%84%90%E1%85%A2%E1%86%A8%E1%84%92%E1%85%A1%E1%84%80%E1%85%B5)

`document.getElementsByClassName('class')`메소드와 마찬가지로 태그 이름으로 요소를 찾는 경우에 여러 개의 요소가 선택될 수 있기 때문에 메소드 이름에 `Element(s)`, _s_가 있고, 실행결과 역시 HTMLCollection을 리턴한다는 점도 함께 기억해 두시면 좋을 것 같습니다.

참고로 css 선택자처럼 `'*'` 값을 전달하게 되면 모든 태그를 선택할 수도 있는데요.

```js
const btns = document.getElementsByTagName('button');
const allTags = document.getElementsByTagName('*');

```

하지만, css 스타일링을 할 때도 태그 이름으로 스타일링을 하는 경우는 거의 없죠?

마찬가지로 명확한 의도가 없이 이렇게 많은 요소들을 한꺼번에 다루게 되면 예상치 못한 실수를 할 가능성이 있기 때문에 자바스크립트에서도 많이 사용되는 메소드는 아닙니다.
