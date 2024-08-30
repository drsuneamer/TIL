# toonpjt

A new Flutter project.

---

Text에 서식 넣고 싶으면 Text("text..", style: TextStyle(color: Colors.white))

Column(세로 중심)의 MainAxis는 수직 방향, CrossAxis는 수평 방향
Row(가로 중심)는 MainAxis가 수평, CrossAxis가 수직 방향

space 주려면 SizedBox 사용

색 커스텀 하는 방법

- backgroundColor: Color(0xFF181818),
- backgroundColor: Color.fromARGB(255, 60, 9, 9)

Container: div와 같이 child를 가지고 있는 단순한 box

---

pub.dev: dart, Flutter 공식 패키지 보관소

Future: 미래에 받을 값의 타입을 알려 준다

await: async 함수 안에서만 사용 가능

builder: UI를 그려주는 함수

ListBuilder: 한 번에 다 불러오는 게 아니고 필요할 때 불러옴 (무한스크롤 느낌)
