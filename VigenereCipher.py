class VigenereCipher():

    @staticmethod
    def pad_key(key, text):
        text_length = len(text)
        key_length = len(key)

        if key_length >= text_length:
            key_stream = key[:text_length]
        else:
            key_full_repetitions = text_length // key_length
            key_remaining_letters = text_length % key_length
            key_stream = key * key_full_repetitions
            key_stream += key[:key_remaining_letters]
        return key_stream

    @staticmethod
    def encode(key, plain_text):
        cipher_text = ''
        key_stream = VigenereCipher.pad_key(key, plain_text)
        i = 0

        for letter in plain_text:
            if not letter.isalpha() or not letter.isascii():
                cipher_text += letter
                continue

            base_char_code = ord('a') if letter.islower() else ord('A')
            key_letter = key_stream[i]
            key_letter_position = ord(key_letter) - ord('a')
            letter_position = ord(letter) - base_char_code

            cipher_letter_position = (
                letter_position + key_letter_position) % 26
            cipher_letter = chr(base_char_code + cipher_letter_position)

            cipher_text += cipher_letter
            i += 1

        return cipher_text

    @staticmethod
    def decode(key, cipher_text):
        key_stream = VigenereCipher.pad_key(key, cipher_text)
        plain_text = ''
        i = 0

        for letter in cipher_text:
            if not letter.isalpha() or not letter.isascii():
                plain_text += letter
                continue

            base_char_code = ord('a') if letter.islower() else ord('A')
            key_letter = key_stream[i]
            key_letter_position = ord(key_letter) - ord('a')
            letter_position = ord(letter) - base_char_code

            plain_letter_position = letter_position - key_letter_position
            if plain_letter_position < 0:
                plain_letter_position += 26

            plain_letter = chr(base_char_code + plain_letter_position)
            plain_text += plain_letter
            i += 1

        return plain_text
