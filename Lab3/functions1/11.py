def palindrome(word):
    rword =''
    for i in range(len(word)-1,-1,-1):
        rword=rword+word[i]
    if rword==word:
        return "It is a palindrome."
    else:
        return "It is not a palindrome."
word="madam"
print(palindrome(word))