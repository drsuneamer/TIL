// mixin: 생성자(constructor)가 없는 class
// class에 property 추가할 때 등 사용함
mixin Strong {
  final double level = 100;
}

mixin Runner {
  void run() {
    print('Run!');
  }
}

mixin Tall {
  final double height = 186;
}

enum Team { red, green, blue }

class Player with Strong, Runner, Tall {
  final Team team;

  Player({required this.team});
}

class Horse with Strong, Runner {}

class Kid with Runner {}

void main() {
  var player = Player(team: Team.green);
}
