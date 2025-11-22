import sys
from stats import word_count, character_count, sort_dict

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_text = get_book_text(sys.argv[1])
    num_count = word_count(book_text)
    char_count = character_count(book_text)
    sorted_count = sort_dict(char_count)

    print("============ BOOKBOT ============\n"
        f"Analyzing book found at {sys.argv[1]}\n"
        "----------- Word Count ----------\n"
        f"Found {num_count} total words\n"
        "--------- Character Count -------")
    
    for i in sorted_count:
        print(f"{i["char"]}: {i["num"]}")
    
    print("============= END ===============")

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
        return file_contents


main()