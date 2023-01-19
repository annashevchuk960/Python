text = input("Текст ")
word = input("Слова ").split(',')
for word in text.split():
 if word.lower() in word:
   text = text.replace(word, word.upper())
print(text)
