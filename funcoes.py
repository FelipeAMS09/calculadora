def soma(*args):
    resultado = 0
    for i in args:
        resultado = resultado + i

    print(f'resultado é {resultado  }')
    return resultado

def subtracao(x,y):
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    resultado = x - y
    return resultado

def multiplicacao(x,y):
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    resultado = x * y
    return resultado

def divisao(x,y):
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    resultado = x / y
    return resultado