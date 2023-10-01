import unittest

from VigenereCipher import Language, break_cipher, decode, discover_key, encode


class Test(unittest.TestCase):
    key = 'mykey'

    @classmethod
    def setUpClass(self):
        self.simple_plain_text = 'A frequencia de letras em um texto tem sido frequentemente estudada para uso em criptografia e analise de frequencia em particular'
        self.simple_cipher_text = 'M dbiogcxggm bo pcfpkw cy sw xcjry xcy qshm rpousqldikqldi cerehypy zepm scs cy abmnfmqvyrgk i yzyvmqq bo jpqoeilogk ik bybxgosvep'

        self.plain_text_file = open('plain_text_test.txt', 'r')
        self.complex_plain_text = self.plain_text_file.read()
        self.cipher_text_file = open('cipher_text_test.txt', 'r')
        self.complex_cipher_text = self.cipher_text_file.read()

    def test_simple_encode(self):
        cipher_text = encode(self.key, self.simple_plain_text)
        self.assertEqual(cipher_text, self.simple_cipher_text)

    def test_complex_encode(self):
        cipher_text = encode(self.key, self.complex_plain_text)
        self.assertEqual(cipher_text, self.complex_cipher_text)

    def test_simple_decode(self):
        plain_text = decode(self.key, self.simple_cipher_text)
        self.assertEqual(plain_text, self.simple_plain_text)

    def test_complex_decode(self):
        plain_text = decode(self.key, self.complex_cipher_text)
        self.assertEqual(plain_text, self.complex_plain_text)

    def test_discover_key(self):
        self.assertEqual(discover_key(self.complex_cipher_text), self.key)

    def test_discover_key_portuguese(self):
        self.assertEqual(discover_key(self.simple_cipher_text,
                                      Language.PORTUGUES), self.key)

    def test_break_cipher(self):
        plain_text = break_cipher(self.complex_cipher_text)
        self.assertEqual(plain_text, self.complex_plain_text)

    @classmethod
    def tearDownClass(self):
        self.plain_text = self.plain_text_file.close()
        self.cipher_text = self.cipher_text_file.close()


if __name__ == '__main__':
    unittest.main()
