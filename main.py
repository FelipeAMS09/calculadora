import funcoes

print('---CALCULADORA---')

try:
    choice = int(input('Escolha uma das opções:\n1-Soma\n2-Subtração\n3-Multiplicação\n4-Divisão\nEscolha: '))

    if choice == 1:
        funcoes.soma(int(input('Digite um número')))

except ValueError:
    print('Valor inválido')
    
