# 01_HTML&CSS

> [강의자료](https://edu.ssafy.com/data/upload_files/crossUpload/openLrn/ebook/unzip/A2022012813080928300/index.html) 2022-02-03

- **HTML & CSS**
  - 이제 더 이상 익스플로러는 브라우저가 아니다. 크롬만이 브라우저다!
  - 웹 개발 할 때도 크롬 위주로 보면 된다.

- Can I use?
  - 이전에는 브라우저마다 지원되는 프로그램이 달라서, 어느 브라우저에서 사용할 수 있는지 확인 가능한 사이트

- 개발 환경 설정 - Text editor

  - Visual Studio Code

    - HTML / CSS 코드 작성을 위한 Visual Studio Code 추천 확장 프로그램

      - Open in browser

      - Auto rename tag

      - Highlight Matching Tag

      - CSS Peek

      - IntelliSense for CSS class names in HTML

        

- 개발 환경 설정 - 크롬 개발자 도구

  - 웹 브라우저 크롬에서 제공하는 개발과 관련된 다양한 기능을 제공

  - 주요 기능

    - Elements - DOM 탐색 및 CSS 확인 및 변경

      - Styles - 요소에 적용된 CSS 확인
      - Computed - 스타일이 계산된 최종 결과
      - Event Listeners - 해당 요소에 적용된 이벤트 (JS)

    - Sources, Network, Performance, Application, Security, Audits 등

      

## HTML

- **HTML?**
  - Hyper Text Markup Language
  - 웹 페이지를 작성(구조화)하기 위한 언어
  
- **Hyper Text**

  - 참조(하이퍼링크)를 통해 사용자가 한 문서에서 다른 문서로 즉시 접근할 수 있는 텍스트

  - 위키 시스템과 유사!

- **Markup Language**
  - 태그 등을 이용하여 문서나 데이터의 <u>구조</u>를 명시하는 언어
  - 대표적인 예 : HTML, Markdown

- **.html**
  - HTML 파일



### HTML 기본구조

- **html** : <u>문서의 최상위(root) 요소</u>
- **head** : <u>문서 메타데이터 요소</u>
  - 메타데이터란? - 데이터를 설명해주는 데이터 (ex. 사진을 찍으면 확인할 수 있는 날짜, 조리개값, 노출 등)
  - 문서 제목, 인코딩, 스타일, 외부 파일 로딩 등
  - 일반적으로 브라우저에 나타나지 않는 내용
- **body** : <u>문서 본문 요소</u>
  - 실제 화면 구성과 관련된 내용



- head 예시
  - < title > : 브라우저 상단 타이틀
  - < meta > : 문서 레벨 메타데이터 요소
  - < link > : 외부 리소스 연결 요소 (CSS 파일, favicon 등)
  - < script > : 스크립트 요소 (JavaScript 파일/코드)
  - < style > : CSS 직접 작성

![image-20220826011428903](01_HTML&CSS.assets/image-20220826011428903.png)



- head 예시 : **Open Graph Protocol**

  - 메타 데이터를 표현하는 새로운 규약
    - HTML 문서의 메타 데이터를 통해 문서의 정보를 전달
    - 메타정보에 해당하는 제목, 설명 등을 쓸 수 있도록 정의

  

#### - DOM(Document Object Model) 트리

- 텍스트 파일인 HTML 문서를 브라우저에서 <u>렌더링</u> 하기 위한 구조
  - HTML 문서에 대한 모델을 구성함
  - HTML 문서 내의 각 요소에 접근 / 수정에 필요한 프로퍼티와 메서드를 제공함

![image-20220826011435414](01_HTML&CSS.assets/image-20220826011435414.png)



#### - 요소(element)

- HTML의 요소는 태그와 내용(contents)로 구성되어 있다.

![image-20220826011442124](01_HTML&CSS.assets/image-20220826011442124.png)

- HTML 요소는 시작 태그와 종료 태그 그리고 태그 사이에 위치한 내용으로 구성
  - 태그(Element, 요소)는 컨텐츠(내용)를 감싸는 것으로 그 정보의 성격과 의미를 정의
- 내용이 없는 태그들
  - br(break line), hr(horizental rule), img, input, link, meta
- 요소는 중첩(nested) 될 수 있음
  - 요소의 중첩을 통해 하나의 문서를 구조화
  - <u>여는 태그와 닫는 태그의 쌍을 잘 확인해야 함</u>
    - 오류를 반환하는 것이 아닌 그냥 레이아웃이 깨진 상태로 출력되기 때문에, 디버깅이 힘들어 질 수 있음



#### - 속성(attribute)

- 태그별로 사용할 수 있는 특성은 다르다

  ![image-20220826011459277](01_HTML&CSS.assets/image-20220826011459277.png)

- 속성 작성 스타일 가이드

  ![image-20220826011510067](01_HTML&CSS.assets/image-20220826011510067.png)

- 속성을 통해 태그의 부가적인 정보를 설정할 수 있음

- 요소는 속성을 가질 수 있으며, 경로나 크기와 같은 추가적인 정보를 제공

- 요소의 시작 태그에 작성하며 보통 이름과 값이 하나의 쌍으로 존재

- 태그와 상관없이 사용 가능한 속성(HTML Global Attribute)들도 있음

  

- **HTML Global Attribute**
  - 모든 HTML 요소가 공통으로 사용할 수 있는 대표적인 속성 (몇몇 요소에는 아무 효과가 없을 수 있음)
    - id : 문서 전체에서 유일한 고유 식별자 지정
    - class : 공백으로 구분된 해당 요소의 클래스의 목록(CSS, JS에서 요소를 선택하거나 접근)
    - data-* : 페이지에 개인 사용자 정의 데이터를 저장하기 위해 사용
    - style : inline 스타일
    - title : 요소에 대한 추가 정보 
    - tabindex : 요소의 탭 순서



#### - 시맨틱 태그

- HTML5에서 의미론적 요소를 담은 태그의 등장
  - 기존 영역을 의미하는 div 태그를 대체하여 사용
- 대표적인 태그 목록
  - header : 문서 전체나 섹션의 헤더(머리말 부분)
  - nav : 내비게이션
  - aside : 사이드에 위치한 공간, 메인 콘텐츠와 관련성이 적은 콘텐츠
  - section : 문서의 일반적인 구분, 컨텐츠의 그룹을 표현
  - article : 문서, 페이지, 사이트 안에서 독립적으로 구분되는 영역
  - footer : 문서 전체나 섹션의 푸터(마지막 부분)

- None semantic 요소는 div, span 등이 있으며 h1, table 태그들도 시맨틱 태그로 볼 수 있음
- 개발자 및 사용자 뿐만 아니라 검색엔진 등에 의미 있는 정보의 그룹을 태그로 표현
- 단순히 구역을 나누는 것 뿐만 아니라 '의미'를 가지는 태그들을 활용하기 위한 노력
- 요소의 의미가 명확해지기 때문에 코드의 가독성을 높이고 유지보수를 쉽게 함
- 검색엔진최적화(SEO)를 위해서 메타태그, 시맨틱 태그 등을 통한 마크업을 효과적으로 활용해야 함



### HTML 문서 구조화

- 인라인 / 블록 요소
- 텍스트 요소

​	![image-20220203163542094](01_HTML&CSS.assets/image-20220203163542094.png)

![image-20220203163654036](01_HTML&CSS.assets/image-20220203163654036.png)

- 그룹 컨텐츠 

​	![image-20220203163625318](01_HTML&CSS.assets/image-20220203163625318.png)

![image-20220203163707644](01_HTML&CSS.assets/image-20220203163707644.png)



#### - table

- table의 각 영역을 명시하기 위해 < thead > < tbody > < tfoot > 요소를 활용

- < tr > 으로 가로 줄을 구성하고 내부에는 < th > 혹은 < td > 로 셀을 구성

- colspan, rowspan 속성을 활용하여 셀 병합

- < caption >을 통해 표 설명 또는 제목을 나타냄

  

#### - form

- < form > 은 정보(데이터)를 서버에 제출하기 위한 영역
- < form > 기본 속성
  - action:  form을 처리할 서버의 URL
  - method: form을 제출할 때 사용할 HTTP 메서드 (GET 혹은 POST)
  - enctype : method가 post인 경우 데이터의 유형
    - application/x-www-form-urlencoded : 기본값
    - multipart/form-data : 파일 전송시 (input type이 file인 경우)
    - text/plain : HTML5 디버깅 용 (잘 사용되지 않음)



#### - input

- 다양한 타입을 가지는 입력 데이터 유형과 위젯이 제공됨

- < input > 대표적인 속성

  - name : form control에 적용되는 이름 (이름/값 페어로 전송됨)
  - value : form contrl에 적용되는 값 (이름/값 페어로 전송됨)
  - required, readonly, autofocus, autocomplete, disabled 등

  ```html
  <form action="/search" method="GET">
    <input type="text" name='q'>
  </form>
  
  <!-- https://www.google.com/search?q=HTML --!>
  ```

  

- **input label**

  - label을 클릭하여 input 자체의 초점을 맞추거나 활성화시킬 수 있음
    - 사용자는 선택할 수 있는 영역이 늘어나 웹 / 모바일(터치) 환경에서 편하게 사용할 수 있음
    - label과 input 입력의 관계가 시각적 뿐만 아니라 화면리더기에서도 label을 읽어 쉽게 내용을 확인할 수 있도록 함
  - < input >에 id 속성을, < label >에는 for 속성을 활용하여 상호 연관을 시킴

  ```html
  <label for="agreement">개인정보 수집에 동의합니다.</label>
  <input type="checkbox" name="agreement" id="agreement">
  ```

  

- **input 유형 -** **일반**

  - 일반적으로 입력을 받기 위하여 제공되며 타입별로 HTML 기본 검증 혹은 추가 속성을 활용할 수 있음

    - text : 일반 텍스트 입력

    - password : 입력 시 값이 보이지 않고 문자를 특수기호(*)로 표현

    - email : 이메일 형식이 아닌 경우 form 제출 불가

    - number : min, max, step 속성을 활용하여 숫자 범위 설정 가능

    - file : accept 속성을 활용하여 파일 타입 지정 가능

      

- **input 유형 - 항목 중 선택**

  - 일반적으로 label을 사용하여 내용을 작성하여 항목 중 선택할 수 있는 input을 제공

  - 동일 항목에 대하여는 name을 지정하고 선택된 항목에 대한 value를 지정해야 함

    - checkbox : 다중 선택
    - radio : 단일 선택

    

- **input 유형 - 기타**

  - 다양한 종류의 input을 위한 picker를 제공

    - color : color picker
    - date : date picker

  - hidden input을 활용하여 사용자 입력을 받지 않고 서버에 전송되어야 하는 값을 설정

    - hidden : 사용자에게 보이지 않는 input

      

- **input 유형 - 종합**

  - < input > 요소의 동작은 type에 따라 달라지므로, 각각의 내용을 숙지할 것

    https://developer.mozilla.org/ko/docs/Web/HTML/Element/Input



----

## CSS

- **CSS?**

  - Cascading Style Sheets
  - <u>스타일을 지정하기 위한 언어</u>
    - <u>선택</u>하고, 스타일을 지정한다
  - CSS 구문은 선택자를 통해 스타일을 지정할 HTML 요소를 선택
  - 중괄호 안에서는 속성과 값, 하나의 쌍으로 이루어진 선언을 진행
  - 각 쌍은 선택한 요소의 속성, 속성에 부여할 값을 의미
    - 속성(property) : <u>어떤</u> 스타일 기능을 변경할지 결정
    - 값(Value) : <u>어떻게</u> 스타일 기능을 변경할지 결정

  

- **CSS 구문 - 용어 정리**

  ![image-20220826011601438](01_HTML&CSS.assets/image-20220826011601438.png)



- **CSS 정의 방법**

  - 인라인(inline) : 해당 태그에 직접 style 속성을 활용 

    - 거의 사용되지 않음. 수정 매우 어려움!

  - 내부 참조(embedding) - < style > : < head > 태그 내에 < style >에 지정

  - 외부 참조(link file) - 분리된 CSS 파일 : 외부 파일을 < head > 내 < link >를 통해 불러오기

    

- **CSS with 개발자 도구**

  - styles : 해당 요소에 선언된 모든 CSS
  - computed : 해당 요소에 최종 계산된 CSS

  

- **CSS 정리**

  - 선택자

    - `*` : 전체 선택
    - `태그명` : 요소 선택자
    - **`.class` : class 선택자**
      - **일반적인 스타일링시 사용되는 것**
    - `#id` : id 선택자
    - `div > .children` : 자식 선택자
      - div 태그 바로 밑에 있는 children 클래스를 가진 것
    - `div .baby` : 자손 선택자
      - div 태그 하위 모든 baby 클래스를 가진 것

  - 기본 선택자 우선순위

    - `!important` : 직접 쓰는 경우 거의 X

    - 인라인, `style`

    - `*` < `태그명` < `.class` < `#id`

      - 같은 점수인 경우에는 CSS가 나중에 선언된 것 (클래스 부여 X!)

        

---

### CSS Selectors

#### - **선택자(Selectors) 유형**

- 기본 선택자

  - 전체 선택자, 요소 선택자
  - 클래스 선택자, 아이디 선택자, 속성 선택자

- 결합자(Combinators)

  - 자손 결합자, 자식 결합자
  - 일반 형제 결합자, 인접 형제 결합자

- 의사 클래스/요소(Psuedo Class)

  - 링크, 동적 의사 클래스

  - 구조적 의사 클래스, 기타 의사 클래스, 의사 엘리먼트, 속성 선택자

    

- **선택자 with 개발자 도구**

  - #sect1 > ul > li:nth-child(1)

    

- **CSS 선택자 정리**
  - 요소 선택자 
    - HTML 태그를 직접 선택
  - 클래스(class) 선택자
    - 마침표(.) 문자로 시작하며, 해당 클래스가 적용된 항목을 선택
  - 아이디(id) 선택자
    - #문자로 시작하며, 해당 클래스가 적용된 항목을 선택
    - 일반적으로 하나의 문서에 1번만 사용. 여러 번 사용해도 동작하지만, 단일 id를 사용하는 것을 권장



#### - CSS 적용 우선순위 (cascading order)

- CSS 우선순위를 아래와 같이 그룹을 지어볼 수 있다.

  - 1. <u>중요도(Importance) - 사용시 주의</u>

       `!important`

  - 2. <u>우선 순위(Specificity)</u>

       인라인 > id > class, 속성, pseudo-class > 요소, pseudo-element

  - 3. <u>CSS 파일 로딩 순서</u>

       

#### - CSS 상속

- CSS는 상속을 통해 부모 요소의 속성을 자식에게 상속한다.
  - 속성(프로퍼티) 중에는 상속이 되는 것과 되지 않는 것들이 있다. 
  - 상속 되는 것 예시
    - Text 관련 요소(font, color, text-align), opacity, visibility 등
  - 상속 되지 않는 것 예시
    - Box model 관련 요소(width, height, margin, padding, border, box-sizing, display)
    - position 관련 요소(position, top/right/bottom/left, z-index 등)



----

### CSS 기본 스타일

#### - 크기 단위

- px(픽셀)

  - 모니터 해상도의 한 화소인 '픽셀' 기준
  - 픽셀의 크기는 변하지 않기 때문에 고정적인 단위

- %

  - 백분율 단위
  - 가변적인 레이아웃에서 자주 사용

- em

  - (바로 위, 부모 요소에 대한) 상속의 영향을 받음

  - 배수 단위, 요소에 지정된 사이즈에 상대적인 사이즈를 가짐

- rem

  - (바로 위, 부모 요소에 대한) 상속의 영향을 받지 않음
  - 최상위 요소(html)의 사이즈를 기준으로 배수 단위를 가짐

- viewport

  - 웹 페이지를 방문한 유저에게 바로 보이게 되는 웹 컨텐츠의 영역(디바이스 화면)
  - 디바이스의 viewport를 기준으로 상대적인 사이즈가 결정됨
  - vw, vh, vmin, vmax



#### - 색상 단위

- 색상 키워드

  - 대소문자를 구분하지 않음
  - red, blue, black과 같은 특정 색을 직접 글자로 나타냄

- RGB 색상

  - 16진수 표기법 혹은 함수형 표기법을 사용해서 특정 색을 표현하는 방식
  - '#' + 16진수 표기법

  - rgb() 함수형 표기법

- HSL 색상

  - 색상, 채도, 명도를 통해 특정 색을 표현하는 방식

- a

  - alpha(투명도)



#### - 문서 표현

- 텍스트

  - 서체, 스타일
  - 자간, 단어 간격, 행간, 들여쓰기 등

- 컬러(color), 배경(background-image, background-color)

- 기타 HTML 태그별 스타일링

  - 목록(li), 표(table)

    

---

### Selectors 심화

#### - 결합자(Combinators)

- 자손 결합자
  - selectorA 하위의 모든 selectorB 요소

![image-20220203172822512](01_HTML&CSS.assets/image-20220203172822512.png)

- 자식 결합자

  - selectorA 바로 아래의 selectorB 요소

    ![image-20220203172832285](01_HTML&CSS.assets/image-20220203172832285.png)

- 일반 형제 결합자

  - selectorA의 형제 요소 중 뒤에 위치하는 selectorB 요소를 모두 선택

    ![image-20220203172843024](01_HTML&CSS.assets/image-20220203172843024.png)

- 인접 형제 결합자

  - selectorA의 형제 요소 중 바로 뒤에 위치하는 selectorB 요소를 선택

    ![image-20220203172854037](01_HTML&CSS.assets/image-20220203172854037.png)



---

### Box model

- CSS 원칙 

  *모든 요소는 네모(박스모델)이고, 위에서부터 아래로, 왼쪽에서 오른쪽으로 쌓인다. (좌측 상단에 배치)*

  

- **Normal Flow**

![image-20220203142434867](01_HTML&CSS.assets/image-20220203142434867.png)

- Box model 구성

  - 모든 HTML 요소는 box 형태로 되어 있음

  - 하나의 박스는 네 부분(영역)으로 이루어짐![image-20220203144522128](01_HTML&CSS.assets/image-20220203144522128.png)

    - **content**
    - **padding**

    ![image-20220203150439280](01_HTML&CSS.assets/image-20220203150439280.png)

    - **border**

    ![image-20220203150520235](01_HTML&CSS.assets/image-20220203150520235.png)

    - **margin**

    ![image-20220203150415306](01_HTML&CSS.assets/image-20220203150415306.png)

  - shorthand를 통해서 표현 가능하다

  ![image-20220203150627497](01_HTML&CSS.assets/image-20220203150627497.png)

![image-20220203150935292](01_HTML&CSS.assets/image-20220203150935292.png)



#### - box-sizing

- 기본적으로 모든 요소의 box-sizing은 content-box
  - padding을 제외한 순수 contents 영역만을 box로 지정
- 다만, 우리가 일반적으로 영역을 볼 때는 border까지의 너비를 100px 보는 것을 원함
  - 그 경우 box-sizing을 border-box로 설정

![image-20220203150327405](01_HTML&CSS.assets/image-20220203150327405.png)





---

### CSS Display

- CSS 원칙 Ⅱ

  모든 요소는 네모(박스모델)이고, 좌측 상단에 배치.

  *display에 따라 크기와 배치가 달라진다!*

  

- 대표적으로 활용되는 display

  - block는 아래로 쌓이고, inline은 오른쪽으로 쌓인다!

  - display : **block**

    - <u>줄 바꿈</u>이 일어나는 요소
    - 화면 크기 전체의 가로 폭을 차지한다.
    - 블록 레벨 요소 안에 인라인 레벨 요소가 들어갈 수 있음

  - display : **inline**

    - 줄 바꿈이 일어나지 않는 행의 일부 요소

    - content 너비만큼 가로 폭을 차지한다.

    - width, height, margin-top, margin-bottom을 지정할 수 없다.

    - 상하 여백은 line-height로 지정한다.

      

- 블록 레벨 요소와 인라인 레벨 요소
  - 블록 레벨 요소와 인라인 레벨 요소 구분 (HTML 4.1까지)
  - 대표적인 블록 레벨 요소
    - https://developer.mozilla.org/ko/docs/Web/HTML/Block-level_elements
    - div / ul, ol, li / p / hr / form 등
  - 대표적인 인라인 레벨 요소
    - https://developer.mozilla.org/ko/docs/Web/HTML/Inline_elements
    - span / a / img / input, label / b, em, i, strong 등

#### - block

- blocking의 개념에 가까움 (위로 올라올 수 없게 막음)

- block의 기본 너비는 가질 수 있는 너비의 100%

- 너비를 가질 수 없다면 margin이 자동으로 부여 (못 올라오게 막는 역할)

  

#### - inline

- inline의 기본 너비는 컨텐츠 영역만큼



#### - 속성에 따른 수평 정렬

![image-20220203153753809](01_HTML&CSS.assets/image-20220203153753809.png)



#### - display 기타

- display : inline-block
  - block과 inline 레벨 요소의 특징을 모두 가짐
  - inline처럼 한 줄에 표시 가능하고, block처럼 width, height, margin 속성을 모두 지정할 수 있음
- display : none
  - 해당 요소를 화면에 표시하지 않고, 공간조차 부여되지 않음
  - 이와 비슷한 visibility : hidden은 해당 요소가 공간은 차지하나 화면에 표시만 하지 않는다.
- 이외 다양한 display 속성은 https://developer.mozilla.org/ko/docs/Web/CSS/display



---

### Position

- CSS Position
  - 문서 상에서 요소 위치 지장
  - Static : 모든 태그의 기본 값(기준 위치)
    - 일반적인 요소의 배치 순서에 따름(좌측 상단)
    - 부모 요소 내에서 배치될 때는 부모 요소의 위치를 기준으로 배치됨
  - 아래는 좌표 프로퍼티(top, bottom, left, right)를 사용하여 이동 가능



- **relative : 상대 위치**

  - 자기 자신의 static 위치를 기준으로 이동 (normal flow 유지)

  - 레이아웃에서 요소가 차지하는 공간은 static일 때와 같음 (normal position 대비 offset)

    

- **absolute : 절대 위치**

  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow)에서 벗어남)

  - static이 아닌 가장 가까이 있는 부모/조상 요소를 기준으로 이동 (없는 경우 body)

    

- **fixed : 고정 위치**

  - 요소를 일반적인 문서 흐름에서 제거 후 레이아웃에 공간을 차지하지 않음 (normal flow에서 벗어남)
  - 부모 요소와 관계없이 viewport를 기준으로 이동
    - 스크롤 시에도 항상 같은 곳에 위치함



### CSS 원칙

- CSS 원칙 Ⅰ, Ⅱ : Normal Flow
  - 모든 요소는 네모(박스모델), 좌측 상단에 배치
  - display에 따라 크기와 배치가 달라짐
- CSS 원칙 Ⅲ
  - position으로 위치의 기준을 변경
    - relative : 본인의 원래 위치
    - absolute : 특정 부모의 위치
    - fixed : 화면의 위치















