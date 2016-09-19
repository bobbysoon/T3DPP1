class AxeSeq(tuple):
	def __new__(cls, tup):
		l=list(tup)
		NA=[0,1,2]
		a= [abs(l[i]) for i in NA ]
		iMin,iMax = a.index(min(a)),a.index(max(a))
		if iMin==iMax: iMap= NA
		else:
			iMid,= {0,1,2}-{iMin,iMax}
			iMap = [iMin,iMid,iMax]
		return tuple.__new__(cls, tuple(iMap))
	def remap(self, tup):
		return tuple([tup[i] for i in self])
	def demap(self, tup):
		lSelf=list(self)
		return tuple([tup[lSelf.index(i)] for i in [0,1,2]])

if __name__=='__main__':
	from random import random
	from sys import argv
	d= [eval(a) for a in argv[1:]]
	print d
	seq=AxeSeq(d)
	print seq
	print
	d=-5,9,-2
	print d
	d= seq.remap(d)
	print d
	print seq.demap(d)
