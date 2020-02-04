import language_check
import unicodedata

def form_sentences(pos_list):
    temp = []
    sentences_tags = []
    for el in pos_list:
        if el[0]!='.':
            temp.append(el[1])
        else:
            sentences_tags.append(temp)
            temp = []
    return sentences_tags


def sentence_structure_errors(pos_list_grammar, score):
    tags_in_sentences = form_sentences(pos_list_grammar)
    print(tags_in_sentences)



def grammar_check1(essay, score):
    tool = language_check.LanguageTool('en-US')
    str1 = " "
    str2 = str1.join(essay)
    mistakes = tool.check(str2)
    error=0
    for each_mistake in mistakes:
        if each_mistake.ruleId not in ['COMMA_PARENTHESIS_WHITESPACE', 'EN_QUOTES', 'EN_UNPAIRED_BRACKETS']:
            print(each_mistake)
            error+=1
    print(error)
    #print(language_check.correct(str2, mistakes))
    return score - len(mistakes)