def permutation(text):
    if len(text) == 1:
        return text
    result = []
    for i in range(len(text)):
        current = text[i]
        remaining = text[0:i] + text[i+1:len(text)+1]

        perms = permutation(remaining)
        print(remaining)

        for j in range (len(perms)):
            result.append(current + perms[j])
        
    return result

text = "abcd"
print(permutation(text))











"""1 var incompleted 
    def rem1_char(word,char):
    word1=""
    flag =True
    for i in word:
        if i==char and flag:
            flag = False
        else:
            word1+=i
    return word1


def left_move(word):
    word1=""
    n=0
    for i in word:
        if n==0:
            n+=1
        else:
            word1+=i
    word1= word1 + word[0]
    return word1
word_list = []
word2 = ""
def permutations(word,lenght):
    global word_list
    global word2
    word1 = word[(len(word))-lenght:len(word)+1]
    for i in range(lenght):
        letter=word1[0]
        word2+=letter
        for i in range(len(word2)+1):
                if not word_list.count(word2) and len(word2)==len(word):
                    word_list.append(word2)
                word2 = left_move(word2)
        if lenght >1:
            permutations(word,lenght-1)
        else:
            word2=word2[0:lenght]


permutations("world",5)
print(word_list)
"""