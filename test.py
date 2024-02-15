import sys
from PyQt5.QtWidgets import QDialog, QApplication,QOpenGLWidget
from module import Ui_Dialog
from OpenGL.GL import *


class PyqtOpengl(QOpenGLWidget):
    def __init__(self,parent=None):
        super().__init__(parent)

    def initialiazeGL(self):
        glClearColor(0,0,1,1)
        glClear(GL_COLOR_BUFFER_BIT)

    def resizeGL(self):
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glOrtho(-50, 50, -50, 50, -50, 50)

    def paintGl(self):
        glColor3f(1.0, 0.0, 0.0)
        glRectf(-5, -5, 5, 5)



class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        glwidget = PyqtOpengl(self.ui.openGLWidget)
        glwidget.setMaximumSize(300, 300)
        glwidget.paintGl()

app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
