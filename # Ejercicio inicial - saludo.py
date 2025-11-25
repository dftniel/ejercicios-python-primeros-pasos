# Ejercicio inicial - saludo
# palabra_clave + nombre_funcion(verbo) + parametros(adjetivos)

# ZONA DE FUNCIONES.
def capturar_nombre():
    nombre_usuario = input("Escriba el nombre del cliente: ")
    return nombre_usuario

def capturar_rol():
    rol_usuario = input("Escriba su rol: ")
    return rol_usuario

def capturar_hora():
    hora_usuario = int(input("Digite la hora actual en formato militar (0-23): "))
    return hora_usuario

def obtener_saludo(hora_usuario):
    if hora_usuario <= 12:
        return ("Buenos días")
    elif hora_usuario <= 18:
        return ("Buenas tardes")
    else: 
        return ("Buenas noches")


def hacer_saludo(nombre_usuario, rol_usuario, hora_usuario):
    saludo_tiempo = obtener_saludo(hora_usuario)
    saludo = f"{saludo_tiempo}, {nombre_usuario}, tu rol es: {rol_usuario}. Bienvenido!"
    print(saludo)

# CÓDIGO PRINCIPAL

nombre = capturar_nombre() # Esta función está hecha para capturar el nombre del cliente; más específicamente, capturar datos.

rol = capturar_rol() # Esta función está hecha para capturar el rol del cliente; lo especifico como capturar rol.

hora = capturar_hora() # Esta función está hecha para capturar la hora actual del cliente. 

hacer_saludo(nombre,rol,hora) # Esta función está hecha para procesar el saludo.

print # Esta función la uso para imprimir el saludo. 

