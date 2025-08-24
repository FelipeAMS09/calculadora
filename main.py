

print('---CALCULADORA---')

while True:
    try:
        number = int(input('Digite um número: '))   
    except ValueError:
        print('Escolha um NÚMERO!!!')
        continue
    while True:
        try:
            choiceOperation = input('Escolha a operação: (+) (-) (*) (/): ')
            if choiceOperation not in '+-/*':
                print('Escolha um dos simbolos!!')
            else:
                break
        except ValueError:
            print('Escolha um dos Simbolos!!')
            continue
    break

while True:

    if choiceOperation == '+':
        try:
            number2 = int(input('Digite outro número: ')) 
        except ValueError:
            print('Escolha um NÚMERO!!')
            continue
        result = number + number2

    elif choiceOperation == '-':
        try:
            number2 = int(input('Digite outro número: '))
        except ValueError:
            print('Escolha um NÚMERO!!')
            continue
        result = number - number2

    elif choiceOperation == '*':
        try:
            number2 = int(input('Digite outro número: '))
        except ValueError:
            print('Escolha um NÚMERO!!')
            continue
        result = number * number2    

    elif choiceOperation == '/':
        try:
            number2 = int(input('Digite outro número: '))
        except ValueError:
            print('Escolha um NÚMERO!!')
            continue
        result = number / number2  

    while True:
        condition = input('Escolha a operação: (+) (-) (*) (/) (=):')
        if condition == '=':
            break
        elif condition == '+':
            print(result)
            while True:
                try:
                    number2 = int(input('Digite outro número: '))
                except ValueError:
                    print('Escolha um NÚMERO!!')
                    continue
                result = result + number2
                break

        elif condition == '-':
            print(result)
            while True:
                try:
                    number2 = int(input('Digite outro número: '))
                except ValueError:
                    print('Escolha um NÚMERO!!')
                    continue
                result = result - number2
                break

        elif condition == '*':
            print(result)
            while True:
                try:
                    number2 = int(input('Digite outro número: '))
                except ValueError:
                    print('Escolha um NÚMERO!!')
                    continue
                result = result * number2 
                break

        elif condition == '/':
            print(result)
            while True:
                try:
                    number2 = int(input('Digite outro número: '))
                except ValueError:
                    print('Escolha um NÚMERO!!')
                    continue
                result = result / number2
                break
    print(result)