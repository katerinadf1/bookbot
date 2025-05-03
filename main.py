from stats import get_word_count

from stats import get_character_count

from stats import sort_on

from stats import make_count_list

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        text = f.read()
    return text

def main():
    file_contents = get_book_text("books/frankenstein.txt")
    char_dict = get_character_count(file_contents)
    count_list = make_count_list(char_dict)
    count_list.sort(reverse=True, key=sort_on)
    print(f"Found {get_word_count(file_contents)} total words")
    for i in range(len(count_list)):
        print(f"{count_list[i]["char"]}: {count_list[i]["num"]}")
    

main()