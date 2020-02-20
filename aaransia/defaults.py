from collections import defaultdict
from typing import OrderedDict

# Project directories
BASE_DIR = './aaransia'
DATA_DIR = '/data'
LOG_DIR = '/log'
TEST_DIR = '/test'

# Data sets
ALPHABET = '/alphabet.csv'
DICTIONARY = '/dictionary.csv'

# Test files
TEST_CASES = '/test_cases.csv'

TEST_MOROCCAN_ALPHABET = '/test_moroccan_alphabet.csv'
TEST_MOROCCAN_WORDS = '/test_moroccan_words.csv'

TEST_MOROCCAN_ARABIC_ALPHABET = '/test_moroccan_arabic_alphabet.csv'
TEST_MOROCCAN_ARABIC_WORDS = '/test_moroccan_arabic_words.csv'

TEST_MOROCCAN_TO_LATIN_ALPHABET = '/test_moroccan_to_latin_alphabet.csv'
TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET = '/test_moroccan_arabic_to_latin_alphabet.csv'

# Test logs files
TEST_CASE_LOG_FILE = '/test_case.log'

TEST_MOROCCAN_ALPHABET_LOG_FILE = '/test_moroccan_alphabet.log'
TEST_MOROCCAN_WORDS_LOG_FILE = '/test_moroccan_words.log'

TEST_MOROCCAN_ARABIC_ALPHABET_LOG_FILE = '/test_moroccan_arabic_alphabet.log'
TEST_MOROCCAN_ARABIC_WORDS_LOG_FILE = '/test_moroccan_arabic_words.log'

TEST_MOROCCAN_TO_LATIN_ALPHABET_LOG_FILE = '/test_moroccan_to_latin_alphabet.log'
TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOG_FILE = '/test_moroccan_arabic_to_latin_alphabet.log'

TEST_STATS_LOG_FILE = '/test_stats.log'

# Loggers
TEST_STATS_LOGGER = 'test_stats_logger'
TEST_CASE_LOGGER = 'test_case_logger'

TEST_MOROCCAN_ALPHABET_LOGGER = 'test_moroccan_alphabet_logger'
TEST_MOROCCAN_WORDS_LOGGER = 'test_moroccan_words_logger'

TEST_MOROCCAN_ARABIC_ALPHABET_LOGGER = 'test_moroccan_arabic_alphabet_logger'
TEST_MOROCCAN_ARABIC_WORDS_LOGGER = 'test_moroccan_arabic_words_logger'

TEST_MOROCCAN_TO_LATIN_ALPHABET_LOGGER = 'test_moroccan_to_latin_alphabet_logger'
TEST_MOROCCAN_ARABIC_TO_LATIN_ALPHABET_LOGGER = 'test_moroccan_arabic_to_latin_alphabet_logger'

# Test strings
TEST_CASE = 'Test Case'
EXPECTED_RESULT = 'Expected Result'

# Double Moroccan Letters
DOUBLE_MOROCCAN_LETTERS = ['la', 'kh', 'sh', 'ou', 'gh', 'ch', 'yi', 'ee', 'ss']

# Double Moroccan Arabic Letters
DOUBLE_MOROCCAN_ARABIC_LETTERS = ['كز','كس']

# Alphabet codes
MOROCCAN_ALPHABET_CODE = 'ma'
ARABIAN_ALPHABET_CODE = 'ar'
LATIN_ALPHABET_CODE = 'la'
ABJADI_ALPHABET_CODE = 'ab'
GREEK_ALPHABET_CODE = 'gr'

# Alphabets
MOROCCAN_ALPHABET = 'Moroccan Alphabet'
ARABIAN_ALPHABET = 'Arabian Alphabet'
LATIN_ALPHABET = 'Latin Alphabet'
ABJADI_ALPHABET = 'Abjadi Alphabet'
GREEK_ALPHABET = 'Greek Alphabet'

# Language list
ALPHABETS = {
    MOROCCAN_ALPHABET_CODE: MOROCCAN_ALPHABET,
    ARABIAN_ALPHABET_CODE : ARABIAN_ALPHABET,
    LATIN_ALPHABET_CODE   : LATIN_ALPHABET,
    ABJADI_ALPHABET_CODE  : ABJADI_ALPHABET,
    GREEK_ALPHABET_CODE   : GREEK_ALPHABET
}

# Exceptions
SOURCE_LANGUAGE_EXCEPTION = "Source language doesn't match the input text"

alphabet = [   
    OrderedDict([   ('Moroccan Alphabet', ' '),
                    ('Arabian Alphabet', ' '),
                    ('Latin Alphabet', ' '),
                    ('Abjadi Alphabet', ' '),
                    ('Greek Alphabet', ' ')]),
    OrderedDict([   ('Moroccan Alphabet', '!'),
                    ('Arabian Alphabet', '!'),
                    ('Latin Alphabet', '!'),
                    ('Abjadi Alphabet', '!'),
                    ('Greek Alphabet', '!')]),
    OrderedDict([   ('Moroccan Alphabet', ','),
                    ('Arabian Alphabet', '،'),
                    ('Latin Alphabet', ','),
                    ('Abjadi Alphabet', ','),
                    ('Greek Alphabet', ',')]),
    OrderedDict([   ('Moroccan Alphabet', '.'),
                    ('Arabian Alphabet', '.'),
                    ('Latin Alphabet', '.'),
                    ('Abjadi Alphabet', '.'),
                    ('Greek Alphabet', '.')]),
    OrderedDict([   ('Moroccan Alphabet', '?'),
                    ('Arabian Alphabet', '؟'),
                    ('Latin Alphabet', '?'),
                    ('Abjadi Alphabet', '?'),
                    ('Greek Alphabet', '?')]),
    OrderedDict([   ('Moroccan Alphabet', 'a'),
                    ('Arabian Alphabet', 'ا'),
                    ('Latin Alphabet', 'a'),
                    ('Abjadi Alphabet', 'a'),
                    ('Greek Alphabet', 'α')]),
    OrderedDict([   ('Moroccan Alphabet', 'b'),
                    ('Arabian Alphabet', 'ب'),
                    ('Latin Alphabet', 'b'),
                    ('Abjadi Alphabet', 'b'),
                    ('Greek Alphabet', 'μπ')]),
    OrderedDict([   ('Moroccan Alphabet', 'ch'),
                    ('Arabian Alphabet', 'ش'),
                    ('Latin Alphabet', 'ch'),
                    ('Abjadi Alphabet', 'sh'),
                    ('Greek Alphabet', 'σ')]),
    OrderedDict([   ('Moroccan Alphabet', 'd'),
                    ('Arabian Alphabet', 'د'),
                    ('Latin Alphabet', 'd'),
                    ('Abjadi Alphabet', 'd'),
                    ('Greek Alphabet', 'δ')]),
    OrderedDict([   ('Moroccan Alphabet', 'd'),
                    ('Arabian Alphabet', 'ذ'),
                    ('Latin Alphabet', 'd'),
                    ('Abjadi Alphabet', 'dh'),
                    ('Greek Alphabet', 'δ')]),
    OrderedDict([   ('Moroccan Alphabet', 'd'),
                    ('Arabian Alphabet', 'ض'),
                    ('Latin Alphabet', 'd'),
                    ('Abjadi Alphabet', 'ḍ'),
                    ('Greek Alphabet', 'δ')]),
    OrderedDict([   ('Moroccan Alphabet', 'd'),
                    ('Arabian Alphabet', 'ظ'),
                    ('Latin Alphabet', 'd'),
                    ('Abjadi Alphabet', 'ẓ'),
                    ('Greek Alphabet', 'δ')]),
    OrderedDict([   ('Moroccan Alphabet', 'e'),
                    ('Arabian Alphabet', ' '),
                    ('Latin Alphabet', 'e'),
                    ('Abjadi Alphabet', 'e'),
                    ('Greek Alphabet', 'ε')]),
    OrderedDict([   ('Moroccan Alphabet', 'e'),
                    ('Arabian Alphabet', 'ا'),
                    ('Latin Alphabet', 'e'),
                    ('Abjadi Alphabet', 'e'),
                    ('Greek Alphabet', 'ε')]),
    OrderedDict([   ('Moroccan Alphabet', 'f'),
                    ('Arabian Alphabet', 'ف'),
                    ('Latin Alphabet', 'f'),
                    ('Abjadi Alphabet', 'f'),
                    ('Greek Alphabet', 'φ')]),
    OrderedDict([   ('Moroccan Alphabet', 'g'),
                    ('Arabian Alphabet', 'ڭ'),
                    ('Latin Alphabet', 'g'),
                    ('Abjadi Alphabet', 'g'),
                    ('Greek Alphabet', 'γ')]),
    OrderedDict([   ('Moroccan Alphabet', 'gh'),
                    ('Arabian Alphabet', 'غ'),
                    ('Latin Alphabet', 'gh'),
                    ('Abjadi Alphabet', 'gh'),
                    ('Greek Alphabet', 'γ')]),
    OrderedDict([   ('Moroccan Alphabet', 'h'),
                    ('Arabian Alphabet', 'ه'),
                    ('Latin Alphabet', 'h'),
                    ('Abjadi Alphabet', 'h'),
                    ('Greek Alphabet', 'χ')]),
    OrderedDict([   ('Moroccan Alphabet', 'y'),
                    ('Arabian Alphabet', 'ي'),
                    ('Latin Alphabet', 'y'),
                    ('Abjadi Alphabet', 'y'),
                    ('Greek Alphabet', 'υ')]),
    OrderedDict([   ('Moroccan Alphabet', 'i'),
                    ('Arabian Alphabet', 'ي'),
                    ('Latin Alphabet', 'i'),
                    ('Abjadi Alphabet', 'i'),
                    ('Greek Alphabet', 'ι')]),
    OrderedDict([   ('Moroccan Alphabet', 'ee'),
                    ('Arabian Alphabet', 'ي'),
                    ('Latin Alphabet', 'ee'),
                    ('Abjadi Alphabet', 'y'),
                    ('Greek Alphabet', 'εε')]),
    OrderedDict([   ('Moroccan Alphabet', 'i'),
                    ('Arabian Alphabet', 'ا'),
                    ('Latin Alphabet', 'i'),
                    ('Abjadi Alphabet', 'i'),
                    ('Greek Alphabet', 'ι')]),
    OrderedDict([   ('Moroccan Alphabet', 'j'),
                    ('Arabian Alphabet', 'ج'),
                    ('Latin Alphabet', 'j'),
                    ('Abjadi Alphabet', 'j'),
                    ('Greek Alphabet', 'ζ')]),
    OrderedDict([   ('Moroccan Alphabet', 'k'),
                    ('Arabian Alphabet', 'ك'),
                    ('Latin Alphabet', 'k'),
                    ('Abjadi Alphabet', 'k'),
                    ('Greek Alphabet', 'κ')]),
    OrderedDict([   ('Moroccan Alphabet', 'c'),
                    ('Arabian Alphabet', 'ك'),
                    ('Latin Alphabet', 'c'),
                    ('Abjadi Alphabet', 'c'),
                    ('Greek Alphabet', 'σ')]),
    OrderedDict([   ('Moroccan Alphabet', 'kh'),
                    ('Arabian Alphabet', 'خ'),
                    ('Latin Alphabet', 'kh'),
                    ('Abjadi Alphabet', 'kh'),
                    ('Greek Alphabet', 'χ')]),
    OrderedDict([   ('Moroccan Alphabet', 'l'),
                    ('Arabian Alphabet', 'ل'),
                    ('Latin Alphabet', 'l'),
                    ('Abjadi Alphabet', 'l'),
                    ('Greek Alphabet', 'λ')]),
    OrderedDict([   ('Moroccan Alphabet', 'la'),
                    ('Arabian Alphabet', 'لا'),
                    ('Latin Alphabet', 'la'),
                    ('Abjadi Alphabet', 'la'),
                    ('Greek Alphabet', 'λα')]),
    OrderedDict([   ('Moroccan Alphabet', 'm'),
                    ('Arabian Alphabet', 'م'),
                    ('Latin Alphabet', 'm'),
                    ('Abjadi Alphabet', 'm'),
                    ('Greek Alphabet', 'μ')]),
    OrderedDict([   ('Moroccan Alphabet', 'n'),
                    ('Arabian Alphabet', 'ن'),
                    ('Latin Alphabet', 'n'),
                    ('Abjadi Alphabet', 'n'),
                    ('Greek Alphabet', 'ν')]),
    OrderedDict([   ('Moroccan Alphabet', 'o'),
                    ('Arabian Alphabet', 'و'),
                    ('Latin Alphabet', 'o'),
                    ('Abjadi Alphabet', 'w'),
                    ('Greek Alphabet', 'ο')]),
    OrderedDict([   ('Moroccan Alphabet', 'o'),
                    ('Arabian Alphabet', 'ا'),
                    ('Latin Alphabet', 'o'),
                    ('Abjadi Alphabet', 'o'),
                    ('Greek Alphabet', 'ο')]),
    OrderedDict([   ('Moroccan Alphabet', 'ou'),
                    ('Arabian Alphabet', 'و'),
                    ('Latin Alphabet', 'ou'),
                    ('Abjadi Alphabet', 'w'),
                    ('Greek Alphabet', 'oυ')]),
    OrderedDict([   ('Moroccan Alphabet', 'p'),
                    ('Arabian Alphabet', 'پ'),
                    ('Latin Alphabet', 'p'),
                    ('Abjadi Alphabet', 'p'),
                    ('Greek Alphabet', 'π')]),
    OrderedDict([   ('Moroccan Alphabet', 'q'),
                    ('Arabian Alphabet', 'ق'),
                    ('Latin Alphabet', 'q'),
                    ('Abjadi Alphabet', 'q'),
                    ('Greek Alphabet', 'κ')]),
    OrderedDict([   ('Moroccan Alphabet', 'r'),
                    ('Arabian Alphabet', 'ر'),
                    ('Latin Alphabet', 'r'),
                    ('Abjadi Alphabet', 'r'),
                    ('Greek Alphabet', 'ρ')]),
    OrderedDict([   ('Moroccan Alphabet', 's'),
                    ('Arabian Alphabet', 'س'),
                    ('Latin Alphabet', 's'),
                    ('Abjadi Alphabet', 's'),
                    ('Greek Alphabet', 'σ')]),
    OrderedDict([   ('Moroccan Alphabet', 's'),
                    ('Arabian Alphabet', 'ص'),
                    ('Latin Alphabet', 's'),
                    ('Abjadi Alphabet', 'ṣ'),
                    ('Greek Alphabet', 'σ')]),
    OrderedDict([   ('Moroccan Alphabet', 'ss'),
                    ('Arabian Alphabet', 'ص'),
                    ('Latin Alphabet', 'ss'),
                    ('Abjadi Alphabet', 'ṣ'),
                    ('Greek Alphabet', 'σσ')]),
    OrderedDict([   ('Moroccan Alphabet', 'sh'),
                    ('Arabian Alphabet', 'ش'),
                    ('Latin Alphabet', 'sh'),
                    ('Abjadi Alphabet', 'sh'),
                    ('Greek Alphabet', 'σ')]),
    OrderedDict([   ('Moroccan Alphabet', 't'),
                    ('Arabian Alphabet', 'ت'),
                    ('Latin Alphabet', 't'),
                    ('Abjadi Alphabet', 't'),
                    ('Greek Alphabet', 'τ')]),
    OrderedDict([   ('Moroccan Alphabet', 't'),
                    ('Arabian Alphabet', 'ط'),
                    ('Latin Alphabet', 't'),
                    ('Abjadi Alphabet', 'ṭ'),
                    ('Greek Alphabet', 'τ')]),
    OrderedDict([   ('Moroccan Alphabet', 't'),
                    ('Arabian Alphabet', 'ة'),
                    ('Latin Alphabet', 't'),
                    ('Abjadi Alphabet', 't'),
                    ('Greek Alphabet', 'τ')]),
    OrderedDict([   ('Moroccan Alphabet', 't'),
                    ('Arabian Alphabet', 'ث'),
                    ('Latin Alphabet', 't'),
                    ('Abjadi Alphabet', 'th'),
                    ('Greek Alphabet', 'θ')]),
    OrderedDict([   ('Moroccan Alphabet', 'u'),
                    ('Arabian Alphabet', 'و'),
                    ('Latin Alphabet', 'u'),
                    ('Abjadi Alphabet', 'w'),
                    ('Greek Alphabet', 'oυ    ')]),
    OrderedDict([   ('Moroccan Alphabet', 'v'),
                    ('Arabian Alphabet', 'ڤ'),
                    ('Latin Alphabet', 'v'),
                    ('Abjadi Alphabet', 'v'),
                    ('Greek Alphabet', 'β')]),
    OrderedDict([   ('Moroccan Alphabet', 'w'),
                    ('Arabian Alphabet', 'و'),
                    ('Latin Alphabet', 'w'),
                    ('Abjadi Alphabet', 'w'),
                    ('Greek Alphabet', 'oυ')]),
    OrderedDict([   ('Moroccan Alphabet', 'x'),
                    ('Arabian Alphabet', 'كز'),
                    ('Latin Alphabet', 'x'),
                    ('Abjadi Alphabet', 'x'),
                    ('Greek Alphabet', 'ξ')]),
    OrderedDict([   ('Moroccan Alphabet', 'x'),
                    ('Arabian Alphabet', 'كس'),
                    ('Latin Alphabet', 'x'),
                    ('Abjadi Alphabet', 'x'),
                    ('Greek Alphabet', 'ξ')]),
    OrderedDict([   ('Moroccan Alphabet', 'yi'),
                    ('Arabian Alphabet', 'ي'),
                    ('Latin Alphabet', 'yi'),
                    ('Abjadi Alphabet', 'y'),
                    ('Greek Alphabet', 'υι')]),
    OrderedDict([   ('Moroccan Alphabet', 'z'),
                    ('Arabian Alphabet', 'ز'),
                    ('Latin Alphabet', 'z'),
                    ('Abjadi Alphabet', 'z'),
                    ('Greek Alphabet', 'ζ')]),
    OrderedDict([   ('Moroccan Alphabet', '2'),
                    ('Arabian Alphabet', 'ء'),
                    ('Latin Alphabet', "'"),
                    ('Abjadi Alphabet', 'ʾ'),
                    ('Greek Alphabet', "'")]),
    OrderedDict([   ('Moroccan Alphabet', '3'),
                    ('Arabian Alphabet', 'ع'),
                    ('Latin Alphabet', "'"),
                    ('Abjadi Alphabet', "'"),
                    ('Greek Alphabet', "'")]),
    OrderedDict([   ('Moroccan Alphabet', '5'),
                    ('Arabian Alphabet', 'خ'),
                    ('Latin Alphabet', 'kh'),
                    ('Abjadi Alphabet', 'kh'),
                    ('Greek Alphabet', 'χ')]),
    OrderedDict([   ('Moroccan Alphabet', '7'),
                    ('Arabian Alphabet', 'ح'),
                    ('Latin Alphabet', 'h'),
                    ('Abjadi Alphabet', 'ḥ'),
                    ('Greek Alphabet', 'χ')]),
    OrderedDict([   ('Moroccan Alphabet', '9'),
                    ('Arabian Alphabet', 'ق'),
                    ('Latin Alphabet', 'q'),
                    ('Abjadi Alphabet', 'q'),
                    ('Greek Alphabet', 'κ')])]