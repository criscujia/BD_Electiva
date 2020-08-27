

def numParImp(numero):
    p = "Par"
    i = "Impar"
    if numero % 2 == 0:
        return p
    else:
        return i

def respuesta(nume,resul):
    print(f"El numero: {nume}  es {resul}")

def leerNumero():
    nume = int(input("Digite el numero ==> "))
    resultado = numParImp(nume)
    respuesta(nume,resultado)
    
    
def main():
    leerNumero() 

if __name__ == "__main__":
    main()