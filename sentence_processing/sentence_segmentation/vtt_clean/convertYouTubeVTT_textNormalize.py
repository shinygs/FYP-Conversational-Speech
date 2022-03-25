# -*- coding: utf-8 -*-
"""
convertYouTubeVTT_withNewTiming
This is a script to read youtube vtt and 
1) remove the rubbish so that its a proper vtt file w/o the repeating sentences as it scroll up
2) find the best break point using the timing provided

Author: chng Eng Siong
16 April 2020
revised: changed format output to allow VLC player to use

"""
import re
from nltk.tokenize import RegexpTokenizer


# This form sentence tries to find the end of sentence.
# given index i -> which word we are exploring now.
def formSentence(i,allListWordsTime):

    if i >= len(allListWordsTime):
        return(['','','',i+1])

    # Lets form the first word    
    elem    = allListWordsTime[i]  
    stTime  = elem[0]
    endTime = elem[1]
    totalDuration = elem[2]        
    retSent = elem[3]+' '
    numWords = 1
    exitFlag = 0
    if (elem[2] > 3):  # this single word is LONG enough!
        exitFlag = 1

    # else lets progress
    i=i+1  # next word
    readyToExit = 0
    while (i<len(allListWordsTime) and exitFlag == 0):
       elem = allListWordsTime[i]  
       totalDuration += elem[2]
       numWords = numWords+1

    
       # we will NOT use a word when the duration is long, or when the addition of it
       #causes it to 
       #if (readyToExit == 1 and elem[2] > 1) or (elem[2]>3) or (numWords>12):
       if ((numWords>5 and (numWords<8)) and elem[2] > 1.5) or  ( (numWords>8 and numWords<15) and elem[2] > 0.5) or (numWords>13 and elem[2] > 0.3) or numWords>15:
          exitFlag = 1  # Lets NOT use this word
       else:
          # we shall use the word
          retSent = retSent+elem[3]+' '
          endTime = elem[1]
          i=i+1
        
    stTime  =  re.sub('<|>', '', stTime)
    endTime =  re.sub('<|>', '', endTime)
    return([retSent,stTime,endTime,i])



def formSingleWord(i,allListWordsTime):

    if i >= len(allListWordsTime):
        return(['','','',i+1])

    # Lets form the first word    
    elem    = allListWordsTime[i]  
    stTime  = elem[0]
    endTime = elem[1]
    totalDuration = elem[2]        
    retSent = elem[3]+elem[1]+' '
    numWords = 1
    exitFlag = 0
    if (elem[2] > 3):  # this single word is LONG enough!
        exitFlag = 1

    # else lets progress
    i=i+1  # next word
    readyToExit = 0
    while (i<len(allListWordsTime) and exitFlag == 0):
       elem = allListWordsTime[i]  
       totalDuration += elem[2]
       numWords = numWords+1

    
       # we will NOT use a word when the duration is long, or when the addition of it
       #causes it to 
       #if (readyToExit == 1 and elem[2] > 1) or (elem[2]>3) or (numWords>12):
       if ((numWords>5 and (numWords<8)) and elem[2] > 1.5) or  ( (numWords>8 and numWords<15) and elem[2] > 0.5) or (numWords>13 and elem[2] > 0.3) or numWords>15:
          exitFlag = 1  # Lets NOT use this word
       else:
          # we shall use the word
          retSent = retSent+elem[3]+elem[1]+' '
          endTime = elem[1]
          i=i+1
        
    stTime  =  re.sub('<|>', '', stTime)
    endTime =  re.sub('<|>', '', endTime)
    return([retSent,stTime,endTime,i])




def  generate_newTranscriptBreak(opFileName, allListWordsTime):
    numWords = len(allListWordsTime)
    
    opfp = open(opFileName,"w")
    opfp.write('WEBVTT\n')
    opfp.write('Kind: captions\n')
    opfp.write('Language: en\n\n')

    i = 0
    while (i+1<len(allListWordsTime)):
        #[retSent,stTime,endTime,i] = formSentence(i,allListWordsTime)
        [retSent,stTime,endTime,i] =  formSingleWord(i,allListWordsTime)
        if retSent != '':
            opStr = stTime+' --> '+endTime+'  align:start position:0\n'+retSent+'\n\n\n'
            opfp.write(opStr)
        
    opfp.close()
    

def  checkVTT_tokenList(listVTTTokens):
     stTime = ''
     endTime = ''
     numElement = len(listVTTTokens)
     #print('P5: numTokens =', numElement)    
     i = 0
     retTokenList  = [] 
     while (i<numElement):
         val = listVTTTokens[i]
         if stTime == '' and re.match('\<[\d+:.]+\>',val):
             stTime = val
             foundWordStr = ''
             while (i+1< numElement): 
                 nextelem = listVTTTokens[(i + 1)]
                 #print('5A2b')
                 # of we found a date, it should be the end date, lets collect the terms
                 if re.match('\<[\d+:.]+\>',nextelem):
                     endTime = nextelem    
                     #print('5A2c: word FOUND == ('+foundWordStr+') with time='+stTime+' --> '+endTime)
                     time1 = getTimeFromStr(stTime)
                     time2 = getTimeFromStr(endTime)
                     difftime = round(time2-time1,4)
                     retTokenList.append([stTime,endTime,difftime, foundWordStr])
                     stTime = ''
                     break
                 else:
                     # we are concatenating strings to form foundWordStr
                     foundWordStr=foundWordStr+nextelem
                     i=i+1
                     #print('5A2d=',foundWordStr)
                                  
         i=i+1  
     # this returns a list, where each entry has 4 elements ([stTime,endTime,difftime, foundWordStr]))
     return(retTokenList)
 

def  parseVTT(inVTTLine, stTime, endTime):
     #print("input = ",inVTTLine)
     p1 = re.sub('<c>|</c>|\n'," ",inVTTLine)    
     #print("P1 = ",p1)
     p2 = '<'+stTime+'> '+p1+' '+'<'+endTime+'>'
     # lets parse the token , stTime,word,endTime  (repeat)
     # lets parse the token , <hh:mm:ss.mmm> word <hh:mm:ss.mmm> (repeat)
     tokenizer = RegexpTokenizer("\<[\d+:.]+\>+|\[\w+\]|\w+'\w+|\w+")
     # practise your regex here: https://www.regexpal.com/?fam=99404
     p3 = tokenizer.tokenize(p2)
     # lets be paranoid and join all tokens not with left/right as time together
     p4 = checkVTT_tokenList(p3)
     return(p4)
     
     

def getTimeFromStr(inTimeStr):
    inTimeStr = re.sub('[<>]', ' ', inTimeStr)
    [hours1, minutes1, seconds1,subsecond1] = [x for x in re.split('[:.]', inTimeStr)]
    timeX = int(hours1) * 3600 + int(minutes1) * 60.0 + int(seconds1) + float(subsecond1)*0.001
    return round(timeX,4)





# begining of my program
infilepath = r'C:\Users\shiny\Documents\Y4S1\FYP\FYP-Conversational-Speech\sentence_processing\sentence_segmentation\vtt_clean\input.vtt'

with open(infilepath) as fp:
    
    allListWordsTime = []

    for cnt, line in enumerate(fp):
       #print("Line {}: {}".format(cnt, line))

       tokens = line.split()
       if len(tokens)>= 2 and tokens[1] == '-->':
           # next 2 lines we are at payload, lets identify if Its a refresh or a proper payload
           
            time1 = getTimeFromStr(tokens[0])
            time2 = getTimeFromStr(tokens[2])
            difftime = time2-time1
            #print(tokens[0],tokens[1],tokens[2],difftime)
            
            if (difftime > 0.1):
                # This is NOT a refresh, next line is refresh, but next+next line is payload 
                lastStartTime = tokens[0]
                lastEndTime = tokens[2]
                nLine1 = next(fp)  # This IS a refresh if its there, the previous line, NOT payload
                inVTTLine = next(fp)  # This is the PayLoad
                print(tokens[0],' --> ', tokens[2],' ', inVTTLine)
                listWordsTime = parseVTT(inVTTLine, lastStartTime, lastEndTime)
                # got to flatten the list before we insert into our list for all words in the vtt file
                for item in listWordsTime:
                    allListWordsTime.append(item)
                    
    print('\n=================================================\n')
    print(allListWordsTime)
    # hi Zin, here is the op of allListWords with time!
    print('\n=================================================\n')
    
    opFileName= r"C:\Users\shiny\Documents\Y4S1\FYP\FYP-Conversational-Speech\sentence_processing\sentence_segmentation\vtt_clean\output.vtt"
    generate_newTranscriptBreak(opFileName, allListWordsTime)
        
    fp.close()
    
    
    
    
