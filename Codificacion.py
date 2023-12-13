##Bienvenida##
print ("Bienvenido a el software de generador seguro de Contraseña")

##Importo la liberia para encriptar##
from cryptography.fernet import Fernet
##Importo la liberia para generar numeros, letras, signos al azar##
import random
##Importo la libreria para ingresar a diferenctes caracteres##
import string

##función principal que coordina todo el proceso##
def generar_contrasena():
    
    ##Solicita al usuario la longitud deseada para la contraseña#
    longitud = validar_longitud()
    
    ##Solicita si quiere incluir mayúsculas, minúsculas, números y símbolos##
    incluir_mayusculas = ingresar("¿Incluir mayúsculas? (Sí = 1, No = 0): ")
    incluir_minusculas = ingresar("¿Incluir minúsculas? (Sí = 1, No = 0): ")
    incluir_numeros = ingresar("¿Incluir números? (Sí = 1, No = 0): ")
    incluir_simbolos = ingresar("¿Incluir símbolos? (Sí = 1, No = 0): ")
   
    ##Aqui toman las preferencias Ingresadas por el usuario##
    contrasena = contrasena_aleatoria(longitud, incluir_mayusculas, incluir_minusculas, incluir_numeros, incluir_simbolos)
    print(f"Contraseña generada: {contrasena}")


 ##Encriptar la contraseña generada##
    clave_encriptacion = Fernet.generate_key()
    contrasena_encriptada = encriptar_contrasena(contrasena, clave_encriptacion)
    print(f"Contraseña encriptada: {contrasena_encriptada}")

def encriptar_contrasena(contrasena, clave):
    cipher_suite = Fernet(clave)
    contrasena_encriptada = cipher_suite.encrypt(contrasena.encode())

    original = cipher_suite.decrypt(contrasena_encriptada).decode()
    print(f"Clave de encriptacion: {clave}")
    print(f"Contrasena original desencriptada: {original}")

    return contrasena_encriptada

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

##Genera la contraseña aleatorea utilizando la liberias string y random##
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
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena
##Se genera la contraseña solicitada##
generar_contrasena()