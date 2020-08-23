import urllib.request
import os
import requests
import os.path
from os import path


if path.exists("./paper.jar"):
    os.system(
        "java -Xms8G -Xmx8G -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar paper.jar nogui"
    )
else:
    versions = requests.get("https://papermc.io/api/v1/paper")
    versions_json = versions.json()
    List = versions_json["versions"]
    buffer = " "
    print("Choose which version to download:", buffer.join(List))

    version = input()
    latestBuild = requests.get("https://papermc.io/api/v1/paper/" + version)
    latestBuild_json = latestBuild.json()
    print(
        "Downloading project: Paper,",
        "Spigot Version: ",
        version,
        "Build:",
        latestBuild_json["builds"]["latest"],
    )

    url = (
        "https://papermc.io/api/v1/paper/"
        + version
        + "/"
        + latestBuild_json["builds"]["latest"]
        + "/download"
    )
    urllib.request.urlretrieve(url, "./paper.jar")

    eula = "./eula.txt"
    eula = open(eula, "w")
    eula.write("eula=true")
    eula.close()

    server_properties = "./server.properties"
    server_properties = open(server_properties, "w")
    server_properties.write("online-mode=false")
    server_properties.close()

    print("How much ram to allocate for the startup of the server?")
    xms = input()

    print("Now enter the maximum memory allocation for the server.")
    xmx = input()

    os.system(
        "java -Xms"
        + xms
        + " -Xmx"
        + xmx
        + " -XX:+UseG1GC -XX:+ParallelRefProcEnabled -XX:MaxGCPauseMillis=200 -XX:+UnlockExperimentalVMOptions -XX:+DisableExplicitGC -XX:+AlwaysPreTouch -XX:G1NewSizePercent=30 -XX:G1MaxNewSizePercent=40 -XX:G1HeapRegionSize=8M -XX:G1ReservePercent=20 -XX:G1HeapWastePercent=5 -XX:G1MixedGCCountTarget=4 -XX:InitiatingHeapOccupancyPercent=15 -XX:G1MixedGCLiveThresholdPercent=90 -XX:G1RSetUpdatingPauseTimePercent=5 -XX:SurvivorRatio=32 -XX:+PerfDisableSharedMem -XX:MaxTenuringThreshold=1 -Dusing.aikars.flags=https://mcflags.emc.gs -Daikars.new.flags=true -jar paper.jar nogui"
    )

