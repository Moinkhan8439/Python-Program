import math
(p,b)=(int(input()),int(input()))
c=math.atan(p/b)
anglec=c*180/math.pi
mc=math.sqrt(p**2+b**2)/2
print("MC",mc)
mb=b**2+mc**2-2*b*mc*math.cos(anglec)
x=(mc**2-b**2-mb**2)/2*b*mb
print("X",x)
rad=math.acos(x)
deg=rad*180/math.pi
print("{}°".format(deg))