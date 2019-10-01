import pickle
end_of_word = "emp"

def in_trie(trie, word):
    current_dict = trie
    for letter in word:
        if letter in current_dict:
            current_dict = current_dict[letter]
        else:
            return False
    if end_of_word in current_dict:
        return True
    else:
        return False
