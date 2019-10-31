import re
import pickle
import enchant
from nltk import pos_tag, wordnet as wn
from Dictionary.usedictionary import in_trie, find_correct_words
from nltk.corpus import wordnet, stopwords
from nltk.tokenize import word_tokenize 
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


f = open("Dictionary/input2.txt", "r")
txt = f.read()
f.close()
essay = re.findall(r"@?\w+", txt)
# print(essay)

end_of_word = 'emp'
incorrect = 0
score = 100
with open("Dictionary/savedict.txt", "rb") as myFile:
    trie = pickle.load(myFile)

misswords = []
incorrect_index = []

# converting to lower case
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
print('incorrect spelling')
print(misswords)
print('no of incorrect words:', incorrect)
print()

#Deduct scores here
if incorrect>0 and incorrect<=4:
    score-=3
elif(incorrect>4 and incorrect<=14):
    score-=2*(incorrect-4)
else:
    score-=20

print(score)
#Find correct replacement for words
#to_use_dict = input("Enter the dictionary (US or UK): ")
to_use_dict = "US"
if to_use_dict.upper() == "US":
    dictionaryUS = enchant.Dict("en_US")
    corrected_words = find_correct_words(misswords, dictionaryUS)
else:
    dictionaryUK = enchant.Dict("en_UK")
    corrected_words = find_correct_words((misswords,dictionaryUK))

print('closest corrected words')
print(corrected_words)
print()

for i in range(len(corrected_words)):
    essay[incorrect_index[i]] = corrected_words[i]
#Replacement done

#Remove stopwords and lemmatize
useless_tags = {'DT', 'PRP', 'PRP$', 'EX', 'IN', 'CC', 'CD', 'TO', 'WP$', 'WP', 'UH', 'WRB', 'MD'}
lemma = wn.WordNetLemmatizer()
pos_list = pos_tag(essay)
# print(pos_list)
# print()


# set of stop words
stop_words = set(stopwords.words('english')) 

# tokens of words  
word_tokens = word_tokenize(txt) 
    
filtered_sentence = [] 
  
for w in word_tokens: 
    if w not in stop_words: 
        filtered_sentence.append(w) 



print("\n\nOriginal Sentence \n\n")
print(" ".join(word_tokens)) 

print("\n\nFiltered Sentence \n\n")
print(" ".join(filtered_sentence)) 

'''
incorrect=0
for word in pos_list:
    ind = essay.index(word[0])
    if word[1] in useless_tags:
        essay.remove(word[0])
        #pos_list.remove(word)       #Refined pos list can be used later in grammar check
    # else:
    #     essay[ind] = lemma.lemmatize(word[0], get_wordnet_pos(word[1]))
    #     if in_trie(trie, essay[ind])==False and word[1]!='NNP' and word[0][0]!="@":
    #         essay.remove(essay[ind])
    #         incorrect+=1'''

lemma_word = []
for w in filtered_sentence:
    word1 = lemma.lemmatize(w, pos = "n")
    word2 = lemma.lemmatize(word1, pos = "v")
    word3 = lemma.lemmatize(word2, pos = ("a"))
    lemma_word.append(word3)

print()
print('lemmatization')
print(lemma_word)

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
# print(word_count)
end = time.time()
print(end-start)