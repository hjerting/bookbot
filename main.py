BOOK = "books/frankenstein.txt"

def main():
    text = get_book_text(BOOK)
    word_count = count_words(text)
    letter_counts = count_letters(text)
    make_report(BOOK, word_count, letter_counts)

def make_report(filename, word_count, letter_counts):
    print()
    print(f'--- Begin report of {filename} ---')
    print(f'{word_count} words found in the document')
    print()
    letter_report(letter_counts)
    print('--- End report ---')

def get_book_text(filename):
    with open(filename) as file:
        return file.read()

def count_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    lower_case = text.lower()
    letter_counts = {}
    for letter in lower_case:
        letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def letter_report(character_dict):
    for key, value in character_dict.items():
        if key.isalpha():
            print(f"The '{key}' character was found {value} times")

main()