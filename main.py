import pandas

nato_data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in nato_data.iterrows()}


while True:
    word = input("Enter a word: ")
    try:
        word_in_nato_code = [nato_alphabet[letter.upper()] for letter in word]
    except KeyError:
        print("Sorry, only letters in the alphabet please.")
    else:
        print(word_in_nato_code)
        break
