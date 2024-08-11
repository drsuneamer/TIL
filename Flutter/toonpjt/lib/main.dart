import 'package:flutter/material.dart';

class Player {
  String name;

  // constructor
  Player({required this.name});
}

void main() {
  var ej = Player(name: 'ej');
  runApp(App());
}

class App extends StatelessWidget {
  // 이 앱의 root
  // build 메소드 구현 필요
  // 모든  widget은 build method 구현해야 한다
  // build: widget의 ui를 반환 (flutter가 실행하게 됨)

  @override // 부모의 method 재정의
  Widget build(BuildContext context) {
    // build도 widget 리턴
    return MaterialApp(
      home: Scaffold(
        appBar: AppBar(
          title: Text("Hello Flutter!"),
        ),
        body: Center(
          child: Text("Hello World!"),
        ),
      ),
    );
  }
}
