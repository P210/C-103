import pandas
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sns

df = pandas.read_csv("data2.csv")
f  = px.scatter(df, x ="date",y ="cases",color="cases")

f.show()
