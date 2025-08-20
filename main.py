import sys
from stats import get_num_words

# BOOK = "books/frankenstein.txt"

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    BOOK = sys.argv[1]
    text = get_book_text(BOOK)
    word_count = get_num_words(text)
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

def count_letters(text):
    lower_case = text.lower()
    letter_counts = {}
    for letter in lower_case:
        if letter.isalpha():
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
    return letter_counts

def letter_report(character_dict):
    sorted_items = sorted(character_dict.items(), key=lambda item: item[1], reverse=True)
    for key, value in sorted_items:
        if key.isalpha():
            print(f"{key}: {value}")

if __name__ == "__main__":
    main()