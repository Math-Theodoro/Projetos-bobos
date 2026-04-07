avaliacao = True #a avaliação serve para que o loop continue a se repetir
while avaliacao == True: #enquanto a avaliação for igual ao True, ela ira repetir o código
    while True: #cria um loop de verificação dentro do loop
        semestre1 = float(input('Digite a nota do 1° semestre: ')) #semestre1 serve para pegar o 1°valor do aluno que vale tanto pro 2° e 3°
        if semestre1 < 0 or semestre1 > 10: #isso verifica se a nota digitada é menor que 0 ou se é maior que 10
                print('A nota deve de 0 a 10') #isso manda um aviso para o usuario que alerta ele sobre a nota que deve ser digitada
                continue #isso reinicia o codigo da onde está, para caso a pessoa digite um valor que seja menor que 0 ou maior que 10, fazendo ela digitar novamente um valor correto
        else:
            break #ele para o loop e avança para o priximo bloco quando o while é true

    while True:
        semestre2 = float(input('Digite a nota do 2° semestre: '))
        if semestre2 < 0 or semestre2 > 10:
            print('A nota deve de 0 a 10')
            continue
        else:
            break

    while True:
        semestre3 = float(input('Digite a nota do 3° semestre: '))
        if semestre3 < 0 or semestre3 > 10:
            print('A nota deve de 0 a 10')
            continue
        else:
            break
        
    nota_final =  (semestre1 + semestre2 + semestre3) / 3 #nessa parte ele soma os 3 valores e depois divide por 3
    print(f'Media do Aluno: {nota_final:.2f}') #aqui ele fala o resultado do calculo do codigo acima
    if nota_final >= 7: #caso o resultado seja 7 ou acima, ele passara de ano
        print('Você passou')
    elif nota_final >= 5: #caso o resultado seja 5 ou abaixo de 7, ele estará de recuperação
        print('Você está de recuperação')
    else: #e se caso nenhuma das duas condições acima sejam atendidas significa que o aluno reprovou pois sua nota foi menos que 5
        print('Você reprovou')
    
    while True:
        continuar = input('Continuar com o proximo aluno? (S/N): ') #ele verifica se o usuario quer ou não continuar a avaliação
        if continuar == 'n' or continuar == 'N': #essa parte verifica se o n / N é maiusculo ou minusculo por conta da preferencia do usuario
            print('Ok, acabamos por aqui!')
            avaliacao = False #ele torna a avaliação Falsa o que encerra o loop do While princial e do while True
            break
        elif continuar == 's' or continuar == 'S':
            print('Ok, proximo aluno!')
            break
        else:
            print('Apenas S ou N')
            continue