def poly_add2(p1, p2):
   sum = [0,0,0]
   sum[0] = (p1[0] + p2[0])
   sum[1] = (p1[1] + p2[1])
   sum[2] = (p1[2] + p2[2])
   return sum

def poly_mult2(p1, p2):
   l = [0,0,0,0,0]
   l[4] = p1[0]*p2[0]
   l[3] = p1[0]*p2[1] + p1[1]*p2[0]
   l[2] = p1[0]*p2[2] + p1[1]*p2[1] + p1[2]*p2[0]
   l[1] = p1[1]*p2[2] + p1[2]*p2[1]
   l[0] = p1[2]*p2[2]
   return l