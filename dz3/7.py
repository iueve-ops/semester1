import string

# Читаем файл
with open('lorem.txt', 'r', encoding='utf-8') as f:
    text = f.read()

# Заменяем каждый знак препинания пробелом
for p in string.punctuation:
    text = text.replace(p, ' ')

# Приводим к нижнему регистру и разбиваем на слова
words = text.lower().split()

# Подсчёт слов
word_count = {}
for word in words:
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1

# Находим 10 самых частых слов
top_10 = []
for _ in range(10):
    max_word = max(word_count, key=word_count.get)
    top_10.append((max_word, word_count[max_word]))
    del word_count[max_word]

# Вывод
for word, count in top_10:
    print(f'{word}: {count}')
