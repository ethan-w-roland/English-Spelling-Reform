import eng_to_ipa as ipa #comes from CMU pronouncing dict
import rank

'''
Maps IPA of word into Reformed English Spelling
Author: Ethan Roland
Date: 04/29/19
'''

#Allows vowel clusters to be mapped onto 5 vowel system
def vCheck(out,word,i):
    if len(word) >= 2 :
        if i < len(word)-1 and word[i+1] in '123əuʊɔɑoɛɪæeia':
            return True
        if i > 0:
            if (word[i-1] in '123əuʊɔɑoɛɪæeia'):
                return True
            if (len(out) >= 2 and out[-1:] in 'aeiou'):
                return True
    return False

#Recursive function to generate all possible spellings from IPA
def poss(input, arr, word, out, i) :
    #print(input + "\t" + word + "\t" + out)
    if i == len(word):
        out = out.replace('auu','au')
        if input[0] == 'h' and out[0] != 'h' : #silent initial h
            out = 'h' + out
        temp = out.replace('ks','x')
        if temp != out :
            poss(input, arr, word, temp, i)
        if out[-1:] in 'vz' and input[-1:] == 'e' and ('z' in input or 'v' in input): #silent final e
            temp = out + 'e'
            arr.append(temp)
        elif out[-1:] in 'lr' and (len(out) >= 2 and (out[-2:-1] not in 'aeiou' or len(out) <= 3)) and input[-1:] == 'e': #silent final e
            temp = out + 'e'
            arr.append(temp)
        elif out[-1:] in 'js' and input[-1:] == 'e' and (len(input) >= 3 and ('g' in input[-3:] or 'c' in input[-3:])): #silent final e
            temp = out + 'e'
            arr.append(temp)
        arr.append(out)
        #print(out)
        return
    if word[i] == '1': #ou
        if (i == len(word) - 1 or vCheck(out,word,i)) :
            poss(input, arr, word, out + 'o', i + 1)
            return
        poss(input, arr, word, out + 'ou', i + 1)
        return
    if word[i] == '2': #ai
        poss(input, arr, word, out + 'ai', i + 1)
        return
    if word[i] == '3': #au
        poss(input, arr, word, out + 'au', i + 1)
        return
    if word[i] == 'e': #ei
        if (i == len(word)-1) and (input[len(input)-1] == 'y'):
            poss(input, arr, word, out + 'ey', i + 1)
            return
        poss(input, arr, word, out + 'ei', i + 1)
        return
    if word[i] == 'æ': #aa
        poss(input, arr, word, out + 'a', i + 1)
        return
    if word[i] == 'i': #ee
        if vCheck(out,word,i):
            if input[-1:] == 'y' and len(word) > 2:
                poss(input, arr, word, out + 'y', i + 1)
            poss(input, arr, word, out + 'i', i + 1)
            return
        if (i == len(word)-1) :
            if len(input) <= 3 and input[-1:] == 'e' and input[-2:-1] != 'e':
                poss(input, arr, word, out + 'e', i + 1)
            if input[-1:] == 'y' and len(word) > 2:
                poss(input, arr, word, out + 'y', i + 1)
            poss(input, arr, word, out + 'i', i + 1)
        poss(input, arr, word, out + 'ea', i + 1)
        if 'ee' in input:
            poss(input, arr, word, out + 'ee', i + 1)
        if i != 0:
            poss(input, arr, word, out + 'ie', i + 1)
        return
    if word[i] == 'ɪ': #ih
        if i == len(word) - 1 and input[len(input)-1] == 'y':
            poss(input, arr, word, out + 'y', i + 1)
        poss(input, arr, word, out + 'i', i + 1)
        poss(input, arr, word, out + 'e', i + 1)
        poss(input, arr, word[:i]+"i"+word[i+1:], out, i)
        return
    if word[i] == 'ɛ': #eh
        poss(input, arr, word, out + 'e', i + 1)
        poss(input, arr, word[:i]+"e"+word[i+1:], out, i) #/ei/
        return
    if word[i] == 'ɔ': #/o/
        if i == len(word)-1 or word[i+1] == 'l':
            poss(input, arr, word, out + 'a', i + 1)
        poss(input, arr, word, out + 'o', i + 1)
        return
    if word[i] == 'ɑ': #ah
        if i == len(word)-1 or word[i+1] == 'r' or word[i+1] == 'l':
            poss(input, arr, word, out + 'a', i + 1)
        poss(input, arr, word, out + 'o', i + 1)
        return
    if word[i] == 'ʊ': #ü
        if vCheck(out,word,i) or (i == len(word) - 1):
            poss(input, arr, word, out + 'u', i + 1)
            return
        if ('oo' in input) :
            poss(input, arr, word, out + 'oo', i + 1)
        poss(input, arr, word, out + 'u', i + 1)
        return
    if word[i] == 'u': #oo
        if vCheck(out,word,i) or (i == len(word) - 1):
            poss(input, arr, word, out + 'u', i + 1)
            return
        if ('oo' in input) :
            poss(input, arr, word, out + 'oo', i + 1)
        poss(input, arr, word, out + 'ue', i + 1)
        return
    if word[i] == 'ə': #uh
        if i == len(word) - 1:
            poss(input, arr, word, out + 'a', i + 1)
            return
        if word[i+1] == 'r':
            poss(input, arr, word, out + 'e', i + 1)
            poss(input, arr, word, out + 'u', i + 1)
            poss(input, arr, word, out + 'a', i + 1)
            poss(input, arr, word, out + 'o', i + 1)
            poss(input, arr, word, out + 'i', i + 1)
            return
        poss(input, arr, word, out + 'u', i + 1)
        poss(input, arr, word, out + 'o', i + 1)
        if i == 0 or (word[i+1] != 'l' and out[-1:] not in 'ig') or (out[-1:] in 'aeiou' and out[-2:-1] in 'aeiou'):
            poss(input, arr, word, out + 'e', i + 1)
        poss(input, arr, word, out + 'a', i + 1)
        if i == 0 or word[i-1] != 'g':
            poss(input, arr, word, out + 'i', i + 1)
        if len(input) >= 4 and i >= 1 and out[-1:] not in 'aeiou':
            poss(input, arr, word, out, i + 1)
        return
    if word[i] == 'g': #g
        poss(input, arr, word, out + 'g', i + 1)
        poss(input, arr, word, out + 'k', i + 1)
        return
    if word[i] == 'k': #k
        poss(input, arr, word, out + 'k', i + 1)
        if i <= len(word) - 2 and word[i+1] == 'w':
            poss(input, arr, word, out + 'qu', i + 2)
        return
    if word[i] == 's': #s
        poss(input, arr, word, out + 's', i + 1)
        if i == len(word)-1:
            poss(input, arr, word, out + 'ss', i + 1)
        if i == len(word)-1 and out[-1:] in 'sjv':
            poss(input, arr, word, out + 'es', i + 1)
        return
    if word[i] == 'd': #d
        poss(input, arr, word, out + 'd', i + 1)
        if i == len(word)-1 and out[-1:] in 'sjv':
            poss(input, arr, word, out + 'ed', i + 1)
        return
    if word[i] == 'z': #z
        poss(input, arr, word[:i]+"s"+word[i+1:], out, i)
        poss(input, arr, word, out + 'z', i + 1)
        return
    if word[i] == 'ʒ': #zh
        poss(input, arr, word, out + 'zh', i + 1)
        if 'j' in input:
            poss(input, arr, word, out + 'j', i + 1)
        return
    if word[i] == 'w': #w
        poss(input, arr, word, out + 'w', i + 1)
        poss(input, arr, word, out + 'u', i + 1)
        return
    if word[i] == 'j': #y
        if i <= len(word) - 2 and (word[i+1] == 'u' or word[i+1] == 'ə' or word[i+1] == 'ʊ'):
            poss(input, arr, word, out + 'eu', i + 2)
            if i == len(word) - 2:
                poss(input, arr, word, out + 'ew', i + 2)
        poss(input, arr, word, out + 'i', i + 1)
        poss(input, arr, word, out + 'y', i + 1)
        return
    if word[i] == 'ʤ': #j
        poss(input, arr, word, out + 'j', i + 1)
        poss(input, arr, word, out + 'dg', i + 1)
        poss(input, arr, word, out + 'dj', i + 1)
        return
    if word[i] == 'ʧ': #ch
        poss(input, arr, word, out + 'ch', i + 1)
        poss(input, arr, word, out + 'tch', i + 1)
        if i < len(word) - 1 and 'r' in word[i+1:i+2]:
            poss(input, arr, word, out + 't', i + 1)
        return
    if word[i] == 'l': #l
        poss(input, arr, word, out + 'l', i + 1)
        if i == len(word) - 1:
            poss(input, arr, word, out + 'll', i + 1)
        return
    poss(input, arr, word, out + word[i], i + 1)
    return

#Converts s(ei) -> c(ei) and j(ei) -> g(ei)
def filter(input, arr, word, out, i) :

    if i == len(word) :
        out = out.replace('cc','kc')
        arr.append(out)
        return
    if i < len(word) - 1 :
        if word[i] == 'g' and word[i+1] in 'eiy' :
            filter(input, arr, word, out + 'gh', i + 1)
            return
        if word[i] == 'j' and word[i+1] in 'eiy' :
            filter(input, arr, word, out + 'g', i + 1)
            filter(input, arr, word, out + 'j', i + 1)
            return
        if word[i] == 's' and word[i+1] in 'eiy' :
            filter(input, arr, word, out + 'c', i + 1)
            filter(input, arr, word, out + 's', i + 1)
            return
        if word[i] == 'k' and word[i+1] not in 'eiy' :
            filter(input, arr, word, out + 'c', i + 1)
            filter(input, arr, word, out + 'k', i + 1)
            return
        else :
            filter(input, arr, word, out + word[i], i + 1)
            return
    if word[i] == 'k' and 'c' in input: #final k -> c
        filter(input, arr, word, out + 'c', i + 1)
    filter(input, arr, word, out + word[i], i + 1)
    return

#main function
def new (input) :

    if len(input) == 0:
        return input
    #print(input)

    #convert word to IPA
    input = input.lower()
    trans = ipa.convert(input)
    if trans[len(trans)-1] == '*':
        print(trans)
        print("error, no transcription")
        return input

    #print(trans)
    trans = trans.replace("ˈ","")
    trans = trans.replace("ˌ","")
    trans = trans.replace("iɛ","ie")
    trans = trans.replace("iɪ","i")
    trans = trans.replace("æŋ","en")
    trans = trans.replace("ŋ","ng")
    trans = trans.replace("ð","th")
    trans = trans.replace("θ","th")
    trans = trans.replace("ʃ","sh")
    trans = trans.replace("ngg","ng")
    trans = trans.replace("ngk","nk")
    trans = trans.replace("oʊ","1")
    trans = trans.replace("aɪ","2")
    trans = trans.replace("aʊ","3")

    #step 1 generate possible spellings
    ar1 = []
    poss(input, ar1, trans, '', 0)

    #step 2 add possibilites associated with g(ei) and c(ei)
    ar2 = []
    for el in ar1:
        #print(el)
        filter(input, ar2, el, '', 0)

    #rank the possible spellings based on their edit distance from
    #the input word. Uses modified damerau-levenshtein algorithm
    best = 1000
    out = ''
    input = input[0] + input[1:-1].replace('y','i') + input[-1:]
    for el in ar2:
        score = rank.dLev(el, input)
        #print(el, "\t", score)
        if score < best :
            out = el
            best = score
    return out