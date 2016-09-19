from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vMath import vSub

class GL_DrawText:
	@classmethod
	def DrawText(cls):
		p0=cls.centroids[0].pos
		p1=cls.centroids[1].pos
		d=vSub(p1,p0)
		s='seq:'+str(cls.perpPlane.seq)
		s+='\nsgn:'+str(cls.perpPlane.s)
		s+='\nshape:'+str(cls.perpPlane.shape)
		if hasattr(cls,'rectGridProbe') and cls.rectGridProbe.count:
			s+='\nscatter plots:%i'%(cls.rectGridProbe.count)
		cls.DrawText_(s, 10,cls.g_Height-20 , col=(1,.5,0) )
	
	@classmethod
	def DrawText_(cls, value, x,y , col=(.5,.5,.5) ):
		glDisable(GL_LIGHTING)
		glColor3f( *col )
		glMatrixMode(GL_PROJECTION);
		matrix = glGetDouble( GL_PROJECTION_MATRIX )
		
		glLoadIdentity()
		glOrtho(0.0, cls.g_Height or 32, 0.0, cls.g_Width or 32, -1.0, 1.0)
		glMatrixMode(GL_MODELVIEW)
		glPushMatrix()
		glLoadIdentity()
		for s in value.split('\n'):
			glRasterPos2i(x, y)
			for c in s:
				glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c));
			y-=18
		
		glPopMatrix();
		glMatrixMode(GL_PROJECTION);
		glLoadMatrixd( matrix )
		
		glMatrixMode(GL_MODELVIEW);
		glEnable(GL_LIGHTING)
	
