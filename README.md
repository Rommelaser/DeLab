# DeLab
Universidad Simón Bolívar

Estudiante: Rommel Contreras

Carnet: 14-10242

Profesora: Emma Di Battista


Tarea de SDN


El programa por defecto hace una consulta de las organizaciones a las que tenemos acceso con la clave el API_KEY entregado y guarda la respuesta en la variable orgData

Se le agregó una nueva feature para tambien consultar los dispositivos asociados a DebLAb

y generar un archivo csv con el inventario de dispositivos wireless y appliance

org_Data(): #Consulta la data de las organizaciones a las que tenemos acceso. Se le agregó el método raise_for_status() de python para validar que las solicitudes están recibiendo la respuesta esperada. Retorna una lista con las organizaciones.

Si todo está ok imprime None

org_Dev(oName): #Consulta los dispositivos de DeLab
(Se le agregó el método raise_for_status() de python para validar que las solicitudes están recibiendo la respuesta esperada.t )
Ahora la función requiere el nombre de la organización a la cual se le quiere consultar los dispositivos que contiene, retorna una lista con los dispositivos.

si todo está Ok imprime None

def printallOrg(): #lista todas las organizaciones

def printOrg(i): #imprime una organización en específico

def  o_id(oName): #busca el organization Id asociado al nombre de organización que se le pasa retorna un string con el id de la organización.

printallOrg(): #lista todas las organizaciones

printOrg(i): #imprime una organización en específico

printallOrgDev(): #imprime todos los dispositivos de la organización DeLab

printOrgDev(i):   #imprime un dispositivo en específico de la organización DeLab

productType(): #retorna una lista de dicionario con los datos de los dispositivos tipo: Wireless y appliance

formpt(p):

jsontocsv(p): #genera un archivo con extensión .csv con el inventario de los dispositivos Wireless y Appliance

printcsvdata(): #imprime en el terminal la data del inventario en formato .json

