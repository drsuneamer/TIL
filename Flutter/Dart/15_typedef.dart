// typedef: 자료형에 alias 붙일 수 있게 해줌
typedef ListOfInts = List<int>;
typedef UserMap = Map<String, String>;

List<int> reverseList(ListOfInts list) {
  var reversed = list.reversed;
  return reversed.toList();
}
String sayHi(Map<String, String> user) {
  return 'Hi, ${user['name']}!';
}q
void main() {
  print(reverseList([1, 2, 3]));  // [3, 2, 1]

}
