from bokeh.plotting import figure, output_notebook, show

output_notebook()

p = figure(width=400, height=400)

p.circle([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="navy", alpha=0.5)

# show the results
show(p)
