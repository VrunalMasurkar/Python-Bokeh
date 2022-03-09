from bokeh.plotting import figure, show, output_notebook
from bokeh.palettes import Category10
output_notebook()

alpha = ['A', 'B', 'C', 'D', 'E']
value = [10,20,30,40,50]

p = figure(x_range=alpha, height=350,
           toolbar_location=None, tools="")

p.vbar(x=alpha, top=value, width=0.25, color=Category10[5])

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
