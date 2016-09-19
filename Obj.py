from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vMath import *

class Obj:
	instances=[]
	def __init__(self, **kwargs):
		self.__dict__.update(kwargs)
		Obj.instances.append(self)

class Sphere(Obj):
	quadric = gluNewQuadric()
	gluQuadricNormals(quadric, GLU_SMOOTH)
	gluQuadricTexture(quadric, GL_TRUE)
	
	def draw(self):
		glPushMatrix()
		glTranslatef( *self.pos )
		glColor3f( *self.col )
		gluSphere( Sphere.quadric, self.radius, 16,16 )
		glPopMatrix()
		
		if hasattr(self,'text'):
			glColor3f( .3,.3,.3 )
			modelview = np.matrix(glGetDoublev(GL_MODELVIEW_MATRIX))
			projection = np.matrix(glGetDoublev(GL_PROJECTION_MATRIX))
			viewport = glGetIntegerv(GL_VIEWPORT)
			x,y,z=self.pos
			winX, winY, winZ= gluProject(x,y,z, modelview, projection, viewport)
			winZ-=self.radius
			p=gluUnProject(winX, winY, winZ, modelview, projection, viewport)
			glDisable(GL_LIGHTING)
			glRasterPos3f(*p)
			for c in self.text:
				glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c));
		glEnable(GL_LIGHTING)
	
	def intersectsRay(self, ray):
		p0,p1=ray
		dist= PointLineDist(self.pos , p0,p1)
		return dist <= self.radius

class Rect(Obj):
	def draw(self):
		x1,y1,z1=self.pMin
		x2,y2,z2=self.pMax
		glColor3f( *self.col )
		glBegin(GL_QUADS)
		glNormal3f( 1,0,0)
		glVertex3f(x1,y1,z1);glVertex3f(x1,y2,z1);glVertex3f(x1,y2,z2);glVertex3f(x1,y1,z2)
		glNormal3f(-1,0,0)
		glVertex3f(x2,y1,z1);glVertex3f(x2,y1,z2);glVertex3f(x2,y2,z2);glVertex3f(x2,y2,z1)
		glNormal3f(0, 1,0)
		glVertex3f(x1,y1,z1);glVertex3f(x1,y1,z2);glVertex3f(x2,y1,z2);glVertex3f(x2,y1,z1)
		glNormal3f(0,-1,0)
		glVertex3f(x1,y2,z1);glVertex3f(x2,y2,z1);glVertex3f(x2,y2,z2);glVertex3f(x1,y2,z2)
		glNormal3f(0,0, 1)
		glVertex3f(x1,y1,z1);glVertex3f(x2,y1,z1);glVertex3f(x2,y2,z1);glVertex3f(x1,y2,z1)
		glNormal3f(0,0,-1)
		glVertex3f(x1,y1,z2);glVertex3f(x1,y2,z2);glVertex3f(x2,y2,z2);glVertex3f(x2,y1,z2)
		glEnd()

class WireRect(Obj):
	def draw(self):
		pMin= self.pMin.pos if isinstance(self.pMin,Obj) else self.pMin
		pMax= self.pMax.pos if isinstance(self.pMax,Obj) else self.pMax
		x1,y1,z1= pMin
		x2,y2,z2= pMax
		glColor3f( *self.col )
		glDisable( GL_LIGHTING )
		glBegin(GL_LINES)
		glVertex3f(x1,y1,z1);glVertex3f(x1,y1,z2)
		glVertex3f(x1,y2,z1);glVertex3f(x1,y2,z2)
		glVertex3f(x2,y2,z1);glVertex3f(x2,y2,z2)
		glVertex3f(x2,y1,z1);glVertex3f(x2,y1,z2)
		glEnd()
		glBegin(GL_LINE_LOOP)
		glVertex3f(x1,y1,z1)
		glVertex3f(x1,y2,z1)
		glVertex3f(x2,y2,z1)
		glVertex3f(x2,y1,z1)
		glEnd()
		glBegin(GL_LINE_LOOP)
		glVertex3f(x1,y1,z2)
		glVertex3f(x1,y2,z2)
		glVertex3f(x2,y2,z2)
		glVertex3f(x2,y1,z2)
		glEnd()
		glEnable( GL_LIGHTING )

