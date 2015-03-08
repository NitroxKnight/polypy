# a0+a1*x+a2*x^2+a3*x^3+a4*x^4

## to do:
# __doc__ aanmaken
# https://docs.python.org/3/reference/datamodel.html#customizing-class-creation (type updatae)
# names (machten,macht)
# https://docs.python.org/3/reference/simple_stmts.html#raise
'''To create a Polynomial:
p = Poly([a0,a1,a2,.....])
then p will be: a0+a1*x+a2*x^2+a3*x^3+a4*x^4...'''
class Poly():
	'''To create a Polynomial:
	p = Poly([a0,a1,a2,.....])
	then p will be: a0+a1*x+a2*x^2+a3*x^3+a4*x^4...'''
	def __init__(self,coefficients): #create
		if type(coefficients)==int or type(coefficients)==float:
			self.macht = [coefficients]
		else:
			self.macht = coefficients
	##doc and str and print
	def __repr__(self):
		return self.__str__()
	def __call__(self,waarde): #bereken 
		if type(waarde)==list or type(waarde)==range:
			m = []
			for j in waarde: m.append(sum([self.macht[i]*j**i for i in range(len(self))]))
			return m
		else:
			return sum([self.macht[i]*waarde**i for i in range(len(self))])
	def __str__(self): #print
		r = 10 #round
		if len(self)==0:
			return '0'
		elif len(self)==1:
			return str(self.macht[0])
		else:
			start =''
			if abs(round(self.macht[0],r))!=0:
				start += str(abs(round(self.macht[0],r)))
			if abs(round(self.macht[1],r))!=0:
				if abs(self.macht[1])==self.macht[1]:
					t='+'
				else:
					t='-'
				if abs(round(self.macht[1],r))==1:
					start += ' '+t+' '+'x'
				else:
					start += ' '+t+' '+str(abs(round(self.macht[1],r)))+'*x'
			for i in range(2,len(self)):
				if abs(round(self.macht[i],r))!=0:
					if abs(self.macht[i])==self.macht[i]:
						t='+'
					else:
						t='-'
					if abs(round(self.macht[i],r))==1:
						start += ' '+t+' ' + 'x^'+str(i)
					else:
						start += ' '+t+' ' + str(abs(round(self.macht[i],r))) + '*x^'+str(i)
			if start[0]==' ':
				if start[1]=='+':
					if start[2]==' ':
						return start[3:]
					return start[2:]
				return start[1:]
			return start
			

	##tools:
	def rzero(self): #remove extra zero
		if sum([abs(i) for i in self.macht]) != 0:
			while self.macht[-1]==0:
				self.macht.pop(-1)
			return self
		else:
			return Poly([0])
	def equallength(self,machten):
		a = max(len(self),len(machten.macht))
		b = [0 for i in range(a)]
		c = [0 for i in range(a)]
		for i,j in enumerate(self.macht):
			b[i] = j
		for i,j in enumerate(machten.macht):
			c[i] = j
		return Poly(b),Poly(c)
	
	##len
	def __len__(self): #len
		return len(self.macht)
	
	##math
	# adding
	def __pos__(self):
		return self	
	def __add__(self,machten):#a+b
		if type(machten)==int or type(machten)==float:
			k = self.macht[:]
			k[0] = k[0]+machten
			return Poly(k)
		else:
			b,c = self.equallength(machten)
			return Poly([i+j for i,j in zip(b.macht,c.macht)])
	def __radd__(self,machten): #b+a
		return self+machten
	def __iadd__(self,machten): #a+=b
		return self+machten
	# subtrackting
	def __neg__(self): #-a
		return Poly([-i for i in self.macht])
	def __sub__(self,machten):#a-b
		if type(machten)==int or type(machten)==float:
			k = self.macht[:]
			k[0] = k[0]-machten
			return Poly(k)
		else:
			b,c = self.equallength(machten)
			return Poly([i-j for i,j in zip(b.macht,c.macht)])
	def __rsub__(self,machten):#b-a
		k = Poly([-i for i in self.macht[:]])
		m = -machten
		return k-m
	def __isub__(self,machten):#a -= b
		return self-machten
	#mulitply
	def __mul__(self,machten):
		if type(machten)==int or type(machten)==float:
			return Poly([i*machten for i in self.macht])
		else:
			b,c = self.equallength(machten)
			p = [0 for i in range(2*len(b)-1)]
			for i in range(len(b)):
				for j in range(len(c)):
					p[i+j] += b.macht[i]*c.macht[j]
			return Poly(p).rzero()
	def __rmul__(self,machten):
		return self*machten
	def __imul__(self,machten):
		return self*machten
	#devide	
	def __truediv__(self,machten): #machtennoom,rest
		if type(machten)==int or type(machten)==float:
			return Poly([i/machten for i in self.macht])
		else:
			q = len(self)-len(machten)
			if q<0:
				return Poly([0]),self
			else:
				atijd = Poly(self.macht[:])
				m = [0 for i in range(q+1)]
				for i in range(q+1):
					m[q-i] = atijd.macht[-1]/machten.macht[-1]
					atijd = atijd-((machten>>(q-i))/machten.macht[-1])*atijd.macht[-1]
					atijd.macht.pop(-1)
				return Poly(m),atijd
	def __itruediv__(self,machten):
		return self/machten
	def __floordiv__(self,machten):
		p,r = self/machten
		return p
	def __ifloordiv__(self,machten):
		return self//machten
	def __mod__(self,machten):
		p,r = self/machten
		return r
	def __imod__(self,machten):
		return self%machten
	def __divmod__(self,machten):
		return self/machten
	# 
	def __rshift__(self,g):
		if g>0:
			a = [0 for i in range(g+len(self))]
			for i in range(len(self)): a[i+g]=self.macht[i]
			return Poly(a)
		elif g<0:
			a = [0 for i in range(g+len(self))]
			for i in range(len(self)+g): a[i] = self.macht[i-g]
			return Poly(a)
		elif g==0:
			return self
	def __irshift__(self,g):
		return self>>g
	def __lshift__(self,g):
		return self>>-g
	def __ilshift__(self,g):
		return self<<g
	
	def __pow__(self,p): #machten**int
		#error handeling
		if p==0:
			return Poly([0])
		elif p == 1:
			return self
		else:
			L = Poly(self.macht[:])
			for i in range(1,p):
				L *= self
			return L.rzero()
	def __ipow__(self,p):
		return self**p

def D(machten):
	return Poly([i*p for i,p in zip(range(1,len(machten)),(machten<<1).macht)])

def I(machten):
	return Poly([p/i for i,p in zip([1]+list(range(1,len(machten)+1)),(machten>>1).macht)])
	
def fzeros(machten,startpunt=0,acc=10**-10):
	p = []
	def fzero(machten,startpunt,acc,doorslag):
		z = []
		af = D(machten)
		x = startpunt
		dx = 1
		i = 0
		while dx>=acc and i<doorslag:
			i += 1
			xoud = x
			t = af(x)
			if t==0:
				z = 'deelnul'
				i = doorslag
			else:
				x -= machten(x)/t
			dx = abs(xoud-x)
		if i==doorslag:
			if z == 'deelnul':
				return 'deelnul'
			else:
				return 'doorslag'
		else:
			return x
	werkmachten = Poly(machten.macht[:]).rzero()
	control = 0
	m = 0
	while True:
		m = fzero(werkmachten,m,acc,50)
		if m=='doorslag':
			return p
		elif m=='deelnul':
			m = control
			control+=1
			if control == 5:
				return p
		else:
			p.append(m)
			werkmachten //= Poly([-m,1])

def pointstopoly(x,y):
	def l(x,i):
		#t/m
		t = Poly([1])
		m = 1
		for p in range(len(x)):
			if p!=i:
				m *= x[i]-x[p]
				t *= Poly([-x[p],1])
		return t/m
	L = Poly([0])
	for i,j in enumerate(y):
		L += j*l(x,i)
	return L.rzero()


