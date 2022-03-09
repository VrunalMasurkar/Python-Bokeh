from bokeh.plotting import figure, output_notebook, show


p = figure(width=400, height=400)

# add a star renderer with a size, color, and alpha
p.star_dot([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], size=20, color="blue", alpha=0.5)

# show the results
show(p)
