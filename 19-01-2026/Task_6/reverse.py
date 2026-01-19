# 6.2 Reversing Words: Write a function that takes a sentence as input and reverses each word in the sentence using string slicing.

def formation(sentence):
    word=sentence.split()
    reverse=[]
    
    for word in word:
        reverse.append(word[::-1])
    return " ".join(reverse)
        
sentence=input("Enter the sentence:")
reversed_sentence=(formation(sentence))
print(reversed_sentence)