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
urld="https://api.meraki.com/api/v1/organizations/681155/devices"

########################################## Headers/Payload ###################################################
payload = None
headers = {
    "Content-Type": "application/json",
    "Accept": "application/json",
    "X-Cisco-Meraki-API-Key": "6bec40cf957de430a6f1f2baa056b99a4fac9ea0"
}
########################################## Default requests ##################################################
response = requests.request('GET', urlo, headers=headers, data = payload)
orgData= json.loads(response.text)
response= requests.request('GET', urld, headers=headers, data = payload)
orgDev= json.loads(response.text)

######################################### functions ###########################################################

def org_Data(): #Consulta la data de las organizaciones a las que tenemos 
    response = requests.request('GET', urlo, headers=headers, data = payload)
    orgData= json.loads(response.text)

def org_Dev(): #Consulta los dispositivos de DeLab
    response= requests.request('GET', urld, headers=headers, data = payload)
    orgDev= json.loads(response.text)

def  oid_DeLab(): #busca el organization Id de DeLab
    DeLab=[]
    for i in range(len(orgData)):
        if(orgData[i]['name']=='DeLab'):    	    
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

def formpt(p):
    for i in range(len(p)):
        pcopy = p[i].copy()
        p[i].clear()

        if pcopy["productType"]=="wireless":
            p[i]["productType"] = pcopy["productType"]
            p[i]["model"] = pcopy["model"]
            p[i]["name"] = pcopy["name"]
            p[i]["mac"] = pcopy["mac"]
            p[i]["lanIp"] = pcopy["lanIp"]
            p[i]["serial"] = pcopy["serial"]
        else:
            p[i]["productType"] = pcopy["productType"]
            p[i]["model"] = pcopy["model"]
            p[i]["name"] = pcopy["name"]
            p[i]["mac"] = pcopy["mac"]
            p[i]["wan1Ip"] = pcopy["wan1Ip"]
            p[i]["wan2Ip"] = pcopy["wan2Ip"]
            p[i]["serial"] = pcopy["serial"]
        
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

def printcsvdata(): #imprime en el terminal la data del inventario en formato .json
    p=productType()
    formpt(p)
    pp(p)