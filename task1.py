def combinations(cnt):
    res = 0
    for digit1 in [i for i in range(cnt)]:
        for digit2 in [i for i in range(cnt)]:
            for digit3 in [i for i in range(cnt)]:
                res += 1
    return res
digits = int(input("Введите кол-во цифр: "))
print(f'Кол-во трёхзначных чисел: {combinations(digits)}')
