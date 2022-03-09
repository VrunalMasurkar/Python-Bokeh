import pandas as pd
from  math import pi
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, output_notebook, output_file, show

df = pd.read_csv("C:/Users/VRUNAL MASURKAR/Downloads/kobe_bryant_points.csv")
x_labels = df['Year'].tolist()
y_values = df['PTS'].tolist()

output_notebook()

source = ColumnDataSource(data=dict(x = x_labels,
            y = y_values, annot = [str(x) for x in y_values] ))

p = figure(width=450, height=400, y_range = (0,3000), x_range = x_labels, tools="", 
           toolbar_location=None)

p.circle('x', 'y', color="black", alpha=0.8, size=5, source=source)
p.line('x', 'y', color="black", alpha=0.8, line_width=2, source=source)

p.xaxis.major_label_orientation = pi/2

labels = LabelSet(x='x', y='y', text='annot', source=source, text_font_size='8pt',
                  x_offset=-11, y_offset=10, render_mode='canvas')


p.xaxis.axis_label = 'Season'

p.xgrid.grid_line_color = None
p.yaxis.visible = False
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.xaxis.minor_tick_line_color = None
p.outline_line_color = None  

p.add_layout(labels)

show(p)
