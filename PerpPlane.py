from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vMath import *
from AxeSeq import AxeSeq
from Obj import Obj

import datetime
current_time = datetime.datetime.now().time()
current_time.isoformat() 

print 'class PerpPlane'
class PerpPlane(Obj):
	def __init__(self, s1,s2, rect):
		Obj.__init__(self,s1=s1,s2=s2, rect=rect )
		self.shape=0
	
	def draw(self):
		c1,c2 = self.s1.pos,self.s2.pos
		d=vSub(c2,c1)
		seq=AxeSeq(d);self.seq=seq
		
		d=seq.remap(d);self.d=d
		a=vAbs(d)
		s=vSgn(d);self.s=s
		c=vDivF(vAdd(c1,c2),2.0)
		
		min1,min2,min3=seq.remap(self.rect.pMin)
		max1,max2,max3=seq.remap(self.rect.pMax)
		c1,c2,c3=seq.remap(c)
		d1,d2,d3=vDivF(d,2.0)
		a1,a2,a3=vDivF(a,2.0)
		s1,s2,s3=s
		Verts=[]
		Poly=[]
		Quads=[]
		if s.count(0.0)==0:
			shape = sign( a3-a2-a1 ) ; self.shape=shape
			if shape>0:
				Verts.append((
					c1-d1,
					c2-d2,
					c3+(a2+a1)*s3
					))
				Verts.append((
					c1+d1,
					c2-d2,
					c3+(a2-a1)*s3
					))
				Verts.append((
					c1+d1,
					c2+d2,
					c3-(a2+a1)*s3
					))
				Verts.append((
					c1-d1,
					c2+d2,
					c3-(a2-a1)*s3
					))
				
				Quads.append([0,1,2,3])
				
				Verts.append((
					min1 if s1>0 else max1,
					c2-d2,
					c3+(a2+a1)*s3
					))
				Verts.append((
					min1 if s1>0 else max1,
					min2 if s2>0 else max2,
					c3+(a2+a1)*s3
					))
				Verts.append((
					c1-d1,
					min2 if s2>0 else max2,
					c3+(a2+a1)*s3
					))
				
				Quads.append([0,4,5,6])
				
				Verts.append((
					c1+d1,
					min2 if s2>0 else max2,
					c3+(a2-a1)*s3
					))
				Verts.append((
					min1 if s1<0 else max1,
					min2 if s2>0 else max2,
					c3+(a2-a1)*s3
					))
				Verts.append((
					min1 if s1<0 else max1,
					c2-d2,
					c3+(a2-a1)*s3
					))
				
				Quads.append([1,7,8,9])
				
				Verts.append((
					min1 if s1<0 else max1,
					c2+d2,
					c3-(a2+a1)*s3
					))
				Verts.append((
					min1 if s1<0 else max1,
					min2 if s2<0 else max2,
					c3-(a2+a1)*s3
					))
				Verts.append((
					c1+d1,
					min2 if s2<0 else max2,
					c3-(a2+a1)*s3
					))
				
				Quads.append([2,10,11,12])
				
				Verts.append((
					c1-d1,
					min2 if s2<0 else max2,
					c3-(a2-a1)*s3
					))
				Verts.append((
					min1 if s1>0 else max1,
					min2 if s2<0 else max2,
					c3-(a2-a1)*s3
					))
				Verts.append((
					min1 if s1>0 else max1,
					c2+d2,
					c3-(a2-a1)*s3
					))
				
				Quads.append([3,13,14,15])
				
				Quads.append([1,0,6,7])
				Quads.append([2,1,9,10])
				Quads.append([3,2,12,13])
				Quads.append([0,3,15,4])
				
			else:
				q = a1-(a3-a2)
				Verts.append(( # sphere 1 axis 3,2 intersect
					c1-d1+s1*q,
					c2-d2,
					c3+d3
					))
				Verts.append(( # sphere 1 axis 3,1 intersect
					c1-d1,
					c2-d2+s2*q,
					c3+d3
					))
				Verts.append(( # 2
					c1-d1,
					c2+d2,
					c3-d3+(a1*2.0-q)*s3
					))
				Verts.append(( # 3
					c1+d1-s1*q,
					c2+d2,
					c3-d3
					))
				Verts.append(( # 4
					c1+d1,
					c2+d2-s2*q,
					c3-d3
					))
				Verts.append(( # 5
					c1+d1,
					c2-d2,
					c3+d3-(a1*2.0-q)*s3
					))
				
				Poly.extend(range(6))
				
				Verts.append((
					c1-d1+s1*q,
					max2 if s2<0 else min2,
					c3+d3
					))
				Verts.append((
					c1-d1+s1*q,
					max2 if s2<0 else min2,
					max3 if s3>0 else min3
					))
				Verts.append((
					c1-d1+s1*q,
					c2-d2,
					max3 if s3>0 else min3
					))
				
				Quads.append([0,6,7,8])
				
				Verts.append(( # sphere 1 axis 3,1 intersect
					c1-d1,
					c2-d2+s2*q,
					max3 if s3>0 else min3
					))
				Verts.append(( # sphere 1 axis 3,1 intersect
					max1 if s1<0 else min1,
					c2-d2+s2*q,
					max3 if s3>0 else min3
					))
				Verts.append(( # sphere 1 axis 3,1 intersect
					max1 if s1<0 else min1,
					c2-d2+s2*q,
					c3+d3
					))
				
				Quads.append([1,9,10,11])
				
				Verts.append((
					max1 if s1<0 else min1,
					c2+d2,
					c3-d3+(a1*2.0-q)*s3
					))
				Verts.append((
					max1 if s1<0 else min1,
					max2 if s2>0 else min2,
					c3-d3+(a1*2.0-q)*s3
					))
				Verts.append((
					c1-d1,
					max2 if s2>0 else min2,
					c3-d3+(a1*2.0-q)*s3
					))
				
				Quads.append([2,12,13,14])
				
				Verts.append(( # 
					c1+d1-s1*q,
					max2 if s2>0 else min2,
					c3-d3
					))
				Verts.append(( # 
					c1+d1-s1*q,
					max2 if s2>0 else min2,
					max3 if s3<0 else min3
					))
				Verts.append(( # 
					c1+d1-s1*q,
					c2+d2,
					max3 if s3<0 else min3
					))
				
				Quads.append([3,15,16,17])
				
				Verts.append(( # 
					c1+d1,
					c2+d2-s2*q,
					max3 if s3<0 else min3
					))
				Verts.append(( # 
					max1 if s1>0 else min1,
					c2+d2-s2*q,
					max3 if s3<0 else min3
					))
				Verts.append(( # 
					max1 if s1>0 else min1,
					c2+d2-s2*q,
					c3-d3
					))
				
				Quads.append([4,18,19,20])
				
				Verts.append(( # 
					max1 if s1>0 else min1,
					c2-d2,
					c3+d3-(a1*2.0-q)*s3
					))
				Verts.append(( # 
					max1 if s1>0 else min1,
					max2 if s2<0 else min2,
					c3+d3-(a1*2.0-q)*s3
					))
				Verts.append(( # 
					c1+d1,
					max2 if s2<0 else min2,
					c3+d3-(a1*2.0-q)*s3
					))
				
				Quads.append([5,21,22,23])
				
				Quads.append([1,0,8,9])
				Quads.append([2,1,11,12])
				Quads.append([3,2,14,15])
				Quads.append([4,3,17,18])
				Quads.append([5,4,20,21])
				Quads.append([0,5,23,6])
		
		elif s.count(0.0)==1:
			Verts.append((
				min1 if s3>0 else max1,
				c2-d2,
				c3+(a2+a1)*s3
				))
			Verts.append((
				min1 if s3<0 else max1,
				c2-d2,
				c3+(a2-a1)*s3
				))
			Verts.append((
				min1 if s3<0 else max1,
				c2+d2,
				c3-(a2+a1)*s3
				))
			Verts.append((
				min1 if s3>0 else max1,
				c2+d2,
				c3-(a2-a1)*s3
				))
			
			Quads.append([0,1,2,3])
			
			Verts.append((
				min1 if s3<0 else max1,
				min2 if s2>0 else max2,
				c3+a2*s3
				))
			Verts.append((
				min1 if s3>0 else max1,
				min2 if s2>0 else max2,
				c3+a2*s3
				))
			
			Quads.append([5,4,1,0])
			
			n2= (c2+d2) if a2==a3 else (min2 if s2<0 else max2)
			n3= (min3 if s3>0 else max3) if a2==a3 else (c3-a2*s3)
			Verts.append((
				min1 if s3>0 else max1,
				n2,
				n3
				))
			Verts.append((
				min1 if s3<0 else max1,
				n2,
				n3
				))
			
			Quads.append([7,6,3,2])
			
		elif s.count(0.0)==2:
			Verts.append((
				min1 if s3>0 else max1,
				min2 if s3>0 else max2,
				c3
				))
			Verts.append((
				min1 if s3<0 else max1,
				min2 if s3>0 else max2,
				c3
				))
			Verts.append((
				min1 if s3<0 else max1,
				min2 if s3<0 else max2,
				c3
				))
			Verts.append((
				min1 if s3>0 else max1,
				min2 if s3<0 else max2,
				c3
				))
			
			Quads.append([0,1,2,3])
		
		Verts = [seq.demap(v) for v in Verts]
		
		if Verts: # debug
			# consistant red-facing normals of quads and poly
			v1=list((Verts[0]))
			v2=list((Verts[1]))
			v3=list((Verts[2]))
			faceNorm= vTriNorm(v1,v2,v3)
			faceNorm= vSgn(faceNorm)
			faceNorm = seq.remap(faceNorm)
			if tuple(vAdd(faceNorm,s)) != (0,0,0):
				for q in Quads: q.reverse()
				Poly.reverse()
			
			glDisable( GL_LIGHTING )
			if Poly:	self.drawPoly(c,Poly,Verts)
			for q in Quads:	self.drawQuad(q,Verts)
			self.drawVerts(Verts)
			glEnable( GL_LIGHTING )
			#glDisbale(GL_CULL_FACE)
	
	def drawLine(self, v1,v2):
		glLineWidth(8)
		glBegin(GL_LINES)
		glVertex3f( *(v1) )
		glVertex3f( *(v2) )
		glEnd()
	
	def drawVerts(self, verts):
		glPointSize(8)
		glBegin(GL_POINTS)
		for v in verts:
			glVertex3f( *(v) )
		glEnd()
		
		glColor3f( 1,1,1 )
		for i in range(len(verts)):
			glRasterPos3f(*(verts[i]))
			s=' v%i'%i
			for c in s:
				glutBitmapCharacter(GLUT_BITMAP_HELVETICA_18, ord(c));
	
	def drawQuad(self, quad, verts):
		glBegin(GL_QUADS)
		glColor3f( 1,0,0 )
		r=range(len(quad))
		for i in r:
			glVertex3f( *(verts[quad[i]]) )
		
		glColor3f( 0,0,1 )
		for i in reversed(r):
			glVertex3f( *(verts[quad[i]]) )
		glEnd()
		
		glColor3f( 1,1,1 )
		glBegin(GL_LINES)
		for i in range(len(quad)):
			v1=verts[quad[i-1]]
			v2=verts[quad[ i ]]
			glVertex3f( *(v1) )
			glVertex3f( *(v2) )
		glEnd()
	
	def drawPoly(self, c, poly, verts):
		glBegin(GL_TRIANGLE_FAN)
		glColor3f( 1,0,0 )
		glVertex3f( *c )
		for i in range(-1,len(poly)):
			glVertex3f( *(verts[poly[i]]) )
		glEnd()
		
		glBegin(GL_TRIANGLE_FAN)
		glColor3f( 0,0,1 )
		glVertex3f( *c )
		for i in reversed(range(-1,len(poly))):
			glVertex3f( *(verts[poly[i]]) )
		glEnd()
		
		glColor3f( 1,1,1 )
		glBegin(GL_LINES)
		for i in range(len(poly)):
			v1=verts[poly[i-1]]
			v2=verts[poly[ i ]]
			glVertex3f( *(v1) )
			glVertex3f( *(v2) )
		glEnd()
	
print PerpPlane
