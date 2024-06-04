# profilnaca
Ce programme génère et trace le profil d'une aile NACA 4 chiffres symétrique.

Les profils NACA sont des formes d’aile testées par le National Advisory Committee for Aeronautics.
Leur forme est déterminée par une ou plusieurs équations mathématiques paramétrées. Pour les profils dits 4 chiffres symétriques NACA00XX, deux paramètres principaux sont utilisés : 
la corde du profil c, qui représente la distance entre le bord d’attaque et le bord de fuite, et l’épaisseur maximale du profil t, 
exprimée en pourcentage de la corde. Cette épaisseur est définie par les deux derniers chiffres du code du profil. Ainsi :  
t=XX/100.
La coordonnée adimensionnelle Xc varie de 0 à 1 le long de la corde, et la demi-épaisseur du profil Yt est également adimensionnée par la corde. 
Elle est paramétrée en fonction de Xc par l’équation :
yt=5t(0.2969√Xc−0.1260Xc−0.3516Xc²+0.2843xc^3 − 0.1036 Xc^4)


Le programme génère les coordonnées (xup,yup) et (xdown,ydown) selon le nombre de points requis sous forme de tableaux numpy. La distribution des points le long de la corde est calculée selon la transformée de Glauert :
Xc = 1/2 (1−cos(θ)) où θ varie de 0 à π pour couvrir les valeurs de Xc de 0 à 1.

***** Instructions d'utilisation :

Installez les bibliothèques Numpy et Matplotlib.
Lancez le programme.
Entrez le numéro du profil NACA 4 chiffres symétrique.
Entrez la corde du profil (en mètre).
Entrez le nombre de points le long de la corde pour le tracé.
Choisissez le type de distribution des points le long de la corde : linéaire ou non-uniforme selon la transformée de Glauert.
Le programme calculera l’épaisseur maximale du profil ainsi que sa position le long de la corde, et affichera ces résultats.
Le programme tracera la forme du profil dans un graphique généré avec matplotlib, comprenant une légende (extrados/intrados), un quadrillage, des étiquettes sur les axes et un titre.