##Bienvenida##
print ("Bienvenido a el sofware de Generacion seguro de Contraseña")

##Liberia para generar numeros, letras, signos al azar##
import random
##Libreria para ingresar a diferenctes caracteres##
import string

##Esta función es la principal que coordina todo el proceso.  y . Luego llama a 
def generar_contrasena():
    ##Pide al usuario la longitud deseada para la contraseña#
    longitud = validar_longitud()
    ##si quiere incluir mayúsculas, minúsculas, números y/o símbolos##
    incluir_mayusculas = ingresar("¿Incluir mayúsculas? (Sí = 1, No = 0): ")
    incluir_minusculas = ingresar("¿Incluir minúsculas? (Sí = 1, No = 0): ")
    incluir_numeros = ingresar("¿Incluir números? (Sí = 1, No = 0): ")
    incluir_simbolos = ingresar("¿Incluir símbolos? (Sí = 1, No = 0): ")
    ##Aqui toman las preferencias Ingresadas por el usuario, y toma las la liberia random y string##
    contrasena = contrasena_aleatoria(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    print(f"Contraseña generada: {contrasena}")

##Validacion de la longitud que sea de minimo 8 y maximo 20##
def validar_longitud():
    while True:
        try:
            longitud = int(input("Ingrese la longitud de la contraseña (entre 8 y 20 caracteres): "))
            if 8 <= longitud <= 20:
                return longitud
            else:
                print("La longitud ingresada no es válida.")
        except ValueError:
            print("Por favor, ingrese un número válido.")
##Mensaje al solicitar la preferencia de la contraseña##
def ingresar(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada in ('0', '1'):
            return entrada == '1'
        else:
            print("Por favor, ingrese 1 para Sí o 0 para No.")
##Donde se genera la contraseña aleatorea utilizando la liberias string y random##
def contrasena_aleatoria(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos):
    caracteres = ''
    if incluir_mayusculas:
        caracteres += string.ascii_uppercase
    if incluir_minusculas:
        caracteres += string.ascii_lowercase
    if incluir_numeros:
        caracteres += string.digits
    if incluir_simbolos:
        caracteres += string.punctuation
    #Se genera la contraseña de acuerdo a lo solicitado
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
##Fin Generar contraseña##
generar_contrasena()