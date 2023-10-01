import re
from argparse import ArgumentParser
from collections import Counter
from enum import Enum


class Mode(Enum):
    ENCODE = 'encode'
    DECODE = 'decode'


class Language(Enum):
    ENGLISH = 'english'
    PORTUGUES = 'português'


letters_frequencies = {
    Language.ENGLISH: {
        'a': 0.0817, 'b': 0.0149, 'c': 0.0278, 'd': 0.0425,
        'e': 0.1270, 'f': 0.0223, 'g': 0.0202, 'h': 0.0609,
        'i': 0.0697, 'j': 0.0015, 'k': 0.0077, 'l': 0.0403,
        'm': 0.0241, 'n': 0.0675, 'o': 0.0751, 'p': 0.0193,
        'q': 0.0010, 'r': 0.0599, 's': 0.0633, 't': 0.0906,
        'u': 0.0276, 'v': 0.0098, 'w': 0.0236, 'x': 0.0015,
        'y': 0.0197, 'z': 0.0007
    },
    Language.PORTUGUES: {
        'a': 0.1463, 'b': 0.0104, 'c': 0.0388, 'd': 0.0499,
        'e': 0.1257, 'f': 0.0102, 'g': 0.0130, 'h': 0.0128,
        'i': 0.0618, 'j': 0.0040, 'k': 0.0002, 'l': 0.0278,
        'm': 0.0474, 'n': 0.0505, 'o': 0.1073, 'p': 0.0252,
        'q': 0.0120, 'r': 0.0653, 's': 0.0781, 't': 0.0434,
        'u': 0.0463, 'v': 0.0167, 'w': 0.0001, 'x': 0.0021,
        'y': 0.0001, 'z': 0.0047,
    }
}


def encode(key: str, plain_text: str):
    return translate(key, plain_text, Mode.ENCODE)


def decode(key: str, cipher_text: str):
    return translate(key, cipher_text, Mode.DECODE)


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


def is_valid_letter(letter):
    return letter.isalpha() and letter.isascii()


def translate(key: str, text: str, mode: str):
    key_stream = pad_key(key, text)
    translated_text = ''
    i = 0

    for letter in text:
        if not is_valid_letter(letter):
            translated_text += letter
            continue

        base_char_code = ord('a') if letter.islower() else ord('A')
        key_letter = key_stream[i]
        key_letter_position = ord(key_letter) - ord('a')
        letter_position = ord(letter) - base_char_code

        if mode is Mode.ENCODE:
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

def find_repeated_groups(text: str):
    repeated_groups = dict()
    MIN_REPETITIONS = 2 if len(text) < 200 else 3
    MIN_GROUP_LENGTH = 3 if len(text) < 200 else 5
    i = 0

    while (i < len(text)):
        j = i + 1
        last_matches = None
        while (j < len(text)):
            search_string = text[i:j]
            matches_index = [m.start()
                             for m in re.finditer(search_string, text)]
            if len(matches_index) >= MIN_REPETITIONS:
                last_matches = (search_string, matches_index)
            elif last_matches:
                group, indexes = last_matches
                if group not in repeated_groups and len(group) >= MIN_GROUP_LENGTH:
                    repeated_groups[group] = indexes
                break
            else:
                break
            j += 1
        i = j
    return repeated_groups


def find_key_length(cipher_text: str):
    repeated_groups = find_repeated_groups(cipher_text)
    matches_index = repeated_groups.values()
    distances = [b - a for indexes in matches_index for a,
                 b in zip(indexes, indexes[1:])]

    def find_divisors(number):
        return [i for i in range(2, number + 1) if number % i == 0]

    divisor_counts = Counter()
    for distance in distances:
        divisor_counts.update(find_divisors(distance))

    most_common_divisors = divisor_counts.most_common(3)

    if len(most_common_divisors):
        key_length, _count = max(
            most_common_divisors, key=lambda x: (x[1], x[0]))
        return key_length


def calculate_letter_frequencies(text):
    letter_count = Counter(text)
    total_letters = len(text)
    frequencies = {letter: count / total_letters for letter,
                   count in letter_count.items()}
    return frequencies


def discover_caesar_shift(cipher_text, language: Language):
    cipher_text_frequencies = calculate_letter_frequencies(
        cipher_text)

    best_shift = None
    best_score = float('inf')

    for shift in range(26):
        shifted_frequencies = {}
        for letter, frequency in cipher_text_frequencies.items():
            shifted_letter = chr(
                ((ord(letter) - ord('a') - shift) % 26) + ord('a'))
            shifted_frequencies[shifted_letter] = frequency

        score = sum((shifted_frequencies.get(letter, 0) - english_frequency)**2
                    for letter, english_frequency in letters_frequencies[language].items())

        if score < best_score:
            best_score = score
            best_shift = shift
    return best_shift


def discover_key(cipher_text: str, language=Language.ENGLISH):
    cleaned_cipher_text: str = (''.join(filter(
        is_valid_letter, cipher_text))).lower()

    key_length = find_key_length(cleaned_cipher_text)

    if not key_length:
        return

    caesar_cipher_texts = ['' for i in range(key_length)]

    for i in range(0, len(cleaned_cipher_text), key_length):
        for j in range(key_length):
            if i + j < len(cleaned_cipher_text):
                caesar_cipher_texts[j] += cleaned_cipher_text[i+j]

    key_shifts = [discover_caesar_shift(text, language)
                  for text in caesar_cipher_texts]

    key = ''.join(map(lambda shift: chr((ord('a') + shift)), key_shifts))
    return key


def break_cipher(cipher_text: str, language=Language.ENGLISH):
    key = discover_key(cipher_text, language)
    if not key:
        return
    return decode(key, cipher_text)


if __name__ == '__main__':
    parser = ArgumentParser()
    parser.add_argument('-i', '--input_file', type=str, required=True)
    parser.add_argument('-o', '--output_file', type=str, default='result.txt')
    parser.add_argument(
        '-e', '--encode', action='store_true', dest='encode_flag')
    parser.add_argument(
        '-d', '--decode', action='store_true', dest='decode_flag')
    parser.add_argument(
        '-b', '--break', action='store_true', dest='break_flag')
    parser.add_argument('-k', '--key', type=str)
    parser.add_argument('-l', '--language', type=str, choices=[
                        Language.ENGLISH.name, Language.PORTUGUES.name], default=Language.ENGLISH.name)
    args = parser.parse_args()

    input_file = args.input_file
    output_file = args.output_file
    encode_flag = args.encode_flag
    decode_flag = args.decode_flag
    break_flag = args.break_flag
    key = args.key
    language = Language[args.language]

    with open(input_file) as f:
        text = f.read()
        output_file = open(output_file, 'w')

        if break_flag:
            key = discover_key(text, language)
            if key:
                print('key found:', key)
                plain_text = decode(key, text)
                output_file.write(plain_text)
                print('Decoded text saved into', output_file.name)
            else:
                print('Unable to break the cipher')
        elif encode_flag:
            if key:
                cipher_text = encode(key, text)
                output_file.write(cipher_text)
                print('Encoded text saved into', output_file.name)
            else:
                print('Key parameter is missing')
        elif decode_flag:
            if key:
                plain_text = decode(key, text)
                output_file.write(plain_text)
                print('Decoded text saved into', output_file.name)
            else:
                print('Key parameter is missing')
        else:
            print('Choose an option (--encode, --decode, --break)')

        output_file.close()
