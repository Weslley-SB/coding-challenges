nums = [1, 2, 3, 3]
# nums = [1, 2, 3, 4]

def TemDuplicado(lista):
    n = len(lista)
    for numeros in range(n):
        for j in range(numeros+1, n):
            if lista[numeros] == lista[j]:
                return True
    return False

print(f"na lista {nums} tem numeros duplicados? {TemDuplicado(nums)}")