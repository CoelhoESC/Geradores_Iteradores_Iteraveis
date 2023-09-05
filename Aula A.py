"""
Geradores, iteradores e iteraveis
"""

# Iteravel --> Lista, tupla, strings, dicio e set (todos são objetos).
Lista = [1, 2, 3, 4, 5, 6]
Tupla = (1, 2, 3, 4, 5, 6)
Dicionario = {'Chave1': 'Valor', 'Chave2': 'Valor2'}
Set = {1, 2, 3, 4, 5}

# Para saber se é iteravel: "hasattr c/ metodo"
# hasattr --> Função do python que esta checando a lista, tupla... se existe o metodo '__iter__'.
print(Lista, hasattr(Lista, '__iter__'))
print(Tupla, hasattr(Tupla, '__iter__'))
print(Dicionario, hasattr(Dicionario, '__iter__'))
print(Set, hasattr(Set, '__iter__'))

# Iterador --> for e while. Tudo que transforma um Iteravel em iterador, obtendo seu valor um de cada vez!
for v in Lista:
    print(v)
print(Lista, hasattr(Lista, '__next__'))  # Verificando se a lista tem o metodo '__next__' para ser um Iterador.

# Para que a Lista seja um Iterador sem o for:
Lista = iter(Lista)
print(next(Lista))  # Mostra cada valor da lista, sem o laço de repetição!
print(next(Lista))  # next do funciona se existir um interador!
