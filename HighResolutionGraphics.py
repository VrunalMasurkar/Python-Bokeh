import pandas as pd
from bokeh.plotting import figure, output_notebook, show, output_file
from bokeh.models import ColumnDataSource, Label, Range1d
from bokeh.layouts import gridplot, row, column
from math import pi

df = pd.read_csv("C:/Users/VRUNAL MASURKAR/Downloads/adult.data", header = None)


def create_age_label_column():
   
    figures = []
    name = ""
    tmp = agelbltit_col(name)
    figures.append(tmp)
    for i in range (20,110,10):
        lower = i-10
        upper = i
        if i == 20:
            lower = 0
        age_grp_lbl = str(lower) + '-' + str(upper) + 'years'
        f = figure(title='', width=200, height=200, toolbar_location=None)
        lbl = Label(x=50, y=90, x_units='screen', y_units='screen', text=age_grp_lbl,
                       border_line_color='black', border_line_alpha=1.0, render_mode = 'css',
                       background_fill_color='white', background_fill_alpha=1.0)

        f.add_layout(lbl)
        figures.append(f)
    return figures


def agelbltit_col(name):
    
    pic = figure(width = 225, height = 40, toolbar_location = None)
    pic.outline_line_color = None
    pic.title.text = name
    pic.title.text_font_size = "15px"
    return (pic)
        
    
def get_age_grps_lbl_cnts(df, col):
    age_grp = []
    bins = []
    for i in range (20,110,10):
        lower = i-10
        upper = i
        if i == 20:
            lower = 0
        age_grp.append(str(lower) + '-' + str(upper))        
        df_slice = df[(df[0] >= lower) & (df[0] < upper)]
        x= df_slice[col].value_counts()
        lbls = x.index.tolist()
        cnts = x.tolist()        
        d = dict(zip(lbls, cnts))
        bins.append(d)
    return(age_grp, bins)
    
    
def create_figure(d, all_lbls):
    x=[]
    y=[]
    for a in all_lbls:
        x.append(a)
        if a in d:
            y.append(d[a])
        else:
            y.append(0)
    f = figure(x_range = x, width = 225, height = 200, toolbar_location = None)
    f.vbar(x=x, top=y, width = 0.05*len(x), color = 'grey')
    f.yaxis.minor_tick_line_color = None
    f.xgrid.grid_line_color = None 
    f.xaxis.visible = False
    return f
    
    
def create_figure_column(df, col, name):
    all_lbls = df[col].unique().tolist()
    wid = len(all_lbls)
    (age_grp, bins) = get_age_grps_lbl_cnts(df, col)    
    fs=[]
    up = title_col(df, all_lbls, name)
    fs.append(up)
    for i in range(len(age_grp)):
        f = create_figure(bins[i], all_lbls)
        fs.append(f)
    x = create_x_label_fig(col, wid)
    fs.append(x)
    return(fs)


def create_x_label_fig(col, ylen):
    width = 40
    xlbls = df[col].unique().tolist()
    f= figure(x_range=xlbls, width=225, height=200,
                toolbar_location=None, title='', x_axis_location='below')
    f.vbar(x=xlbls, top=[0]*len(xlbls), width=0.5, color='white')
    f.xaxis.major_label_orientation = pi / 2
    f.xgrid.grid_line_color = None
    f.xaxis.major_tick_line_color = None
    f.yaxis.minor_tick_line_color = None
    f.yaxis.visible = False
    f.xaxis.axis_line_color = None
    f.yaxis.axis_line_color = None
    f.ygrid.grid_line_color = None
    f.outline_line_color = None
    return f


def title_col(d, all_lbls, name):   
    x=[]
    y=[]
    for a in all_lbls:
        x.append(a)
        if a in d:
            y.append(d[a])
        else:
            y.append(0)
    pic = figure(x_range = x, width = 225, height = 40, toolbar_location = None)
    pic.outline_line_color = None
    pic.title.text = name
    pic.title.text_font_size = "15px"
    return (pic)

    
f_mar = create_figure_column(df, 5, 'Marital Status')    
f_edu = create_figure_column(df, 3, 'Education') 
f_wrk = create_figure_column(df, 1, 'Working Class') 
f_inc = create_figure_column(df, 14, 'Income') 
f_age_grps = create_age_label_column()

show(row(column(f_age_grps), column(f_wrk), column(f_edu), column(f_mar), column(f_inc))) 

output_notebook()
