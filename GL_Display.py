from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Obj import *

class GL_Display:
	@classmethod
	def display(cls):
		glClear(GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT)
		
		glLoadIdentity()
		gluLookAt(0, 0, -cls.g_fViewDistance, 0, 0, 0, -.1, 0, 0)
		
		glMatrixMode(GL_PROJECTION)
		glLoadIdentity()
		gluPerspective(cls.zoom, float(cls.g_Width)/float(cls.g_Height), cls.g_nearPlane, cls.g_farPlane)
		glLightfv(GL_LIGHT0,GL_POSITION,[ .0, 0.0, -10., 0. ] )
		glMatrixMode(GL_MODELVIEW)
		
		cls.polarView()
		
		for obj in Obj.instances: obj.draw()
		
		cls.DrawText()
		
		glutSwapBuffers()
		
	
