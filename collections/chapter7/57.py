def no_vowel():
    with open('files/words.txt', 'r', encoding='utf-8') as f1:
        word_list = f1.readlines()
    vowels = ['a', 'e', 'i', 'o', 'u']
    new_list = [word for word in word_list if word[0] not in vowels]
    with open('files/new_words.txt', 'w', encoding='utf-8') as f2:
        f2.writelines(new_list)


if __name__ == '__main__':
    no_vowel()
