//String cap(String? name) => name.toUpperCase();
//String cap(String? name) => name != null ? name.toUpperCase() : 'ANON';
String cap(String? name) => name?.toUpperCase() ?? 'ANON';

// left ?? right
// left가 null이면 right를 반환, 아니면 left를 반환

void main() {
  cap('ej');
  cap(null);

  String? name;
  name ??= 'ej'; // name이 null이라면 우항의 값 할당
}
