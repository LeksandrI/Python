# Напишите программу, которая принимает на вход список слов такого вида:
# words = ["Speak ","to", "me ", "of", "Florence" ,"And ", "of", "the", "Renaissanc
# e"]
# а возвращает список
# words_clean = ["speak", "to", "me", "of", "florence", "and", "of", "the", "renaiss
# ance"]
# Другими словами, программа убирает пробелы в словах и приводит все слова к нижнему регистру.
# Подсказка: запросите help() по методам strip() и lower()

words = ["Speak "," to ", " me ", "of ", " Florence " ," And ", " of ", " the ", " Renaissance "]
print(words)

tipi = [name.strip() for name in words]
print(tipi)

# lower = []
# for k in words:
#    lower.append(k.strip())
#
# print(lower)

reg = [k.lower() for k in tipi]
print(reg)