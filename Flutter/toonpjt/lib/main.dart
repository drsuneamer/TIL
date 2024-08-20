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
        // Colors. dot 찍으면 색상 미리보기, 선택 가능
        home: Scaffold(
      backgroundColor: Color(0xFF181818),
      // column: 수직, row: 수평 배열
      body: Padding(
        padding: EdgeInsets.all(40),
        child: Column(children: [
          SizedBox(
            // 공간 만들기
            height: 80,
          ),
          Row(
            // MainAxisAlignment: 수평 정렬
            mainAxisAlignment: MainAxisAlignment.end,
            children: [
              Column(
                crossAxisAlignment: CrossAxisAlignment.end,
                children: [
                  Text(
                    'Hello, drsuneamer',
                    style: TextStyle(
                        color: Colors.white,
                        fontSize: 25,
                        fontWeight: FontWeight.w600),
                  ),
                  Text(
                    'Welcome back',
                    style: TextStyle(
                      color: Colors.white.withOpacity(0.7),
                      fontSize: 18,
                    ),
                  ),
                ],
              )
            ],
          )
        ]),
      ),
    ));
  }
}
