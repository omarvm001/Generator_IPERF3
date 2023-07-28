# BY OMAR
# >>>>>>>>>>>>>>>>>>>>>>>>>> STATUT OK
# FONCTION : permet de rechercher un mot dans un ficher et affiche toutes les lignes ou se trouve le mot.
#from _multiprocessing import send
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
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=224)  # AF23
    #l4 = UDP(dport=RawVal(b"chaine2"))
    l4 = UDP(dport=554)
    #print(chaine2)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_CS6_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=192)  # AF23
    #l4 = UDP(dport=RawVal(b"chaine2"))
    l4 = UDP(dport=554)
    #print(chaine2)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_CS5_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=160)  # AF23
    #l4 = UDP(dport=RawVal(b"chaine2"))
    l4 = UDP(dport=554)
    #print(chaine2)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_CS4_boutton():
    chaine= time_entry.get()
    time_entry.get()
    l3 = IP(dst=chaine, tos=128)  # AF23
    #l4 = UDP(dport=RawVal(b"chaine2"))
    l4 = UDP(dport=554)
    #print(chaine2)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_CS3_boutton():
    chaine= time_entry.get()
    time_entry.get()
    l3 = IP(dst=chaine, tos=96)  # AF23
    #l4 = UDP(dport=RawVal(b"chaine2"))
    l4 = UDP(dport=554)
    #print(chaine2)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')


def rechercher_CS2_boutton():
    chaine= time_entry.get()
    time_entry.get()
    l3 = IP(dst=chaine, tos=64)  # AF23
    #l4 = UDP(dport=RawVal(b"chaine2"))
    l4 = UDP(dport=554)
    #print(chaine2)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')


def rechercher_CS1_boutton():
    chaine= time_entry.get()
    time_entry.get()
    l3 = IP(dst=chaine, tos=32)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_BE_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=0)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')


def rechercher_EF_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=184)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF31_boutton():
    chaine= time_entry.get()
    time_entry.get()
    l3 = IP(dst=chaine, tos=104)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF32_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=112)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF33_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=120)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF11_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=40)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF12_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=48)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')


def rechercher_AF13_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=56)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF21_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=72)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF22_boutton():
    chaine= time_entry.get()
    time_entry.get()

    l3 = IP(dst=chaine, tos=80)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')

def rechercher_AF23_boutton():
    chaine= time_entry.get()

    l3 = IP(dst=chaine, tos=88)  # AF23
    l4 = UDP(dport=554)
    print("=========================")
    pkt = l3 / l4
    # ========================================= count=10
    send(pkt, count=10, inter=0.2)
    pkt.show()
    print("444")
    # sendp(pkt, loop=1, inter=0.2)
    # srloop(pkt)
    # =========================================
    print('SEND OK')



#items = ["a", "b", "c", "d"]
#with open("outputfile.txt", "w") as opfile:
#    opfile.write("\n".join(doc2))


window = tkinter.Tk()

# INFORMATIONS : Le Gestionnaire d'emplacement (on a 3 : Pack,grid, )
window.title("Python Packet Generator for DSCP Marking - By Omar")
window.geometry("400x300")

# Afficher le LABEL
tkinter.Label(text="Choisir une addresse IPv4 Dst").pack()

# Afficher le CHAMP pour écrire
time_entry= tkinter.Entry()
time_entry.pack()



#tkinter.Label(text="Entrez le mot à rechercher P2P").pack()

# Afficher le boutton Browser
#tkinter.Button(text='Browse', command=askopenfile).pack()

# Afficher le boutton
tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS7",command=rechercher_CS7_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS6",command=rechercher_CS6_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS5",command=rechercher_CS5_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS4",command=rechercher_CS4_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS3",command=rechercher_CS3_boutton).pack()

tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS2",command=rechercher_CS2_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en CS1",command=rechercher_CS1_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en BE" ,command=rechercher_BE_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en EF" ,command=rechercher_EF_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF31",command=rechercher_AF31_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF32",command=rechercher_AF32_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF33",command=rechercher_AF33_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF11",command=rechercher_AF11_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF12",command=rechercher_AF12_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF13",command=rechercher_AF13_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF21",command=rechercher_AF21_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF22",command=rechercher_AF22_boutton).pack()
tkinter.Button(text="Générer un flux UDP IPv4 marqué en AF23",command=rechercher_AF23_boutton).pack()




#filename = askopenfile(title="Ouvrir votre document",filetypes=[('txt files','.txt'),('all files','.*')])
#fichier = open(filename, "r")
#content = fichier.read()
#fichier.close()

#Label(fenetre, text=content).pack(padx=10, pady=10)

# Afficher la fenetre
window.mainloop()

# event.loop
