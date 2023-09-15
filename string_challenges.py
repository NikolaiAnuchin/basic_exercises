# Вывести последнюю букву в слове
word = 'Архангельск'

print(word[-1])


# Вывести количество букв "а" в слове
word = 'Архангельск'

print("Количество букв \"а\" в слове:", word.lower().count('а'))


# Вывести количество гласных букв в слове
word = 'Архангельск'

vowels = set("аеоуиюэя")
number_of_vowels = 0

for letter in word:
    if letter in vowels:
        number_of_vowels += 1

print("Количество гласных букв  в слове:", number_of_vowels)

# Вывести количество слов в предложении
sentence = 'Мы приехали в гости'

print("Количество слов в предложении:", len(sentence.split()))

# Вывести первую букву каждого слова на отдельной строке
sentence = 'Мы приехали в гости'

for word in sentence.split():
    print(word[0])


# Вывести усреднённую длину слова в предложении
sentence = 'Мы приехали в гости'

number_of_letters = 0
for word in sentence.split():
    number_of_letters += len(word)

print("Усредненная длина слова в предложении:", number_of_letters/len(sentence.split()) )