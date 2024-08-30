import 'package:flutter/material.dart';
import 'package:toonpjt/models/webtoon_model.dart';
import 'package:toonpjt/services/api_service.dart';

class HomeScreen extends StatelessWidget {
  HomeScreen({super.key}); // Future이 있으면 const 불가능

  Future<List<WebtoonModel>> webtoons = ApiService.getTodaysToons();

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      backgroundColor: Colors.white,
      appBar: AppBar(
        elevation: 1,
        foregroundColor: Colors.green,
        backgroundColor: Colors.white,
        title: const Text(
          '오늘의 웹툰',
          style: TextStyle(
            fontSize: 24,
            fontWeight: FontWeight.bold,
          ),
        ),
      ),
      body: FutureBuilder(
          future: webtoons,
          builder: (context, snapshot) {
            if (snapshot.hasData) {
              return const Text("Data is here");
            }
            return const Text('Loading...');
          }),
    );
  }
}
