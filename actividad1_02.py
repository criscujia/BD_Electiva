

def consulta(num):
    if num % 2 == 0:
        print(f"el numero {num} es Par")
    else:
        print(f"el numero {num} es Impar")



def leerNumero():
    numero=int(input("Digite el numero a consultar: "))
    consulta(numero)

def main():
  leerNumero()


if __name__ =="__main__":
    main()   