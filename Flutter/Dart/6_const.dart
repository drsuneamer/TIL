void main() {
  // const: compile-time constant
  // 컴파일 하기 전에 답을 알 수 있는 경우에 사용
  // 값 변경은 불가능
  // final은 런타임 중에 만들어질 수 있음

  const API = fetchApi(); // 이건 compile 시점에 알 수 없음
  const API = fetchApi(); // 이건 가능
}
