대부분의 브라우저에 있는 개발자 도구는 `console.log`와 `console.dir`메소드를 지원합니다. 두 메소드 모두 파라미터로 전달받은 값을 콘솔에 출력하는 역할을 합니다. 과연 이 둘은 어떤 차이가 있을까요?

```js
const str = 'Codeit';
const num = 123;
const bool = true;
const arr = [1, 2, 3];
const obj = {
  name: 'Codeit',
  email: 'codeit@codeit.kr',
};

function func() {
  console.log('I love Codeit!');
}

console.log('--- str ---');
console.log(str);
console.dir(str);
console.log('--- num ---');
console.log(num);
console.dir(num);
console.log('--- bool ---');
console.log(bool);
console.dir(bool);
console.log('--- arr ---');
console.log(arr);
console.dir(arr);
console.log('--- obj ---');
console.log(obj);
console.dir(obj);
console.log('--- func ---');
console.log(func);
console.dir(func);

```

![console.dir?-1](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3783&directory=console.dir?-1.png&name=console.dir%3F-1.png)

이렇게 다양한 유형의 값들을 만들어서 출력 결과를 놓고서 천천히 비교해봅시다.

# 1. 출력하는 자료형이 다르다.

![console.dir?-2](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3783&directory=console.dir?-2.png&name=console.dir%3F-2.png)

먼저 문자열, 숫자, 불린 부분을 봅시다. 각 값을 출력할 때 두 번째 `dir` 부분에서 출력되는 값의 색이 다른 게 보이시나요? **dir 메소드는 문자열 표시 형식으로 콘솔에 출력**합니다.

# 2. log는 값 자체에, dir은 객체의 속성에!

![console.dir?-3](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3783&directory=console.dir?-3.png&name=console.dir%3F-3.png)

`log` 메소드는 **파라미터로 전달받은 값**을 위주로 출력하는 반면, `dir` 메소드는 **객체의 속성**을 좀 더 자세하게 출력합니다.

`dir` 메소드가 출력한 부분을 자세히 보면 객체의 유형이 먼저 출력되고, 특히 함수 부분에서는 클릭해서 펼쳤을 때 함수가 가진 속성들을 더 보여주는 모습을 확인할 수 있습니다. (`log` 메소드는 펼쳐지지 않음)

# 3. log는 여러 개, dir은 하나만!

```js
console.log(str, num, bool, arr, obj, func);
console.dir(str, num, bool, arr, obj, func);

```

![console.dir?-4](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3783&directory=console.dir?-4.png&name=console.dir%3F-4.png)

둘 사이의 차이는 파라미터로 전달할 수 있는 값의 개수에도 있는데요. `log` 메소드는 여러 값을 쉼표로 구분해서 전달하면 전달받은 **모든 값을 출력**하는 반면, `dir` 메소드는 여러 값을 전달하더라도 **첫 번째 값만 출력**합니다.

# 4. DOM 객체를 다룰 때..

```js
const myDOM = document.body;

console.log(myDOM);
console.dir(myDOM);

```

![console.dir?-5](https://bakey-api.codeit.kr/api/files/resource?root=static&seqId=3783&directory=console.dir?-5.png&name=console.dir%3F-5.png)

지난 시간에도 확인했듯 `log`와 `dir` 메소드의 가장 큰 차이는 DOM 객체를 다룰 때 나타납니다. 값에 좀 더 중점을 둔 **log 메소드는 대상을 HTML 형태로 출력**하고, 객체의 속성에 좀 더 중점을 둔 **dir 메소드는 대상을 객체 형태로 출력**합니다.

# 마무리

지금까지 `console` 객체의 `log` 메소드와 `dir` 메소드의 차이점에 대해 살펴봤는데요. **콘솔에서 값 자체를 확인하고 싶다면** `log`메소드를, **객체의 속성들을 살펴보고 싶다면** `dir` 메소드를 활용하면 좋을 것 같습니다.
