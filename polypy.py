

## to do:
# https://docs.python.org/3/reference/datamodel.html#customizing-class-creation (type updatae)
# error raiseing: https://docs.python.org/3/reference/simple_stmts.html#raise
# make equallength more effective
# test
'''

# polypy
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
	singlezero = fsinglezero(foo,startx,acc=10**-14,maxinter=200)
	
'''


class poly():
	'''
	
	a polynomial is defind as a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 .... an*x^n
	p = poly([a0,a1,a2,.....])
	to calculate a point, p(x)
	
	'''
	def __init__(self,coefficients): #create
		if type(coefficients)==int or type(coefficients)==float:
			self.terms = [coefficients]
		else:
			self.terms = coefficients
	##doc and str and print
	def __repr__(self):
		return self.__str__()
	def __call__(self,x): #bereken 
		if type(x)==list or type(x)==range:
			m = []
			for j in x: m.append(sum([self.terms[i]*j**i for i in range(len(self))]))
			return m
		else:
			return sum([self.terms[i]*x**i for i in range(len(self))])
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
		'''
		removal of the end zeros of the p.data array
		1+x+0*x**2+0*x**3 --> 1+x
		'''
		if sum([abs(i) for i in self.terms]) != 0:
			while self.terms[-1]==0:
				self.terms.pop(-1)
			return self
		else:
			return poly([0])
	def equallength(self,powers):
		'''
		
		returns 2 polynomial of the same length
		
		'''
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
		'''
		return the amount of terms (that is equal to the highst power+1)
		len(1+x) --> 2 
		len(x+x**2) --> 3
		'''
		return len(self.terms)
	
	##math
	# adding
	def __pos__(self): #+a
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
		'''
		returns the multiple of 2 polynomials (also works with int and float)
		
		'''		
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
	def __truediv__(self,powers): #polynomial,remainder
		'''
		If the denominator is an int or a foat:
			all the terms will get diveded by the int/foat
		
		If the denominator is an poly:
			more info on: http://en.wikipedia.org/wiki/Polynomial#Divisibility
			self/powers == polynomial+remainder/powers --> self == powers*polynomial+remainder
			This finds the polynomial and remainder suchs that this is true.
			returns the (polynomial,remainder)
			note: both polynomial and remainder is a polynomial
		
		'''
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
		'''
		return just the polynomial in self/powers
		'''
		p,r = self/powers
		return p
	def __ifloordiv__(self,powers):
		return self//powers
	def __mod__(self,powers):
		'''
		returns just the remainder of self/powers
		'''
		p,r = self/powers
		return r
	def __imod__(self,powers):
		return self%powers
	def __divmod__(self,powers):
		'''
		same as self/powers
		'''
		return self/powers
	#a>>2 is the same as a*x**2 and a<<2 is the same as (a/x**2)//1
	def __rshift__(self,g):
		'''
		this is no real mathematical operation but here it is defind as:
			self>>2==self*x**2
			self<<2==self//x**2 (//==floordiv)
		'''
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
		'''
		this is no real mathematical operation but here it is defind as:
			self>>2==self*x**2
			self<<2==self//x**2 (//==floordiv)
		'''
		return self>>-g
	def __ilshift__(self,g):
		return self<<g
	#powers**int
	def __pow__(self,p): 
		'''
		returns the self**p==self*self**(p-1)
		with self**0==1
		'''
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
	'''
	gives the d/dx*powers
	'''
	return poly([i*p for i,p in zip(range(1,len(powers)),(powers<<1).terms)])

def I(powers):
	'''
	give the integral of a polynomial
	with c=0
	'''
	return poly([p/i for i,p in zip([1]+list(range(1,len(powers)+1)),(powers>>1).terms)])

def fsinglezero(powers,startx,acc=10**-14,maxinter=200):
	'''
	finds a root of the polynomial close to the startx
	'''
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
			z = 'flat'
			i = maxinter
		else:
			x -= powers(x)/t
		dx = abs(xoud-x)
	if i==maxinter:
		if z == 'flat':
			return 'flat'
		else:
			return 'no zeros found'
	else:
		return x

def fzeros(powers,startx=0,acc=10**-10):
	'''
	
	This function gives all* the real roots (poly=0) for a given polynomial
	
	* if the function is not to complex it will find all the roots
	example: 0.1+x**2-(10**-10)*x**4
	
	'''
	p = []
	workworkpowers = poly(powers.terms[:]).rzero()
	control = 0
	m = startx
	while True:
		m = fsinglezero(workworkpowers,m,acc,50)
		if m=='no zeros found':
			return p
		elif m=='flat':
			m = control
			control+=1
			if control == 5:
				return p
		else:
			p.append(m)
			workworkpowers //= poly([-m,1])

def ptopoly(x,y):
	'''
	genartes a polynomial through the x and y point given
	More info how this is done: http://en.wikipedia.org/wiki/Lagrange_polynomial
	'''
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


