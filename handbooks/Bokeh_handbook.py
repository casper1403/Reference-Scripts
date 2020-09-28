
""" Bokeh is a data visualizations library used for the creation of interactive and static data visualizations"""

""" Basic imports """

from bokeh.plotting import figure, output_file, show

# the show object is used for showing the graph
# THe output_file object is the file the graph will be made made in
output_file("line.html")
x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]
# The figure object is the graph that you're going to be working in
p = figure(plot_width=400, plot_height=400)

# Label the axis
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Value'


# add a line renderer
p.line(x,y, line_width=2)

# the show object is used for showing the graph
show(p)



"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Different types of plots Line, Circle(Scatter), Time series,
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """

# Create a green line
p = figure(plot_width=400, plot_height=400)

p.line(x,y, line_width=2, line_color='green')
# show(p)


# plot a circle plot
p = figure(plot_width=400, plot_height=400)
p.circle(x,y, size=10,line_color='red',fill_color='blue')
# show(p)


# Time series
from bokeh.sampledata.glucose import data
data.head()
week = data.loc['2010-10-01':'2010-10-08']
p = figure(x_axis_type="datetime", title="Glocose Range", plot_height=350, plot_width=800)
p.xgrid.grid_line_color=None
p.ygrid.grid_line_alpha=0.5
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Value'
p.line(week.index, week.glucose)
# show(p)


""""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
                                              Colors
There are many places where you may need to specify colors. Bokeh can accept colors in a variety of different ways:

    -any of the 140 named HTML/CSS colors, e.g 'green', 'indigo'
    -an RGB(A) hex value, e.g., '#FF0000', '#44444444'
    -a 3-tuple of integers (r,g,b) between 0 and 255
    -a 4-tuple of (r,g,b,a) where r, g, b are integers between 0 and 255 and a is a floating point value between 0 and 1
----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- """

p = figure(plot_width=400, plot_height=400)

# Label the axis
p.xaxis.axis_label = 'Time'
p.yaxis.axis_label = 'Value'

# Set the visuals of the graphs outline

# Thickness of the outline
p.outline_line_width = 7

# Transparity fo the outline
p.outline_line_alpha = 1

# Color of the outline
p.outline_line_color = "navy"

p.line(x,y, line_width=5, line_color='red', line_alpha=0.5)
# show(p)


"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
The Axis object

Axis properties
Axes objects have many configurable properties that afford control over most visual aspects of an axis. These can be grouped by function according to prefix.
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""
from math import pi

p = figure(plot_width=400, plot_height=400)
p.asterisk(x, y, size=12, color="olive")

# Set the direction of you labe
p.xaxis.major_label_orientation = pi/4

# change just some things about the x-axes
#label
p.xaxis.axis_label = "Temp"
#Set a line
p.xaxis.axis_line_width = 3
#set color of line
p.xaxis.axis_line_color = "red"

# change just some things about the y-axes
# label
p.yaxis.axis_label = "Pressure"
# change color of text of
p.yaxis.major_label_text_color = "orange"
# Change orientation
p.yaxis.major_label_orientation = "horizontal"

# change things on all axes
p.axis.minor_tick_in = -3
p.axis.minor_tick_out = 6

# Remove the axis label
p.axis.axis_label=None

#remove the axis
p.axis.visible=False

#remove th egrid
p.grid.grid_line_color = None


#
# show(p)


"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 multiple graphs and legends
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """

import numpy as np

x = np.linspace(0, 4*np.pi, 100)
y = np.sin(x)

p = figure(height=400)

# plot multiple graphs and add legend with legend_label argument, styling will appear in the legend as well .
p.circle(x, y, legend_label="sin(x)")
p.line(x, 2*y, legend_label="2*sin(x)", line_dash=[4, 4], line_color="orange", line_width=2)
p.line(x, 4*y, legend_label="4*sin(x)", line_color="red", line_width=2)
# show(p)


"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Rows columns and layout of different plots
 ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- """

from bokeh.layouts import row

# Output a row of plots

x = list(range(11))
y0, y1, y2 = x, [10-i for i in x], [abs(i-5) for i in x]


# create a new plot
s1 = figure(width=250, plot_height=250)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create another one
s2 = figure(width=250, height=250)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create and another
s3 = figure(width=250, height=250)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# show the results in a row
# show(row(s1, s2, s3))

from bokeh.layouts import gridplot

# Outputs a grid of plots
# create a new plot
s1 = figure(width=250, plot_height=250)
s1.circle(x, y0, size=10, color="navy", alpha=0.5)

# create another one
s2 = figure(width=250, height=250)
s2.triangle(x, y1, size=10, color="firebrick", alpha=0.5)

# create and another
s3 = figure(width=250, height=250)
s3.square(x, y2, size=10, color="olive", alpha=0.5)

# put all the plots in a gridplot
p = gridplot([[s1, s2], [s3, None]], toolbar_location=None)

# show the results
# show(p)


# INTERACTIVE GRID PLOT
from bokeh.models import ColumnDataSource

x = list(range(-20, 21))
y0, y1 = [abs(xx) for xx in x], [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "box_select,lasso_select,help"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300)
left.circle('x', 'y0', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, width=300, height=300)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

# show(p)



"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
       Working with different data sources

We've seen how Bokeh can work well with Python lists, NumPy arrays, Pandas series, etc. At lower levels, these inputs are converted to a Bokeh ColumnDataSource.
 This data type is the central data source object used throughout Bokeh.
 Although Bokeh often creates them for us implicitly, there are times when it is useful to create them explicitly.
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """

from bokeh.models import ColumnDataSource

# Create the Data Source
source = ColumnDataSource(data={
    'x' : [1, 2, 3, 4, 5],
    'y' : [3, 7, 8, 5, 1],
})

# call the source within yout plot
p = figure(plot_width=400, plot_height=400)
p.circle('x', 'y', size=20, source=source)
# show(p)


"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Creating a Pie chart with cumsum()
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

from math import pi
import pandas as pd
from bokeh.palettes import Category20c # palette for color mapping
from bokeh.transform import cumsum

x = { 'United States': 157, 'United Kingdom': 93, 'Japan': 89, 'China': 63,
      'Germany': 44, 'India': 42, 'Italy': 40, 'Australia': 35, 'Brazil': 32,
      'France': 31, 'Taiwan': 31, 'Spain': 29 }

data = pd.Series(x).reset_index(name='value').rename(columns={'index':'country'})
data['color'] = Category20c[len(x)]

# represent each value as an angle = value / total * 2pi
data['angle'] = data['value']/data['value'].sum() * 2*pi

p = figure(plot_height=350, title="Pie Chart", toolbar_location=None,
           tools="hover", tooltips="@country: @value")

p.wedge(x=0, y=1, radius=0.4,

        # use cumsum to cumulatively sum the values for start and end angles
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='country', source=data)

# Remove the x and y axis
p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

# show(p)

"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Adding tools to your plot
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """

from bokeh.models import ColumnDataSource

x = list(range(-20, 21))
y0, y1 = [abs(xx) for xx in x], [xx**2 for xx in x]

# create a column data source for the plots to share
source = ColumnDataSource(data=dict(x=x, y0=y0, y1=y1))

TOOLS = "box_select,lasso_select,help,pan,wheel_zoom"

# create a new plot and add a renderer
left = figure(tools=TOOLS, width=300, height=300)
left.circle('x', 'y0', source=source)

# create another new plot and add a renderer
right = figure(tools=TOOLS, width=300, height=300)
right.circle('x', 'y1', source=source)

p = gridplot([[left, right]])

show(p)

"""
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Create linear color shift
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
"""

from bokeh.transform import linear_cmap

N = 4000
data = dict(x=np.random.random(size=N) * 100,
            y=np.random.random(size=N) * 100,
            r=np.random.random(size=N) * 1.5)

p = figure()

p.circle('x', 'y', radius='r', source=data, fill_alpha=0.6,

         # color map based on the x-coordinate
         color=linear_cmap('x', 'Viridis256', 0, 100))

# show(p)


"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
 Changing the graph when items are selected
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """


p = figure(plot_width=400, plot_height=400, tools="tap", title="Select a circle")
renderer = p.circle([1, 2, 3, 4, 5], [2, 5, 8, 2, 7], size=50,

                    # set visual properties for selected glyphs
                    selection_color="firebrick",

                    # set visual properties for non-selected glyphs
                    nonselection_fill_alpha=0.2,
                    nonselection_fill_color="grey",
                    nonselection_line_color="firebrick",
                    nonselection_line_alpha=1.0)

# show(p)

"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Adding a hover tool
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """

from bokeh.models import HoverTool

source = ColumnDataSource(
        data=dict(
            x=[1, 2, 3, 4, 5],
            y=[2, 5, 8, 2, 7],
            desc=['A', 'b', 'C', 'd', 'E'],
        )
    )

hover = HoverTool(
        tooltips=[
            ("index", "$index"),
            ("(x,y)", "($x, $y)"),
            ("desc", "@desc"),
        ]
    )

p = figure(plot_width=300, plot_height=300, tools=[hover], title="Mouse over the dots")

p.circle('x', 'y', size=20, source=source)

show(p)


"""
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
Interactive circle plot
 -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------  """



from numpy.random import random

from bokeh.layouts import column, row
from bokeh.plotting import figure
from bokeh.models import ColumnDataSource, Select, TextInput
from bokeh.models.widgets import Slider
from bokeh.models import HoverTool

def get_data(N):
    return dict(x=random(size=N), y=random(size=N), r=random(size=N) * 0.03)

COLORS = ["black", "firebrick", "navy", "olive", "goldenrod"]

def modify_doc(doc):
    source = ColumnDataSource(data=get_data(200))

    p = figure( toolbar_location=None)
    r = p.circle(x='x', y='y', radius='r', source=source,
                 color="navy", alpha=0.6, line_color="white")


    select = Select(title="Color", value="navy", options=COLORS)
    input = TextInput(title="Number of points", value="200")

    def update_color(attrname, old, new):
        r.glyph.fill_color = select.value
    select.on_change('value', update_color)

    def update_points(attrname, old, new):
        N = int(input.value)
        source.data = get_data(N)
    input.on_change('value', update_points)

    layout = column(row(select, input, width=400), row(p))

    doc.add_root(layout)

show(modify_doc)
