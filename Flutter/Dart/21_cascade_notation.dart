class Player {
  String name;
  int xp;
  String team;

  Player({
    required this.name,
    required this.xp,
    required this.team,
  });

  void sayHi() {
    print('Hi, I\'m $name!');
  }
}

void main() {
  // var ej = Player(name: 'ej', xp: 9797, team: 'green');
  // ej.name = 'jj';
  // ej.xp = 9999;
  // ej.team = 'blue';

  var ej = Player(name: 'ej', xp: 9797, team: 'green')
    ..name = 'jj'
    ..xp = 9999
    ..team = 'blue';

  // 이렇게 불러와서도 가능
  var newjj = ej
    ..name = 'newjj'
    ..xp = 10000
    ..team = 'red';
}
