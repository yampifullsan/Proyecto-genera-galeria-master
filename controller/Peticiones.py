# coding=utf-8
import os
import shutil
import sys


class Peticiones:

    def __init__(self):
        pass

    @classmethod
    def pedir_numero(cls, mensaje, limite_izquierda, limite_derecha):
        
        while True:
            numero = raw_input(mensaje)
            try:
                numero = int(numero)
                if limite_izquierda <= numero <= limite_derecha:
                    return numero
                else:
                    print('Error... escribe numero valido')
            except ValueError:
                print('Error introduce un número válido')
            except Exception, e:
                print 'Error peticiones la clase es: ' + str(e.__class__)

    @classmethod
    def es_numero(cls, numero):
        
        try:
            num = int(numero)
            return num
        except Exception, e:
            print('No es un número: {0}'.format(e.message))
            return False

    @classmethod
    def limpiar_pantalla(cls):
        
        if os.name == "posix":
            os.system("clear")
        elif os.name == ("ce", "nt", "dos"):
            os.system("cls")

    @classmethod
    def copiar_archivos_responsive(cls, nombre_proyecto):
        
        try:
            a = sys.path
            archivos = str(a[0])+'/model/Skeleton'
            proyecto = str(a[0])+'/' + nombre_proyecto
            shutil.copytree(archivos, proyecto)
        except Exception, e:
            print('Error al copiar directorio: ' + str(e))

    @classmethod
    def log_twitter(cls, error):
       

        try:
            archivo_log = open('logs/twitter.error', 'a+')
            archivo_log.write(error + '\n')
            archivo_log.close()
        except IOError, e:
            print('Error al abrir archivo de log (Clase LogError): ' + str(e))

    @classmethod
    def log_instagram(cls, error):
        
        try:
            archivo_log = open('logs/instagram.error', 'a+')
            archivo_log.write(error + '\n')
            archivo_log.close()
        except IOError, e:
            print('Error al abrir archivo de log (Clase LogError): ' + str(e))

    @classmethod
    def log(cls, error):
        
        try:
            archivo_log = open('logs/log.error', 'a+')
            archivo_log.write(error + '\n')
            archivo_log.close()
        except IOError, e:
            print('Error al abrir archivo de log (Clase LogError): ' + str(e))
