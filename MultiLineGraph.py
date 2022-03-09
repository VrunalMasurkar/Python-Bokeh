from bokeh.plotting import figure, output_file, show

output_file("patch.html")

p = figure(width=400, height=400)

#multi_line function accepts two or more line coordinates and can be grouped as shown below
p.multi_line([[1, 3, 2], [3, 4, 6, 6], [1,3,5]], [[2, 1, 4], [4, 7, 8, 5], [9,7,5]],
             color=["firebrick", "navy","lime"], alpha=[0.8, 0.3,0.5], line_width=4)

show(p)
