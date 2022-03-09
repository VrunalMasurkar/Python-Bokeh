from bokeh.models import ColumnDataSource, Label, LabelSet
from bokeh.plotting import figure, output_notebook, show

output_notebook()

source = ColumnDataSource(data=dict(province=['Victoria', 'Queensland', 'Tasmania', 
            'New South Wales', 'Western Australia', 'Southern Australia'],
            aa=[463000, 617000, 302000, 104000, 99000, 140000],
            annot=['463000', '617000', '302000', '104000', '99000', '140000']))

p = figure( y_range = ['Victoria', 'Queensland', 'Tasmania', 
            'New South Wales', 'Western Australia', 'Southern Australia'], x_range = (0, 750000) ,
            height=350, toolbar_location=None, tools="")

p.hbar(y='province', right='aa', height=0.5, left=0, color='grey',  source=source)

p.yaxis.axis_label = 'Province'

labels = LabelSet(x='aa', y='province', text='annot',
                  x_offset=5, y_offset=-5, source=source, render_mode='canvas')

p.xaxis.visible = False
p.xgrid.grid_line_color = None
p.ygrid.grid_line_color = None
p.xaxis.minor_tick_line_color = None
p.outline_line_color = None  

p.ygrid.grid_line_color = None

p.add_layout(labels)

show(p)
