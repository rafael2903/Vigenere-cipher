# plain_text = 'teste testando o texto de teste para o trabalho'
# key = 'mysupersecretkey'

plain_text = 'joao e o pe de feijao ana'
key = 'mykey'

plain_text_size = len(plain_text)
key_size = len(key)

if key_size >= plain_text_size:
    key_stream = key[:plain_text_size]
else:
    key_full_repetitions = plain_text_size // key_size
    key_remaining_letters = plain_text_size % key_size
    key_stream = key * key_full_repetitions
    key_stream += key[:key_remaining_letters]

print(key_stream)
