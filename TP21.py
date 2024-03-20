#Exercice 1 :
def recherche_motif(motif, texte):
    result = []
    for i in range(len(texte)):
        if texte[i:i+len(motif)] == motif:
            result.append(i)
    return result

print(recherche_motif("ab", ""))
print(recherche_motif("ab", "cdcdcdcd"))
print(recherche_motif("ab", "abracadabra"))
print(recherche_motif("ab", "abracadabraab"))

#
#
#Exercice 2 :
def parcours(adj, x, acc):
    '''Réalise un parcours en profondeur récursif
    du graphe donné par les listes d'adjacence adj
    depuis le sommet x en accumulant les sommets
    rencontrés dans acc'''
    if x not in acc:
        acc.append(x)
        for y in adj[x]:
            parcours(adj, y, acc)

def accessibles(adj, x):
    '''Renvoie la liste des sommets accessibles dans le
    graphe donné par les listes d'adjacence adj depuis
    le sommet x.'''
    acc = []
    parcours(adj, x, acc)
    return acc

print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 0))
print(accessibles([[1, 2], [0], [0, 3], [1], [5], [4]], 4))