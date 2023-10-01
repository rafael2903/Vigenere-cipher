# Vigenere Cipher

## Description

This is a simple implementation of the Vigenere Cipher in Python. It is a polyalphabetic cipher that uses a key to encrypt and decrypt a message. The key is a word or phrase that is repeated until it is the same length as the message. The key is then used to shift the letters of the message to create the ciphertext. The ciphertext can then be decrypted by shifting the letters back to their original positions. The program can also break the cipher text using the Kasiski Examination.

## Module Usage

```python
from vigenere import Language, break_cipher, decode, encode

# Encoding
encoded_text = encode("key", "plain text")

# Decoding
decoded_text = decode("key", "cipher text")

# Breaking
decoded_text = break_cipher("cipher text", Language.ENGLISH)

```

## CLI Usage

```bash
usage: vigenere.py [-h] -i INPUT_FILE [-o OUTPUT_FILE] [-e] [-d] [-b] [-k KEY] [-l {ENGLISH,PORTUGUES}]

options:
  -h, --help            show this help message and exit
  -i INPUT_FILE, --input_file INPUT_FILE
  -o OUTPUT_FILE, --output_file OUTPUT_FILE
  -e, --encode
  -d, --decode
  -b, --break
  -k KEY, --key KEY
  -l {ENGLISH,PORTUGUES}, --language {ENGLISH,PORTUGUES}
```

### Examples

#### Encoding

```bash
$ python vigenere.py -e -i plain_text.txt -o cipher_text.txt -k "key"
```

#### Decoding

```bash
$ python vigenere.py -d -i cipher_text.txt -o plain_text.txt -k "key"
```

#### Breaking

```bash
$ python vigenere.py -b -i cipher_text.txt -o plain_text.txt -l PORTUGUES
```

## API

### encode(key, plain_text)

Encodes the plain text using the key.

#### Parameters

-   `key` - The key to be used to encode the plain text.
-   `plain_text` - The plain text to be encoded.

#### Returns

The encoded text.

### decode(key, cipher_text)

Decodes the cipher text using the key.

#### Parameters

-   `key` - The key to be used to decode the cipher text.
-   `cipher_text` - The cipher text to be decoded.

#### Returns

The decoded text.

### break_cipher(cipher_text, language)

Breaks the cipher text using the language.

#### Parameters

-   `cipher_text` - The cipher text to be decoded.

-   `language` - The language of the cipher text, used to analyze the frequency of the letters and break the cipher. It can be `Language.ENGLISH` or `Language.PORTUGUES`. The default value is `Language.ENGLISH`.

#### Returns

The decoded text.

## Test

```bash
$ python -m unittest -v tests.py
```
