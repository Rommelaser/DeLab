# DeLab
Universidad Simón Bolívar

Estudiante: Rommel Contreras

Carnet: 14-10242

Profesora: Emma Di Battista


Tarea de SDN

# Nueva actualización

Se realizó un contador para que se actualizara el archivo de inventario cada 5 minutos, esto inhabilita la entrada del usuario ya que no se esta trabajando con hilos.

######################################################################################################################################

El programa por defecto hace una consulta de las organizaciones a las que tenemos acceso con la clave el API_KEY entregado y guarda la respuesta en la variable orgData

Se le agregó una nueva feature para tambien consultar los dispositivos asociados a DebLAb

y generar un archivo csv con el inventario de dispositivos wireless y appliance

org_Data(): #Consulta la data de las organizaciones a las que tenemos acceso. Se le agregó el método raise_for_status() de python para validar que las solicitudes están recibiendo la respuesta esperada. Retorna una lista con las organizaciones.

Si todo está ok imprime un mensaje indicando donde se guarda la consulta y que todo esta bien

org_Dev(oId): #Consulta los dispositivos de DeLab
(Se le agregó el método raise_for_status() de python para validar que las solicitudes están recibiendo la respuesta esperada.t )
Ahora la función requiere el Id a la cual se le quiere consultar los dispositivos que contiene, retorna una lista con los dispositivos.

Si todo está ok imprime un mensaje indicando donde se guarda la consulta y que todo esta bien

def printallOrg(): #lista todas las organizaciones

def printOrg(i): #imprime una organización en específico

def  o_id(oName): #busca el organization Id asociado al nombre de organización que se le pasa retorna un string con el id de la organización.

printallOrg(): #lista todas las organizaciones

printOrg(i): #imprime una organización en específico

printallOrgDev(): #imprime todos los dispositivos de la organización DeLab

printOrgDev(i):   #imprime un dispositivo en específico de la organización DeLab

productType(): #retorna una lista de dicionario con los datos de los dispositivos tipo: Wireless y appliance

formpt(p,s): Formatea el p con los campos necesarios para generar el inventario, requiere p lista de diccionarios con la información asociada a produtos wireles y appliance y s lista de dicionarios con la información de los status de los dispositivos de la organización.

jsontocsv(p): #genera un archivo con extensión .csv con el inventario de los dispositivos Wireless y Appliance



