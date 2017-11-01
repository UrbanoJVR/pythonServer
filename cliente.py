#!/usr/bin/python
# -*- coding: utf-8 -*-
 
# Ejemplo cliente - servidor en python
# Programa Cliente
# www.elfreneticoinformatico.com

import socket #utilidades de red y conexion

#declaramos las variables
ipServidor = "127.0.0.1" #es lo mismo que "localhost" o "0.0.0.0"
puertoServidor = 9797

#Configuramos los datos para conectarnos con el servidor
#socket.AF_INET para indicar que utilizaremos Ipv4
#socket.SOCK_STREAM para utilizar TCP/IP (no udp)
#Estos protocolos deben ser los mismos que en el servidor
cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
cliente.connect((ipServidor, puertoServidor))
print("Conectado con el servidor ---> %s:%s" %(ipServidor, puertoServidor))

while True:
    msg = raw_input("> ")
    cliente.send(msg)
    respuesta = cliente.recv(4096)
    print(respuesta)
    if respuesta == "exit":
        break;

print("------- CONEXIÓN CERRADA ---------")
cliente.close()
