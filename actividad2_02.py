

def primo(num):
    s = "si"
    n = "no"
    if num < 1:
        return n
    else:
        if num == 2:
            return s
        else:
            for i in range(2, num):
                if num % i == 0:
                    return n
            return s            


def respuesta(num,res):
    print(f"El numero {num} {res} es primo")


def leerNumero():
    numer = int(input("Escribe un numero ==> "))
    resultado = primo(numer)
    respuesta(numer,resultado)


def main():
  leerNumero()


if __name__ =="__main__":
    main() 