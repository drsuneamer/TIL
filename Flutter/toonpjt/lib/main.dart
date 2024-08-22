import 'package:flutter/material.dart';
import 'package:toonpjt/widgets/button.dart';
import 'package:toonpjt/widgets/currency_card.dart';

class Player {
  String name;

  // constructor
  Player({required this.name});
}

void main() {
  var ej = Player(name: 'ej');
  runApp(const App());
}

class App extends StatelessWidget {
  const App({super.key});

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
      backgroundColor: const Color(0xFF181818),
      // column: 수직, row: 수평 배열
      body: Padding(
        padding: const EdgeInsets.symmetric(
          horizontal: 40,
        ),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: [
            const SizedBox(
              // 공간 만들기
              height: 60,
            ),
            Row(
              // MainAxisAlignment: 수평 정렬
              mainAxisAlignment: MainAxisAlignment.end,
              children: [
                Column(
                  crossAxisAlignment: CrossAxisAlignment.end,
                  children: [
                    const Text(
                      'Hello, drsuneamer',
                      style: TextStyle(
                          color: Colors.white,
                          fontSize: 30,
                          fontWeight: FontWeight.w600),
                    ),
                    Text(
                      'Welcome back',
                      style: TextStyle(
                        color: Colors.white.withOpacity(0.7),
                        fontSize: 20,
                      ),
                    ),
                  ],
                )
              ],
            ),
            const SizedBox(
              height: 50,
            ),
            Text(
              'Total balance',
              style: TextStyle(
                fontSize: 22,
                color: Colors.white.withOpacity(0.8),
              ),
            ),
            const SizedBox(
              height: 5,
            ),
            const Text(
              '\$ 7 997 412',
              style: TextStyle(
                fontSize: 48,
                fontWeight: FontWeight.w600,
                color: Colors.white,
              ),
            ),
            const SizedBox(
              height: 30,
            ),
            const Row(
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                Button(
                  text: 'Transfer',
                  bgColor: Color(0xFFF2B33A),
                  textColor: Colors.black,
                ),
                Button(
                  text: 'Request',
                  bgColor: Color(0xFF1F2123),
                  textColor: Colors.white,
                ),
              ],
            ),
            const SizedBox(
              height: 100,
            ),
            Row(
              crossAxisAlignment: CrossAxisAlignment.end,
              mainAxisAlignment: MainAxisAlignment.spaceBetween,
              children: [
                const Text(
                  "Wallets",
                  style: TextStyle(
                    color: Colors.white,
                    fontSize: 36,
                  ),
                ),
                Text(
                  "View All",
                  style: TextStyle(
                    color: Colors.white.withOpacity(0.7),
                  ),
                )
              ],
            ),
            const SizedBox(height: 20),
            const CurrencyCard(
              name: 'Euro',
              code: 'EUR',
              amount: '6 422',
              icon: Icons.euro,
              isInverted: false,
            ),
            const CurrencyCard(
              name: 'Bitcoin',
              code: 'BTC',
              amount: '1 234',
              icon: Icons.currency_bitcoin,
              isInverted: true,
            ),
            const CurrencyCard(
              name: 'Dollar',
              code: 'USD',
              amount: '629',
              icon: Icons.attach_money_outlined,
              isInverted: false,
            ),
          ],
        ),
      ),
    ));
  }
}
