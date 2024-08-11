// class 생성 시에는 타입 명시 필수 (함수 안에서는 var 사용 가능한 것과 다름)
class Player {
  // String name = 'ej';
  final String name = 'ej'; // final 선언하면 값 변경 불가
  int xp = 9797;

  void sayHi() {
    //this.name; // 가능하지만 class method 안에서는 사용하지 않는 것 권고
    print('Hi, I\'m $name!');

    // var name = 'nc';
    // 위와 같이 같은 이름의 변수 선언 후 Player의 name을 가져오려면 this.name이라고 명시
  }
}

void main() {
  var player = Player(); // player 인스턴스 생성
  // var player = new Player();  new 키워드는 옵션

  print(player.name); // ej
  // player.name = 'nc';  final 선언하는 순간 값 변경 불가
  player.sayHi(); // Hi, I'm ej!
}
