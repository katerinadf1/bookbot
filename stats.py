def get_word_count(word_count):
    word_list = word_count.split()
    return len(word_list)

def get_character_count(text):
    character_count = {}
    for i in text:
        if i.lower() in character_count:
            character_count[i.lower()] += 1
        else:
            character_count[i.lower()] = 1
    return character_count