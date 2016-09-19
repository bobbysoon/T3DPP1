from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Obj import *

class RectGridProbe(Obj):
	buffers={}
	def __init__(self, GL ):
		self.GL=GL
		Obj.__init__(self, verts=[], col=(.25,.75,.25), size=2 , count=0 )
		self.buffer = glGenBuffers(1)
		glBindBuffer(GL_ARRAY_BUFFER, self.buffer )
	
	def reset(self):
		self.verts=[]
		self.count=0
	
	def update(self):
		self.count=len(self.verts)
		if self.count:
			vertices = np.array(self.verts, dtype='float32')
			glBufferData(GL_ARRAY_BUFFER, vertices, GL_STATIC_DRAW)
	
	def extend(self, count=16):
		p0=self.GL.centroids[0].pos
		p1=self.GL.centroids[1].pos
		rect= self.GL.rect
		pMin,pMax = rect.pMin,rect.pMax
		d=vSub(pMax,pMin)
		
		for iter in range(count):
			for i in [0,1,2]:
				j,k = {0,1,2} - {i}
				ni0=p0[i]
				ni1=p1[i]
				nj=pMin[j] + d[j]*random()
				nk=pMin[k] + d[k]*random()
				rp0,rp1 = [0,0,0],[0,0,0]
				rp0[i]=ni0
				rp0[j]=nj
				rp0[k]=nk
				rp1[i]=ni1
				rp1[j]=nj
				rp1[k]=nk
				ray= rp0,rp1
				p= self.GL.TaxiProbe(ray)
				if p:
					self.verts.append(p)
		
		self.update()
			
	def draw(self):
		if self.count:
			glPointSize(self.size)
			glColor3f(*self.col)
			glDisable( GL_LIGHTING )
			
			glEnableClientState(GL_VERTEX_ARRAY)
			glBindBuffer(GL_ARRAY_BUFFER, self.buffer )
			glVertexPointer(3, GL_FLOAT, 0, None)
			glDrawArrays(GL_POINTS, 0, self.count )
			
			glEnable( GL_LIGHTING )

