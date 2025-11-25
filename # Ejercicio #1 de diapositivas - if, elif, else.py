#  Ejercicio #1 de diapositivas - if, elif, else.
             
# Realice un ejercicio en donde le solicite al usuario un número y el programa identifique si es positivo, negativo  o neutro.

# ZONA DE FUNCIONES.

def tomar_numero():
    numero = int(input("Escriba el número: "))
    return numero

def validar_numero(dato_numero):
    if dato_numero > 0:
        mensaje = "El número es positivo"
    elif dato_numero == 0:
        mensaje = "El número es neutro"
    else: 
        mensaje = "El número es negativo"
    return mensaje

def imprimir_dato(dato_mensaje):
    print("El número es: " + dato_mensaje)
           
# CÓDIGO PRINCIPAL

dato_numero = tomar_numero() # Esta función la usamos para capturar el número que el cliente ingrese.

dato_mensaje = validar_numero(dato_numero) # Con esta función procesamos los datos en el programa, en este caso el número

imprimir_dato(dato_mensaje) # Con esta función mostramos el resultado al cliente, si su número es positivo, neutro o negativo. 