# BY OMAR
# >>>>>>>>>>>>>>>>>>>>>>>>>> STATUT OK
# FONCTION : permet de rechercher un mot dans un ficher et affiche toutes les lignes ou se trouve le mot.
import os

from scapy.config import conf
from scapy.fields import RawVal
from scapy.layers import l2
from scapy.layers.inet import IP, UDP, TCP
from scapy.layers.l2 import Ether, Dot1Q
from scapy.sendrecv import sendp, send, srloop
from scapy.themes import BrightTheme

import tkinter
from tkinter.filedialog import askopenfile
from tkinter import filedialog
doc2 = []
def rechercher_CS7_boutton():
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0xE0")
    # CS7
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0xE0")
    print(test2)
    # =========================================
    print('SEND OK')

def rechercher_CS6_boutton():
    # CS6
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c "+str(chaine) +" -p 5003 -S 0xC0")
    print(test2)
    # =========================================
    print('SEND OK')

def rechercher_CS5_boutton():
    # CS5
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0xA0")
    # CS5
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c "+str(chaine) +" -p 5003 -S 0xA0")
    print(test2)


    # =========================================
    print('SEND OK')

def rechercher_CS4_boutton():
    # CS4
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x80")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c "+str(chaine) +" -p 5003 -S 0x80")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_CS3_boutton():
    # CS3
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x60")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x60")
    print(test2)
    # =========================================
    print('SEND OK')


def rechercher_CS2_boutton():
    # CS2
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x40")
    chaine = time_entry.get()
    time_entry.get()

    #test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x40")
    #test2 = os.system("iperf -c " + str(chaine) + " -p 5003 -TOS 0x40")
    test2 = os.system("iperf -c " + str(chaine) + " -p 5001 ")
    print(test2)

    # =========================================
    print('SEND OK')


def rechercher_CS1_boutton():
    # CS1
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x20")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x20")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_BE_boutton():
    # BE
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x00")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x00")
    print(test2)

    # =========================================
    print('SEND OK')


def rechercher_EF_boutton():
    # EF
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0xB8")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0xB8")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF31_boutton():
    # AF31
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x68")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x68")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF32_boutton():
    # AF32
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x70")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x70")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF33_boutton():
    # AF33
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x78")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x78")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF11_boutton():
    # AF11
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x28")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x28")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF12_boutton():
    # AF12
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x30")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x30")
    print(test2)

    # =========================================
    print('SEND OK')


def rechercher_AF13_boutton():
    # AF13
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x38")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x38")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF21_boutton():
    # AF21
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x48")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x48")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF22_boutton():
    # AF22
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x50")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x50")
    print(test2)

    # =========================================
    print('SEND OK')

def rechercher_AF23_boutton():
    # AF23
    #test2 = os.system("iperf3 -c 176.143.171.36 -p 5003 -S 0x58")
    chaine = time_entry.get()
    time_entry.get()

    test2 = os.system("iperf3 -c " + str(chaine) + " -p 5003 -S 0x58")
    print(test2)

    # =========================================
    print('SEND OK')



#items = ["a", "b", "c", "d"]
#with open("outputfile.txt", "w") as opfile:
#    opfile.write("\n".join(doc2))


window = tkinter.Tk()

# INFORMATIONS : Le Gestionnaire d'emplacement (on a 3 : Pack,grid, )
window.title("IPERF3 -- Packet Generator for DSCP Marking              By Omar")
window.geometry("600x650")

# Afficher le LABEL
tkinter.Label(text="Choisir une addresse IPv4 Dst").pack()

# Afficher le CHAMP pour écrire
time_entry= tkinter.Entry()
time_entry.pack()



#tkinter.Label(text="Entrez le mot à rechercher P2P").pack()

# Afficher le boutton Browser
#tkinter.Button(text='Browse', command=askopenfile).pack()

# Afficher le boutton
tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS7",command=rechercher_CS7_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS6",command=rechercher_CS6_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS5",command=rechercher_CS5_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS4",command=rechercher_CS4_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS3",command=rechercher_CS3_boutton).pack()

tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS2",command=rechercher_CS2_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en CS1",command=rechercher_CS1_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en BE" ,command=rechercher_BE_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en EF" ,command=rechercher_EF_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF31",command=rechercher_AF31_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF32",command=rechercher_AF32_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF33",command=rechercher_AF33_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF11",command=rechercher_AF11_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF12",command=rechercher_AF12_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF13",command=rechercher_AF13_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF21",command=rechercher_AF21_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF22",command=rechercher_AF22_boutton).pack()
tkinter.Button(text="Générer un flux TCP IPv4 marqué en AF23",command=rechercher_AF23_boutton).pack()




#filename = askopenfile(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
#fichier = open(filename, "r")
#content = fichier.read()
#fichier.close()

#Label(fenetre, text=content).pack(padx=10, pady=10)

# Afficher la fenetre
window.mainloop()

# event.loop

