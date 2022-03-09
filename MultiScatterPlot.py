from bokeh.plotting import figure, output_notebook, show

output_notebook()

p = figure(width=400, height=400, title="Lecture Activity")

p.circle([1, 2, 3, 4], [5, 4, 3, 2], size=20, color="green", alpha=0.5)
p.circle([1, 4, 5, 6], [3, 7, 2, 5], size=20, color="blue", alpha=0.5)

show(p)
