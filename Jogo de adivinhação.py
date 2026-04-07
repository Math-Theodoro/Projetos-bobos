import random
numero_secreto = random.randint(1,10)
tentativa = 0
while tentativa <= 2:
    chute = int(input('Chute um numero de 1 a 10: '))
    if chute == numero_secreto:
        print('Você acertou')
        break
    elif chute > numero_secreto:
        print(f'O numero é menor que {chute}')
    else:
        print(f'O numero é maior que {chute}')
    tentativa = tentativa + 1
    print(f'Tentativas usadas {tentativa}: Você tem mais {3 - tentativa}')
if chute != numero_secreto:
    print(f'Game Over, o numero era: {numero_secreto}')