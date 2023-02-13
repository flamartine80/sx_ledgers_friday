import dash
import pandas as pd
from dash import html, dcc, callback, Input, Output, dash_table, State
import xlwings as xw
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc


dash.register_page(__name__)

offcanvas = html.Div(
    [
        dbc.Button("Open Offcanvas", id="open-offcanvas", n_clicks=0),
        dbc.Offcanvas(
            html.P(
                "This is the content of the Offcanvas. "
                "Close it by clicking on the close button, or "
                "the backdrop."
            ),
            id="offcanvas",
            title="Title",
            is_open=False,
        ),
    ]
)


layout = offcanvas

@callback(
    Output("offcanvas", "is_open"),
    Input("open-offcanvas", "n_clicks"),
    State("offcanvas", "is_open")
    ,
)
def toggle_offcanvas(n1, is_open):
    if n1:
        return not is_open
    return is_open