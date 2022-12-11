a = (5,7)
b = a
for c,i in enumerate(a, 0):
    a[c] += 1
    print(f"a:{a} b:{b}")