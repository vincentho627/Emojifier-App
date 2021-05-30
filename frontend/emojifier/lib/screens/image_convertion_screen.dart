import 'dart:typed_data';

import 'package:emojifier/screens/emoji_image_screen.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:http/http.dart' as http;
import 'dart:io';
import 'dart:convert';
import 'package:image_picker/image_picker.dart';

class ImageScreen extends StatefulWidget {
  const ImageScreen({Key key}) : super(key: key);
  static const String id = "ImageScreen";

  @override
  _ImageScreenState createState() => _ImageScreenState();
}

class _ImageScreenState extends State<ImageScreen> {
  PickedFile file;
  String status = '';
  File tmpFile;
  String base64Image;
  Uri uploadEndPoint = Uri.http("127.0.0.1:5000", "/image");

  void chooseImage() async {
    file = await ImagePicker().getImage(source: ImageSource.gallery);
    setState(() {
      tmpFile = File(file.path);
    });
  }

  void uploadImage() async {
    if (tmpFile != null) {
      List<int> imageBytes = await tmpFile.readAsBytes();
      base64Image = base64Encode(imageBytes);
      var body = jsonEncode(<String, String>{
        'image': base64Image,
        "testing": "true",
      });
      upload(body);
    }
  }

  void upload(body) async {
    await http
        .post(uploadEndPoint,
            headers: <String, String>{
              'Content-Type': 'application/json; charset=UTF-8',
            },
            body: body)
        .then((response) {
      String byteArray = jsonDecode(response.body)['image'].toString();
      Uint8List base64List = base64Decode(byteArray);
      Navigator.push(context, MaterialPageRoute(builder: (context) {
        return EmojiImageScreen(byteArray: base64List);
      }));
    }).catchError((error) {
      print(error);
      AlertDialog alert = AlertDialog(
        title: const Text('Backend Error'),
        content: const Text('Please contact us about the issue'),
        actions: <Widget>[
          TextButton(
            onPressed: () => Navigator.pop(context, 'Cancel'),
            child: const Text('Cancel'),
          ),
          TextButton(
            onPressed: () => Navigator.pop(context, 'OK'),
            child: const Text('OK'),
          ),
        ],
      );

      showDialog(
        context: context,
        builder: (BuildContext context) {
          return alert;
        },
      );
      // setStatus(error);
    });
  }

  Widget showImage() {
    if (file != null) {
      return Image.file(tmpFile);
    }
    return Text("Haven't chose image", textAlign: TextAlign.center,);
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Image Converter"),
      ),
      body: Container(
        padding: EdgeInsets.all(30.0),
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.stretch,
          children: [
            OutlinedButton(onPressed: chooseImage, child: Text("Choose Image")),
            SizedBox(height: 20.0),
            showImage(),
            SizedBox(height: 20.0),
            OutlinedButton(onPressed: uploadImage, child: Text("Upload Image")),
            SizedBox(height: 20.0),
          ],
        ),
      ),
    );
  }
}
