from bokeh.plotting import figure, show, output_notebook
output_notebook()

year = ['2014', '2015', '2016', '2017']
percentage = [25, 27, 30, 26]

p = figure(x_range=year, height=350,
           toolbar_location=None, tools="")
p.xaxis.axis_label = 'Year'
p.yaxis.axis_label = 'Percentage of 4-year graduates'

p.line(year, percentage, line_width=1, color='black')

p.xgrid.grid_line_color = None
p.y_range.start = 0

show(p)
