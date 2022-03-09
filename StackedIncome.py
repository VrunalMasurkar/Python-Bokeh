import pandas as pd

d = pd.read_csv("C:/Users/VRUNAL MASURKAR/Downloads/adult.data", header=None)

x = d[[3,14]].groupby([3,14])[3].agg('count')
x.index
education_level=[]
x_low = []
x_high = []

v=0
for i in x.index:
    if(v%2==0):  
        education_level.append(i[0])
        x_low.append(x[i])
        if i[0]==' Preschool':
            x_high.append(0)
            v+=1
    else:
        x_high.append(x[i])
    v+=1
    
for i in range(len(education_level)):
    print(education_level[i], x_low[i], x_high[i])
    
y_num=[]
for i in range(len(education_level)):
    y_num.append(i+0.5)
    
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure, output_notebook, show

output_notebook()

source = ColumnDataSource(data=dict(
    y = y_num,
    x1= x_low,
    x2= x_high,
))
p = figure(title='Education Income', y_range=education_level, tools="", toolbar_location=None)

p.hbar_stack(['x1', 'x2'], y='y', height=0.8, color=("gold", "darkkhaki"), source=source)

show(p)
