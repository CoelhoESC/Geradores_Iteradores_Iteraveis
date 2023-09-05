import sys


# Com gerador, eles possui os metodos '__next__' e '__iter__', com isso, posso usar o for ou next para iterar!

def gerador():
    texto = 'Olá mundo'
    yield texto
    texto = 'Tudo bem?'
    yield texto
    texto = 'Deus está com conosco'
    yield texto


for x in gerador():
    print(x)
# texto = gerador()
# print(next(texto))
# print(next(texto))
# print(next(texto))
# print()

print("Mostrando a diferença de bytes entre Lista e Gerador:")
# Podemos criar um gerador facilmente:
L1 = [v for v in range(1000)]
L2 = (v for v in range(1000))  # gerador
print(f'Lista possui {sys.getsizeof(L1)} de bytes')
print(f'Gerador possui {sys.getsizeof(L2)} de bytes')
