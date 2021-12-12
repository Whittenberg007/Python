
import os
import requests
import json

API_KEY = os.environ.get('api_key')

url = "https://api.meraki.com/api/v1/organizations/361444/devices/statuses?"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': API_KEY
}

response = requests.request("GET", url, headers=headers, data=payload)

allDevices = json.loads(response.text)

#Puts them into a list
for device in allDevices:
     if device["model"]=="MX60" and device["publicIp"]==device["wan1Ip"]:
        print("Model: {}".format(device["model"]))
        #Prints the name, model, and serial of the device on the network.
        print("Network ID: {} \t Model: {} \t Serial: {}".format(device["networkId"], device["model"], device["serial"]))
        #Prints the status, & lastReportedAt time of the device on the network
        print("Status: {} \t LastReportedAt: {}".format(device["status"], device["lastReportedAt"]))
        #Prints Public IP, & "This Device Is Currently On Wan1Ip."
        print("Public IP: {} \t ".format(device["publicIp"]) + "\nThis Device Is Currently On Wan1Ip. \n")

     elif device["model"]=="MX60" and device["publicIp"]!=device["wan1Ip"]:
        print("Model: {}".format(device["model"]))
        #Prints the name, model, and serial of the device on the network.
        print("Network ID: {} \t Model: {} \t Serial: {}".format(device["networkId"], device["model"], device["serial"]))
        #Prints the status, & lastReportedAt time of the device on the network
        print("Status: {} \t LastReportedAt: {}".format(device["status"], device["lastReportedAt"]))
        #Prints Public IP, & "This Device Is Currently On Wan1Ip."
        print("Public IP: {} \t ".format(device["publicIp"]) + "\nThis Device Is NOT Currently On Primary IP, Please Investigate This Device! \n")   

     elif device["model"]=="MX64" and device["publicIp"]==device["wan1Ip"]:
        print("Model: {}".format(device["model"]))
        #Prints the name, model, and serial of the device on the network.
        print("Network ID: {} \t Model: {} \t Serial: {}".format(device["networkId"], device["model"], device["serial"]))
        #Prints the status, & lastReportedAt time of the device on the network
        print("Status: {} \t LastReportedAt: {}".format(device["status"], device["lastReportedAt"]))
        #Prints Public IP, & "This Device Is Currently On Wan1Ip."
        print("Public IP: {} \t ".format(device["publicIp"]) + "\nThis Device Is Currently On Wan1Ip. \n")

     elif device["model"]=="MX64" and device["publicIp"]!=device["wan1Ip"]:
        print("Model: {}".format(device["model"]))
        #Prints the name, model, and serial of the device on the network.
        print("Network ID: {} \t Model: {} \t Serial: {}".format(device["networkId"], device["model"], device["serial"]))
        #Prints the status, & lastReportedAt time of the device on the network
        print("Status: {} \t LastReportedAt: {}".format(device["status"], device["lastReportedAt"]))
        #Prints Public IP, & "This Device Is Currently On Wan1Ip."
        print("Public IP: {} \t ".format(device["publicIp"]) + "\nThis Device Is NOT Currently On Primary IP, Please Investigate This Device! \n")