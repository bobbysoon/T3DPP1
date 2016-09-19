from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class GL_Basics:
	@classmethod
	def resetView(cls):
		cls.zoom = 65.
		cls.xRotate = 0.
		cls.yRotate = 0.
		cls.zRotate = 0.
		cls.xTrans = 0.
		cls.yTrans = 0.
		glutPostRedisplay()

	@classmethod
	def polarView(cls):
		glTranslatef( cls.yTrans/100., 0.0, 0.0 )
		glTranslatef( 0.0, -cls.xTrans/100., 0.0)
		glRotatef( -cls.zRotate, 0.0, 0.0, 1.0)
		glRotatef( -cls.yRotate, .0, 1.0, 0.0)
		glRotatef( -cls.xRotate, 1.0, 0.0, 0.0)
	
	@classmethod
	def MOVE_EYE(cls, x, y):
		cls.xRotate +=  x - cls.xStart
		cls.yRotate += (y - cls.yStart) * .5
		
		cls.xStart = x
		cls.yStart = y 
		glutPostRedisplay()
	
	@classmethod
	def TRANS(cls, x, y):
		cls.xTrans += x - cls.xStart
		cls.yTrans += y - cls.yStart
		
		cls.xStart = x
		cls.yStart = y 
		glutPostRedisplay()
	
	@classmethod
	def ZOOM(cls, x, y):
		cls.zoom -= y - cls.yStart
		if cls.zoom > 150.:
				cls.zoom = 150.
		elif cls.zoom < 1.1:
				cls.zoom = 1.1
		
		cls.xStart = x
		cls.yStart = y 
		glutPostRedisplay()
	
