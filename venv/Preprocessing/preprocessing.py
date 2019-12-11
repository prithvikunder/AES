from Preprocessing.spellcorrector import spellcheck_and_correct
from Preprocessing.stopword_removal import remove_stopwords
from Preprocessing.lemmatization import lemmatize , lemmatize1
from Preprocessing.checkstructures import sentence_proportion, check_punctuations_capitalization
import time

start = time.time()
score = 100
f = open("Dictionary/input.txt", "r")
txt = f.read()
f.close()
essay, score = spellcheck_and_correct(txt, score)
print("Score after spell check: ",score)
print("Essay after spell checking and correction: ",essay)

cleaned_essay, pos_list_punctuations, pos_list_grammar = remove_stopwords(essay, txt)
print("Essay after stopword removal: ", cleaned_essay)

print(pos_list_punctuations)


cleaned_essay = lemmatize(cleaned_essay)
print("Essay after lemmatization: ", cleaned_essay)


score = sentence_proportion(essay, score)
print("Score so far: ", score)

score = check_punctuations_capitalization(pos_list_punctuations, score)

end = time.time()
print(end-start)


