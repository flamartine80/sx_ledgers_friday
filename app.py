import dash
from dash import Dash, html, dcc

app = Dash(__name__, use_pages=True)

# app.layout = html.Div([
#     html.Div(className='regular_sidebar'),
#     html.Div(className='regular_body'),
#     html.Img( src=app.get_asset_url('infralis_dark.png' ), className='item_centering' ),
#
#     html.Div(
#         [
#             html.Button(
#                 dcc.Link(
#                     f"{page['name']}", href=page["relative_path"], className="spheader_renewed_button"
#                 )
#             )
#             for page in dash.page_registry.values()
#         ]
#     ),
#
# 	dash.page_container
# ])

app.layout = html.Div([
    html.Div([html.Img( src=app.get_asset_url( 'DeafultSonnedixLogo.png' ), style={"height":"10%", "width":"50%"}, ),
              html.Div( [
        html.Div(
        [html.Button( dcc.Link( f"{page['name']}", href=page["relative_path"], className='sidebarInfralis_button' ) )
            for page in dash.page_registry.values()],className="sidebarInfralis_buttonCentering" ), ] ),

    ],className='regular_sidebar'),
	dash.page_container
], )

if __name__ == '__main__':
	app.run_server(debug=True)