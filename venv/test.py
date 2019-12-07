from nltk import pos_tag, wordnet as wn
lemma = wn.WordNetLemmatizer()
w1 = lemma.lemmatize('better', 'a')
w2 = lemma.lemmatize(w1, pos='n')
w3 = lemma.lemmatize(w2, pos='v')

print(w1, w2, w3)