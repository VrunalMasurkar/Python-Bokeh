from bokeh.plotting import figure, show, output_notebook, output_file
output_notebook()

import pandas as pd
df = pd.read_csv('C:/Users/VRUNAL MASURKAR/Downloads/names.txt',delimiter='\t', header=None)

names = df[0]
age = df[1]

p = figure(x_range=names, height=350, title="Person Ages",
           toolbar_location=None, tools="")

p.vbar(x=names, top=age, width=0.5, color='blue')

p.xgrid.grid_line_color = None
p.y_range.start = 0

output_file("person_age.html")

show(p)
