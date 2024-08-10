class Player {
  final String name;
  int xp;
  String team;
  int age;

  //Player(this.name, this.xp, this.team, this.age);

  // positional arguments를 named arguments로 변경
  //can't have a value of 'null' 방지하는 방법 2가지: 1. 기본값, 2. required
  Player({
    required this.name,
    required this.xp,
    required this.team,
    required this.age,
  });

  void sayHi() {
    print('Hi, I\'m $name!');
  }
}

void main() {
  // positional arguments는 혼란을 줄 수 있음
  // var player1 = Player('nc', 7979, 'team1', 22);
  var player1 = Player(
    name: 'nc',
    xp: 7979,
    team: 'team1',
    age: 22,
  );

  //var player2 = Player('jo', 7878, 'team2', 20);
  var player2 = Player(
    name: 'jo',
    xp: 7878,
    team: 'team2',
    age: 20,
  );
}
