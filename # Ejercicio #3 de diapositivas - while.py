# Ejercicio #3 de diapositivas - while.

# Realizar un programa que la variable sea diferente a cero esté pidiendo un valor por consola e indicar si el número digitado  es par o impar

# ZONA DE FUNCIONES. 

def tomar_numero():
    num = 1
    num = int(input())
    return num

def procesar_numero(num):
        if num % 2 == 0:
            print ("El número es par\n")
            return True
        else:
            print("El número es impar\n")
            return True

def imprimir_resultado():
    print("El programa finalizó.\n")


# CÓDIGO PRINCIPAL.

num = 1

while num != 0:
        print("Digite un número: ")
        num = tomar_numero() # La uso para solicitarle al usuario el número que hará que el programa funcione.
        if num != 0:
             procesar_numero(num) # Es la variable que uso para poder procesar.

imprimir_resultado() # Con esto le muestro el resultado al cliente, dependiendo de si el número par o impar.