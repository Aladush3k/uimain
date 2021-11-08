import sys
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPainter, QColor
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication
from random import randint


class DrawStar(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)
        self.pushButton.clicked.connect(self.draww)
        self.draw = False

    def paintEvent(self, event):
        if self.draw:
            qp = QPainter()
            qp.begin(self)
            qp.setBrush(QColor(Qt.yellow))
            for i in range(randint(1, 100)):
                r = randint(1, 100)
                qp.drawEllipse(randint(1, 1000), randint(1, 1000), r, r)
            self.draw = False

    def draww(self):
        self.draw = True
        self.repaint()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = DrawStar()
    ex.show()
    sys.exit(app.exec_())