String sayHello(
    // 1. default value 지정
    //{String name = 'johnDoe', int age = 100, String country = 'sunshineCity'}) {

    // 2. required modifier
    {required String name,
    required int age,
    required String country}) {
  return 'Hello $name, you are $age years old, and you are from $country';
}

void main() {
  // positional parameter의 단점: 파라미터의 의미 직관적으로 알기 어려움
  // print(sayHello('EJ', 23, 'Korea'));

  // 해결책: named arguments
  // 순서 관계 없이 자료형 맞춰주면 사용 가능
  print(sayHello(age: 19, country: 'taiwan', name: 'NC'));
}
