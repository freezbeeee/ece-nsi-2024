#Exercice 1 :
def liste_puissances(a, b):
    result = [a]
    for i in range(b-1):
        result.append(result[i]*a)
    return result
        
def liste_puissances_borne(a, b):
    if a < b:
        result = [a]
    else:
        return []
    for i in range(b):
        if result[i]*a < b:
            result.append(result[i]*a)
        else:
            break
    return result

print(liste_puissances(3, 5))
print(liste_puissances(-2, 4))
print(liste_puissances_borne(2, 16))
print(liste_puissances_borne(2, 17))
print(liste_puissances_borne(5, 5))

#--------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------
#Exercice 2 :

dico = {"A": 1, "B": 2, "C": 3, "D": 4, "E": 5, "F": 6,
        "G": 7, "H": 8, "I": 9, "J": 10, "K": 11, "L": 12,
        "M": 13, "N": 14, "O": 15, "P": 16, "Q": 17,
        "R": 18, "S": 19, "T": 20, "U": 21, "V": 22,
        "W": 23, "X": 24, "Y": 25, "Z": 26}

def codes_parfait(mot):
    """Renvoie un triplet 
    (code_additionne, code_concatene, mot_est_parfait) où :
    - code_additionne est la somme des codes des lettres du mot ;
    - code_concatene est le code des lettres du mot concaténées ;
    - mot_est_parfait est un booléen indiquant si le mot est parfait."""
    code_concatene = ""
    code_additionne = 0 
    for c in mot:
        code_concatene = code_concatene + str(dico[c]) 
        code_additionne = code_additionne + dico[c] 
    code_concatene = int(code_concatene)
    mot_est_parfait = not bool(code_concatene % code_additionne)
    return code_additionne, code_concatene, mot_est_parfait

print(codes_parfait("PAUL"))
print(codes_parfait("ALAIN"))