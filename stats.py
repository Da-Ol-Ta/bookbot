def get_num_words(text):
    num_words = len(text.split())
    return num_words

def count_each_letter(text):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    letter_dict = {}
    for letter in alphabet:
        letter_dict[letter] = 0
    
    for letter in text:
        l = letter.lower()
        if l in alphabet:
            letter_dict[l] += 1

    return letter_dict

def get_sorted_dict(count_dict):
    l = []
    for key, value in count_dict.items():
        l.append({'name':key, 'num':value})
    l.sort(reverse=True, key=lambda x: x['num'])
    return l