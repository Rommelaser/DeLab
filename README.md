# DeLab
Universidad Simón Bolívar

Estudiante: Rommel Contreras
Carnet: 14-10242
Profesora: Emma Di Battista


Tarea de SDN


El programa por defecto hace una consulta de las organizaciones a las que tenemos acceso con la clave el API_KEY entregado y guarda la respuesta en la variable orgData

Se le agregó una nueva feature para tambien consultar los dispositivos asociados a DebLAb

y generar un archivo csv con el inventario de dispositivos wireless y appliance

org_Data(): #Consulta la data de las organizaciones a las que tenemos Se le agregó el método raise_for_status() de python para validar que las solicitudes están recibiendo la respuesta esperada.

org_Dev(): #Consulta los dispositivos de DeLab
(Se le agregó el método raise_for_status() de python para validar que las solicitudes están recibiendo la respuesta esperada.t )

def printallOrg(): #lista todas las organizaciones

def printOrg(i): #imprime una organización en específico

oid_DeLab(): #busca el organization Id de DeLab

printallOrg(): #lista todas las organizaciones

printOrg(i): #imprime una organización en específico

printallOrgDev(): #imprime todos los dispositivos de la organización DeLab

printOrgDev(i):   #imprime un dispositivo en específico de la organización DeLab

productType(): #retorna una lista de dicionario con los datos de los dispositivos tipo: Wireless y appliance

formpt(p):

jsontocsv(p): #genera un archivo con extensión .csv con el inventario de los dispositivos Wireless y Appliance

printcsvdata(): #imprime en el terminal la data del inventario en formato .json

