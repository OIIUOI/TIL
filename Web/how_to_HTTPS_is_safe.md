# HTTPS

> 내가 어떤 웹사이트에 보내는 정보를 다른 누군가 훔쳐보지 못하게 한다
> 
> 로그인 할 때라면 뒤죽박죽 된 텍스트로 변경해서 보냄
> 
> 1. 내가 사이트에 보내는 정보들을 제 3자가 못 보게 함
> 
> 2. 접속한 사이트가 믿을 만한 곳인지를 알려준다 -> 비대칭키로 피싱사이트 거름

## 대칭키, 비대칭키

> 대칭키는 똑같은 키를 가지고 있어서 ASDF를 1번키로 *&^%라고 보내고 다시 1번 키로 ASDF로 번역
> 
> 비대칭키는 ASDF를 공개키로 *&^%라고 보내고 개인키로 ASDF로 번역하는데 개인키가 아니면 해석X, 따라서 피싱사이트를 거를 수 있다



네이버에서 우리에게 보내는 정보들은 일부가 네이버의 개인키로 암호화가 되어있고 네이버의 공개키로 풀어서 알아볼 수 있는건 네이버의 개인키로 암호화된 정보들 뿐이다

네이놈에서 온 정보들은 네이버의 공개키로 풀리지 않기 때문에 네이버의 공개키로 열어보려하면 오류가 날 것

신뢰할 수 있는 기관에서 우리에게 네이버의 공개키만 검증해준다면 우린 이걸 기준으로 안전하게 네이버를 이용할 수 있다

네이버가 뿌린 공개키가 정품인지 확인할 수 있어야 한다 이게 네이놈의 공개키일 수도 있으니까

이걸 공인된 민간기업들이 있는데 CA라고 부름

브라우저인 크롬 사파리 파이어폭스 등등에는 이 CA의 목록이 내장되어있다

클라이언트는 아직 사이트를 신뢰하지 못해서 탐색을 하는데 HANDSHAKE(악수) 라고 부

------------------------------------------악수----------------------------------------------

우선 클라이언트가 랜덤 데이터를 생성해서 서버에 보냄

서버는 답변으로 무작위 데이터 + 해당 사이트의 인증서를 보냄

--------------------------------------------끝------------------------------------------------

---------브라우저가 인증서가 진짜인지 확인하는 과정(비대칭키)----------

CA의 인증을 받은 인증서들은 해당 CA의 개인키로 암호화가 되어있어

CA의 공개키로 복호화가 되어 네이버인 걸 알 수 있음!

복호화가 안 된다? CA인증 X 못믿는 사이트

----------------------------------------------끝------------------------------------------------

네이버인 걸 확실화 한 다음에는 비대칭키을 끝내고 대칭키를 쓰는데

비대칭키 방식으로 메시지를 암호화 및 복화하면 컴퓨터에 훨씬 큰 부담이기 때문

사이트 이용할 때마다 다량의 데이터를 비대칭으로 하는 것은 무리

아까 악수할 때 받은 2개의 랜덤 데이터를 혼합해 어떤 문자열을 만들어

클라이언트가 공개키를 이용해 서버로 보내고 이 보내진 문자열이 일련의 과정을 거쳐

양쪽에서 대칭키로 만들어짐, 이 대칭키는 서버와 클라이언트 둘만 갖고 있어

이후 서로 주고받아지는 데이터를 3자가 알아볼 수 없음
