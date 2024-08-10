class Player {
  final String name;
  int xp;
  String team;

  Player.fromJson(Map<String, dynamic> playerJson)
      : name = playerJson['name'],
        xp = playerJson['xp'],
        team = playerJson['team'];

  void sayHi() {
    print('Hi, I\'m $name!');
  }
}

void main() {
  var apiData = [
    {
      "name": "ej",
      "team": "green",
      "xp": 0,
    },
    {
      "name": "nc",
      "team": "pink",
      "xp": 0,
    },
    {
      "name": "jo",
      "team": "blue",
      "xp": 0,
    },
  ];

  apiData.forEach((playerJson) {
    var player = Player.fromJson(playerJson);
    player.sayHi();
  });

  //Hi, I'm ej!
  //Hi, I'm nc!
  //Hi, I'm jo!
}
