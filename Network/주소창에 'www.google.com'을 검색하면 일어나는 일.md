# 주소창에 'www.google.com'을 입력하면 일어나는 일
🤔주소창에 'www.google.com'을 입력하면 어떤 작업들이 일어나서 우리의 PC에 구글 사이트가 보여질까?
<br>웹이 어떻게 동작하는 지에 대해서 알아보도록 하자!

## 용어 정리
- **DNS (Domain Name System Servers)**
<br>    **'도메인 이름 시스템 서버'** 는 URL들의 이름과 IP주소를 저장하고 있는 데이터베이스로, **웹사이트를 위한 주소록**이라고 생각하면 된다.
<br>    숫자로 된 IP주소(ex. 63.245.217.105) 대신 사용자가 사용하기 편리하도록 주소를 매핑해주는 역할을 한다.
<br>    도메인을 컴퓨터가 처리할 수 있는 숫자로 된 IP주소로 바꾸는 시스템 혹은 이런 역할을 하는 서버 컴퓨터라고 할 수 있다.

- **TCP/IP (Transmission Control Protocol / Internet Protocol)**
<br>    **'전송제어규약'** 과 **'인터넷규약'** 은 데이터가 어떻게 웹을 건너 여행하는지 정의하는 통신 규약이다.
<br>    이를 사용하겠다는 것은, IP주소 체계를 따르며 TCP의 특성을 활용해 송신자와 수신자의 논리적 연결을 생성하고 신뢰성을 유지할 수 있도록 하겠다는 의미이다. 
<br>    즉 **송신자가 수신자에게 IP주소를 사용해서 데이터를 전달하고 그 데이터가 제대로 갔는지**에 대해 이야기하는 것이다.

- **HTTP (Hypertext Transfer Protocol)**
<br>    클라이언트와 서버가 서로 통신할 수 있게 하기 위한 언어를 정의하는 어플리케이션 규약으로, 쉽게 말해 요청과 응답으로 이루어져 있어 "어떤 데이터 주세요"라고 요청하면,
"이 데이터 줄게요" 라고 응답하는 것이라고 할 수 있다.
<br>    주로 HTML문서를 주고 받는데에 사용된다.

## 웹 동작과정
이제 본론으로 돌아가서 브라우저 주소창에 'www.google.com' 입력하면 어떻게 되는지 웹 동작과정을 알아보자.
<p align="center"><img src="https://media.vlpt.us/images/eassy/post/44f24431-5192-477d-b36c-87fc0b10a204/image.png" width="60%" height="60%" align="center"></img></p>

### 1. 사용자가 웹브라우저 검색창에 www.google.com 입력한다.
### 2. 웹브라우저는 캐싱된 DNS 기록들을 통해 해당 도메인 주소와 대응하는 IP주소가 있는지 확인한다.
캐싱된 기록에 없을 경우, 다음 단계로 넘어간다.
### 3. 웹브라우저가 HTTP를 사용하여 DNS에게 입력된 도메인 주소를 요청한다.
### 4. DNS가 웹브라우저에게 찾는 사이트의 IP주소를 응답한다.
ISP(Internet Service Provider)의 DNS서버가 호스팅하고 있는 서버의 IP주소를 찾기 위해 DNS query를 날린다.
<details>
<summary>DNS query의 목적</summary>
<div markdown="1">

DNS query의 목적
DNS 서버들을 검색해서 해당 사이트의 IP주소를 찾는데에 있다.
IP주소를 찾을 때 까지 DNS서버에서 다른 DNS서버를 오가며 에러가 날때까지 반복적으로 검색한다. = recursive search
DNS recursor(ISP의 DNS서버)는 name server들에게 물어물어 올바른 IP주소를 찾는데에 책임이 있다. name server는 도메인 이름 구조에 기반해서 주소를 검색하게 되는데, 예를 들어 설명해보자면,

<p align="center"><img src="https://devjin-blog.com/static/df40acaf929fb371a270155e2ef49a36/fcda8/browser_work_dns_2.png" width="60%" height="60%" align="center"></img></p>

'www.google.com' 주소에 대해 검색할 때,
1. DNS recursor가 root name server에 연락
2. .com 도메인 name server로 리다이렉트
3. google.com name server로 리다이렉트
4. 최종적으로 DNS기록에서 'www.google.com' 에 매칭되는 IP주소 찾기
5. 찾은 주소를 DNS recursor로 보내기
이 모든 요청들과 DNS recursor, IP주소는 작은 데이터 패킷을 통해 보내진다.
원하는 DNS기록을 가진 DNS서버에 도달할 때까지
클라이언트 ↔️ 서버를 여러번 오가는 과정을 거친다.

</div>
</details>

### 5. 웹브라우저가 웹서버에게 IP주소를 이용하여 html문서를 요청한다.
TCP로 연결이 되면, 브라우저는 GET요청을 통해 서버에게 www.google.com의 웹페이지를 요구한다.
### 6. 웹어플리케이션서버(WAS)와 데이터베이스에서 우선 웹페이지 작업을 처리한다.
웹 서버 혼자서 모든 로직을 수행하고 데이터를 관리할 수 있다면 간단하겠지만 서버에 과부하가 일어날 수 있다.
그렇기 때문에 서버의 일을 돕는 조력자 역할을 하는 것이 `웹어플리케이션서버(Web Application Server)`이다.
WAS는 **사용자의 컴퓨터나 장치에 웹어플리케이션을 수행해주는 미들웨어**를 말한다.

브라우저로부터 요청을 받으면,
웹서버는 페이지의 로직이나 데이터베이스(DB)의 연동을 위해 WAS에게 이들의 처리를 요청한다.
그러면 WAS는 이 요청을 받아 동적인 페이지처리를 담당하고,
DB에서 필요한 데이터 정보를 받아서 파일을 생성한다.

<details>
<summary>웹서버와 웹어플리케이션서버(WAS)의 차이점</summary>
<div markdown="1">
  
- **웹서버** : 정적인 컨텐츠(HTML, CSS, IMAGE 등)를 요청받아 처리<br>
  - 종류 : IIS, apache, tMax WebtoB
- **WAS** : 동적인 컨텐츠(JSP, ASP, PHP 등)를 요청받아 처리<br>
  - 종류 : tomcat, tMax jeus, BEA Web Logic, IBM Web Spere, JBOSS, Bluestone, Gemston, Inprise, Oracle, PowerTier, Apptivity, SilverStream<br>
    => DB서버에 대한 접속 정보가 있기 때문에 외부에 노출 될 경우 보안상의 문제를 이유로 웹서버와의 연결을 통해 요청을 전달받음
  
</div>
</details>

### 6. 위의 작업처리 결과를 웹서버로 전송한다.
### 7. 웹서버는 웹브라우저에게 html 문서결과를 응답해준다.
response는 status code로 서버 요청에 따른 상태를 보낸다.
다음과 같은 5가지의 종류가 있다.

- 1xx : 정보만 담긴 메세지
- 2xx : response 성공
- 3xx : 클라이언트를 다른 URL로 리다이렉트
- 4xx : 클라이언트 측에서 에러 발생
- 5xx : 서버 측에서 에러 발생
### 8. 웹브라우저는 화면에 웹페이지 내용물 출력한다.

## References
[[번역] Browser에 www.google.com을 검색하면 어떤 일이 일어날까?](https://devjin-blog.com/what-happen-browser-search/)  
[웹의 동작방식](https://developer.mozilla.org/ko/docs/Learn/Getting_started_with_the_web/How_the_Web_works)  
[WAS](https://enderbridge.tistory.com/37)
