def pyg_word(word):
    # Convert single word, manage punctuation marks
    Satzzeichen = ""
    if not word[len(word)-1].isalpha():
        Satzzeichen=word[len(word)-1]
        word= word[0:len(word)-2]
    word = word.lower()
    first = word[0]
    new_word = word + first + "ay"
    new_word = new_word [1:len(new_word)]+Satzzeichen
    return(new_word)

def pyg_sentence(sentence):
    #convert sentence into single words and apply pyg-style
    words= sentence.split()
    new_sentence=""
    for n in range(len(words)):
        new_sentence=new_sentence+pyg_word(words[n])+" "
    return new_sentence

satz= input ("satz?")
print (pyg_sentence(satz))
