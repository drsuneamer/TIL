import 'package:flutter/material.dart';
import 'package:toonpjt/screens/home_screen.dart';
import 'package:toonpjt/services/api_service.dart';

void main() {
  ApiService().getTodaysToons();
  runApp(const App());
}

class App extends StatelessWidget {
  // 이 위젯의 key를 stateless widget이라는 슈퍼클래스에 전달
  // 위젯에는 ID같은 식별자 역할을 하는 key가 있음
  const App({super.key});

  @override
  Widget build(BuildContext context) {
    return const MaterialApp(
      home: HomeScreen(),
    );
  }
}
