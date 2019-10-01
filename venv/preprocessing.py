import re
import pickle
import enchant
from Dictionary.usedictionary import in_trie

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

f = open("Dictionary\input.txt", "r")
txt = f.read()
x = re.findall(r"@?\w+", txt)
end_of_word = 'emp'
incorrect = 0
print(x)
with open("Dictionary/savedict.txt", "rb") as myFile:
    trie = pickle.load(myFile)

misswords = []
for el in x:
    if '@' not in el and is_number(el)==False:
        isthere = in_trie(trie, el.lower())
        if(isthere==False):
            misswords.append(el.lower())
            incorrect+=1

print(misswords)
print(incorrect)
