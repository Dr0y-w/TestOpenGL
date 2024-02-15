import sys
from PyQt5.QtWidgets import QDialog, QApplication
from module import Ui_Dialog

from PyQt5.QtWidgets import QOpenGLWidget
from PyQt5.QtCore import pyqtSignal, QPoint, QSize, Qt
from PyQt5.QtGui import QColor

import OpenGL.GL as gl
from OpenGL.GLU import *

vertices = (
    (1, -1, -1),    (1, 1, -1),    (-1, 1, -1),    (-1, -1, -1),
    (1, -1, 1),    (1, 1, 1),    (-1, -1, 1),    (-1, 1, 1)
)

# les arretes / edge
edges = (
    (0, 1),    (0, 3),    (0, 4),    (2, 1),    (2, 3),    (2, 7),
    (6, 3),     (6, 4),    (6, 7),    (5, 1),    (5, 4),    (5, 7))


class GLWidget(QOpenGLWidget):

    def __init__(self, parent=None):
        super(GLWidget, self).__init__(parent)

        self.object = 0

    def initializeGL(self):


    def paintGL(self):
        gl.glClear(gl.GL_COLOR_BUFFER_BIT | gl.GL_DEPTH_BUFFER_BIT)
        gl.glBegin(gl.GL_LINES)
        for edge in edges:
            for vertex in edge:
                gl.glVertex3fv(vertices[vertex])

        gl.glEnd()

    def resizeGL(self, width, height):
        side = min(width, height)
        if side < 0:
            return

        gl.glViewport((width - side) // 2, (height - side) // 2, side,
                           side)

        gl.glMatrixMode(gl.GL_PROJECTION)
        gl.glLoadIdentity()
        gl.glOrtho(-0.5, +0.5, +0.5, -0.5, 4.0, 15.0)
        gl.glMatrixMode(gl.GL_MODELVIEW)



class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.ui.widget = GLWidget()
        self.show()


app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
