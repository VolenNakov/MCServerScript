import urllib.request
import os
import os.path
from os import path

if path.exists("./server.jar"):
    os.system("java -jar server.jar")
else:
    print('Downloading latest Paper spigot...')
    url = 'https://papermc.io/api/v1/paper/1.14.4/latest/download'
    urllib.request.urlretrieve(url, './server.jar')
    
    eula = "./eula.txt"
    eula = open(eula, "w")
    eula.write("eula=true")
    eula.close()

    server_properties = "./server.properties"
    server_properties = open(server_properties, "w")
    server_properties.write("online-mode=false")
    server_properties.close()
    
    os.system("java -jar server.jar")

