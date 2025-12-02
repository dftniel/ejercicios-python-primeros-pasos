# Ejercicio #5 de diapositivas - switch, match. 

# Realizar un programa que por medio del número del mes, indique el nombre del mes que le corresponde al número.


# ZONA DE FUNCIONES.

def tomar_numero():
    return int(input("Digite un número del 1 al 12: "))

def procesar_resultado(num):
    match num:
        case 1:
            print ("El mes es Enero.")
        case 2: 
            print ("El mes es Febrero.")
        case 3: 
            print ("El mes es Marzo.")
        case 4: 
            print ("El mes es Abril.")
        case 5: 
            print ("El mes es Mayo.")
        case 6: 
            print ("El mes es Junio.")
        case 7:
            print ("El mes es Julio.")
        case 8:
            print ("El mes es Agosto.")
        case 9:
            print ("El mes es Septiembre.")
        case 10:
            print ("El mes es Octubre.")
        case 11:
            print ("El mes es Noviembre.")
        case 12: 
            print ("El mes es Diciembre.")

def imprimir_resultado():
    print("El programa finalizó.")
# CÓDIGO PRINCIPAL 

num = tomar_numero() # La uso para solicitarle al usuario que ingrese el número del 1 al 12

procesar_resultado(num) # La uso para darle una respuesta de acuerdo a la respuesta del cliente

imprimir_resultado() # Lo uso para mostrarle al cliente que el programa finaliza



