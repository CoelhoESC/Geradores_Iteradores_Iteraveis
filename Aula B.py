import sys, time

# Geradores --> São utilizados, quando precisamos usar valores que não gasta muita memoria, ou tempo, ou performa-se. Ex

Lista = list(range(10))
# As lista salva os valores na memoria, consumindo memoria(bytes)!
print('Pegando o consumo de bytes da lista =', Lista, (sys.getsizeof(Lista)))


def gera():
    r = []
    for n in range(20):
        r.append(n)
        time.sleep(0.1)  # Simulando um função "pesada". A um consumo grande de memoria, pois a lista salva os valores!
    return r


lista = list(gera())


def gerador():
    for v in range(20):
        yield v  # Pausa e entrega um valor (Qualquer tipo de dado)


gerador = list(gerador())


def gerador_ecomico():
    return (v for v in range(20))


gerador_ecomic = list(gerador_ecomico())

# Manda um valor de cada vez, e economiza byte! Pq diferente da lista, ele não as salvas totalmente
print("Consumo de memoria")
print('Gerador com yield ->', gerador, 'Memoria:', sys.getsizeof(gerador))
print('Lista ->', lista, 'Memoria:', sys.getsizeof(lista))
print('Gerador economico ->', gerador_ecomic, 'Memoria:', sys.getsizeof(gerador_ecomico()))
