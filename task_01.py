#1. Напишите программу, удаляющую из текста все слова, содержащие "абв". В тексте используется разделитель пробел.
# in
#Number of words: 10
#out
#авб абв бав абв вба бав вба абв абв абв
#авб бав вба бав вба

import random

def get_words(count: int) -> str:
    result = ""
    arr = [x + y + z for x in "абв" for y in "абв" for z in "абв"]
    for i in range(count):
        result += f"{random.choice(arr)} "
    print(f"Создана строка из {count} рандомных слов: \n{result}")
    return result

def remove_str(arr: str, remove_word: str) -> list:
    if remove_word in arr:
        result = arr.replace(remove_word, "").split()
        print(*result)
        return result
    else:
        print(-1)
        return [-1]

all_list = get_words(int(input("Введите кол-во слов в строке: ")))
new_list = remove_str(all_list, input("Введите словосочетание которое нужно убрать: "))