# Даны два неупорядоченных набора целых чисел (может быть, с повторениями).
# Выдать без повторений в порядке возрастания все те числа, которые встречаются в обоих наборах.
# Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
# Затем пользователь вводит сами элементы множеств.

n = int(input(f"Введите количество элементов первого множества => "))
m = int(input(f"Введите количество элементов второго множества => "))
n_set = set(input(f'Введите {n} элемента(ов) первого множества через пробел: ').split())
m_set= set(input(f'Введите {m} элемента(ов) второго множества через пробел: ').split())
print(n_set)
print(m_set)
sorted_set = sorted(n_set.intersection(m_set))
print(sorted_set)
