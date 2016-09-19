from OpenGL.GL import *
from OpenGL.GLU import *
from OpenGL.GLUT import *

from vMath import *
import numpy as np
from time import time
from random import random

import atexit

from GL_Init import *
from GL_Basics import *
from GL_Display import *
from GL_Mouse import *
from GL_Keyboard import *
from GL_DrawText import *
from GL_Probe import *

import PerpPlane
import RectGridProbe

class GL(GL_Init, GL_Basics, GL_Display, GL_Mouse, GL_Keyboard, GL_DrawText, GL_Probe):
	@staticmethod
	def reload():
		try:
			reload(PerpPlane)
			Obj.instances.remove(GL.perpPlane)
			GL.perpPlane= PerpPlane.PerpPlane( GL.sphere1, GL.sphere2, GL.rect )
			print 'reloaded'
		except:
			print 'failed to reload'


GL.resetView()
GL.glutHooks()
atexit.register(glutMainLoop)

if __name__=="__main__":
	GL.KeyBinds['r'] = GL.reload
	
	GL.rect= Rect( pMin=(-3,-4,-5),pMax=(5,4,3) , col=(.25,.25,.25) )
	
	c=1,1,1
	d=1,0,0
	p1=vAdd(c,d)
	p2=vSub(c,d)
	GL.sphere1= Sphere(pos=p1,col=(1,0,0),radius=.25, text='c1' )
	GL.sphere2= Sphere(pos=p2,col=(0,0,1),radius=.25, text='c2' )
	GL.centroids= [GL.sphere1,GL.sphere2]
	GL.wireRect= WireRect(col=(0,1,0),pMin=GL.sphere1,pMax=GL.sphere2)
	
	GL.perpPlane= PerpPlane.PerpPlane( GL.sphere1, GL.sphere2, GL.rect )
	GL.rectGridProbe = RectGridProbe.RectGridProbe(GL)
	
	
	def PlayPause():
		GL.paused=not GL.paused
		GL.rectGridProbe.reset()
		glutIdleFunc(GL.idle)
	
	GL.paused=True
	GL.KeyBinds[' '] = PlayPause
	
	GL.sphere1.inertia = vNorm_(vRnd())
	GL.sphere2.inertia = vNorm_(vRnd())

