import dash
import pandas as pd
from dash import html, dcc, callback, Input, Output, dash_table
import xlwings as xw
import dash_mantine_components as dmc


dash.register_page(__name__)

layout = html.Div(children=[
    # html.H1(children='Projects Available', className='infralis_titles'),

    html.Div([
        dmc.Card(
            children=[
                dmc.CardSection(
                    dmc.Image(
                        # src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                        src="https://image.cnbcfm.com/api/v1/image/106852164-1615406420020-GettyImages-1162866632.jpg?v=1615406618",
                        height=100,
                    )
                ),
                dmc.Group(
                    [
                        dmc.Text("North Paraguay Wind Farm", weight=500),
                        dmc.Badge("70k USD", color="red", variant="light"),
                    ],
                    position="apart",
                    mt="md",
                    mb="xs",
                ),
                dmc.Text(
                    "This pre-development considers several feasible spots for wind farms in Northern Paraguay",
                    size="sm",
                    color="dimmed",
                ),
                dmc.Button(
                    "Go to Pre-Dev Summary",
                    variant="light",
                    color="blue",
                    fullWidth=True,
                    mt="md",
                    radius="md",
                ),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"width": 350},
        ),

        dmc.Card(
            children=[
                dmc.CardSection(
                    dmc.Image(
                        src="https://images.unsplash.com/photo-1527004013197-933c4bb611b3?ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&ixlib=rb-1.2.1&auto=format&fit=crop&w=720&q=80",
                        height=160,
                    )
                ),
                dmc.Group(
                    [
                        dmc.Text("Naamandu - Paraguayan Chaco", weight=500, className='infralis_timeVariable_table'),
                        dmc.Badge("70k USD", color="red", variant="light"),
                    ],
                    position="apart",
                    mt="md",
                    mb="xs",
                ),
                dmc.Text(
                    "Ideal for Green Hydrogen Development",
                    size="sm",
                    color="dimmed",
                    className=''
                ),
                dmc.Button(
                    "Book classic tour now",
                    variant="light",
                    color="blue",
                    fullWidth=True,
                    mt="md",
                    radius="md",
                ),
            ],
            withBorder=True,
            shadow="sm",
            radius="md",
            style={"width": 350},
        )

    ])

],className='regular_body')