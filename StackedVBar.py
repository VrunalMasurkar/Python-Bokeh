from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook, show

output_notebook()

source = ColumnDataSource(data=dict(
    y=[1, 2, 3, 4, 5],
    x1=[1, 2, 4, 3, 4],
    x2=[1, 4, 2, 2, 3],
))
p = figure(width=400, height=400)

p.vbar_stack(['x1', 'x2'], x='y', width=0.8, color=("lightblue", "blue"), source=source)

show(p)
