class Human {
  final String name;

  //Human(this.name);  // positional arguments 사용
  Human({required this.name}); // named arguments 사용

  void sayHi() {
    print('Hi, I\'m $name!');
  }
}

enum Team { red, green, blue }

class Player extends Human {
  final Team team;

  Player({
    required this.team,
    required String name,
    //}) : super(name); // name을 super 생성자에 전달 (OOP)
  }) : super(name: name); // super: 확장한 부모 클래스

  @override
  void sayHi() {
    super.sayHi();
    print('I\'m on the ${team} team!');

    //Hi, I'm ej!
    //I'm on the Team.green team!
  }
}

void main() {
  var player = Player(team: Team.green, name: 'ej');
  player.sayHi();
}
