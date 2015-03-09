

import polypy
po = polypy

a = po.poly([1])
for i in range(6):
	a *= po.poly([i,1])
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
a //= po.poly([1,1])
a **= 2
a >>= 2
a <<= 2
b = po.I(po.D(a))
if b.terms!=a.terms:
	print('002 integral en dif')
print('done')