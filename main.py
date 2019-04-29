import alt
#Author: Ethan Roland
#Date: 4/29/19
#Algorithmic generation of reformed English Spelling

#words for which the CMU dictionary has sub-par transcriptions
dict = {'us':'us'
        ,'power':'pauer'
        ,'the':'the'
        ,'to':'tu'
        ,'of':'of'
        ,'i':'i'
        ,'as':'as'
        ,'just':'just'
        ,'current':'curent'
        ,'our':'aur'
        ,'does':'dos'
        ,'their':'their'
        ,'promotion':'proumoshon'}


#various input strings to test:
input = "Diets in this period were almost universally vegetable based, especially outside Europe, for the simple reason that land devoted to cultivation is much more efficient. Braudel focuses on three major crops: wheat, rice, and maize. These crops sit at the basis of everything: they determine population size, and their required inputs determine labor relations, animal usage (which in turn need their own crops), and so on."
#input = "Well that's sort of the point, isn't it? If you enjoy doing other things then do them. Some people enjoy having these sorts of discussions and don't consider them 'useless'. You do. That's fine. We don't all have to like the same things. Many people view these conversations as just a tool to interact with other people or as a method to clarify their own ideas on the subject (which may appear to be useless, because there's not much that you can do about the Braves winning a WC position, but it's exercising the brain)."
#input = "All human beings are born free and equal in dignity and rights. They are endowed with reason and conscience and should act towards one another in a spirit of brotherhood."
#input = "Whereas recognition of the inherent dignity and of the equal and inalienable rights of all members of the human family is the foundation of freedom, justice and peace in the world, Whereas disregard and contempt for human rights have resulted in barbarous acts which have outraged the conscience of mankind, and the advent of a world in which human beings shall enjoy freedom of speech and belief and freedom from fear and want has been proclaimed as the highest aspiration of the common people, Whereas it is essential, if man is not to be compelled to have recourse, as a last resort, to rebellion against tyranny and oppression, that human rights should be protected by the rule of law, Whereas it is essential to promote the development of friendly relations between nations, Whereas the peoples of the United Nations have in the Charter reaffirmed their faith in fundamental human rights, in the dignity and worth of the human person and in the equal rights of men and women and have determined to promote social progress and better standards of life in larger freedom, Whereas Member States have pledged themselves to achieve, in co‐operation with the United Nations, the promotion of universal respect for and observance of human rights and fundamental freedoms, Whereas a common understanding of these rights and freedoms is of the greatest importance for the full realization of this pledge, Now, therefore, The General Assembly Proclaims this Universal Declaration of Human Rights as a common standard of achievement for all peoples and all nations, to the end that every individual and every organ of society, keeping this Declaration constantly in mind, shall strive by teaching and education to promote respect for these rights and freedoms and by progressive measures, national and international, to secure their universal and effective recognition and observance, both among the peoples of Member States themselves and among the peoples of territories under their jurisdiction."

#generate the reformed spelling
input = input.replace('-',' ')
arr = input.split(' ')
word = ''
for el in arr:
    temp = el
    temp = temp.replace(')','')
    temp = temp.replace('(','')
    temp = temp.replace(';','')
    temp = temp.replace(':','')
    temp = temp.replace('.','')
    temp = temp.replace(',','')
    temp = temp.replace('!','')
    temp = temp.replace('?','')
    temp = temp.replace("'s",'')
    #print(temp)
    new = ''
    #memoization via dict
    if temp.lower() in dict:
        new = dict[temp.lower()]
    else :
        new = alt.new(temp.lower())
        dict[temp.lower()] = new
    if temp[0].isupper() :
        new = new.capitalize()
    #print(new)
    el = el.replace(temp,new)
    word = word + ' ' + el
word = word.strip()
print(input)
print(word)
# for x, y in dict.items():
#    print(x, y)
