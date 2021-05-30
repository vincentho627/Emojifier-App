import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';

class EmojiImageScreen extends StatefulWidget {
  const EmojiImageScreen({this.byteArray});

  static const String id = "EmojiImageScreen";

  final byteArray;

  @override
  _EmojiImageScreenState createState() => _EmojiImageScreenState();
}

class _EmojiImageScreenState extends State<EmojiImageScreen> {

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Emoji Image"),
      ),
      body: Container(
          padding: EdgeInsets.all(30.0),
          child: Column(
              children: [
                Image.memory(widget.byteArray),
                SizedBox(height: 20.0),
                // OutlinedButton(onPressed: saveCloud, child: Text("Save on cloud")),
              ]
          )
      ),
    );
  }
}
