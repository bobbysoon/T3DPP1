from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vMath import *
from PointsArray import *

class GL_Probe:
	@classmethod
	def Region(cls, p):
		dists = {mDist(p,c.pos):c for c in cls.centroids}
		return dists[min(dists.keys())]
	
	@classmethod
	def TaxiProbe(cls, ray):
		p0,p1=ray
		r0=cls.Region(p0)
		r1=cls.Region(p1)
		if r0 != r1:
			while vDist(p0,p1)>.01:
				p=vDivF(vAdd(p0,p1),2.0)
				r=cls.Region(p)
				if r==r0:	p0=p
				else:		p1=p
			return p
	
	@classmethod
	def ProbeSpray(cls, x,y , count=32 ):
		verts=[]
		p0,p1 = cls.MouseRay(x,y)
		for i in range(count):
			p1_=vAdd(p1,vRnd(32.0))
			r=p0,p1_
			p= cls.TaxiProbe(r)
			if p:
				verts.append(p)
		if verts:
			PointsArray(verts, col=(1,0,1))
		cls.display()
	
