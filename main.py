import nmap3
import netifaces
import json
import platform

banner = """

Author: Fabrizio Fadigati
Status: IN PROGRESS

---Automatic LAN scanning with python nmap----

One of my personal software experiments


"""

print(banner)

nmap = nmap3.Nmap()

if platform.version() == "Linux":

    nic_int_json = json.loads(netifaces.ifaddresses("enp3s0")[2])

    addr = nic_int_json["addr"]
    netmask = nic_int_json["netmask"]

    #To be developed

else:   
    print("To be developed")







    



