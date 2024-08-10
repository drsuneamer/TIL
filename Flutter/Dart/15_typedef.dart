// typedef: 자료형에 alias 붙일 수 있게 해줌
typedef ListOfInts = List<int>;
typedef UserMap = Map<String, String>;

//List<int> reverseList(List<int> list) {
ListOfInts reverseList(ListOfInts list) {
  var reversed = list.reversed;
  return reversed.toList();
}

//String sayHi(Map<String, String> user) {
String sayHi(UserMap user) {
  return 'Hi, ${user['name']}!';
}

void main() {
  print(reverseList([1, 2, 3])); // [3, 2, 1]
  sayHi({"name": "ej"});
}
