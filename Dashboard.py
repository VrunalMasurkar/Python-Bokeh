import pandas as pd
from bokeh.plotting import figure, output_notebook, show
from bokeh.models import ColumnDataSource
from bokeh.layouts import gridplot, row
from math import pi

df = pd.read_csv("C:/Users/VRUNAL MASURKAR/Downloads/adult.data", header = None)

### Function for creating figures for Working Class Distribution, ###
### Education Distribution, Marital Status Distribution ###

def create_distr_figure(df, col_id, t):
    distr = df[col_id].value_counts()
    x_lbls = distr.index.tolist()
    y_cnts = distr.tolist()
    p = figure(x_range = x_lbls, width = 500, height=550, title=t,
                toolbar_location=None, tools="")
    p.vbar(x=x_lbls, top=y_cnts, width = 0.05*len(x_lbls), color='grey')
    p.xaxis.major_label_orientation = pi/4
    p.xgrid.grid_line_color = None
    p.ygrid.grid_line_color = None
    p.xaxis.minor_tick_line_color = None
    p.outline_line_color = None  

    return(p)
    
### Creating Figure for Age Distribution ###
    
def create_age_distr_figure(df):
    ages = df[0].tolist()
    ages_d = {'<20':0}
    for i in range(20, 60, 10):
        ages_d[str(i) + 's'] = 0
    ages_d['60+'] = 0
    
    for a in ages:
            x = int(a/10)*10
            if x<20:
                ages_d['<20'] +=  1
            elif x >= 60:
                ages_d['60+'] += 1
            else: 
                ages_d[str(x) + 's'] += 1
    age_lbls = []
    age_cnts = []
    for k,v in ages_d.items():
        age_lbls.append(k)
        age_cnts.append(v)
    
    f = figure(width = 500, height = 500, x_range = age_lbls, 
               title='Age Distribution', toolbar_location=None, tools="")
    f.vbar(x=age_lbls, top=age_cnts, width= 0.05*len(age_lbls), color='grey')
    f.xgrid.grid_line_color = None
    f.ygrid.grid_line_color = None
    f.xaxis.minor_tick_line_color = None 

    return f
    
f_w = create_distr_figure(df, 1, 'Working Class Distribution')
f_e = create_distr_figure(df, 3, 'Education Distribution')
f_m = create_distr_figure(df, 5, 'Marital Status Distribution')
f_a = create_age_distr_figure(df)

output_notebook()

grid = gridplot([[f_a, f_m], [f_w, f_e]], width=500, height=500)

show(grid)
