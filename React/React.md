## React

> youtube 생활코딩 강의 참고 https://www.youtube.com/playlist?list=PLuHgQVnccGMCOGstdDZvH41x0Vtvwyxu7

### 1. 수업 소개

- 리액트의 핵심적인 역할: `사용자 정의 태그`를 만드는 것
- `사용자 정의 태그`
  - 부품으로 사용된다
  - 공유 가능
  - 거대한 공급망 존재



- 리액트를 만드는 두 가지 방법

  - `class`

  - `function`
    - 최근에 더 많이 사용



### 2. 실습환경 구축

- React 문서 https://ko.reactjs.org/docs/getting-started.html

- 온라인 플레이그라운드: 온라인 서비스를 이용하여 실습 가능
  - Stackblitz https://stackblitz.com/edit/react-djprfm?file=src%2FApp.js

- 새로운 React 앱 만들기 https://ko.reactjs.org/docs/create-a-new-react-app.html

  - create-react-app  

    - https://github.com/facebook/create-react-app

    - https://create-react-app.dev/

    - ```bash
      npx create-react-app <appname>   # 사용 위해 node.js 필요
      ```

      - 터미널에서 실행 시 create-react-app 바로 사용 가능



- 실습

  - ```bash
    $ npx create-react-app . # . => 현재 디렉토리를 의미함
    ```

    - 설치 여부 물으면 yes

    ![image-20220619232419875](C:\Users\drsuneamer\AppData\Roaming\Typora\typora-user-images\image-20220619232419875.png)

    ![image-20220619232432435](C:\Users\drsuneamer\AppData\Roaming\Typora\typora-user-images\image-20220619232432435.png)

  

  - npm start 명령어 입력 시 리액트 개발환경 실행

    - 웹 브라우저가 뜨면서 샘플 리액트 앱이 뜸

    ![image-20220619232643329](C:\Users\drsuneamer\AppData\Roaming\Typora\typora-user-images\image-20220619232643329.png)

