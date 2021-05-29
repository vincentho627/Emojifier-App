import 'package:flutter/cupertino.dart';
import 'icon_content.dart';

class ReusableCard extends StatelessWidget {

  final Color color;
  final IconContent icon;
  final Function onTap;

  const ReusableCard({@required this.color, this.icon, this.onTap});

  @override
  Widget build(BuildContext context) {
    return GestureDetector (
      onTap: () {
        if (onTap != null) {
          onTap();
        }
      },
      child: Container(
        margin: EdgeInsets.all(15.0),
        child: icon,
        decoration: BoxDecoration(
            color: color,
            borderRadius: BorderRadius.circular(10.0)),
      ),
    );
  }
}