import re
import pickle
import enchant
from nltk import pos_tag, wordnet as wn
from porter2stemmer import Porter2Stemmer
from Dictionary.usedictionary import in_trie, find_correct_words
from nltk.corpus import wordnet
import time

start = time.time()

def is_number(n):
    try:
        int(n)
        return True
    except ValueError:
        return False

def get_wordnet_pos(tag):
    if tag.startswith('J'):
        return wordnet.ADJ
    elif tag.startswith('V'):
        return wordnet.VERB
    elif tag.startswith('N'):
        return wordnet.NOUN
    elif tag.startswith('R'):
        return wordnet.ADV
    else:
        return ''


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
essay = [el.lower() for el in essay]
#Checking for words
for i in range(len(essay)):
    el = essay[i]
    if '@' not in el and is_number(el)==False:
        isthere = in_trie(trie, el)
        if(isthere==False):
            misswords.append(el)
            incorrect_index.append(i)
            incorrect+=1
#print(misswords)
#Deduct scores here
if incorrect>0 and incorrect<=4:
    score-=3
elif(incorrect>4 and incorrect<=14):
    score-=2*(incorrect-4)
else:
   score-=20

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
#Replacement done

#Remove stopwords and stemming
useless_tags = ['DT', 'PRP', 'PRP$', 'EX', 'IN', 'CC', 'CD', 'TO', 'WP$', 'WP', 'UH', 'WRB', 'MD']
lemma = wn.WordNetLemmatizer()
pos_list = pos_tag(essay)
print(pos_list)
incorrect=0
#print(pos_list)
for word in pos_list:
    ind = essay.index(word[0])
    if word[1] in useless_tags:
        essay.remove(word[0])
        #pos_list.remove(word)       #Refined pos list can be used later in grammar check
    else:
        essay[ind] = lemma.lemmatize(word[0], get_wordnet_pos(word[1]))
        if in_trie(trie, essay[ind])==False and word[1]!='NNP' and word[0][0]!="@":
            essay.remove(essay[ind])
            incorrect+=1
print(essay)
print(score)

## sentence vectors
# list to store each sentence
sentences = []
line = ''
# list to store number of letters in each sentence
word_count = []
count = 0
for letter in txt:
    if letter == '.':
        sentences.append(line)
        word_count.append(count)
        line = ''
        count = 0
    else:
        if letter == ' ':
            count += 1
        line += letter

# print(sentences)
print(word_count)
end = time.time()
print(end-start)