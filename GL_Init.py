from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from sys import argv

class GL_Init:
	g_fViewDistance = 9.
	g_Width = 600
	g_Height = 600
	
	g_nearPlane = 1.
	g_farPlane = 1000.
	
	xStart = yStart = 0.
	zoom = 65.
	
	xRotate = 0.
	yRotate = 0.
	zRotate = 0.
	
	xTrans = 0.
	yTrans = 0.
	
	glutInit()
	
	glutInitDisplayMode (GLUT_DOUBLE | GLUT_RGB| GLUT_DEPTH)      # zBuffer
	glutInitWindowSize (g_Width,g_Height) 
	glutInitWindowPosition (0 + 4, g_Height / 4)
	glutCreateWindow (argv[0])
	
	# Initialize OpenGL graphics state
	glEnable(GL_NORMALIZE)
	
	glEnable(GL_CULL_FACE)
	
	glLightfv(GL_LIGHT0,GL_POSITION,[ .0, 10.0, 10., 0. ] )
	glLightfv(GL_LIGHT0,GL_AMBIENT,[ .0, .0, .0, 1.0 ]);
	glLightfv(GL_LIGHT0,GL_DIFFUSE,[ 1.0, 1.0, 1.0, 1.0 ]);
	glLightfv(GL_LIGHT0,GL_SPECULAR,[ 1.0, 1.0, 1.0, 1.0 ]);
	glEnable(GL_LIGHT0)
	glEnable(GL_LIGHTING)
	
	glEnable(GL_DEPTH_TEST)
	glDepthFunc(GL_LESS)
	glShadeModel(GL_SMOOTH)
	glEnable(GL_COLOR_MATERIAL)
	
	@classmethod
	def glutHooks(cls):
		#glutReshapeFunc(reshape)
		glutIdleFunc(cls.idle)   
		glutDisplayFunc(cls.display)    
		glutMouseFunc(cls.MouseButton)
		#glutMotionFunc(cls.motion)
		glutKeyboardFunc(cls.KeyDown)
		glutSpecialFunc(cls.SpecialKey)
		glutSpecialUpFunc(cls.SpecialKeyUp)
	
