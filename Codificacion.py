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
    incluir_mayusculas = ingresar("¿Incluir mayúsculas? (Sí = 1, No = 0): ")    #llamdo a la funcion Ingresar para preguntar al usuario
    incluir_minusculas = ingresar("¿Incluir minúsculas? (Sí = 1, No = 0): ")    #llamdo a la funcion Ingresar para preguntar al usuario
    incluir_numeros = ingresar("¿Incluir números? (Sí = 1, No = 0): ")          #llamdo a la funcion Ingresar para preguntar al usuario
    incluir_simbolos = ingresar("¿Incluir símbolos? (Sí = 1, No = 0): ")        #llamdo a la funcion Ingresar para preguntar al usuario
   
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
def validar_longitud():                                                 #Funcion que se encarga de obtener y validar la longitud 
    while True:                                                         #El bucle while True garantiza que la función siga ejecutándose hasta que se cumpla la condición para salir del bucle.
        try:                                                            #Se incia el bloque Try para manejar posibles errores   
            longitud = int(input("Ingrese la longitud de la contraseña (entre 8 y 20 caracteres): "))   #Input para pedir al usuario que ingrese la longitud
            if 8 <= longitud <= 20:                                     #Verificar si es longitud esta dentro del rando
                return longitud                                         #Si es valido retorna la longitud valida indicada  
            else:                                                       #Si no es valido el valor indicado
                print("La longitud ingresada no es válida.")            #Imprime el mensaje
        except ValueError:                                              #El bloque Except maneja esta excepcion 
            print("Por favor, ingrese un número válido.")               #Imprime que ingrese un numero valido

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
    caracteres = ''                                                     #Crea una cadena vacía caracteres 
    if incluir_mayusculas:                                              #Si incluir_mayusculas es verdadero
        caracteres += string.ascii_uppercase                            #Agrega todas las letras mayúsculas de la libreria string.ascii_uppercase
    if incluir_minusculas:                                              #Si incluir_minusculas es verdadero
        caracteres += string.ascii_lowercase                            #Agregar todas las letras minusculade la liberia string.ascii_lowercase
    if incluir_numeros:                                                 #Si incluir_numeros es verdadero
        caracteres += string.digits                                     #Agregar todas los numero de la liberia string.digits
    if incluir_simbolos:                                                #Si incluir_simbolos es verdadero
        caracteres += string.punctuation                                #Agrega todos los símbolos de puntuación (string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))    #Utiliza una comprensión de lista y random.choice adicioanl genera una comtraseña aleatoria deacuerdo a la longitud solicitada 
    return contrasena                                                   #Retorna una contraseña generada 
##Se genera la contraseña solicitada##
generar_contrasena()