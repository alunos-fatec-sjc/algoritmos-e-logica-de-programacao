from random import sample
v = sample(range(1, 101), 20)
par = []
impar = []
for x in v:
  if x % 2 == 0:
    par.append(x)
  else:
    impar.append(x)
print("Lista: {}".format(v))
print("N�meros pares dessa lista: {}".format(par))
print("N�meros �mpares dessa lista: {}".format(impar))
