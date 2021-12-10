import requests
import json
#import schedule
#import time

url = "https://api.meraki.com/api/v1/organizations/"Put Your Organization ID Here"/devices/statuses?"

payload={}
headers = {
  'X-Cisco-Meraki-API-Key': 'Put Your API Key Here'
}

response = requests.request("GET", url, headers=headers, data=payload)

allDevices = json.loads(response.text)

#Puts them into a list
for device in allDevices:
    #attempts to find all devices that match the MX60 and if they exist print them in a list with the following additional information
    if device["model"]=="MX60" or device["model"]=="MX64":
        print("Model: {}".format(device["model"]))
        #Prints the name, model, and serial of the device on the network.
        print("Network ID: {} \t Model: {} \t Serial: {}".format(device["networkId"], device["model"], device["serial"]))
        #Prints the status, & lastReportedAt time of the device on the network
        print("Status: {} \t LastReportedAt: {}".format(device["status"], device["lastReportedAt"]))
        #Prints UsingCellularFailover
        print("PublicIp: {} \t UsingCellularFailover: {} \n\n".format(device["publicIp"], device["usingCellularFailover"]))
    #elif device["model"]!="MX60" or device["model"]!="MX60":
        #print("This Device Is Not A Security Appliance.")


#prints the list of MX60 & MX64 Devices Along with other listed critera
print(AllDevices)
#defines the job
#def apiscript():
    #Tells the job what to do
    #print(device)
#Schedules every day at 5:00 AM to do the job
#schedule.every(20).seconds.do(apiscript)
#schedule.every().day.at("05:00").do(apiscript)
#
#while True:
    #schedule.run_pending()
    #time.sleep(1)
