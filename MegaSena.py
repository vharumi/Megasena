from random import randint

lista1 = list()
jogos = list()
print('=' * 30)
print('          MEGASENA      ')
print('=' * 30)


def GeraAposta():
    quant = int(input('Quantos jogos você quer fazer? '))
    while True:
        numeros = int(input('Quantos números você quer jogar? '))
        if 6 <= numeros <= 15:
            break
        print('Você deve escolher um número entre 6 e 15')
    tot = 1
    while tot <= quant:
        cont = 0
        while True:
            num = randint(1, 60)
            if num not in lista1:
                lista1.append(num)
                cont += 1
            if cont >= numeros:
                break
        lista1.sort()
        jogos.append(lista1[:])
        lista1.clear()
        tot += 1
    for i, l in enumerate(jogos):
        print(f'Jogo {i + 1}:{l}')

    return jogos


def MegaSena():
    sorteado = list()
    contagem = 0
    while True:
        bola = randint(1, 60)
        if bola not in sorteado:
            sorteado.append(bola)
            contagem += 1
            if contagem == 6:
                break

    return sorteado

apostas=GeraAposta()
for i, l in enumerate(lista1):
    print(f'Jogo {i + 1}:{l}')

sorteios=MegaSena()
print('=*' * 30)
print(f'Os números da Mega Sena são:\n {sorteios}'.upper())
print('=*' * 30)

print('RESULTADO: ')
print('=*' * 30)
pontos = list()
for jogada, lista1 in enumerate(apostas):
    print(f'Na {jogada+1} jogada, você marcou: ', end="")
    for n, num in enumerate(lista1):
        if num in sorteios:
            pontos.append(num)
    print(pontos)
    pontos.clear()