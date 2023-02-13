import dash
import pandas as pd
from dash import html, dcc, callback, Input, Output, dash_table
import xlwings as xw


dash.register_page(__name__)


data = xw.Book('2C - Naamandu - FINANCIAL MODEL - working_file.xlsx').sheets('Time Variables').range(
    'a1:e18').value

df = pd.DataFrame(data = data)
df.columns = df.iloc[0]
df = df[1:]


layout = html.Div(children=[
    html.H1(children='Time Variables'),
	html.Div([
        "Select a city: ",
        dcc.RadioItems(['New York City', 'Montreal','San Francisco'],
        'Montreal',
        id='analytics-input')
    ]),
	html.Br(),
    html.Div(id='analytics-output'),
    html.Div(children=[dash_table.DataTable(
        data = df.to_dict('records'),
        style_data  = {'font-size' : '10px',
                        'font-family' : 'Inter Medium'}
    )
    ])

])

@callback(
    Output(component_id='analytics-output', component_property='children'),
    Input(component_id='analytics-input', component_property='value'),
)
def update_city_selected(input_value):
    return f'You selected: {input_value}'