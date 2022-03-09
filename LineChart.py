from bokeh.plotting import figure, output_file, show

output_file("line.html")

p = figure(width=400, height=400)

# add a line renderer
#similar coordinates to the circle plotting but draws a line between x and y coordinates mentioned using 
#two brackets
p.line([1, 2, 3, 4, 5], [6, 7, 2, 4, 5], line_width=2)

show(p)
