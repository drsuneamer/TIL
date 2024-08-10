class Player {
  final String name;
  int xp, age; // 같은 타입 한 줄에 선언 가능
  String team;

  Player({
    required this.name,
    required this.xp,
    required this.team,
    required this.age,
  });

  Player.createRedPlayer({
    required String name,
    required int age,
  })  : this.age = age, // parameter로 받은 age를 this.age에 할당
        this.name = name,
        this.team = 'blue',
        this.xp = 0;

  Player.createBluePlayer(
      String name, int age) // 기본적으로 모든 positional arguments는 required
      : this.age = age, // parameter로 받은 age를 this.age에 할당
        this.name = name,
        this.team = 'red',
        this.xp = 0;

  void sayHi() {
    print('Hi, I\'m $name!');
  }
}

void main() {
  // positional arguments는 혼란을 줄 수 있음
  // var player1 = Player('nc', 7979, 'team1', 22);
  var player1 = Player.createRedPlayer(
    name: 'nc',
    age: 22,
  );

  //var player2 = Player('jo', 7878, 'team2', 20);
  var player2 = Player.createBluePlayer(
    'jo',
    20,
  );
}
