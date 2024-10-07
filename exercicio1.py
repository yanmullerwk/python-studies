#crie um programa que recebe dois inteiros A e B pelo teclado
#e imprime o valor de de A dividido Por B. Entretando, se o 
# valor de B for 0, imprima uma mensagem de erro e não faça a divisão


A = float(input("digite um numero para ser o dividendo: "))
B = float(input("digite um numero para ser o divisor: "))

if B!=0:
    print("o seu divisor é", B,"e seu dividendo é", A, ",o resultado é", A/B)
else:
    print("Erro")