import unittest

from VigenereCipher import VigenereCipher


class Test(unittest.TestCase):
    key = 'mykey'

    @classmethod
    def setUpClass(self):
        self.simple_plain_text = 'teste testando o texto de teste para o trabalho'
        self.simple_cipher_text = 'fccxc fccxyzby s rqvds bq rowrq nkvy a rbezmjrs'

        self.plain_text_file = open('plain_text_test.txt', 'r')
        self.complex_plain_text = self.plain_text_file.read()
        self.cipher_text_file = open('cipher_text_test.txt', 'r')
        self.complex_cipher_text = self.cipher_text_file.read()

    def test_simple_encode(self):
        cipher_text = VigenereCipher.encode(self.key, self.simple_plain_text)
        self.assertEqual(cipher_text, self.simple_cipher_text)

    def test_complex_encode(self):
        cipher_text = VigenereCipher.encode(self.key, self.complex_plain_text)
        self.assertEqual(cipher_text, self.complex_cipher_text)

    def test_simple_decode(self):
        plain_text = VigenereCipher.decode(self.key, self.simple_cipher_text)
        self.assertEqual(plain_text, self.simple_plain_text)

    def test_complex_decode(self):
        plain_text = VigenereCipher.decode(self.key, self.complex_cipher_text)
        self.assertEqual(plain_text, self.complex_plain_text)

    @classmethod
    def tearDownClass(self):
        self.plain_text = self.plain_text_file.close()
        self.cipher_text = self.cipher_text_file.close()


if __name__ == '__main__':
    unittest.main()
