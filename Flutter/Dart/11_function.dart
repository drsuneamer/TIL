String sayHello(String name) {
  return 'Hello $name';
}

// fat arrow syntax
// 즉시 리턴 등의 한 줄 코드에서 사용 가능
String sayHello2(String name) => 'Hello $name';

num plus(num a, num b) => a + b;

void main() {
  print(sayHello("EJ"));
}
