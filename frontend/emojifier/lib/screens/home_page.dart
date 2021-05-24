import 'package:emojifier/components/icon_content.dart';
import 'package:emojifier/components/reusable_card.dart';
import 'package:flutter/cupertino.dart';
import 'package:flutter/material.dart';
import 'package:font_awesome_flutter/font_awesome_flutter.dart';

const primaryColor = Color(0xFF1D1E33);
const comingSoon = "Coming Soon!";

class HomePage extends StatefulWidget {
  static const String id = "HomePage";

  @override
  State<StatefulWidget> createState() => _HomePage();
}

class _HomePage extends State<HomePage> {
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
                    text: comingSoon,
                  ),
                ))
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
