#Exercice 1 :
def renverse(mot):
    result = ""
    for i in range(len(mot)):
        result += mot[-i - 1]
    return result

assert renverse("") == ""
assert renverse("abc") == "cba", renverse("abc")
assert renverse("informatique") == "euqitamrofni", renverse("informatique")

#Exercice 2 :
def crible(n):
    """Renvoie un tableau contenant tous les nombres premiers
    plus petits que n."""
    premiers = []
    tab = [True] * n
    tab[0], tab[1] = False, False
    for i in range(n):
        if tab[i]:
            premiers.append(i)
            multiple = 2*i
            while multiple < n:
                tab[multiple] = False
                multiple = int((multiple / i + 1) * i)
    return premiers

assert crible(40) == [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37]
assert crible(5) == [2, 3]