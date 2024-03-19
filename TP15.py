#Exercice 1 :
def moyenne(tab):
    result = 0.0
    for i in range(len(tab)):
        result += tab[i]
    return result / len(tab)

print(moyenne([1.0]))
print(moyenne([1.0, 2.0, 4.0]))

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

print(binaire(83))
print(binaire(6))
print(binaire(127))
print(binaire(0))
