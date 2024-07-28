void main() {
  // 컴파일 전에 null 참조 잡아내기 (Runtime Error 방지)
  // null이 될 수 있는 값 명시해줄 것
  // 기본적으로 모든 변수는 non-nullable

  String? ej = 'EJ';
  ej = null;

  ej.length;
  // ej가 null일 수도 있기 때문에 에러

  if (ej != null) {
    ej.isNotEmpty; // 여기서는 사용 가능
  }

  ej?.isNotEmpty; // 이렇게 간단하게 체크할 수도 있음

}