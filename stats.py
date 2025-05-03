def get_word_count(word_count):
    word_list = word_count.split()
    return len(word_list)

def get_character_count(text):
    character_count = {}
    for i in text:
        if i.isalpha():
            if i.lower() in character_count:
                character_count[i.lower()] += 1
            else:
                character_count[i.lower()] = 1
    return character_count

def sort_on(dict):
    return dict["num"]

def make_count_list(dict):
    count_list = []
    for i in dict:
        count_list.append({"char": i, "num": dict[i]})
    return count_list