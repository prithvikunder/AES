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
    lastFullStop = -1

    for i in range(len(pos_list)):
        if pos_list[i][1][0] == 'V':
            hasSeenVerb = True

        if pos_list[i][0] == '.':
            lastFullStop = i
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

        if pos_list[i][0] == ',':
            if i==0 or i==len(pos_list)-1:
                mistakes+=1
            else:
                isJustified = False
                if pos_list[i+1][1] == pos_list[i-1][1] and pos_list[i+1][1][0]=='J':
                    isJustified = True
                elif pos_list[i+1][1][0] == pos_list[i-1][1][0] == 'N' and i+1!=len(pos_list)-1:
                    isJustified = True
                elif pos_list[i+1][1] == 'CC':
                    isJustified = True
                elif pos_list[i+1][0] in ['which', '"']:
                    isJustified = True
                elif pos_list[i+1][0][0] == 'W':
                    isJustified = True
                elif '.' in pos_list[i-2:i+3][0]:
                    isJustified = True
                if(isJustified==False):
                    print(pos_list[i-2:i+3])
                    mistakes+=1

        if pos_list[i][0] == '?':
            if lastFullStop == -1:
                if(pos_list[0][0][0]=='W')

    if pos_list[len(pos_list)-1][0] != '.' or hasSeenVerb == False:
        mistakes += 1
    print('Mistakes: ', mistakes)
    return score