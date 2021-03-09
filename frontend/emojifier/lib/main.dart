import 'package:flutter/material.dart';
import './homePage.dart';

void main() => runApp(
      MaterialApp(
        home: EmojiPage(),
      ),
    );

class EmojiPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark().copyWith(
        primaryColor: Color(0xFF0A0E21),
        scaffoldBackgroundColor: Color(0xFF0A0E21),
      ),
      home: HomePage(),
    );
  }
}
