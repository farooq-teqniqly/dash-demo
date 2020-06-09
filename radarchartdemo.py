import plotly.express as px
import pandas as pd

names = ["Farooq", "Emily", "Andrew", "Noor", "Yasin"]
ages = [42, 44, 12, 13, 10]

df = pd.DataFrame(dict(ages=ages, names=names))
chart = px.line_polar(df, range_r=(0, 60), theta='names', line_close=True)
chart.show()