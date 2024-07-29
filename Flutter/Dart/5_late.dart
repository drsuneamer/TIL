void main() {
  // late: var / final 앞에 붙여줄 수 있음
  // 초기 데이터 없이 변수 선언하게 해줌

  late final String name;
  print(name); // -> 아직 name 값이 없으니 작동할 수 없음

  // 데이터 받아오기 등 작업
  name = 'EJ';

  print(name);  // 이제 가능
}