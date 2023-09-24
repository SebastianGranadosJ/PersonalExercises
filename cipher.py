alphabet = "abcdefghijklmnopqrstuvwxyz"
punctuation = ".,?'! "
def decoder(message, offset):
    cipher_message = ""
    for index in range(len(message)):
        if not message[index] in punctuation:
            x = alphabet.index(message[index]) + offset
            if x > 25:
                x = x - 26
                cipher_message += alphabet[x]
            else:
                cipher_message += alphabet[x]
        else:
            cipher_message += message[index]
    print(cipher_message)

def coder(my_message, offset):
    my_message_coded = ""
    for letter in my_message:
        if not letter in punctuation:
            my_message_coded += alphabet[alphabet.index(letter) - offset]
        else:
            my_message_coded += letter
    print(my_message_coded)

def vigenere(message, keyword):
    decoded_message = ""
    keyword_phrase = ""
    keyword_index = 0
    for letter in message:
        if not letter in punctuation:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
            if keyword_index == len(keyword):
                keyword_index = 0
        else:
            keyword_phrase += letter

    for letter_index in range(len(message)):
        if not message[letter_index] in punctuation:
            x = alphabet.index(message[letter_index]) - alphabet.index(keyword_phrase[letter_index])
            decoded_message += alphabet[x]
        else:
            decoded_message += message[letter_index]
    print(decoded_message)

vigenere("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friends")

def code_vigenere(message, keyword):
    coded_message = ""
    keyword_phrase = ""
    keyword_index = 0
    for letter in message:
        if not letter in punctuation:
            keyword_phrase += keyword[keyword_index]
            keyword_index += 1
            if keyword_index == len(keyword):
                keyword_index = 0
        else:
            keyword_phrase += letter
    
    for letter_index in range(len(message)):
        if not message[letter_index] in punctuation:
            x = alphabet.index(message[letter_index]) + alphabet.index(keyword_phrase[letter_index])
            if x > 25:
                x = x -26
                coded_message += alphabet[x]
            else:
                coded_message += alphabet[x]
        else:
            coded_message += message[letter_index]
    print(coded_message)

epic_message = vigenere("dfc aruw fsti gr vjtwhr wznj? vmph otis! cbx swv jipreneo uhllj kpi rahjib eg fjdkwkedhmp!", "friends")

