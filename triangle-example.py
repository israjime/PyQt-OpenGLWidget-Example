import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *

class OpenGLWidgetExample(QOpenGLWidget):
    def __init__(self, parent=None):
        QOpenGLWidget.__init__(self, parent)
        self.timer = QTimer(self)
        self.timer.timeout.connect(self.update)
        self.timer.start(0)

    def initializeGL(self):
        # Mandatory Field
        glEnable(GL_DEPTH_TEST)
        glEnable(GL_LIGHT0)
        glEnable(GL_LIGHTING)
        glColorMaterial(GL_FRONT_AND_BACK,GL_AMBIENT_AND_DIFFUSE)
        glEnable(GL_COLOR_MATERIAL)

    def paintGL(self):
        # Mandatory Field 
        glMatrixMode(GL_PROJECTION)
        glClearColor(1.0,1.0,1.0,0.0)
        glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
        glColor3f(0.0,0.0,1.0)
        glBegin(GL_TRIANGLES)
        glVertex3f(-0.5, -0.5, 0.0)
        glVertex3f(0.5,-0.5, 0.0)
        glVertex3f(0.0,0.5, 0.0)
        glEnd()

    def resizeGL(self, w, h):
        # Optional
        glViewport(0,0,w,h)

# class MainWindow(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.openGLWidget = OpenGLWidgetExample(self)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = OpenGLWidgetExample()
    window.show()
    sys.exit(app.exec_())
