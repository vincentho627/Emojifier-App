import 'package:emojifier/screens/welcome_screen.dart';
import 'package:flutter/material.dart';
import 'screens/home_page.dart';
import 'screens/login_screen.dart';
import 'screens/register_screen.dart';
import 'screens/camera_access.dart';


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
      home: WelcomeScreen(),
      routes: {
        WelcomeScreen.id: (context) => WelcomeScreen(),
        HomePage.id: (context) => HomePage(),
        RegisterScreen.id: (context) => RegisterScreen(),
        LoginScreen.id: (context) => LoginScreen(),
        CameraAccess.id: (context) => CameraAccess(null)
      },
    );
  }
}
