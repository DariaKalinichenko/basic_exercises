# Вывести последнюю букву в слове
word = 'Архангельск'
print(f'Вывести последнюю букву в слове: {word[-1]}')


# Вывести количество букв "а" в слове
word = 'Архангельск'
print(f'Вывести количество букв "а" в слове: {len(word)}')


# Вывести количество гласных букв в слове
word = 'Архангельск'
count = 0
for i in word:
    if i in 'ауоыиэяюёе':
        count += 1
print(f'Количество гласных: {count}')

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'
len_sentence = len(sentence.split(' '))
print(f'количество слов в предложении: {len_sentence}')


# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'
print(f'Вывести первую букву каждого слова на отдельной строке:')
for i in sentence.split(' '):
    print(i[0])

# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'
sentence = sentence.split(' ')
sum = 0
for i in sentence:
    sum+=len(i)
print(f'Усреднённая длина слова в предложении: {sum//len(sentence)}')

