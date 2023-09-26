# plain_text = 'teste testando o texto de teste para o trabalho'
# key = 'mysupersecretkey'

plain_text = 'joao e o pe de feijao ana'
key = 'mykey'

plain_text_length = len(plain_text)
key_length = len(key)

if key_length >= plain_text_length:
    key_stream = key[:plain_text_length]
else:
    key_full_repetitions = plain_text_length // key_length
    key_remaining_letters = plain_text_length % key_length
    key_stream = key * key_full_repetitions
    key_stream += key[:key_remaining_letters]

cipher_text = ''

i = 0
for letter in plain_text:
    if not letter.isalpha():
        cipher_text += letter
        continue

    key_letter = key_stream[i]
    key_letter_position = ord(key_letter) - ord('a')
    letter_position = ord(letter) - ord('a')
    cipher_letter_position = (letter_position + key_letter_position) % 26
    cipher_letter = chr(ord('a') + cipher_letter_position)
    cipher_text += cipher_letter
    i += 1

print(cipher_text)
