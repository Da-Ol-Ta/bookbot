from stats import get_num_words, count_each_letter, get_sorted_dict
import sys

def get_book_text(file_path):
    with open(file_path) as f:
        return f.read()
    
def main():
    args = sys.argv
    if len(args) !=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(args[1])
    num_words = get_num_words(book_text)
    letter_count = count_each_letter(book_text)
    sorted_list = get_sorted_dict(letter_count)

    print('============ BOOKBOT ============')
    print('Analyzing book found at books/frankenstein.txt...')
    print('---------- Word Count ----------')
    print(f'Found {num_words} total words')
    print('--------- Character Count -------')
    for item in sorted_list:
        print(f'{item['name']}: {item['num']}')
    print("============= END ===============")


main()