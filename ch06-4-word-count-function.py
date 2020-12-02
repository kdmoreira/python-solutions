# 6.4
def processText(your_text):
    """This function processes text and returns a list of words"""
    new_text = your_text.split()
    for i in new_text:
        word = i.strip("\".,;!?()")
        word = word.casefold()
        word_list.append(word)
    return word_list

def countWords(any_list):
    """This function counts word frequency"""
    for word in any_list:
        if word in counter:
            counter[word] += 1
        else:
            counter[word] = 1
    for word in counter:
        print("{} appears {} time(s).".format(word, counter[word]))

wiki = "Python is dynamically typed and garbage-collected. \
It supports multiple programming paradigms, including structured \
(particularly, procedural), object-oriented, and functional programming. \
Python is often described as a \"batteries included\" language due to \
its comprehensive standard library."
word_list = []
counter = {}
processText(wiki)
countWords(word_list)
