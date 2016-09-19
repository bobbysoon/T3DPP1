import numpy as np
from math import *
from random import random

class V(tuple):
	@classmethod
	def rnd(cls,s=1.0): return cls((rnd(s),rnd(s),rnd(s)))
	
	def abs(self):				return V(( abs(self[0]) , abs(self[1]) , abs(self[2]) ))
	def min(self):				return min(self)
	def max(self):				return max(self)
	def sgn(self):				return V(( copysign(1,self[0]) , copysign(1,self[1]) , copysign(1,self[2]) ))
	
	def __add__(self, other):
		if type(other) is int: other=float(other)
		if type(other) is float: other=other,other,other
		return V(( self[0]+other[0] , self[1]+other[1] , self[2]+other[2] ))
	def __sub__(self, other):
		if type(other) is int: other=float(other)
		if type(other) is float: other=other,other,other
		return V(( self[0]-other[0] , self[1]-other[1] , self[2]-other[2] ))
	def __mul__(self, other):
		if type(other) is int: other=float(other)
		if type(other) is float: other=other,other,other
		return V(( self[0]*other[0] , self[1]*other[1] , self[2]*other[2] ))
	def __div__(self, other):
		if type(other) is int: other=float(other)
		if type(other) is float: other=other,other,other
		return V(( self[0]/other[0] , self[1]/other[1] , self[2]/other[2] ))


def sign(n):
	return -1. if n<0 else 1. if n>0 else 0.
sgn=sign

def rnd(s): return (random()-random())*s
def vRnd(s=1.0): return rnd(s),rnd(s),rnd(s)
def cRnd(): return .5+rnd(.5),.5+rnd(.5),.5+rnd(.5),.5+rnd(.5)

def vDot(u,v):	return u[0]*v[0] + u[1]*v[1] + u[2]*v[2]
def vCross(a, b):
	a0,a1,a2=a
	b0,b1,b2=b
	return (a1*b2 - a2*b1,
			a2*b0 - a0*b2,
			a0*b1 - a1*b0)

def vTriNorm(v1,v2,v3):
	return vCross(
		( map(lambda x,y:x-y, v1,v2) ) ,
		( map(lambda x,y:x-y, v1,v3) ) )

def vAdd(a,b): return map(lambda x,y:x+y, a,b)
def vSub(a,b): return map(lambda x,y:x-y, a,b)
def vMul(a,b): return map(lambda x,y:x*y, a,b)
def vDiv(a,b): return map(lambda x,y:x/y, a,b)

def vAddF(a,b): return map(lambda x:x+b, a)
def vSubF(a,b): return map(lambda x:x-b, a)
def vMulF(a,b): return map(lambda x:x*b, a)
def vDivF(a,b): return map(lambda x:x/b, a)

def vAbs(v): return map(lambda n:abs(n), v)
def vSgn(v): return map(lambda n:(1.0 if n>0 else -1.0 if n<0 else 0.0), v)
def vLen(v): return sqrt(sum( map(lambda n:n*n, v) ))
def vNorm(v):	return sqrt(vDot(v,v))
def vNorm_(v):
	l=vLen(v)
	return map(lambda n:n/l, v)
def vDist(p1,p2): return vLen(vSub(p1,p2))

def vAvrg(a,b): return map(lambda x,y:(x+y)/2.0, a,b)

def vCol(p): return vDivF(vAddF(p,10.0),20.0)

def mDist(a,b): return sum(map(lambda x,y:abs(x-y), a,b))

centroids = []
def Centroids(count=None, tooSmall=.1, scale=1.0 ):
	global centroids
	if count:
		print 'Centroids...' # Stuck here? Reduce count or tooSmall, or increase scale
		while True:
			C=[vRnd(scale) for i in range(count)]
			smallest = min( [min(map(lambda x,y:abs(x-y), C[i],C[j] )) for i in range(1,len(C)) for j in range(i)] )
			if smallest>tooSmall: break
		centroids=C
	return centroids

def Regions(pos,ep=.1):
	global centroids
	l=len(centroids)
	dists= [mDist(pos,c) for c in centroids]
	md=min(dists)+ep
	dists= [(dists[i],centroids[i]) for i in range(l) if dists[i]<md]
	return zip(*sorted(dists,key=lambda tup:tup[0]))[1]

def Region(pos,ep=.01):
	global centroids
	l=len(centroids)
	dists= [sum(map(lambda x,y:abs(x-y), pos,c)) for c in centroids]
	md=min(dists)
	return centroids[dists.index(md)]

def PointLineDist(c , p0,p1):
	v= vSub(p1,p0)
	w= vSub(c,p0)
	c1= vDot(w,v)
	c2= vDot(v,v)
	b= c1/c2
	p= vAdd(p0,vMulF(v,b))
	return vNorm(vSub(c,p))


def VecRot(vec, axis, theta):
	axis = np.asarray(axis)
	theta = np.asarray(theta)
	axis = axis/sqrt(np.dot(axis, axis))
	a = cos(theta/2.0)
	b, c, d = -axis*sin(theta/2.0)
	aa, bb, cc, dd = a*a, b*b, c*c, d*d
	bc, ad, ac, ab, bd, cd = b*c, a*d, a*c, a*b, b*d, c*d
	rotation_matrix = np.array([[aa+bb-cc-dd, 2*(bc+ad), 2*(bd-ac)],
										[2*(bc-ad), aa+cc-bb-dd, 2*(cd+ab)],
										[2*(bd+ac), 2*(cd-ab), aa+dd-bb-cc]])

	return np.dot(rotation_matrix, vec)



if __name__=='__main__':
	from time import time
	r=range(100000)
	a=1.1,2.2,3.3
	b=3.3,2.2,1.1
	
	va,vb = V(a),V(b)
	
	a1,a2,a3=a
	b1,b2,b3=b
	
	t1=time() # fastest
	for i in r:
		c=a1/b1,a2/b2,a3/b3
	t2=time()
	print t2-t1
	
	t1=time() # 2nd fastest
	for i in r:
		c=a[0]/b[0],a[1]/b[1],a[2]/b[2]
	t2=time()
	print t2-t1
	
	t1=time() # slower
	for i in r:
		c=map(lambda x,y:x/y, a,b)
	t2=time()
	print t2-t1
	
	t1=time() # slower
	for i in r:
		c=va/vb
	t2=time()
	print t2-t1
	
	t1=time() # slowest
	for i in r:
		c=vDiv(a,b)
	t2=time()
	print t2-t1



