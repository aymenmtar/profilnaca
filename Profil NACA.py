#Ce programme génère et trace le profil d'une aile NACA 4 chiffres symétrique.

import numpy as np
import matplotlib.pyplot as plt

print("Ce programme génère et trace le profil d'une aile NACA 4 chiffres symétrique.")
print("un profil NACA est une forme d'aile standardisée utilisée en aéronautique. \nLes profils NACA sont définis par la National Advisory Committee for Aeronautics (NACA) et sont caractérisés par une série de chiffres qui décrivent leur forme.")
print("pour plus d'informations sue le profil NACA : https://fr.wikipedia.org/wiki/Profil_NACA")

while True:
    numero_naca = input("Entrez le numéro du profil NACA 4 chiffres symétrique (ex. 0012):").strip()
    if len(numero_naca) == 4 and numero_naca.isdigit() and numero_naca.startswith("00"):
        break
    print("Entrée invalide.svp entrer un numéro de profil NACA à 4 chiffres symétriques (ex. 0012).")

while True:
    try:
        longueur_corde = float(input("Entrez la longueur de la crde (en mètre):"))
        if longueur_corde > 0:
            break
        else:
            print("La longueur de la corde doit être un nombre positif.")
    except ValueError:
        print("Entrée invalide. entrer un nombre valide pour la longueur de la corde.")

while True:
    try:
        nb_points = int(input("Entrez le nombre de points le long de la corde pour le tracé:"))
        if nb_points > 1:
            break
        else:
            print("Le nombre de points doit être un entier supérieur à 1.")
    except ValueError:
        print("Entrée invalide. entrer un nombre entier valide pour le nombre de points.")

while True:
    type_distribution = input("Entrez le type de distribution des points ('l' pour linéaire, 'n' pour non-uniforme) : ").strip().lower()
    if type_distribution in ['l', 'n']:
        break
    print("Entrée invalide! Veuillez entrer 'l' pour linéaire ou 'n' pour non-uniforme.")

def profil_naca(numero_naca, longueur_corde, nb_points, type_distribution):
    t = int(numero_naca[2:]) / 100 #l'épaisseur max du profil à partir du numéro NACA
    if type_distribution == 'n': #la distribution des points le long de la corde
        teta = np.linspace(0, np.pi, nb_points)
        xc = 0.5 * (1 - np.cos(teta))
    else:  #distribution linéaire
        xc = np.linspace(0, 1, nb_points)

    #Calcul la demi-épaisseur du profil yt :
    yt = 5 * t * (0.2969 * np.sqrt(xc) - 0.1260 * xc - 0.3516 * xc ** 2 + 0.2843 * xc ** 3 - 0.1036 * xc ** 4)

    #Calcul les coordonnées des points du profil:
    x_up = xc * longueur_corde
    x_down = xc * longueur_corde
    y_up = yt * longueur_corde
    y_down = -yt * longueur_corde

    #Calcul d'épaisseur maximale et sa position:
    epaisseur_maximale = np.max(yt) * longueur_corde
    position_epaisseur_maximale = xc[np.argmax(yt)] * longueur_corde

    return x_up, y_up,x_down,y_down,epaisseur_maximale,position_epaisseur_maximale


def tracer_profil_naca(x_up, y_up, x_down, y_down, numero_naca, longueur_corde, epaisseur_maximale,position_epaisseur_maximale):
    plt.figure(figsize=(10, 5))
    plt.plot(x_up, y_up, label='Extrados')
    plt.plot(x_down, y_down, label='Intrados')
    plt.legend()
    plt.grid(True)
    plt.xlabel('Longueur de la corde (m)')
    plt.ylabel('Épaisseur (m)')
    plt.title(f'Profil NACA {numero_naca} - Corde : {longueur_corde} m')
    plt.annotate(f'Épaisseur max: {epaisseur_maximale:.4f} m\nPosition: {position_epaisseur_maximale:.4f} m',
                 xy=(position_epaisseur_maximale, epaisseur_maximale),
                 xytext=(position_epaisseur_maximale + 0.05, epaisseur_maximale),
                 arrowprops=dict(facecolor='black', shrink=0.05))
    plt.show()
#Génération du profil NACA:
x_up,y_up, x_down, y_down, epaisseur_maximale, position_epaisseur_maximale = profil_naca(numero_naca, longueur_corde,nb_points,type_distribution)

# Affichage des résultats:
print(f"Épaisseur maximale: {epaisseur_maximale:.4f} m")
print(f"Position de l'épaisseur maximale: {position_epaisseur_maximale:.4f} m")

#trace de profil NACA
tracer_profil_naca(x_up,y_up,x_down,y_down, numero_naca, longueur_corde, epaisseur_maximale, position_epaisseur_maximale)
