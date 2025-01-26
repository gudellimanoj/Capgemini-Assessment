# 17.Word Counter
# - Create a program to count the occurrences of each word in a sentence provided by the user.
def word_count(s):
    words=s.split()
    word_count={}
    for word in words:
        if word in word_count:
            word_count[word]+=1
        else:
            word_count[word]=1
    return word_count   
s=input('Enter the sentence: ')
print(word_count(s))

