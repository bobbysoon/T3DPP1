from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Obj import *

class _PointsArray(Obj):
	buffers={}
	def __init__(self, verts, col=(0,1,0), size=2.0 ):
		Obj.__init__(self, verts=verts, col=col, size=size, count=len(verts) )
		
		PointsArray.buffers[self] = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, PointsArray.buffers[self])
		
		vertices = np.array(verts, dtype='float32')
		glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	
	def __del__(self):
		glDeleteBuffers( PointsArray.buffers[self] )
	
	def draw(self):
		glPointSize(self.size)
		glColor3f(*self.col)
		glDisable( GL_LIGHTING )
		
		glEnableClientState(GL_VERTEX_ARRAY)
		glBindBuffer(GL_ARRAY_BUFFER, PointsArray.buffers[self])
		glVertexPointer(3, GL_FLOAT, 0, None)
		glDrawArrays(GL_POINTS, 0, self.count )
		
		glEnable( GL_LIGHTING )
	
