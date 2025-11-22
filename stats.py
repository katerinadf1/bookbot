def word_count(text):
    words = text.split()
    return len(words)

def character_count(text):
    character = {}
    char_list = list(text)
    for i in char_list:
        if i.lower() in character:
            character[i.lower()] += 1
        else:
            character[i.lower()] = 1
    return character

def sort_on(items):
    return items["num"]

def sort_dict(char_dict):
    char_list = []
    for key, value in char_dict.items():
        if key.isalpha():
            new_dict = {"char": key, "num":value}
            char_list.append(new_dict)
        continue
    char_list.sort(reverse=True, key=sort_on)
    return char_list