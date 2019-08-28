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
print("Números pares dessa lista: {}".format(par))
print("Números ímpares dessa lista: {}".format(impar))

03)
from random import sample
v1 = sample(range(1, 101), 10)
v2 = sample(range(1, 101), 10)
print ("Lista 1: {}".format(v1))
print ("Lista 2: {}".format(v2))
v3 = []
for k in range(10):
  v3.append(v1[k])
  v3.append(v2[k])
print ("Lista intercalada: {}".format(v3))

04)
import string
frase = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''
frase = frase.replace(':', ' ')
frase = frase.replace(',', ' ')
frase = frase.replace('.', ' ')
frase = frase.lower()
frase = frase.split()
lista = []
for p in frase:
  if p[0] in 'python' or p[-1] in 'python':
    lista.append (p)
print (lista)

05)
import string
frase = '''The Python Software Foundation and the global Python community welcome and encourage participation by everyone. Our community is based on mutual respect, tolerance, and encouragement, and we are working to help each other live up to these principles. We want our community to be more diverse: whoever you are, and whatever your background, we welcome you'''
frase = frase.replace(':', ' ')
frase = frase.replace(',', ' ')
frase = frase.replace('.', ' ')
frase = frase.lower()
frase = frase.split()

def pitônica(palavra):
  for letra in palavra:
    if letra in 'python':
      return True
  return False

lista = []
for p in frase:
  if pitônica(p) and len(p) > 4:
    lista.append(p)
print (lista)
print (len(lista))
