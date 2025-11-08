import random


numero =  random.randint(1,6)
match numero:
    case 1:
        print('😁')
    case 2:
        print('😈')
    case 3:
        print('🤡')
    case 4:
        print('😎')   
    case 5:
        print('🎃')   
    case 6:
        print('🤑') 




n  =  int(input('Digite um numero: '))


match n:
    case 0:
        print('Zero')
    case n if n > 0:
        print('positivo')
    case n if n < 0:
        print('Negativo')
    case _:
        print('Desconhecido')      


match idade:
    case idade if idade >= 65:
        print('idoso')
    case idade if idade >= 35 and idade <=64:
        print('Adulto')   
    case idade if idade >= 18 and idade <=34:
        print('jovem')  
    case idade if idade >= 14 and idade <=17:
        print('Adolescente')                   
    case _:
        print('Criança')