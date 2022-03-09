from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, show, output_notebook
output_notebook()

source = ColumnDataSource(data=dict(year = ['2014', '2015', '2016', '2017'],
            percentage = [25, 27, 30, 26],
            annot=['25%', '27%', '30%', '26%']))

p = figure(x_range=['2014', '2015', '2016', '2017'], y_range=(0,33), height=350,
           toolbar_location=None, tools="")
p.xaxis.axis_label = 'Year'

p.line('year', 'percentage', line_width=1, color='black', source=source)
p.circle('year', 'percentage', alpha=0.8, size=5, color='black', source=source)

labels = LabelSet(x='year', y='percentage', text='annot',
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
