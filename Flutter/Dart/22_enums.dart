enum Team { red, green, blue } // "" 사용하지 않아도 됨

enum XP { beginner, intermediate, advanced }

class Player {
  String name;
  XP xp;
  Team team;

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
  var ej = Player(name: 'ej', xp: XP.intermediate, team: Team.blue)
    ..name = 'jj'
    ..xp = XP.advanced
    ..team = Team.green;

  var newjj = ej
    ..name = 'newjj'
    ..xp = XP.beginner
    ..team = Team.red;
}
