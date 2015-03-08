

import polypy
po = polypy

a = po.Poly([1])
for i in range(6):
	a *= po.Poly([i,1])
z = po.fzeros(a)
m = a(z)
if sum([abs(i) for i in m])>10**-6:
	print('001 zerofinder')
b = -a
a += 1
a += a
a *= 1
a *= a
a -= a
a -= 1
a //= po.Poly([1,1])
a **= 2
a >>= 2
a <<= 2
b = po.I(po.D(a))
if b.macht!=a.macht:
	print('002 integral en dif')