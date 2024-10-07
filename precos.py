produto = float(input("digite um valor: "))

if produto<=0:
    print("preço invalido")
elif produto<=30:
    print("preço baixo")
elif produto<=50:
    print("preço medio")
else:
    print("preço alto")