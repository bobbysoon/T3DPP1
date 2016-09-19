from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

class GL_Keyboard:
	KeyBinds = { '\x1B':glutLeaveMainLoop }
	SpcKeyBinds = {}
	SpcKeyUpBinds = {}
	
	@classmethod
	def KeyDown(cls, key, x, y):
		if key in cls.KeyBinds: cls.KeyBinds[key]()
	
	@classmethod
	def SpecialKey(cls, key, x, y):
		if key in cls.SpcKeyBinds: cls.SpcKeyBinds[key]()
	
	@classmethod
	def SpecialKeyUp(cls, key, x, y):
		if key in cls.SpcKeyUpBinds: cls.SpcKeyUpBinds[key]()
	
