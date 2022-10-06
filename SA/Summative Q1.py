# entering sentence
sentence = input("Please enter a sentence of atleast 5 words: ")
totalWords = int(len(sentence.split()))

def reverseWordSentence(sentence):
    #sentence split into a list
    words = sentence.split(" ")
    #reverse words per word
    revWordSentence = " ".join(reversed(words))
    return revWordSentence

def reverseLetterSentence(sentence):
    #sentence split into a list
    words = sentence.split(" ")
    #reverse words per letter
    revLetterSentence = "".join(reversed(sentence))
    return revLetterSentence

def newReverseWordSentence(newSentence):
    #sentence split into a list
    words = newSentence.split(" ")
    #reverse words per word
    revWordSentence = " ".join(reversed(words))
    return revWordSentence

def newReverseLetterSentence(newSentence):
    #sentence split into a list
    words = sentence.split(" ")
    #reverse words per letter
    revLetterSentence = "".join(reversed(newSentence))
    return revLetterSentence

if totalWords == totalWords >= 5:
    print(reverseWordSentence(sentence))
    print(reverseLetterSentence(sentence))

else:
    #re-entering a sentence
    newSentence = input("Please enter a sentence with atleast 5 words: ")
    print(newReverseWordSentence(newSentence))
    print(newReverseLetterSentence(newSentence))
        



