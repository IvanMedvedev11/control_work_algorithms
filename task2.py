def combinations_repl(digits):
    for i in range(len(digits)):
        for j in range(i, len(digits)):
            yield digits[i] + digits[j]
def combinations(digits):
    for i in range(len(digits)):
        for j in range(i + 1, len(digits)):
            yield digits[i] + digits[j]
nums = input("Введите цифры без пробелов: ")
print("С повторами:")
for res in combinations_repl(nums):
    print(res)
print("Без повторов:")
for res in combinations(nums):
    print(res)
