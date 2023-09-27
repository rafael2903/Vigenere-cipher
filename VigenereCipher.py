class VigenereCipher():
    def __init__(self, key: str):
        self.key = key.lower()

    def encode(self, plain_text: str):
        plain_text_length = len(plain_text)
        key_length = len(self.key)

        if key_length >= plain_text_length:
            key_stream = self.key[:plain_text_length]
        else:
            key_full_repetitions = plain_text_length // key_length
            key_remaining_letters = plain_text_length % key_length
            key_stream = self.key * key_full_repetitions
            key_stream += self.key[:key_remaining_letters]

        cipher_text = ''
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

    def decode(self, cipher_text: str):
        pass


