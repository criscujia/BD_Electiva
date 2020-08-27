

def consultar(nume):
    acum = 0
    s = "si"
    n = "no"
    for i in range (1, nume):
        if nume % i == 0:
            acum = acum + i
    if acum == nume:
        return s
    else:
        return n

def respuesta(r):
    print(f"El numero Digitado {r} es perfecto")


def leerNumero():
    numero = int(input("Digite el numero que dese saber si es perfecto o no ==> "))
    resp = consultar(numero)
    respuesta(resp)


def main():
  leerNumero()


if __name__ =="__main__":
    main() 