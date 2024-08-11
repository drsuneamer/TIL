void main() {
  // dynamic: 타입 알기 전에 좋음 (flutter, json에 유용)
  // 이상적으로는 dynamic 쓰는 것을 피할 것

  var name1;
  name1 = 'EJ';
  name1 = 97;
  name1 = true;

  // var name3 = 'NC';
  // name3 = 79; // 에러 발생

  dynamic name2;
  if (name2 is String) {
    // 이 안에서는 name2가 String인 것 알 수 있음
    // name2.   -> 그래서 더 다양한 메소드 조회 가능
  }

  dynamic name3 = 'NC';
  name3 = 79; // 에러 발생하지 않음
}
