from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook, show

output_notebook()

source = ColumnDataSource(data=dict(
    y=['Apples', 'Oranges', 'Pears'],
    x1=[50, 20, 60],
    x2=[20, 70, 40],
))
p = figure(width=400, height=400, y_range= ['Apples', 'Oranges', 'Pears'])

p.hbar_stack(['x1', 'x2'], y='y', height=0.25, color=("grey", "lightgrey"), source=source)

show(p)
