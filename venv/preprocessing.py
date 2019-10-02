import re
import pickle
import enchant
from nltk import pos_tag, wordnet
from Dictionary.usedictionary import in_trie, find_correct_words

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False


f = open("Dictionary\input.txt", "r")
txt = f.read()
essay = re.findall(r"@?\w+", txt)
end_of_word = 'emp'
incorrect = 0
score = 100
with open("Dictionary/savedict.txt", "rb") as myFile:
    trie = pickle.load(myFile)

misswords = []
incorrect_index = []

#Checking for words
for el in essay:
    if '@' not in el and is_number(el)==False:
        isthere = in_trie(trie, el.lower())
        if(isthere==False):
            misswords.append(el.lower())
            incorrect_index.append(essay.index(el))
            incorrect+=1
#print(misswords)
#Deduct scores here
if(incorrect>4):
    score-=2*incorrect

#Find correct replacement for words
#to_use_dict = input("Enter the dictionary (US or UK): ")
to_use_dict = "US"
if to_use_dict.upper() == "US":
    dictionaryUS = enchant.Dict("en_US")
    corrected_words = find_correct_words(misswords, dictionaryUS)
else:
    dictionaryUK = enchant.Dict("en_UK")
    corrected_words = find_correct_words((misswords,dictionaryUK))

#print(corrected_words)
for i in range(len(corrected_words)):
    essay[incorrect_index[i]] = corrected_words[i]
#print(essay)
#Replacement done

#Remove stopwords and stemming
print(essay)
useless_tags = ['DT', 'PRP', 'PRP$', 'EX', 'IN', 'CC', 'CD', 'TO', 'WP$', 'WP', 'UH']
lemma = wordnet.WordNetLemmatizer()
pos_list = pos_tag(essay)
#print(pos_list)
for word in pos_list:
    if word[1] in useless_tags:
        essay.remove(word[0])
        #pos_list.remove(word)       #Refined pos list can be used later in grammar check
    else:
        print(essay[essay.index(word[0])])
        print(lemma.lemmatize(word[0]))
        essay[essay.index(word[0])] = lemma.lemmatize(word[0])

print(essay)
