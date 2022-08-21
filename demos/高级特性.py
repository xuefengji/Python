a = list(range(0,10))
print(a)

b = [x*x for x in a]
print(b)

c = (x*x for x in a)
print(c)
