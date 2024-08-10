// 다른 클래스들이 직접 구현해야 하는 메소드를 모아 놓은 blueprint
abstract class Human {
  void walk();
}

// Human을 extend 한 경우 walk 메소드를 구현해야 함
class Player extends Human {
  void walk() {
    print('player is walking');
  }
}

class Coach extends Human {
  void walk() {
    print('coach is walking');
  }
}

void main() {}
