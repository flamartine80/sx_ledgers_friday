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
    html.Div([html.Img( src=app.get_asset_url('SONNEDIX_WHT(transparent)_RGB.png'), style={"height":"15%",
                                                                                           "width":"75%"}, ),
              html.Div([
        html.Div(
        # [html.Button( dcc.Link( f"{page['name']}", href=page["relative_path"]) )
        # [html.Button( dcc.Link( f"{page['name']}", href=page["relative_path"], className='button_sx' ) )
        [html.Button( dcc.Link( f"{page['name']}", href=page["relative_path"],className='link_sx' ),
                      className='button_sx'  )
            for page in dash.page_registry.values()],className='parent-container_sx' ), ] ),


    ],className='regular_sidebar'),
	dash.page_container
], )

if __name__ == '__main__':
	app.run_server(debug=True)