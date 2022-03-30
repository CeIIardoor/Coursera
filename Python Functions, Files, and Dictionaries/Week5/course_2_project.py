# function called strip_punctuation which takes one parameter, a string which represents a word, and removes characters considered punctuation from everywhere in the word. (Hint: remember the .replace() method for strings.)


from numpy import negative


punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    punctuation = punctuation_chars
    for char in word:
        if char in punctuation:
            word = word.replace(char, "")
    return word
#Next, copy in your strip_punctuation function and define a function called get_pos which takes one parameter, a string which represents one or more sentences, and calculates how many words in the string are considered positive words. Use the list, positive_words to determine what words will count as positive. The function should return a positive integer - how many occurrences there are of positive words in the text. Note that all of the words in positive_words are lower cased, so you’ll need to convert all the words in the input string to lower case as well.

positive_words = []
negative_words = []

def get_pos(string):
    string = string.lower()
    string = strip_punctuation(string)
    string = string.split()
    count = 0
    for word in string:
        if word in positive_words:
            count += 1
    return count



def get_neg(string):
    string = string.lower()
    string = strip_punctuation(string)
    string = string.split()
    count = 0
    for word in string:
        if word in negative_words:
            count += 1
    return count



