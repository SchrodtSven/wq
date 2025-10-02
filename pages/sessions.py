# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
from dd import DD

sub_title = "Analyse der Sitzungen"
df = pd.read_csv('exporte/sessions.csv')
df['datum'] = pd.to_datetime(df['datum'],format='%Y-%m-%d')

df['Sitzung_min'] = round(df["session_duration"]/60, 2)
print(df.columns)
#fig_2 = fig = px.line(df_f, x="Jahr", y="Anzahl")

# Anfangsbelegung
#tmp = list(df.columns)
# Jahr ist obligatorisch (auf der X-Achse)
#del tmp[0]


opt = [{"label": k, "value": k} for k in DD.session_y]
start_val = DD.session_y
start_val = ["sessions"]
fig = px.line(df, x="datum", y=start_val)

register_page(__name__)

 
@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-check-item", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.line(df, x="datum", y=col_chosen, title=sub_title)
    return fig


layout = html.Div(
    [
        html.H3(sub_title),
        html.H4("Sitzungsverfolgung"),
        html.Div(className='custom-dropdown-style-2', children=[
        dcc.Dropdown(
            id="controls-and-check-item",
            options=opt,
            value=start_val,
            multi=True,
            #style={"backgroundColor": "black"},
        )]),
        dcc.Graph(figure=fig, id="controls-and-graph"),
         dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": x, "headerName": DD.col_transl[x]}
                for x in df.columns
            ],  
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        
    ]
)
