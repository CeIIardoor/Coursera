# Assign to the variable num_lines the number of lines in the file school_prompt.txt.

num_lines = 0;

with open("school_prompt.txt") as file:
    data = file.read()
    num_lines = len(data.splitlines())

# Assign the first 30 characters of school_prompt.txt as a string to the variable beginning_chars.

with open("school_prompt.txt") as file:
    data = file.read()
    beginning_chars = data[:30]
    
# Using the file school_prompt.txt, assign the third word of every line to a list called three.

three = []
with open("school_prompt.txt") as file:
    data = file.read()
    #read line by line
    lines = data.splitlines()
    for line in lines:
        #split line by space
        words = line.split()
        #assign third word to three
        three.append(words[2])
        #remove ',', '.', '!' from end of word
        three[-1] = three[-1].strip(".,!")

# print(three)

# Using the file school_prompt.txt, if the character ‘p’ is in a word, then add the word to a list called p_words.
p_words = []

with open("school_prompt.txt") as file:
    data = file.read()
    #read line by line
    lines = data.splitlines()
    for line in lines:
        #split line by space
        words = line.split()
        #check if p is in word
        for word in words:
            if "p" in word:
                p_words.append(word)
                
# print(p_words)
