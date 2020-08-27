

def calculo(numero):
    res = 1 + numero
    for i in range(2,51):
        numerador = exponencial(numero,i)
        denominador = factorial(i)
        res = res + (numerador/denominador)
    return res


def exponencial(nume,exponente):
    resul = nume
    for i in range(1,exponente):
        resul = nume*resul    
    return resul


def factorial(num):
    if num==0 or num==1:
         resultado=1
    else:
        resultado = 1
        for i in range(1,num+1):
            resultado = i*resultado
    return resultado

def respuesta(r,e):
    print(f"El resultado de epsilon elevado a {e} es {r}")

def epsilon():
    exp = int(input("Digite exponente de a funcion epsilon ==>"))
    resultado=calculo(exp)
    respuesta(resultado,exp)    
    
def main():
  epsilon()


if __name__ =="__main__":
    main() 