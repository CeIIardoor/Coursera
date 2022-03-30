#Find the total number of words in the file and assign this value to the variable num_words.

num_words = 0;

with open("emotion_words.txt") as file:
    data = file.read()
    num_words = len(data.split())
    
print(num_words)

#Create a list called emotions that contains the first word of every line in emotion_words.txt.

emotions = []

with open("emotion_words.txt") as file:
    data = file.read()
    #read line by line
    lines = data.splitlines()
    for line in lines:
        #split line by space
        words = line.split()
        #assign first word to emotions
        emotions.append(words[0])
        
print(emotions)