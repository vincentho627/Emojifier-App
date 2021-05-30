import 'package:emojifier/components/camera_arguments.dart';
import 'package:emojifier/components/icon_content.dart';
import 'package:emojifier/components/reusable_card.dart';
import 'package:emojifier/screens/image_convertion_screen.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';
import 'package:camera/camera.dart';

import 'camera_access.dart';


const primaryColor = Color(0xFF1D1E33);
const comingSoon = "Coming Soon!";

class HomePage extends StatefulWidget {
  static const String id = "HomePage";

  @override
  State<StatefulWidget> createState() => _HomePage();
}

class _HomePage extends State<HomePage> {

  bool cameraSuccess = true;

  void openCamera() async {
    List<CameraDescription> cameras = await availableCameras();
    if (cameras.isNotEmpty){
      CameraDescription firstCamera = cameras.first;
      CameraController controller = CameraController(firstCamera, ResolutionPreset.medium);

      Navigator.pushNamed(context, CameraAccess.id, arguments: CameraArguments(controller, firstCamera, "Hello"));
    }

    // suppose to alert
    // Navigator.push(context, MaterialPageRoute(builder: (context) => CameraAccess(CameraArguments(null, null, "hello"))));

    AlertDialog alert = AlertDialog(
      title: const Text('Camera Not Found'),
      content: const Text('Please allow camera access in settings'),
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
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(
        title: Text("Emojifier"),
      ),
      body: Column(
        children: [
          Expanded(
            child: Row(
              children: [
                Expanded(
                    child: ReusableCard(
                      color: primaryColor,
                      icon: IconContent(
                        icon: CupertinoIcons.textformat_alt,
                        text: comingSoon,
                      ),
                    )),
                Expanded(
                    child: ReusableCard(
                      color: primaryColor,
                      icon: IconContent(
                        icon: CupertinoIcons.photo,
                        text: "Picture Converter",
                      ),
                      onTap: (() => Navigator.pushNamed(context, ImageScreen.id)),
                    ))
              ],
            ),
          ),
          Expanded(
            child: Row(
              children: [
                Expanded(
                    child: ReusableCard(
                      onTap: (() => openCamera()),
                      color: primaryColor,
                      icon: IconContent(
                        icon: CupertinoIcons.camera,
                        text: "AR CAMERA!",
                      ),
                    )),
              ],
            ),
          ),
          Expanded(
            child: Row(
              children: [
                Expanded(
                    child: ReusableCard(
                      color: primaryColor,
                      icon: IconContent(
                        icon: FontAwesomeIcons.grinTongue,
                        text: comingSoon,
                      ),
                    )),
                Expanded(
                    child: ReusableCard(
                      color: primaryColor,
                      icon: IconContent(
                        icon: FontAwesomeIcons.dizzy,
                        text: comingSoon,
                      ),
                    ))
              ],
            ),
          )
        ],
      ),
    );
  }
}
