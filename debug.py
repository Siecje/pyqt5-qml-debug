import os
import sys

from PyQt5 import QtQml, QtWidgets


if __name__ == '__main__':
    if 'CONFIG' in os.environ:
        print(os.environ['CONFIG'])
    app = QtWidgets.QApplication(sys.argv + ["-nograb"])
    engine = QtQml.QQmlApplicationEngine("Debug.qml")
    sys.exit(app.exec_())
