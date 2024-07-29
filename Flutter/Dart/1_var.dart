void main() {
  // dart style guide에서는 var 사용 권장
  // 특정 자료형은 class property 작성할 때 유용

  var name1 = 'EJ';
  String name2 = 'NC';
  name2 = 'NCLS';
  
  // 값 바꿀 때는 자료형 같아야 함
  // name1 = 97;
  // name2 = 79;  
  
  // 권장: 지역 변수 등에는 var 사용 (컴파일러는 String임을 알고 있음)
}
