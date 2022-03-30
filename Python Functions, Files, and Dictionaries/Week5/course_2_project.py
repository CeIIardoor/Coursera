

punctuation_chars = ["'", '"', ",", ".", "!", ":", ";", '#', '@']

def strip_punctuation(word):
    punctuation = punctuation_chars
    for char in word:
        if char in punctuation:
            word = word.replace(char, "")
    return word

# lists of words to use
positive_words = []
with open("positive_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            positive_words.append(lin.strip())


negative_words = []
with open("negative_words.txt") as pos_f:
    for lin in pos_f:
        if lin[0] != ';' and lin[0] != '\n':
            negative_words.append(lin.strip())
            

def get_pos(b):
    c = 0
    words = b.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in positive_words:
            c += 1
    return c

def get_neg(b):
    c = 0
    words = b.split()
    for word in words:
        word = strip_punctuation(word)
        if word.lower() in negative_words:
            c += 1
    return c

t = open('project_twitter_data.csv','r')
o = open("resulting_data.csv","w")
o.write("Number of Retweets, Number of Replies, Positive Score, Negative Score, Net Score")
o.write('\n')

l = t.readlines()
headers = l[0]

print(headers)

for row in l[1:]:
    
    v = row.strip().split(',')
    row_string = '{},{},{},{},{}'.format(v[1],v[2],get_pos(v[0]),get_neg(v[0]),get_pos(v[0])-get_neg(v[0]))
    o.write(row_string)
    o.write('\n')


o.close()
t.close()
