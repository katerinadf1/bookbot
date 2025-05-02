def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    print(f"{get_word_count(file_contents)} words found in the document")

from stats import get_word_count

main()