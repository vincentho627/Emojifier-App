import 'package:flutter/material.dart';
import './home_page.dart';

const primaryColor = Color(0xFF0A0E21);

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
        primaryColor: primaryColor,
        scaffoldBackgroundColor: primaryColor,
      ),
      home: HomePage(),
    );
  }
}
