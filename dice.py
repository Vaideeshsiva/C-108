import random
import plotly.express as px
import plotly.figure_factory as ff

dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)
diceResult = []

print(dice1)

count = []

for i in range(100):
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6)
    diceResult.append(dice1 + dice2)
    count.append(i)

print(diceResult)

#fig = px.bar(x=diceResult, y=count)
fig = ff.create_distplot([diceResult], ["result"])
fig.show()

