import pandas as pd
from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import ColumnDataSource

df = pd.read_csv("C:/Users/VRUNAL MASURKAR/Downloads/adult.data", header = None)

dups_shape = df.pivot_table(columns=[14], aggfunc='size')
list1 = [dups_shape[0], dups_shape[1]]

source = ColumnDataSource(data=dict(values = ['Less than 50K', 'Greater than 50K'],
            amount = list1, annot = [str(x) for x in list1]))

p = figure(x_range=['Less than 50K', 'Greater than 50K'], height=450,
           toolbar_location=None, tools="")

p.vbar(x='values', top='amount', width=0.1, color='grey', source=source)

labels = LabelSet(x='values', y='amount', text='annot',
                  x_offset=-20, y_offset=7, source=source,  render_mode='canvas')

p.xgrid.grid_line_color = None
p.y_range.start = 0

p.xgrid.grid_line_color = None
p.yaxis.visible = False
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.xaxis.minor_tick_line_color = None
p.outline_line_color = None  

output_notebook()

p.add_layout(labels)

show(p)
