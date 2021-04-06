a: list[int] = [10, 20, 30]
b: list[int] = [30, 40, 50]
c: list[int] = []

i = 0
while i < (len(a) - 1):
  c[i] = a[i] + b[i]
  c.append(c[i])
  i += 1
  


print(c)