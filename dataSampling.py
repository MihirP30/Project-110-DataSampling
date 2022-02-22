import plotly.figure_factory as ff
import statistics
import random
import pandas as pd
import csv

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

# Finding the sampling means
def random_means(amount):
    sample_data = []
    for i in range(0, amount):
        index = random.randint(0,len(data))
        value = data[index]
        sample_data.append(value)
    mean = statistics.mean(sample_data)
    return mean

list_of_means = []

for i in range(0,100):
    set_of_means= random_means(30)
    list_of_means.append(set_of_means)

# Output
df = list_of_means
fig = ff.create_distplot([df], ["reading_time"], show_hist=False)
fig.show()

print("Population Mean is ", statistics.mean(data))
print("Sampling Mean is ", statistics.mean(list_of_means))