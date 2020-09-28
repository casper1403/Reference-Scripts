"""
Casper van der Vliet
11052953
"""
from bokeh.io import output_file, show, output_notebook
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.palettes import brewer
from bokeh.io.doc import curdoc
from bokeh.models import Slider, HoverTool, Select, Dropdown
from bokeh.layouts import widgetbox, column
from transformation import get_data
import pandas as pd

frame = get_data()

def get_data(frame, data, year):

    """ Function that fetches the data for the visualization to use. Input is the dataframe, name of the dataset and the requested year
    Output is a dictionary for a  """

    dataDict = dict()
    # Select the data
    dataFrame = frame.loc[frame['data'] == data]
    # fetch the countries, xs and ys as well as the data for the year given as input
    dataDict['Country'] = dataFrame['NAME']
    dataDict['xs'] = dataFrame['xs']
    dataDict['ys'] = dataFrame['ys']
    dataDict['year'] = dataFrame[str(year)]

    # Determine which color distribution to use for every element in the dropdown menu
    if data == "Mobile subscriptions per 100 people":
        color_mapper.high = 180
    elif data == "Broadband subscriptions per 100 people":
        color_mapper.high = 50
    elif data == "Share of the population using the Internet":
        color_mapper.high = 100

    return dataDict

def update_data(attr,old,new):
    source.data = get_data(frame,dataType.value,yearSlider.value)

# create a source object
source = ColumnDataSource(data={'xs':frame['xs'],'ys':frame['ys'], 'year':[0 for i in range(10449)]})

#define a color palette and a color bar
palette = brewer['YlGnBu'][8]
palette = palette[::-1]
color_mapper = LinearColorMapper(palette = palette, low = 0, high = 140)
color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20, border_line_color=None,location = (0,0), orientation = 'horizontal')

#Create the figure object
p = figure(title=" World Map visualizion of The Difference in Internet Usage between 1990-2016 ",plot_width = 1750, plot_height = 900,  toolbar_location = None,  tools="hover", tooltips=[("Country", "@Country"),("Value","@year")])
p.patches('xs', 'ys', source=source, fill_color = {'field' : 'year', 'transform' : color_mapper}, line_color = 'black', line_width = 0.25, fill_alpha = 1)
p.axis.axis_label = None
p.axis.visible = False
p.grid.grid_line_color = None
p.add_layout(color_bar, 'below')

# add the dropdown menu and the slider.
dataType = Select(title="Data", value="Share of the population using the Internet", options=["Share of the population using the Internet", "Mobile subscriptions per 100 people", "Broadband subscriptions per 100 people"])
dataType.on_change('value', update_data)
yearSlider = Slider(start=1990, end=2016, value=1990, step=1, title="year")
yearSlider.on_change('value', update_data)

# Add the visualization to the server socket
layout = column(dataType,p,yearSlider)
curdoc().add_root(layout)
