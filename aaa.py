
def is_palindrome(word):
    i = 0
    j = len(word)
    for i in range (j):
        if word[i] != word[j-i-1]:
            return (False)
    return (True)
   






print(is_palindrome("rotator")) #=True
print(is_palindrome("flower"))  #=False
print(is_palindrome("토마토"))