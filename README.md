How do you debug QML code when using PyQt5?

```shell
$ python3.5 -m venv venv
$ source venv/bin/activate
$ pip install PyQt5
```

```shell
$ CONFIG=qml_debug python debug.py --qmljsdebugger=port:9030,block
qml_debug
QML Debugger: Ignoring "-qmljsdebugger=port:9030,block". Debugging has not been enabled.
```

https://riverbankcomputing.com/pipermail/pyqt/2013-October/033373.html
