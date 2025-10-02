# Whisky Online Shop Data analysis & prediction stuff
# Projekt "Data on the rox"
# AUTHOR 
# SINCE 2025-09-26

# 3rd party libs
from dash import (
    Dash,
    html,
    page_registry,
    page_container,
    clientside_callback,
    Input,
    Output,
    dcc,
    Patch
)
import dash_mantine_components as dmc
import dash_bootstrap_components as dbc
from dash_bootstrap_templates import load_figure_template
import dash
from dd import DD

templates = [
    "bootstrap",
    "minty",
    "pulse",
    "flatly",
    "quartz",
    "cyborg",
    "darkly",
    "vapor",
]

load_figure_template(templates)

# This stylesheet defines the "dbc" class.  Use it to style dash-core-components
# and the dash DataTable with the bootstrap theme.
dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates/dbc.min.css"
#dbc_css = "https://cdn.jsdelivr.net/gh/AnnMarieW/dash-bootstrap-templates@master/dbc.css"

#   dbc_css = "https://cdn.jsdelivr.net/npm/bootstrap@5.3.6/dist/css/bootstrap.min.css"
    

app = Dash(
    __name__,
    use_pages=True,
    external_stylesheets=[dbc_css,dbc.themes.SLATE,], # 
    suppress_callback_exceptions=True,
)
app.title = '“Data on the rocks”: Datenanalyse und Vorhersagen'
#dash.register_page(__name__)
navbar = dbc.NavbarSimple(
    [   
        # dbc.DropdownMenu(
        #     [
        #         dbc.DropdownMenuItem(DD.pages[page["name"]], href=page["path"])
        #         for page in page_registry.values()
        #         if page["module"] != "pages.not_found_404"
        #     ],
        #     #menu_variant= 'dark',
        #     nav=True,
        #     label="Auswahl",
        # ),
        html.Div(
                    dcc.Link(f"| {page['name']} ", href=page["path"]),
                )
                for page in dash.page_registry.values()
    ],
    brand=app.title,
    color="primary",
    dark=False,
    className="mb-2",
)
server = app.server
app.layout = dbc.Container(
    [navbar, page_container], 
    fluid=True, 
    #className="dbc"
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=8888)
    
