import unittest

from VigenereCipher import VigenereCipher


class Test(unittest.TestCase):
    key = 'mykey'
    cipher = VigenereCipher(key)

    @classmethod
    def setUpClass(self):
        self.plain_text_file = open('plain_text_test.txt', 'r')
        self.plain_text = self.plain_text_file.read()
        self.cipher_text_file = open('cipher_text_test.txt', 'r')
        self.cipher_text = self.cipher_text_file.read()

    @classmethod
    def tearDownClass(self):
        self.plain_text = self.plain_text_file.close()
        self.cipher_text = self.cipher_text_file.close()

    def test_encode1(self):
        plain_text = 'teste testando o texto de teste para o trabalho'
        cipher_text = 'fccxc fccxyzby s rqvds bq rowrq nkvy a rbezmjrs'
        self.assertEqual(self.cipher.encode(plain_text), cipher_text)

    def test_encode2(self):
        self.assertEqual(self.cipher.encode(self.plain_text), self.cipher_text)

    def test_decode(self):
        plain_text = 'teste testando o texto de teste para o trabalho'
        cipher_text = 'fccxc fccxyzby s rqvds bq rowrq nkvy a rbezmjrs'
        self.assertEqual(self.cipher.decode(cipher_text), plain_text)


if __name__ == '__main__':
    unittest.main()
