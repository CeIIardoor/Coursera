#create a scatter plot from resulting_data.csv
import matplotlib.pyplot as plt
with open("c:/Users/lenovo/Desktop/Coursera/Python Functions, Files, and Dictionaries/Week5/resulting_data.csv") as f:
    data = f.read()
    lines = data.splitlines()
    i = 0
    xdata = []
    ydata = []
    for line in lines:
        words = line.split(",")
        #labels
        if i==0:
            x = words[4]
            y = words[0]
            i+=1
            continue
        #data
        xdata = xdata + [float(words[4])]
        ydata = ydata + [float(words[0])]
#make a scatter plot from data
plt.xlabel(x)
plt.ylabel(y)
plt.title("Project - Part 2: Sentiment Analysis")
plt.scatter(xdata,ydata)
plt.show()

    
    