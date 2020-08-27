

def consultar(nume):
    acum = 0
    for i in range (1, nume):
        if nume % i == 0:
            acum = acum + i
    if acum == nume:
        print(f"El numero {nume} es perfecto")
    else:
        print(f"El numero {nume} no es perfecto")


def leerNumero():
    numero = int(input("Digite el numero que dese saber si es perfecto o no ==> "))
    consultar(numero)


def main():
  leerNumero()


if __name__ =="__main__":
    main() 