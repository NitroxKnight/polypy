# a0+a1*x+a2*x^2+a3*x^3+a4*x^4

## to do:
# make __doc__
# https://docs.python.org/3/reference/datamodel.html#customizing-class-creation (type updatae)
# error raiseing: https://docs.python.org/3/reference/simple_stmts.html#raise

'''# polypy
This module was made to do polynomial calculus with python. Made for python 3

features are:
  * Generate a polynomial from x and y point.
  * Integrating and differentiate a polynomial
  * Finding roots (real)
  * General calculus with polynomials (like:+,-,\*,/,//,%,**)
  
To install place the polypy.py file in the \Python(vers)\Lib folder or past the polypy.py in the folder were the module is used.

## How to use the module
Every polinomial is defind as: 
	a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 .... an*x^n
to create a polinomial, 
	foo = polypy.poly([a0,a1,a2,a3,a4,..an])
to create a polinomial from points, 
	foo = polypy.ptopoly(x,y) 
to calculate a point, 
	value = foo(x)  (x can also be a list or a range)
to differentiate, 
	dif = polypy.D(foo)
to Integrate, 
	inte = polypy.I(foo)
to find zeros, 
	zerolist = polypy.fzeros(foo,startx=0,acc=10**-10)
to find a single zeros (most property the closest to the startx):
	singlezero = fsinglezero(foo,startx,acc=10**-14,maxinter=200)'''


class poly():
	'''a polynomial is defind as a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 .... an*x^n
	p = poly([a0,a1,a2,.....])
	to calculate a point, p(x)'''
	def __init__(self,coefficients): #create
		if type(coefficients)==int or type(coefficients)==float:
			self.terms = [coefficients]
		else:
			self.terms = coefficients
	##doc and str and print
	def __repr__(self):
		return self.__str__()
	def __call__(self,waarde): #bereken 
		if type(waarde)==list or type(waarde)==range:
			m = []
			for j in waarde: m.append(sum([self.terms[i]*j**i for i in range(len(self))]))
			return m
		else:
			return sum([self.terms[i]*waarde**i for i in range(len(self))])
	def __str__(self): #print
		r = 10 #round
		if len(self)==0:
			return '0'
		elif len(self)==1:
			return str(self.terms[0])
		else:
			start =''
			if abs(round(self.terms[0],r))!=0:
				start += str(abs(round(self.terms[0],r)))
			if abs(round(self.terms[1],r))!=0:
				if abs(self.terms[1])==self.terms[1]:
					t='+'
				else:
					t='-'
				if abs(round(self.terms[1],r))==1:
					start += ' '+t+' '+'x'
				else:
					start += ' '+t+' '+str(abs(round(self.terms[1],r)))+'*x'
			for i in range(2,len(self)):
				if abs(round(self.terms[i],r))!=0:
					if abs(self.terms[i])==self.terms[i]:
						t='+'
					else:
						t='-'
					if abs(round(self.terms[i],r))==1:
						start += ' '+t+' ' + 'x^'+str(i)
					else:
						start += ' '+t+' ' + str(abs(round(self.terms[i],r))) + '*x^'+str(i)
			if start[0]==' ':
				if start[1]=='+':
					if start[2]==' ':
						return start[3:]
					return start[2:]
				return start[1:]
			return start
			

	##tools:
	def rzero(self): #remove extra zero on the end of a polynomial
		if sum([abs(i) for i in self.terms]) != 0:
			while self.terms[-1]==0:
				self.terms.pop(-1)
			return self
		else:
			return poly([0])
	def equallength(self,powers):
		a = max(len(self),len(powers.terms))
		b = [0 for i in range(a)]
		c = [0 for i in range(a)]
		for i,j in enumerate(self.terms):
			b[i] = j
		for i,j in enumerate(powers.terms):
			c[i] = j
		return poly(b),poly(c)
	
	##len
	def __len__(self): #len
		return len(self.terms)
	
	##math
	# adding
	def __pos__(self):
		return self	
	def __add__(self,powers):#a+b
		if type(powers)==int or type(powers)==float:
			k = self.terms[:]
			k[0] = k[0]+powers
			return poly(k)
		else:
			b,c = self.equallength(powers)
			return poly([i+j for i,j in zip(b.terms,c.terms)])
	def __radd__(self,powers): #b+a
		return self+powers
	def __iadd__(self,powers): #a+=b
		return self+powers
	# subtrackting
	def __neg__(self): #-a
		return poly([-i for i in self.terms])
	def __sub__(self,powers):#a-b
		if type(powers)==int or type(powers)==float:
			k = self.terms[:]
			k[0] = k[0]-powers
			return poly(k)
		else:
			b,c = self.equallength(powers)
			return poly([i-j for i,j in zip(b.terms,c.terms)])
	def __rsub__(self,powers):#b-a
		k = poly([-i for i in self.terms[:]])
		m = -powers
		return k-m
	def __isub__(self,powers):#a -= b
		return self-powers
	#multiply
	def __mul__(self,powers):
		if type(powers)==int or type(powers)==float:
			return poly([i*powers for i in self.terms])
		else:
			b,c = self.equallength(powers)
			p = [0 for i in range(2*len(b)-1)]
			for i in range(len(b)):
				for j in range(len(c)):
					p[i+j] += b.terms[i]*c.terms[j]
			return poly(p).rzero()
	def __rmul__(self,powers):
		return self*powers
	def __imul__(self,powers):
		return self*powers
	#divide	
	def __truediv__(self,powers): #powersnoom,rest
		if type(powers)==int or type(powers)==float:
			return poly([i/powers for i in self.terms])
		else:
			q = len(self)-len(powers)
			if q<0:
				return poly([0]),self
			else:
				atijd = poly(self.terms[:])
				m = [0 for i in range(q+1)]
				for i in range(q+1):
					m[q-i] = atijd.terms[-1]/powers.terms[-1]
					atijd = atijd-((powers>>(q-i))/powers.terms[-1])*atijd.terms[-1]
					atijd.terms.pop(-1)
				return poly(m),atijd
	def __itruediv__(self,powers):
		return self/powers
	def __floordiv__(self,powers):
		p,r = self/powers
		return p
	def __ifloordiv__(self,powers):
		return self//powers
	def __mod__(self,powers):
		p,r = self/powers
		return r
	def __imod__(self,powers):
		return self%powers
	def __divmod__(self,powers):
		return self/powers
	#a>>2 is the same as a*x**2 and a<<2 is the same as (a/x**2)//1
	def __rshift__(self,g):
		if g>0:
			a = [0 for i in range(g+len(self))]
			for i in range(len(self)): a[i+g]=self.terms[i]
			return poly(a)
		elif g<0:
			a = [0 for i in range(g+len(self))]
			for i in range(len(self)+g): a[i] = self.terms[i-g]
			return poly(a)
		elif g==0:
			return self
	def __irshift__(self,g):
		return self>>g
	def __lshift__(self,g):
		return self>>-g
	def __ilshift__(self,g):
		return self<<g
	#powers**int
	def __pow__(self,p): 
		#error handeling
		if p==0:
			return poly([0])
		elif p == 1:
			return self
		else:
			L = poly(self.terms[:])
			for i in range(1,p):
				L *= self
			return L.rzero()
	def __ipow__(self,p):
		return self**p

def D(powers):
	return poly([i*p for i,p in zip(range(1,len(powers)),(powers<<1).terms)])

def I(powers):
	return poly([p/i for i,p in zip([1]+list(range(1,len(powers)+1)),(powers>>1).terms)])

def fsinglezero(powers,startx,acc=10**-14,maxinter=200):
	z = []
	af = D(powers)
	x = startx
	dx = 1
	i = 0
	while dx>acc and i<maxinter:
		i += 1
		xoud = x
		t = af(x)
		if t==0:
			z = 'deelnul'
			i = maxinter
		else:
			x -= powers(x)/t
		dx = abs(xoud-x)
	if i==maxinter:
		if z == 'deelnul':
			return 'deelnul'
		else:
			return 'maxinter'
	else:
		return x

def fzeros(powers,startx=0,acc=10**-10):
	'''This function gives all[1] the real roots (poly=0) for a given polynomial
	
	[1] if the function is not to complex it will find all the roots
	example: 0.1+x**2-(10**-10)*x**4'''
	p = []
	workworkpowers = poly(powers.terms[:]).rzero()
	control = 0
	m = startx
	while True:
		m = fsinglezero(workworkpowers,m,acc,50)
		if m=='maxinter':
			return p
		elif m=='deelnul':
			m = control
			control+=1
			if control == 5:
				return p
		else:
			p.append(m)
			workworkpowers //= poly([-m,1])

def ptopoly(x,y):
	def l(x,i):
		#t/m
		t = poly([1])
		m = 1
		for p in range(len(x)):
			if p!=i:
				m *= x[i]-x[p]
				t *= poly([-x[p],1])
		return t/m
	L = poly([0])
	for i,j in enumerate(y):
		L += j*l(x,i)
	return L.rzero()


