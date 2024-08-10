// arguments를 받아서 초기화하는 생성자

class Player {
  // 값은 나중에 받아 올 것이기 때문에 late
  // late final String name;
  // late int xp = 9797;

  // Player(String name, int xp) {
  //   this.name = name;
  //   this.xp = xp;
  // }

  // 개선된 코드
  final String name;
  int xp = 9797;

  Player(this.name, this.xp);

  void sayHi() {
    print('Hi, I\'m $name!');
  }
}

void main() {
  var player1 = Player('nc', 7979);
  player1.sayHi(); // Hi, I'm nc!

  var player2 = Player('jo', 7878);
  player2.sayHi(); // Hi, I'm jo!
}
