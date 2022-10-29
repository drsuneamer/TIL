### State

- useState의 작동 방식

  - useState는 항상 **배열**을 리턴한다. 이 배열에는 **두 개의 element**가 있다.
  - 그 배열을 **상수에 저장**하거나 배열을 **de-structuring** 할 수 있다. (두 개의 값을 저장할 수 있는 자바스크립트의 기능)
  - 항상 두 개의 element가 있고 각각의 상수에 할당될 것이다.

  ```jsx
  const [ modalIsOpen, setModalIsOPpen ] = useState(false);
  ```

  - 배열의 첫 번째 element는 

    현재 state의 snapshot

     (위 코드 안에서는 괄호 안의 `false`를 가리킨다.

    - 리액트 state를 리액트가 관리하는 변수로 생각할 수도 있다.
    - 초기값을 괄호 안에 정의하고 나중에 그 값을 변경할 수도 있다.

  - 두 번째 element는 

    state값을 변경할 수 있게 하는 함수

    이다.

    - 새로운 값을 modalIsOpen에 할당하는 식으로는 state를 변경할 수 없고, 두 번째 함수를 호출해서 새로운 값을 지정해야 한다.