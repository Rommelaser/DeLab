
########################################### Imports ########################################################
import pprint
import json
from urllib import response
import requests
import csv
import os
from pprint import pp

########################################## Urls #############################################################

urlo = "https://api.meraki.com/api/v1/organizations"
urld="https://api.meraki.com/api/v1/organizations/organizationId/devices"
urlds = "https://api.meraki.com/api/v0/organizations/organizationId/deviceStatuses"

########################################## Headers/Payload ###################################################

payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}


######################################### functions ###########################################################


def org_Data(): #Consulta la data de las organizaciones a las que tenemos 
    response = requests.request('GET', urlo, headers=headers, data = payload)
    orgData = json.loads(response.text)
    if(response.raise_for_status()==None):
        print("se ha consultado exitosamente las organizaciones a las que puede acceder con su API_kEY \\ el resultado de la consulta se encuentra en la variable: orgData\n")
    return orgData

def org_Dev(oId): #Consulta los dispositivos de DeLab
    aux_url="https://api.meraki.com/api/v1/organizations/organizationId/devices".replace('organizationId', oId)
    #print(aux_url) #Debug print
    response= requests.request('GET', aux_url, headers=headers, data = payload)
    if(response.raise_for_status()==None):
        print("se ha consultado exitosamente Los Dispositivos asociados al organization id N: ", oId,  " \\ el resultado de la consulta se encuentra en la variable: orgDev\n")
    orgDev= json.loads(response.text)
    
    return orgDev

def  o_id(): #busca el organization Id asociado al nombre de organización que se le pasa
    oName=input("introduce el nombre de la organización de la cual quieres consultar sus dispositivos: ")
    #print(oName)   #Debug print
    DeLab=[]
    for i in range(len(orgData)):
        if(orgData[i]['name']==oName):    	    
            DeLab.append(orgData[i])
        DeLab.append(0)
    return DeLab[0]['id']

def printallOrg(): #lista todas las organizaciones
    pp(orgData)

def printOrg(i): #imprime una organización en específico
    pp(orgData[i])

def printallOrgDev(): #imprime todos los dispositivos de la organización DeLab
    pp(orgDev)

def printOrgDev(i):   #imprime un dispositivo en específico de la organización DeLab
    pp(orgDev[i])

def productType(): #retorna una lista de dicionario con los datos de los dispositivos tipo: Wireless y appliance
    pt=[]
    for i in range(len(orgDev)):
        if(orgDev[i]["productType"]== "appliance"):
            pt.append(orgDev[i])
        if(orgDev[i]["productType"]== "wireless"):
            pt.append(orgDev[i])
    return pt

def prodevS():
    ps=[]
    for i in range(len(devStatus)):
        if(devStatus[i]["status"] =='online'):
            ps.append(devStatus[i])
        if(devStatus[i]["status"] =='online'):
            ps.append(devStatus[i])
    return ps

def formpt(p,s):
    for i in range(len(p)):
        pcopy = p[i].copy()
        p[i].clear()

        if pcopy["productType"]=="wireless":
            p[i]["productType"] = pcopy["productType"]
            p[i]["model"] = pcopy["model"]
            p[i]["name"] = pcopy["name"]
            p[i]["mac"] = pcopy["mac"]
            for k in range (len(s)):
                if p[i]["mac"] == s[k]["mac"]:
                    p[i]["publicIp"] = s[k]["publicIp"]
            p[i]["lanIp"] = pcopy["lanIp"]
            p[i]["serial"] = pcopy["serial"]
            for j in range(len(s)):
                if p[i]['serial']==s[j]['serial']:
                    p[i]["status"]=s[j]['status']
        else:
            p[i]["productType"] = pcopy["productType"]
            p[i]["model"] = pcopy["model"]
            p[i]["name"] = pcopy["name"]
            p[i]["mac"] = pcopy["mac"]
            for k in range (len(s)):
                if p[i]["mac"] == s[k]["mac"]:
                    p[i]["publicIp"] = s[k]["publicIp"]
            p[i]["wan1Ip"] = pcopy["wan1Ip"]
            p[i]["serial"] = pcopy["serial"]
            for j in range (len(s)):
                if p[i]["serial"] == s[j]["serial"]:
                    p[i]["status"] = s[j]["status"]
        
def jsontocsv(p): #genera un archivo con extensión .csv con el inventario de los dispositivos Wireless y Appliance
    blank=[]
    header=p[0].keys()
    with open('inventory.csv',mode='w') as inventory:
        inventory_writer= csv.writer(inventory,delimiter=',')
        inventory_writer.writerow(header)
        for i in range(len(p)):
            if(p[0]['productType']==p[i]['productType']):
                inventory_writer.writerow(p[i].values())
        i=0
        while(p[0]['productType']==p[i]['productType']):
            i=1+i
        header=p[i].keys()
        inventory_writer.writerow(blank)
        inventory_writer.writerow(header)
        for i in range(len(p)):
            if(p[0]['productType']!=p[i]['productType']):
                inventory_writer.writerow(p[i].values())


def deviceStatuses(oId): # realiza una consulta para ver el Status de los dispositivos asociados al oId
    aux_url="https://api.meraki.com/api/v0/organizations/organizationId/deviceStatuses".replace('organizationId', oId)
    #print(aux_url) #Debug print
    response= requests.request('GET', aux_url, headers=headers, data = payload)
    deviceS= json.loads(response.text)
    if(response.raise_for_status()==None):
        print("se ha consultado exitosamente el estado dispositivos asociados al organization id N: ", oId,  " \\ el resultado de la consulta se encuentra en la variable: devStatus\n")
    return deviceS







########################################## Default requests ##################################################
orgData=org_Data()
oId=o_id()
orgDev= org_Dev(oId)
devStatus= deviceStatuses(oId)

######################################### Default Data #######################################################

print("¿Desea generar el inventario para los dispositivos wireless y appliance?")
if(input("y or n : \n")=='y'):
    orgDev=productType()
    formpt(orgDev,devStatus)
    jsontocsv(orgDev)
    print("¿Desea imprimir en la terminal la información asociada al inventario?")
    if(input("y or n : \n")=='y'):
        pp(orgDev)






            









