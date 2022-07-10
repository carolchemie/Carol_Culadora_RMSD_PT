class bcolors:
    red = '\033[91m'
    green = '\033[92m'
    bold = '\033[1m'
    reset = '\033[0m'

print(' ')
print(
    f'{bcolors.bold}CAROLCULADORA (RMSD_1) -  CALCULO DE RMSD PARA COMPARAÇÃO DE DUAS MÓLECULAS COM QUATRO ÁTOMOS {bcolors.reset}')
print(" ")
print(f'{bcolors.bold}***INSIRA OS PARAMETROS SOLICITADOS DAS ESTRUTURAS A SEREM ANALISADAS*** {bcolors.reset}')
atms1 = str(input('Qual o átomo 1 das estruturas analisadas ? ')).upper()
atms2 = str(input('Qual o átomo 2 das estruturas analisadas ? ')).upper()
atms3 = str(input('Qual o átomo 3 da estruturas analisadas ? ')).upper()
atms4 = str(input('Qual o átomo 4 da estruturas analisadas ? ')).upper()
print(' ')
print(f'{bcolors.green}INSIRA AS COORDENADAS DA ESTRUTURA 1 {bcolors.reset}')
print('Coordenadas x, y, e, z do átomo', atms1)
x11 = float(input('Insira o valor da coordenada x: '))
y11 = float(input('Insira o valor da coordenada y: '))
z11 = float(input('Insira o valor da coordenada z: '))

print(' ')

print('Coordenadas x, y e z do átomo', atms2)
x12 = float(input('Insira o valor da coordenada x: '))
y12 = float(input('Insira o valor da coordenada y: '))
z12 = float(input('Insira o valor da coordenada z: '))

print(' ')

print('Coordenadas x, y e z do átomo', atms3)
x13 = float(input('Insira o valor da coordenada x: '))
y13 = float(input('Insira o valor da coordenada y: '))
z13 = float(input('Insira o valor da coordenada z: '))

print(' ')

print('Coordenadas x, y e z do átomo', atms4)
x14 = float(input('Insira o valor da coordenada x: '))
y14 = float(input('Insira o valor da coordenada y: '))
z14 = float(input('Insira o valor da coordenada z: '))

print(' ')

print(f'{bcolors.green}INSIRA AS COORDENADAS DA ESTRUTURA 2 {bcolors.reset}')
print('Coordenadas x, y e z do átomo', atms1)
x21 = float(input('Insira o valor da coordenada x da segunda estrutura: '))
y21 = float(input('Insira o valor da coordenada y da segunda estrutura: '))
z21 = float(input('Insira o valor da coordenada z da segunda estrutura: '))

print(' ')
print('Coordenadas x, y e z do átomo', atms2)
x22 = float(input('Insira o valor da coordenada x da segunda estrutura: '))
y22 = float(input('Insira o valor da coordenada y da segunda estrutura: '))
z22 = float(input('Insira o valor da coordenada z da segunda estrutura: '))

print(' ')

print('Coordenadas x, y e z do átomo', atms3)
x23 = float(input('Insira o valor da coordenada x da segunda estrutura: '))
y23 = float(input('Insira o valor da coordenada y da segunda estrutura: '))
z23 = float(input('Insira o valor da coordenada z da segunda estrutura: '))

print(' ')

print('Coordenadas x, y e z do átomo', atms4)
x24 = float(input('Insira o valor da coordenada x da segunda estrutura: '))
y24 = float(input('Insira o valor da coordenada y da segunda estrutura: '))
z24 = float(input('Insira o valor da coordenada z da segunda estrutura: '))

def sub_quadrado(param1, param2):
    subtracao = param1 - param2
    return subtracao ** 2


valor_atm1ab = sub_quadrado(x11, x21) + sub_quadrado(y11, y21) + sub_quadrado(z11, z21)
valor_atm2ab = sub_quadrado(x12, x22) + sub_quadrado(y12, y22) + sub_quadrado(z21, z22)
valor_atm3ab = sub_quadrado(x13, x23) + sub_quadrado(y13, y23) + sub_quadrado(z13, z23)
valor_atm4ab = sub_quadrado(x14, x24) + sub_quadrado(y14, y24) + sub_quadrado(z14, z24)

divisao = (valor_atm1ab + valor_atm2ab + valor_atm3ab + valor_atm4ab) / 4

raiz = divisao ** 0.5
print(' ')
print('O valor de RMSD calculado é de:',float(round(raiz)))
print(' ')
print('Created by @carol.chemie, on 07/2022')