import urllib.request
import requests
import tkinter
import os
from tkinter import (
    StringVar,
    OptionMenu,
    Tk,
    Button,
    DISABLED,
    END,
    Checkbutton,
    IntVar,
    ttk,
)


versions = requests.get("https://papermc.io/api/v1/paper")
versions_json = versions.json()
options = versions_json["versions"]

window = Tk()


def download():
    drop.config(state=DISABLED)
    downloadButton.config(state=DISABLED)
    latestBuild = requests.get("https://papermc.io/api/v1/paper/" + clicked.get())
    latestBuild_json = latestBuild.json()
    url = (
        "https://papermc.io/api/v1/paper/"
        + clicked.get()
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

    # if var.get() == 1:
    #     os.remove("tk.py")
    #     return ()


w = tkinter.Spinbox(window)
w.insert(END, "2")
w.pack()
var = IntVar()
scriptButton = tkinter.Checkbutton(window, text="Delete Script", variable=var)
scriptButton.pack()

clicked = StringVar()
clicked.set(options[0])

drop = OptionMenu(window, clicked, *options)
drop.pack(fill=tkinter.X)

downloadButton = Button(window, text="Download", command=download)
downloadButton.pack(fill=tkinter.X)

window.mainloop()

