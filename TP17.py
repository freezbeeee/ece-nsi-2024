#Exercice 1 :
def nb_repetitions(elt, tab):
    result = 0
    for i in range(len(tab)):
        if elt == tab[i]:
            result += 1
    return result

print(nb_repetitions(5, [2, 5, 3, 5, 6, 9, 5]))
print(nb_repetitions('A', ['B', 'A', 'B', 'A', 'R']))
print(nb_repetitions(12, [1, '!', 7, 21, 36, 44]))

#
#
#Exercice 2 :
def binaire(a):
    if a == 0:
        return '0'
    bin_a = ''
    while a > 0:
        bin_a = str(a % 2) + bin_a
        a = a // 2
    return bin_a

print(binaire(0))
print(binaire(77))