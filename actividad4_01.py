

def calculo(expo):
    res = 1 + expo       
    for i in range(2,51):
        # exponencial
        numerador =expo
        for j in range(1,i):
            numerador = expo*numerador  
        # factorial
            if i==0 or i==1:
                denomidador=1
            else:
                denomidador = 1
                for j in range(1,i+1):
                    denomidador = j*denomidador
        #resultado
        res = res + (numerador/denomidador)
    print(f"el resultado de epsilo elevado a {expo} es igual a {res}")



def epsilon():
    exp = int(input("Digite exponente de a funcion epsilon ==> 3"))
    
    calculo(exp)



def main():
  epsilon()


if __name__ =="__main__":
    main() 