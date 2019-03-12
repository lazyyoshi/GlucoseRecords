# GlucoseRecords
A sample program for iOS widget and SQLite3 on Pythonista3. This program is based on original sample program "Calculator.py" provided by Pythonista3.  
  
  This application is daily recorder of glucose for diabetes.

# Dependency
* Pythonista3 Interpreter 3.6
* iOS 10 or later.
  
# Setup  

1. Copy following 3 files to same holder in your Pythonista file system.  addBSW.py dbcont.py dbs.db
2. Open addBSW.py
3. Run
4. In case you would like to use this application as widget, please push [Use in "Today"] button.
  
# Usage  

<img src="http://i-gallop.luna.weblife.me/images/GlucoseRecords/GlucoseRD.PNG" width="400px">   
1. Input your glucose by numeric keys.   
2. Set when glucose was mesured by one of BB-BT keys, i.e., BB is meaning of Before Breakfast. That will be displaied on top of center.  
3. Push [+] button, then the glucose will be added as new record.  
4. [C] button, clear glucose entry.  
5. This version is unable to change time stamp.
  
# Data Base Schema  
CREATE TABLE "BSRecords" (  
	"BS"	INTEGER,  
	"DateTime"	TEXT,  
	"Type"	TEXT,  
	"ID"	INTEGER,
	PRIMARY KEY("ID")  
)

# Licence  

This software is released under MIT License, see LICENSE.  
  
# References   

[Pythonista Manual Top](http://omz-software.com/pythonista/docs/)  
[About Widget](http://omz-software.com/pythonista/docs/ios/pythonista.html)  
[SQLite Operation in Python](https://sebastianraschka.com/Articles/2014_sqlite_in_python_tutorial.html)  
