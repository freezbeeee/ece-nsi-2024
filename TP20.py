#Exercice 1 :
import random

def lancer(n):
    result = []
    for i in range(n):
        result.append(random.randint(1, 6))
    return result

def paire_6(tab):
    temp = 0
    for i in range(len(tab)):
        if tab[i] == 6:
            temp += 1
    if temp >= 2:
        return True
    else:
        return False
    
lancer1 = lancer(5)
print(lancer1)
print(paire_6(lancer1))

lancer2 = lancer(5)
print(lancer2)
print(paire_6(lancer2))

lancer3 = lancer(3)
print(lancer3)
print(paire_6(lancer3))

lancer4 = lancer(0)
print(lancer4)
print(paire_6(lancer4))

#
#
#Exercice 2 :
def nombre_lignes(image):
    '''renvoie le nombre de lignes de l'image'''
    return len(image) 

def nombre_colonnes(image):
    '''renvoie la largeur de l'image'''
    return len(image[0])

def negatif(image):
    '''renvoie le negatif de l'image sous la forme
       d'une liste de listes'''
    # on cree une image de 0 aux memes dimensions 
    # que le parametre image
    nouvelle_image = [[0 for k in range(nombre_colonnes(image))]
         for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            nouvelle_image[i][j] = 255 - image[i][j]
    return nouvelle_image

def binaire(image, seuil):
    '''renvoie une image binarisee de l'image sous la forme
       d'une liste de listes contenant des 0 si la valeur
       du pixel est strictement inferieure au seuil et 1 sinon'''
    nouvelle_image = [[0] * nombre_colonnes(image)
                      for i in range(nombre_lignes(image))]

    for i in range(nombre_lignes(image)):
        for j in range(nombre_colonnes(image)): 
            if image[i][j] < seuil : 
                nouvelle_image[i][j] = 0 
            else:
                nouvelle_image[i][j] = 1 
    return nouvelle_image

img=[[20, 34, 254, 145, 6], [23, 124, 237, 225, 69], [197, 174, 207, 25, 87], [255, 0, 24, 197, 189]]
print(nombre_lignes(img))
print(nombre_colonnes(img))
print(negatif(img))
print(binaire(img, 120))