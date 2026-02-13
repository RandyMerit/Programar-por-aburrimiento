def primo():
    print("PRIMO O COMPUESTO")
    z="S"
    while(z=="S"):
        n=input("Ingrese un Número Entero\n")
        #Verificar si el dato de entrada es un número entero
        try:
            n=int(n)
        except ValueError,TypeError:
            print("¡ERROR!,",n,"NO ES un Número Entero")
        else:
            #Si el número es negativo o es 0
            if n>=0:
                inicio = 1
                fin = n+1
                paso = 1
            #Si el número es positivo
            else:
                inicio = -1
                fin = n-1
                paso = -1
            cont = 0 #Contador de divisores de N
            #Contar los divisores de N
            for i in range(inicio,fin,paso):
                if n%i==0:
                    cont+= 1
            if cont==0:
                #Esta condición aplica para el 0
                res = "Neutro"
            if cont==1:
                #Esta condición aplica para el 1
                res = "Unidad"
            if cont==2:
                #Los números primos tienen 2 divisores, ni más ni menos
                res = "Primo"
            if cont>2:
                res = "Compuesto"
            print(n,"es un número",res)
            print("¿Quiere probar otro número? (S/N)")
            z=""
            while(z!="S") and(z!="N"):
                z=input()
                z=z.upper()
primo()