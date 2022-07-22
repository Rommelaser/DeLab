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

######################################### functions ###########################################################

def org_Data(): #Consulta la data de las organizaciones a las que tenemos 
    response = requests.request('GET', urlo, headers=headers, data = payload)
    orgData= json.loads(response.text)

def printallOrg(): #lista todas las organizaciones
    pp(orgData)
    
def printOrg(i): #imprime una organización en específico
    pp(orgData[i])