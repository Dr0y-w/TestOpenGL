import sys
from PyQt5.QtWidgets import QDialog, QApplication
from module import Ui_Dialog

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QOpenGLWidget
from OpenGL.GL import *
from OpenGL.GLU import *


# les nodes / sommet / vertex
vertices = (
    (1, -1, -1),    (1, 1, -1),    (-1, 1, -1),    (-1, -1, -1),
    (1, -1, 1),    (1, 1, 1),    (-1, -1, 1),    (-1, 1, 1)
)

# les arretes / edge
edges = (
    (0, 1),    (0, 3),    (0, 4),    (2, 1),    (2, 3),    (2, 7),
    (6, 3),     (6, 4),    (6, 7),    (5, 1),    (5, 4),    (5, 7))

def cube():
    glBegin(GL_LINES)
    for edge in edges:
        for vertex in edge:
            glVertex3fv(vertices[vertex])
    glEnd()

class AppWindow(QDialog):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Dialog()
        self.ui.setupUi(self)
        self.show()
        self.ui.openGLWidget.paintGL()




QApplication.setAttribute(Qt.AA_UseDesktopOpenGL)
app = QApplication(sys.argv)
w = AppWindow()
w.show()
sys.exit(app.exec_())
