text = input("Текст ")
num_sentences = text.count('.') + text.count('!') + text.count('?')
print(f"кількість пропозицій у цьому тексті: {num_sentences}")