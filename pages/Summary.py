import dash
from dash import html, dcc

dash.register_page(__name__, path='/')

layout = html.Div(children=[
    html.H1(children='Project Summary'),

    html.Div(children='''
        Summary
    '''),

],className='sx_body')