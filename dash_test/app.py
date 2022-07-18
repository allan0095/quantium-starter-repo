# Run this app with `python app.py` and
# visit http://127.0.0.1:8050/ in your web browser.

from dash import Dash, html, dcc, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

# assume you have a "long-form" data frame
# see https://plotly.com/python/px-arguments/ for more options
df = pd.read_csv('data/pink_morsel_sales.csv')

new_names = {}
regions = []
for i in df.region.unique():
    new_names[i] = i.title()
    regions.append(i.title())

regions.append('All')
my_input = 'North'

app.layout = html.Div(children=[
    html.H1(children='Pink Morsel - Soul Foods',
            id='header',
            className="app-header--title",
            style={'textAlign': 'center'}),

    html.Div(children=[
            html.Label('Select region:', style={'font-size': '20px', 'font-weight': 'bold'}),
            dcc.RadioItems(regions, my_input, id='category')
            ], style={'padding': 10, 'flex': 1, 'text-align': 'center'}),

    dcc.Graph(
        id='indicator-graphic'
    )
])

@app.callback(
    Output(component_id='indicator-graphic', component_property='figure'),
    Input(component_id='category', component_property='value')
)
def update_graph(region):

    if region == 'All':
        mask = [True] * len(df.index)
    else:
        mask = df.region == region.lower()

    fig = px.line(df[mask], x="date", y="sales", color="region", title='Sales by Region',
                  labels={'date': 'Date', 'sales': 'Sales (AU$)', 'region': 'Region'})

    fig.for_each_trace(lambda t: t.update(name=new_names[t.name],
                                          legendgroup=new_names[t.name],
                                          hovertemplate=t.hovertemplate.replace(t.name, new_names[t.name])
                                          )
                       )
    fig.update_layout(
        font = dict(family = 'Roboto',
                    size = 16),
        font_color='#000000',
        title_font_color='#000000')
    return fig

if __name__ == '__main__':
    app.run_server(debug=True)
