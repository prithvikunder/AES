def sentence_proportion(essay, score):
    punctuations = ["'", '"', '.', ',', '?', '!']
    ct = 0
    mistakes = 0
    for word in essay:
        if(word=='.'):
            if(ct<8 or ct>20):
                mistakes+=1
            ct = 0
        else:
            if word not in punctuations:
                ct+=1
    if mistakes>20:
        score-=20
    else:
        score-=mistakes
    return score


def check_punctuations_capitalization(pos_list, score):
    punctuations = ["'", '"', '.', ',', '?', '!']
    mistakes = 0
    hasSeenVerb = False
    nextCapital = False

    for i in range(len(pos_list)):
        if pos_list[i][1][0] == 'V':
            hasSeenVerb = True

        if pos_list[i][0] == '.':
            #Check for capitalization
            if  i!= len(pos_list)-1:
                if pos_list[i+1][0].islower() and pos_list[i+1][0][0]!='@':
                    nextCapital = False
                else:
                    nextCapital = True

                if hasSeenVerb == False or nextCapital == False:
                    print(pos_list[i+1])
                    mistakes+=1
                else:
                    if pos_list[i+1][1] in ['NNP', 'NNPS']:
                        j=i+1
                        verbInside = False
                        while(pos_list[j][0]!='.'):
                            if pos_list[j][1][0] == 'V':
                                verbInside = True
                                break
                            j+=1
                        if verbInside == False:
                            mistakes+=1

                hasSeenVerb = False
                nextCapital = False
    if pos_list[len(pos_list)-1][0] != '.' or hasSeenVerb == False:
        mistakes += 1
    print('Mistakes: ', mistakes)
    return score