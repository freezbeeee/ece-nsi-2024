# Exercice 1 :
notes_eval = [2, 0, 5, 9, 6, 9, 10, 5, 7, 9, 9, 5, 0, 9, 6, 5, 4]

def effectif_notes(notes):
    result = []
    for i in range(11):
        j = 0
        for n in notes:
            if n == i:
                j += 1
        result.append(j)
    return result

print(effectif_notes(notes_eval))

def notes_triees(notes):
    result = []
    for i in range(11):
        for j in range(notes[i]):
            result.append(i)
    return result

print(notes_triees(effectif_notes(notes_eval)))


#-------------------------------------------------------------------------------------------
#-------------------------------------------------------------------------------------------
# Exercice 2 :

def dec_to_bin(nb_dec):
    q, r = nb_dec // 2, nb_dec % 2
    if q == 0: 
        return str(r) 
    else:
        return dec_to_bin(q) + str(r)

def bin_to_dec(nb_bin):
    if len(nb_bin) == 1:
        if nb_bin == '0': 
            return 0
        else:
            return 1 
    else:
        if nb_bin[-1] == '0':
            bit_droit = 0
        else:
            bit_droit = 1
        return 2 * bin_to_dec(nb_bin[:-1]) + bit_droit 


print(dec_to_bin(25))
print(bin_to_dec('101010'))