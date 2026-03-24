def main():
    #Funciones y Procedimientos
    def no_es_número(entrada):
        print("¡ERROR!:",entrada,"no es un número")
    #Encabezado
    print("TABLAS DE MULTIPLICAR")
    print("Elaborado por: Randy Merit")
    #Programa Principal
    respuesta = "S"
    while respuesta=="S":
        n = ""
        #Entrada de Datos
        while type(n)!=int and type(n)!=float:
            n = input("Ingresa un número: ")
            #Validación de Número
            punto = False
            for caracter in n:
                if caracter==".":
                    punto = True
            if punto==True:
                try:
                    n = float(n)
                except ValueError:
                    no_es_número(n)
            if punto==False:
                try:
                    n = int(n)
                except ValueError:
                    no_es_número(n)
        #Salida de Datos
        print("TABLA DE MULTIPLICAR DEL "+str(n)+":")
        for i in range(1,11):
            print(n,"x",i,"=",n*i)
        #Decición del Usuario para Continuar
        print("¿Quiere ver la tabla de multiplicar de otro número? (S/N)")
        respuesta = ""
        while respuesta!="S" and respuesta !="N":
            respuesta = input()
            respuesta = respuesta.upper()
main()