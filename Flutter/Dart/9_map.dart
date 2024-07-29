void main() {
  // python의 dictionary와 유사
  // dart에서 object는 어떤 것도 될 수 있음 (typescript의 any와 유사)

  // Type: Map<String, Object>
  // dart에서는 컴파일러가 자동으로 타입 파악
  var player1 = {
    'name': 'EJ',
    'xp': 97,
    'power': false,
  };

  // 컴파일러 대신 직접 타입 설정할 수 있음
  Map<int, bool> player2 = {
    1: true,
    // 2: 1; => 에러 발생
  };

  // API에서 값을 얻어 오는 경우에는 map 대신 class 권장
}
