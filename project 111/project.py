
import plotly.figure_factory as ff
import csv
import plotly.graph_objects as go
import random
import pandas as pd
import statistics

df = pd.read_csv("medium_data.csv")
data = df["reading_time"].tolist()

mean_sample = statistics.mean(data)
sd = statistics.stdev(data)
print("MEAN OF SAMPLE 3 : ", mean_sample)
print("STANDARD DEVIATION : ", sd)

def randomSetMeans(counter):
    data_set = []
    for i in range(0,counter):
        random_index = random.randint(0,len(data) - 1)
        value = data[random_index]
        data_set.append(value)
    mean = statistics.mean(data_set)
    return mean

mean_list = []
for i in range(0,1000):
    set_of_means = randomSetMeans(100)
    mean_list.append(set_of_means)

sd = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)
print("STANDARD DEVIATION OF SAMPLE DISTRIBUTION : ", sd)
print("MEAN OF SAMPLING DISTRIBUTION : ", mean) 

fsds,fsde = mean - sd, mean + sd
ssds,ssde = mean - (2*sd), mean + (2*sd)
tsds,tsde = mean - (3*sd), mean + (3*sd)

z_score = (mean_sample - mean)/sd
print("Z SCORE : ", z_score)

fig = ff.create_distplot([mean_list],["Math Scores"], show_hist = False)
fig.add_trace(go.Scatter(x = [mean,mean], y = [0,0.2], mode = "lines", name = "MEAN"))
fig.add_trace(go.Scatter(x = [fsds,fsds], y = [0,0.17], mode = "lines", name = "First Standard Deviation"))
fig.add_trace(go.Scatter(x = [fsde,fsde], y = [0,0.17], mode = "lines", name = "First Standard Deviation"))

fig.add_trace(go.Scatter(x = [ssds,ssds], y = [0,0.17], mode = "lines", name = "Second Standard Deviation"))
fig.add_trace(go.Scatter(x = [ssde,ssde], y = [0,0.17], mode = "lines", name = "Second Standard Deviation"))

fig.add_trace(go.Scatter(x = [tsds,tsds], y = [0,0.17], mode = "lines", name = "Third Standard Deviation"))
fig.add_trace(go.Scatter(x = [tsde,tsde], y = [0,0.17], mode = "lines", name = "Third Standard Deviation"))

#fig.show()

