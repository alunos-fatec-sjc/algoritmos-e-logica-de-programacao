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
