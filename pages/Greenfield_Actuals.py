import dash
import pandas as pd
from dash import html, dcc, callback, Input, Output, dash_table, State
import xlwings as xw
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
import dash_ag_grid as dag
# import yfinance as yf
import psycopg2
# from sx_ledgers_writedb import conn

dash.register_page(__name__)
#
#
# data = {
#     "ticker": ['bse','hur','pip','coor','ryui','jorgt','futew','partl'],
#     # "company": [name for name in equities.values()],
#     "quantity": [75, 40, 100, 50, 40, 60, 20, 40],
#     # "price": [last_close(ticker) for ticker in equities],
#     "position": ["buy", "sell", "hold", "hold", "hold", "hold", "hold", "hold"],
#     "comments": ["Notes" for i in range(8)],
# }
#
# columnDefs = [
#     {
#         "headerName": "Stock Ticker",
#         "field": "ticker",
#     },
#     {
#         "headerName": "Shares",
#         "field": "quantity",
#         "type": "rightAligned",
#         "filter": "agNumberColumnFilter",
#         "editable": True,
#     },
#     # {
#     #     "headerName": "Last Close Price",
#     #     "field": "price",
#     #     "type": "rightAligned",
#     #     "filter": "agNumberColumnFilter",
#     #     "valueFormatter": {"function": "d3.format('$,.2f')(params.value)"},
#     #     "cellRenderer": "agAnimateShowChangeCellRenderer",
#     # },
#     # {
#     #     "headerName": "Market Value",
#     #     "type": "rightAligned",
#     #     "filter": "agNumberColumnFilter",
#     #     "valueGetter": {"function": "Number(params.data.price) * Number(params.data.quantity)"},
#     #     "valueFormatter": {"function": "d3.format('$,.2f')(params.value)"},
#     #     "cellRenderer": "agAnimateShowChangeCellRenderer",
#     # },
#     {
#         "headerName": "Position",
#         "field": "position",
#         "editable": True,
#         "cellEditor": "agSelectCellEditor",
#         "cellEditorParams": {
#             "values": ["buy", "sell", "hold"],
#         },
#     },
#     {
#         "headerName": "Comments",
#         "field": "comments",
#         "editable": True,
#         "cellEditorPopup": True,
#         "cellEditor": "agLargeTextCellEditor",
#     },
# ]
#
# defaultColDef = {
#     "filter": True,
#     "resizable": True,
#     "sortable": True,
#     "editable": False,
#     "floatingFilter": True,
#     "minWidth": 125,
# }
#
#
# df = pd.DataFrame(data)
#
# table = dag.AgGrid(
#     id="portfolio-grid",
#     className="ag-theme-alpine-dark",
#     columnDefs=columnDefs,
#     rowData=df.to_dict("records"),
#     columnSize="sizeToFit",
#     defaultColDef=defaultColDef,
#     # cellStyle=cellStyle,
#     dashGridOptions={"undoRedoCellEditing": True, "rowSelection": "single"},
# )
# conn_2 = psycopg2.connect( database='sonnedix_chile', user='postgres', password='Rondamon_1988',
#                           host='database-2.culhcfcdryty.us-east-2.rds.amazonaws.com',
#     port='5432' )


conn_2 = psycopg2.connect( database='sx_chile_local', user='postgres', password='Zenon_1917',
                         host='localhost',port='5432' )
#
# @callback(
#  Output('display_table_section','children'),
#  Input('display_table_button','n_clicks'),
# )
# def display_records_table(display_table_button):
#     if True:
#         conn = conn_2
#         cur = conn.cursor()
#         read_table_b_query = "SELECT * FROM table_b "
#         with conn as connection:
#             dv = pd.read_sql(read_table_b_query, connection )
#             return html.Div(children=[dash_table.DataTable( data=dv.to_dict( 'records' ),
#                                      columns=[{'name': str( col ), 'id': str( col )} for col in dv.columns],
#                                      style_data={'color': 'black', 'backgroundColor': 'white' },
#                                      style_cell={'font-family':'Inter'})],className='input_revenue_card')



conn = conn_2
cur = conn.cursor()
read_table_b_query = "SELECT * FROM consolidated_info_2 "
with conn_2 as connection:
    dv = pd.read_sql(read_table_b_query, connection )

table = html.Div(children=[dash_table.DataTable( data=dv.to_dict( 'records' ),
                             columns=[{'name': str( col ), 'id': str( col )} for col in dv.columns],
                             style_data={'color': 'white', 'backgroundColor': 'black' },
                             style_cell={'font-family':'Arial'},
                             style_table={'height':'400px','overflowY': 'auto'})],className='sx_table')



layout  = html.Div([
    html.Div([
        html.H1('TEST'),
    ]),
    html.Div([
        table
    ],className='sx_body'),
],className='sx_container')

# @callback(
#     Output("offcanvas", "is_open"),
#     Input("open-offcanvas", "n_clicks"),
#     State("offcanvas", "is_open")
#     ,
# )
# def toggle_offcanvas(n1, is_open):
#     if n1:
#         return not is_open
#     return is_open