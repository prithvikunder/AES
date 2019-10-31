import re
from nltk import pos_tag

f = open("Dictionary/input2.txt", "r")
txt = f.read()
essay = re.findall(r"@?\w+", txt)
f.close()

pos_list = pos_tag(essay)
print(pos_list)

# full-stops
split = txt.split(')
print(split)


