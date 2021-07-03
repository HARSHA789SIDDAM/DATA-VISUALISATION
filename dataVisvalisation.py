import pandas as pd
import plotly.express as px

df = pd.read_csv("data.csv")
#fig = px.bar(df, x='country',y='cases')
#fig = px.scatter(df, x="country",y="cases",size_max=60)
df = pd.read_csv("data.csv")
fig = px.line(df, x = "date", y = "cases")

fig.show()