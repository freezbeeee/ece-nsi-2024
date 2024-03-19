#Exercice 1 :
def correspond(a,b):
    if len(a) != len(b):
        return False
    else:
        for i in range(len(a)):
            if b[i] == '*':
                pass
            elif a[i]!= b[i]:
                return False
            else:
                return True

print(correspond('INFORMATIQUE', 'INFO*MA*IQUE'))
print(correspond('AUTOMATIQUE', 'INFO*MA*IQUE'))
print(correspond('STOP', 'S*'))
print(correspond('AUTO', '*UT*'))

#
#
# Exercice 2 :l

def est_cyclique(plan):
    '''Prend en paramètre un dictionnaire `plan` correspondant à 
    un plan d'envoi de messages (ici entre les personnes A, B, C,
    D, E, F).
    Renvoie True si le plan d'envoi de messages est cyclique et 
    False sinon.'''
    expediteur = 'A'
    destinataire = plan[expediteur] 
    nb_destinataires = 1

    while destinataire != expediteur:
        destinataire = plan[destinataire] 
        nb_destinataires = nb_destinataires + 1 

    return nb_destinataires == len(plan)

print('----- Exo 2 -----')
print(est_cyclique({'A':'E','F':'A','C':'D','E':'B','B':'F','D':'C'}))
print(est_cyclique({'A':'E','F':'C','C':'D','E':'B','B':'F','D':'A'}))
print(est_cyclique({'A':'B','F':'C','C':'D','E':'A','B':'F','D':'E'}))
print(est_cyclique({'A':'B','F':'A','C':'D','E':'C','B':'F','D':'E'}))
