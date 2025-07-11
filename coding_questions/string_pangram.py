import string

def is_pangram(sentence):
    alphabet = set(string.ascii_lowercase)
    return alphabet.issubset(set(sentence.lower()))

text = "The quick brown fox jumps over the lazy dog"
print("Is Pangram : ", is_pangram(text))
