String sayHello(String name, int age, [String? country = 'taiwan']) =>
    'Hello $name, you are $age years old, and you are from $country';
// 대괄호, nullabla 표시, default value 지정

void main() {
  print(sayHello('EJ', 2));
  // Hello EJ, you are 2 years old, and you are from taiwan
}
