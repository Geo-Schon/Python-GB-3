n, m = map(int, input('Введите через пробел количество элементов первого и второго множеств: ').split())
a = set(map(int, input('Введите элементы первого множества: ').split()))
b = set(map(int, input('Введите элементы второго множества: ').split()))
print(*sorted(a & b))