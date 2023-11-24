a= "Bienvenido a ´Generacion de Contraseña´"
print (a)

import random
import string

def generar_contrasena():
    longitud = input("Ingresar la longitud requerida: ")
    incluir_mayusculas = ingreso("¿Incluir mayúsculas? (Sí = 1, No = 0): ")
    incluir_minusculas = ingreso("¿Incluir minúsculas? (Sí = 1, No = 0): ")
   

    contrasena = "Prueba"
    print(f"Contraseña generada: {contrasena}")

1
def ingreso(mensaje):
    while True:
        entrada = input(mensaje)
        if entrada in ('0', '1'):
            return entrada == '1'
        else:
            print("Por favor, ingrese 1 para Sí o 0 para No.")


generar_contrasena()
