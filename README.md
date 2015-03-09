# polypy
This module was made to do polynomial calculus with python. Made for python 3

features are:
  * Generate a polynomial from x and y point.
  * Integrating and differentiate a polynomial
  * Finding roots (real)
  * General calculus (like:+,-,\*,/,//,%,**)
  
To install place the polypy.py file in the \Python34\Lib folder or past the file in the folder were the module is used.

## How to use the module

Every polinomial is defind as: a0 + a1*x + a2*x^2 + a3*x^3 + a4*x^4 .... an*x^n

to create a polinomial, foo = polypy.poly([a0,a1,a2,a3,a4,..an])

to create a polinomial from points, foo = polypy.ptopoly(x,y) 

to calculate a point, value = foo(x)  (x can also be a list or a range)

to differentiate, dif = polypy.D(foo)

to Integrate, inte = polypy.I(foo)

to find zeros, zerolist = polypy.fzeros(foo,startx=0,acc=10**-10)

