"""
Dash is an interactive python library build to create interactive web apps with data visualizations.

This handbook will consist of the following topics

- Layout

"""

"""
        Dash apps are composed of two parts.
        The first part is the "layout" of the app and it describes what the application looks like.
        The second part describes the interactivity of the application and will be covered in the next chapter.

        Dash provides Python classes for all of the visual components of the application.
        We maintain a set of components in the dash_core_components and the dash_html_components library
        but you can also build your own with JavaScript and React.js.

"""
# download componants
import dash
# The core componants consist of various dash componants like graphs, dropdowns, slider, etc
import dash_core_components as dcc
# The html componant provide you with the html needed
import dash_html_components as html

# styling file
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

# Create and instance of the dash app
app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

# define colors for the app to use
colors = {
    'background': '#111111',
    'text': '#7FDBFF'
}


# Here you can devine the layour of the app.
# You can add html elements by the dash_html_components
# Dash is declaritive which means all things are describes through keyword arguments
app.layout = html.Div(style={'backgroundColor': colors['background']}, children=[
    html.H1(children='Hello Dash',
        style={
                'textAlign': 'center',
                'color': colors['text']
             }
        ),

    # by convention the childrens attribute is always first it can contain a string, a number, a single component, or a list of components.
    html.Div(children='''
        Dash: A web application framework for Python.
    '''),

    # create a graph, here you specify every keywork argument to provide information about the graph.
    dcc.Graph(
        id='example-graph',
        figure={
            'data': [
                {'x': [1, 2, 3], 'y': [4, 1, 2], 'type': 'bar', 'name': 'SF'},
                {'x': [1, 2, 3], 'y': [2, 4, 5], 'type': 'bar', 'name': u'Montréal'},
            ],
            'layout': {
                'title': 'Dash Data Visualization',
            }
        }
    )
])

# if __name__ == '__main__
#     app.run_server(debug=True)


"""
By writing markup in python we can create complex reusable componants.
An example is a html table
"""

import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

# fetch data
df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/c78bf172206ce24f77d6363a2d754b59/raw/c353e8ef842413cae56ae3920b8fd78468aa4cb2/usa-agricultural-exports-2011.csv')


# reusable function with dataframe as input
def generate_table(dataframe, max_rows=10):
    # return html table
    return html.Table([
        # table header
        html.Thead(
        # loop over df columns to create table columns
            html.Tr([html.Th(col) for col in dataframe.columns])
        ),
        #  Double loop the create the columns
        html.Tbody([
            html.Tr([
                html.Td(dataframe.iloc[i][col]) for col in dataframe.columns]) for i in range(min(len(dataframe), max_rows))
        ])
    ])


external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

app.layout = html.Div(children=[
    html.H4(children='US Agriculture Exports (2011)'),
    generate_table(df)
])

# if __name__ == '__main__':
#     app.run_server(debug=True)


""" The dash Graph attribute can compute graphical interfaces """


import dash
import dash_core_components as dcc
import dash_html_components as html
import pandas as pd

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

df = pd.read_csv('https://gist.githubusercontent.com/chriddyp/5d1ea79569ed194d432e56108a04d188/raw/a9f9e8076b837d541398e999dcbac2b2826a81f8/gdp-life-exp-2007.csv')


app.layout = html.Div([
    dcc.Graph(
        id='life-exp-vs-gdp',
        figure={
            'data': [
                dict(
                    x=df[df['continent'] == i]['gdp per capita'],
                    y=df[df['continent'] == i]['life expectancy'],
                    text=df[df['continent'] == i]['country'],
                    mode='markers',
                    opacity=0.7,
                    marker={
                        'size': 15,
                        'line': {'width': 0.5, 'color': 'white'}
                    },
                    name=i
                ) for i in df.continent.unique()
            ],
            'layout': dict(
                xaxis={'type': 'log', 'title': 'GDP Per Capita'},
                yaxis={'title': 'Life Expectancy'},
                margin={'l': 40, 'b': 40, 't': 10, 'r': 10},
                legend={'x': 0, 'y': 1},
                hovermode='closest'
            )
        }
    )
])

if __name__ == '__main__':
    app.run_server(debug=True)
