

def soma(x):
    number2 = int(input('Digite outro número: '))
    result = x + number2
    while True:
        condition = input('Escolha a operação: (+) (-) (*) (/) (=):')
        if condition == '=':
            break
        elif condition == '+':
            print(result)
            number2 = int(input('Digite outro número: '))
            result = result + number2
        elif condition == '-':
            print(result)
            number2 = int(input('Digite outro número: '))
            result = result - number2
        elif condition == '*':
            print(result)
            number2 = int(input('Digite outro número: '))
            result = result * number2  
        elif condition == '/':
            print(result)
            number2 = int(input('Digite outro número: '))
            result = result / number2   
    print(result)

def subtracao(x):
    number2 = int(input('Digite outro número: '))
    result = x - number2
    while True:
        condition = input('Escolha a operação: (+) (-) (*) (/) (=):')
        if condition == '=':
            break
        elif condition == '-':
            print(result)
            number2 = int(input('Digite outro número: '))
            result = result - number2    
    print(result)

def multiplicacao(x):
    number2 = int(input('Digite outro número: '))
    result = x * number2
    while True:
        condition = input('Escolha a operação: (+) (-) (*) (/) (=):')
        if condition == '=':
            break
        elif condition == '*':
            print(result)
            number2 = int(input('Digite outro número: '))
            result = result * number2    
    print(result)

def divisao(x,y):
    x = int(input('Digite um número: '))
    y = int(input('Digite outro número: '))
    resultado = x / y
    return resultado