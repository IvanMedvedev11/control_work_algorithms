def combinations_repl(elems):
    for i in range(len(elems)):
        for j in range(i, len(elems)):
            yield elems[i] + "\n" + elems[j] + "\n"
def combinations(elems):
    for i in range(len(elems)):
        for j in range(i + 1, len(elems)):
            yield elems[i] + "\n" + elems[j] + "\n"
elems = input("Введите предметы через пробел: ").split()
print("С повторами:")
for res in combinations_repl(elems):
    print(res)
print("Без повторов:")
for res in combinations(elems):
    print(res)
