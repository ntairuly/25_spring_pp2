def reverse_s(sentence):
    word = list(sentence.split(" "))
    rsentence =''
    for i in range(len(word)-1,-1,-1):
        rsentence=rsentence+word[i]+" "
    return rsentence
sentence="ready"
print(reverse_s(sentence))