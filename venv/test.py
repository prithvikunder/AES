import nltk

grammar = nltk.CFG.fromstring("""
  S -> NP VP
  NP -> DT NP1 VP4 | pronoun NP4 | DT NP6 | DT NP7 | propernoun NP3 | noun
  VP -> V NP | V NP PP
  PP -> P NP
  V -> "saw" | "ate" | "walked"
  Det -> "a" | "an" | "the" | "my"
  N -> "man" | "dog" | "cat" | "telescope" | "park"
  P -> "in" | "on" | "by" | "with"
  noun -> 'NN' | 'NNS' | 'POS'
  propernoun -> 'NNP' | 'NNPS' | 'POS'
  DT -> 'DT' | 'WDT'
  adjective -> 'JJ' | 'JJR' | 'JJS'
  adverb -> 'RB' | 'RBR' | 'RBS'
  conjunction -> 'IN' | 'CC'
  prep -> 'IN'
  pronoun -> 'PRP' | 'PRP$'
  """)

sent = "Mary saw Bob".split()
rd_parser = nltk.RecursiveDescentParser(grammar1).parse(sent)
result = set(tree.freeze() for tree in rd_parser)
print(len(result))
