import geopandas as gpd
import pandas as pd
import shapely
import pycountry
from IPython.display import display
from bokeh.io import output_file, show, output_notebook
from bokeh.models import GeoJSONDataSource, LinearColorMapper, ColorBar, ColumnDataSource
from bokeh.plotting import figure, curdoc
from bokeh.palettes import brewer
from bokeh.io.doc import curdoc
from bokeh.models import Slider, HoverTool, Select, Dropdown
from bokeh.layouts import widgetbox, column
import pandas as pd

gdf = pd.read_json('geoframeCont.json')

df = pd.read_csv('obisityCleaned.csv')

df = df.drop(columns=['Unnamed: 0', 'Unnamed: 0.1'])

gdf = pd.merge(gdf,df,right_on='ISO3',left_on='ISO3')

gdf = gdf.loc[gdf['Continent_Name'] == 'Europe']


# source = ColumnDataSource(data={'xs':gdf['xs'],'ys':gdf['ys']})
#
# #define a color palette and a color bar
# palette = brewer['YlGnBu'][8]
# palette = palette[::-1]
# color_mapper = LinearColorMapper(palette = palette, low = 0, high = 140)
# color_bar = ColorBar(color_mapper=color_mapper, label_standoff=8,width = 500, height = 20, border_line_color=None,location = (0,0), orientation = 'horizontal')
#
# #Create the figure object
# p = figure(title=" World Map visualizion of The Difference in Internet Usage between 1990-2016 ",plot_width = 1750, plot_height = 900,  toolbar_location = None,  tools="hover", tooltips=[("Country", "@Country"),("Value","@year")])
# p.patches('xs', 'ys', source=source,  line_color = 'black', line_width = 0.25, fill_alpha = 1)
# p.axis.axis_label = None
# p.axis.visible = False
# p.grid.grid_line_color = None
# p.add_layout(color_bar, 'below')
#
# # Add the visualization to the server socket
# layout = column(p)
# curdoc().add_root(layout)
