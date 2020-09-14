import time


def linha():
    print('=='*20)


def criptografa_msg():  # criptografar menssagem  [1]

    linha()
    mensagem = input('digite sua mensagem: ')
    rotacao = input('Digite o número da rotação: ')

    if mensagem == '':
        print('\033[1;91m___________ERRO__________\n'
              'você não pode deixar campos em branco\n\033[m')

    elif rotacao == '' or not rotacao.isnumeric():
        print('\033[1;91m___________ERRO__________\n'
              'você não pode deixar campos em branco\n'
              'e a rotção deve ser um número\033[m')

    else:
        msg_cifrada = ''

        for letra in mensagem:
            if letra not in alfabeto:  # se um elemento da mensagem não estiver no alfabeto ele só repete
                msg_cifrada += letra
            else:  # cifrando a mensagem

                posicao = alfabeto.index(letra)
                msg_cifrada += alfabeto[(posicao + int(rotacao)) % len(alfabeto)]
        print('cifrando mensagem...')
        time.sleep(1)
        print(f'\033[33m{msg_cifrada}\033[m')


def decifra_msg():  # decifra mensagem criptografada [2]

    linha()
    mensagem = str(input('Digite a mensagem cifrada: '))
    rotacao = input('Digite a rotação do alfabeto: ')
    if mensagem == '':
        print('\033[1;91m___________ERRO__________\n'
              'você não pode deixar campos em branco\033[m')

    elif rotacao == '' or not rotacao.isnumeric():
        print('\033[1;91m___________ERRO__________\n'
              'você não pode deixar campos em branco\n'
              'e a rotção deve ser um número\033[m')

    else:
        mgs_descifrada = ''
        for letra in mensagem:
            if letra not in alfabeto:  # se um elemento não estiver no alfabeto ele só repete
                mgs_descifrada += letra
            else:  # decifrando a mensagem
                posicao = alfabeto.index(letra)
                mgs_descifrada += alfabeto[(posicao - int(rotacao)) % len(alfabeto)]
        print('decifrando mensagem...')
        time.sleep(1)
        print(f'\033[33m{mgs_descifrada}\033[m')


def ataque_forcabruta():  # ataque de força bruta para descifrar a mensagem criptografada [3]

    linha()
    mensagem = input('Digite a mensagem cifrada: ')
    if mensagem == '':
        print('\033[1;91m___________ERRO__________\n'
              'você não pode deixar campos em branco\n'
              'a mensagem deve ser uma palavra ou frase\n\033[m')

    else:
        print('aqui estão listados os posseveis resultados e sua respectiva rotação:')
        rotacao = 0
        mgs_descifrada = ''
        while rotacao < 27:
            for letra in mensagem:
                if letra not in alfabeto:  # se um elemento não estiver no alfabeto ele só repete
                    mgs_descifrada += letra
                else:
                    posicao = alfabeto.index(letra)
                    mgs_descifrada += alfabeto[posicao - rotacao]

            print(f'{mgs_descifrada}, {rotacao}')
            mgs_descifrada = ''
            rotacao += 1


alfabeto = 'abcdefghijklmnopqrstuvwxyz'
while True:

    linha()
    time.sleep(0.3)
    # menu de opções
    print('[1] crifrar\n'  
          '[2] decifrar\n'
          '[3] atque de força bruta\n'
          '[4] sair do programa')
    opcao = input('o que voce deseja fazer agora?  ')

    if opcao == '1':  # cifra mensagem
        criptografa_msg()

    elif opcao == '2':  # decifra mensagem
        decifra_msg()

    elif opcao == '3':  # ataque de força bruta para decifrar a mensagem
        ataque_forcabruta()

    elif opcao == '4':  # sair
        break

    else:  # opção invalida
        print('opção invalida!')
        continue

print('programa encerrado')
