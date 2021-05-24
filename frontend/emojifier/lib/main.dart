import 'package:flutter/material.dart';
import 'screens/home_page.dart';
import 'screens/login_screen.dart';

const primaryColor = Color(0xFF0A0E21);

void main() => runApp(EmojiPage());

class EmojiPage extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    return MaterialApp(
      theme: ThemeData.dark().copyWith(
          primaryColor: primaryColor,
        scaffoldBackgroundColor: primaryColor,
          // textTheme: TextTheme(
          //    bodyText1: TextStyle(color: Colors.black54),
          // )
      ),
      home: LoginScreen(),
      routes: {
        HomePage.id: (context) => HomePage(),
        LoginScreen.id: (context) => LoginScreen()
      },
    );
  }
}
