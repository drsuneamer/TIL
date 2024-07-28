void main() {
  // const: compile-time constant
  // 값 변경은 불가능
  // final은 런타임 중에 만들어질 수 있음
  
  const API = fetchApi(); // 이건 compile 시점에 알 수 없음
  const API = fetchApi(); // 이건 가능 
}