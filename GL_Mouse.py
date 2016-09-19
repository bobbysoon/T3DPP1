from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from Obj import *

import os

def MouseRay(x,y):
	global MM, PM, VM
	MM = np.matrix(glGetDoublev(GL_MODELVIEW_MATRIX))
	PM = np.matrix(glGetDoublev(GL_PROJECTION_MATRIX))
	VM = glGetIntegerv(GL_VIEWPORT)
	wx,wy = float(x),float(VM[3] - float(y))
	z0,z1= float(0),float(1)
	p0= gluUnProject(wx, wy, z0, MM, PM, VM)
	p1= gluUnProject(wx, wy, z1, MM, PM, VM)
	return p0,p1

from time import time

class GL_Mouse:
	objSelected=None
	
	@classmethod
	def HitTest(cls, ray):
		hits = {}
		for obj in Obj.instances:
			if hasattr(obj, 'intersectsRay'):
				if obj.intersectsRay(ray):
					hits[vDist(ray[0],obj.pos)]= obj
		
		if hits:
			return hits[min(hits.keys())]
	
	@classmethod
	def MouseButton(cls, button, state, x, y):
		if state == GLUT_DOWN:
			if (button==GLUT_LEFT_BUTTON):
				ray=MouseRay(x,y)
				cls.objSelected= cls.HitTest(ray)
				if cls.objSelected:
					cls.MOVE_OBJ_Start(x,y)
				else:
					glutMotionFunc(cls.MOVE_EYE)
			
			elif (button==GLUT_MIDDLE_BUTTON):
				glutMotionFunc(cls.TRANS)
			elif (button==GLUT_RIGHT_BUTTON):
				glutMotionFunc(cls.MOVE_EYE)
			elif (button==3):
				if cls.zoom > 1.1:
					cls.zoom *= .9
					glutPostRedisplay()
			elif (button==4):
				if cls.zoom < 150.:
					cls.zoom /= .9
					glutPostRedisplay()
			
			cls.xStart = x
			cls.yStart = y
		if state == GLUT_UP:
			glutMotionFunc(None)
			if cls.objSelected: cls.MOVE_OBJ_End()
			#else: cls.ProbeSpray_End()
	
	@classmethod
	def MOVE_OBJ_Start(cls, x,y):
		global MM, PM, VM
		if hasattr(cls,'rectGridProbe'):
			cls.rectGridProbe.reset()
		#get screen relative obj offset, & world dist
		objX , objY , objZ = cls.objSelected.pos
		winX , winY , winZ = gluProject( objX , objY , objZ , MM, PM, VM ) 
		cls.objMoveOffset = winX-x , (VM[3]-winY)-y , winZ
		glutMotionFunc(cls.MOVE_OBJ)
		glutIdleFunc(cls.display)
	
	@classmethod
	def MOVE_OBJ(cls, x, y):
		global MM, PM, VM
		winX , winY , winZ = cls.objMoveOffset
		winY= VM[3]-(y+winY)
		p= list(gluUnProject(x+winX, winY, winZ, MM, PM, VM))
		
		other, = {cls.sphere1,cls.sphere2} - {cls.objSelected}
		op= list(other.pos)
		a=vAbs(vSub(op,p))
		nMax=max(a)
		for n in set(a) - {nMax}:
			if n<nMax/16.0:
				i=a.index(n)
				p[i] = op[i] # snap
		
		cls.objSelected.pos = p
	
	@classmethod
	def MOVE_OBJ_End(cls):
		cls.objSelected=None
		glutIdleFunc(cls.idle)
	
	lastTime = time()
	st_mtime = os.stat('PerpPlane.py').st_mtime
	@classmethod
	def idle(cls):
		if cls.paused:
			if hasattr(cls,'rectGridProbe') and cls.rectGridProbe.count<16000:
				cls.rectGridProbe.extend()
			
			st_mtime= os.stat('PerpPlane.py').st_mtime
			if st_mtime>cls.st_mtime:
				print st_mtime,cls.st_mtime
				cls.st_mtime = st_mtime
				cls.reload()
		else:
			t=time()
			tDelta=t-cls.lastTime
			cls.lastTime=t
			r2=2.0*cls.sphere1.radius
			pMin=vAddF(cls.rect.pMin,r2)
			pMax=vSubF(cls.rect.pMax,r2)
			pSize=vSub(pMax,pMin)
			for s in [cls.sphere1,cls.sphere2]:
				p = vAdd(s.pos,vMulF(s.inertia,tDelta))
				flip= vMul(vSgn(vSub(p,pMin)),vSgn(vSub(pMax,p)))
				if not -1 in flip:
					s.pos=p
				s.inertia= vMul(s.inertia,flip)
			
		cls.display()


