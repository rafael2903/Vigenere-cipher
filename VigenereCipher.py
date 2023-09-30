class VigenereCipher():
    ENCODE = 'encode'
    DECODE = 'decode'

    @staticmethod
    def encode(key: str, plain_text: str):
        return VigenereCipher.translate(key, plain_text, VigenereCipher.ENCODE)

    @staticmethod
    def decode(key: str, cipher_text: str):
        return VigenereCipher.translate(key, cipher_text, VigenereCipher.DECODE)

    @staticmethod
    def pad_key(key: str, text: str):
        key = key.lower()
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
    def translate(key: str, text: str, mode: str):
        key_stream = VigenereCipher.pad_key(key, text)
        translated_text = ''
        i = 0

        for letter in text:
            if not letter.isalpha() or not letter.isascii():
                translated_text += letter
                continue

            base_char_code = ord('a') if letter.islower() else ord('A')
            key_letter = key_stream[i]
            key_letter_position = ord(key_letter) - ord('a')
            letter_position = ord(letter) - base_char_code

            if mode is VigenereCipher.ENCODE:
                translated_letter_position = (
                    letter_position + key_letter_position) % 26
            else:
                translated_letter_position = (
                    letter_position - key_letter_position) % 26

            translated_letter = chr(
                base_char_code + translated_letter_position)
            translated_text += translated_letter
            i += 1

        return translated_text
