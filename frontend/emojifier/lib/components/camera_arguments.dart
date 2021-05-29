import 'package:camera/camera.dart';


class CameraArguments {
  final CameraController controller;
  final CameraDescription firstCamera;
  final String text;

  CameraArguments(this.controller, this.firstCamera, this.text);
}