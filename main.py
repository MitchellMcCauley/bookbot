from stats import word_counter, letter_counter, sort_letter_dicts
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

filepath = sys.argv[1]

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def main():
    file_contents = get_book_text(filepath)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")
    # Example: count words
    num_words = word_counter(file_contents)
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    letter_counts = letter_counter(file_contents)
    print("--------- Character Count -------")    
    sorted_letters = sort_letter_dicts(letter_counts)
    for item in sorted_letters:
        print(f"{item['char']}: {item['num']}")
    print("============= END ===============")

main()