# Sitzungsverfolgung
from dash import Dash, html, dash_table, dcc, callback, Output, Input, register_page
import plotly.express as px
import pandas as pd
import dash_ag_grid as dag
    
from dd import DD
    
sub_title = DD.pages['Sales']
df = pd.read_csv('Whiskyquartier_Rohdaten/products.csv')
#df['Tag'] = pd.to_datetime(df['Tag'],format='%Y-%m-%d')
#print(df.columns)
#fig_2 = fig = px.line(df_f, x="Jahr", y="Anzahl")
 
# Anfangsbelegung
#tmp = list(df.columns)
# Jahr ist obligatorisch (auf der X-Achse)
#del tmp[0]

colz = ["prod_name","invent_start","invent_end","sold_units","sell_rate"]
strt_colz = ["prod_name"]
 
#opt = [{"label": k, "value": k} for k in colz]
#fig = px.line(df, x="Tag", y=strt_colz, color='Vertriebskanal')


register_page(__name__)

layout = html.Div(
    [
        html.H3(sub_title),
        dag.AgGrid(
            id="main_grid_basic",
            rowData=df.to_dict("records"),
            columnDefs=[
                {"field": x, "headerName": x}
                for x in colz
            ],  
            columnSize="responsiveSizeToFit",
            dashGridOptions={"pagination": True},
        ),
        
    ]
)
