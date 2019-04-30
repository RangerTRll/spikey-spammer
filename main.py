#!/usr/bin/python
#Spikey Spammer
#Developed by Jagreet Das Gupta
#Author : V0!D
#Copyright : V!$(3R4
#Version : 1.1

import getpass
from spammer import spam_mail

print '\nSCRIPT OUTPUT INFO : '
print '\'->\' antes de una salida indica que es un registro no detallado'
print '\'!>\' antes de una salida indica que es un registro detallado'
print '\'~>\' antes de que una salida indique que es un registro de errores'
print '\'?>\' antes de una salida indica que es una entrada'
print '\n--------------------------------------------------'

#My Publicity :) :)
print '\n-> Spikey Spammer v1.1'
print '-> Developed by Jagreet Das Gupta'
print '-> Copyright : V!$(3R4'
print '\n----------------------------------------------------'
mlserve = raw_input ('?> Proveedor de servicio ? (gmail/yahoo) : ')
reci = raw_input('?> Email del destinatario: ')
username = raw_input('?> Email del remitente : ')
password = getpass.getpass('?> Contraseña del remitente: ')
y = raw_input('?> ¿Quieres incluir un tema predefinido? ? (y/n)')
set_sub = 0
if y=='y':
	subject = raw_input('?> Tema: ') 
	set_sub = 1

message_body = raw_input('?> Mensaje: ')
files = []
y3 = raw_input('?> ¿Quieres adjuntar archivos? ? (y/n) ')
if y3=='y':
	no = input('?> Enter Number of Files to Attach ? ')
	for i in range(1,no+1):
		prompt = '?> Enter Filename#'+str(i)+' with path ? '
		files.append(raw_input(prompt))
number = input('?> Number of messages to send: ')
spam_mail(reci,username,password,message_body,mlserve,number,set_sub,files)
