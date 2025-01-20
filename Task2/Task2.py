
text = input()
k = len(text)
a = text.count('a')
if a > 0:
    print ("Количество букв а = ", a)
else:
   print ("False")
e = text.count('e')
if e > 0:
    print ("Количество букв e = ", e)
else:
   print ("False")
i= text.count('i')
if i > 0:
    print ("Количество букв i = ", i)
else:
   print ("False")
o = text.count('o')
if o > 0:
    print ("Количество букв o = ", o)
else:
   print ("False")
u = text.count('u')
if u > 0:
    print ("Количество букв u = ", u)
else:
   print ("False")
g = a+e+i+o+u
print ("Общее количество гласных = ", g)
print ("Общее количество согласных = ",k-g)
