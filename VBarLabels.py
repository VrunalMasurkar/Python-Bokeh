from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, show, output_notebook
output_notebook()

source = ColumnDataSource(data=dict(years = ['4', '5', '6', '7', '8', '9'],
            percentage = [35, 19 , 20 , 10, 9, 7],
            annot=['35%', '19%' , '20%' , '10%', '9%', '7%']))


p = figure(x_range=['4', '5', '6', '7', '8', '9'], y_range=(0,38), height=350,
           toolbar_location=None, tools="")
p.xaxis.axis_label = 'Years'

p.vbar(x='years', top='percentage', width=0.25, color='gray', source=source)

labels = LabelSet(x='years', y='percentage', text='annot',
                  x_offset=-8, y_offset=7, source=source, render_mode='canvas')


p.xgrid.grid_line_color = None
p.y_range.start = 0

p.yaxis.visible = False
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.xaxis.minor_tick_line_color = None
p.outline_line_color = None  

p.add_layout(labels)

show(p)
