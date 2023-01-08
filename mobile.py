import plotly.express as px
import pandas as pd
import csv
import plotly.figure_factory as ff

df = pd.read_csv("mobile.csv")
fig = ff.create_distplot([df["Avg Rating"].tolist()], ["Rating"], show_hist= False )
fig.show()