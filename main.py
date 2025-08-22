import funcoes


print('---CALCULADORA---')
number = int(input('Digite um número: '))
choiceOperation = input('Escolha a operação: (+) (-) (*) (/): ')


if choiceOperation == '+':
    funcoes.soma(number)
