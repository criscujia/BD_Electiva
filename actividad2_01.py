
def primo(num):
    if num < 1:
        print(f"El numero {num} no es primo")
        return None
    else:
        if num == 2:
            print(f"El numero {num} es primo")
            return None
        else:
            for i in range(2, num):
                if num % i == 0:
                    print(f"El numero {num} no es primo")
                    return None
            print(f"El numero {num} es primo")            


def leerNumero():
    numer = int(input("Escribe un numero ==> "))
    primo(numer)


def main():
  leerNumero()


if __name__ =="__main__":
    main() 