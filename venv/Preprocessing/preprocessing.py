from Preprocessing.spellcorrector import spellcheck_and_correct
from Preprocessing.stopword_removal import remove_stopwords
from Preprocessing.lemmatization import lemmatize , lemmatize1
import time

start = time.time()
score = 100
f = open("Dictionary/input.txt", "r")
txt = f.read()
f.close()
essay, score = spellcheck_and_correct(txt, score)
print("Score after spell check: ",score)
print("Essay after spell checking and correction: ",essay)

essay, pos_list_punctuations, pos_list_grammar = remove_stopwords(essay, txt)
print("Essay after stopword removal: ", essay)

essay = lemmatize(essay)
print("Essay after lemmatization: ", essay)
end = time.time()
print(end-start)


