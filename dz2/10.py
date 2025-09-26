glasnie = 'ауеыаоэяию'
with open('input_10.txt', 'r', encoding='utf-8') as file:
    line = file.readline().strip()
    words = line.split()

    result_words = []

    for word in words:
        new_word = []
        i = 0
        while i < len(word):
            new_word.append(word[i])
            if word[i] in glasnie:
                if i != len(word) - 1  and word[i + 1] not in glasnie:
                    new_word.append('с' + word[i])
                elif i + 1 == len(word):
                    new_word.append('с' + word[i])
            i += 1

        result_words.append(''.join(new_word))

    print(' '.join(result_words))