import pandas as pd

from ast import literal_eval

from dash import Dash, html, dcc, callback, Output, Input, dash_table
import dash_bootstrap_components as dbc

import plotly.graph_objects as go

from cardimages import get_card_image


df = pd.read_csv("./data/cardprices.csv").drop("meta", axis=1)

app = Dash(
    __name__, suppress_callback_exceptions=False
)  # Supress errors because the table with id "tbl" does not exist yet on startup


app.layout = dbc.Container(
    [
        html.H1(children="MTG Card Track", style={"textAlign": "center"}),
        dcc.Dropdown(
            df.name.unique(), id="dropdown-selection", placeholder="Select a card"
        ),
        # Container to store the data returned by searching through the df
        dcc.Store(id="current-data"),
        # Visual representation of data as table
        html.Div(
            id="tbl-container", children=dash_table.DataTable(id="tbl")
        ),  # empty by default
        # Showing which line of the df was selected
        dbc.Alert(id="tbl-out"),
        html.Img(id="card-image", alt="image"),
        html.Div(id="graph-container", children=dcc.Graph(id="price-graph")),
    ]
)


@callback(Output("current-data", "data"), Input("dropdown-selection", "value"))
def update_df(value):
    if not value:
        return None

    data = df[df.name == value]  # .drop("data", axis=1)

    return data.to_dict(orient="records")


@callback(Output("tbl-container", "children"), Input("current-data", "data"))
def update_df(data):
    if not data:
        return None

    selected_df = pd.DataFrame.from_dict(data).drop("data", axis=1)

    return dash_table.DataTable(
        selected_df.to_dict(orient="records"),
        [{"name": i, "id": i} for i in selected_df.columns],
        id="tbl",
    )


@callback(Output("tbl-out", "children"), Input("tbl", "active_cell"))
def update_selection(active_cell):
    return str(active_cell) if active_cell else "Click the table"


@callback(
    Output("graph-container", "children"),
    Input("current-data", "data"),
    Input("tbl", "active_cell"),
)
def update_graph(data, active_cell):
    if not data or not active_cell:
        return None

    selected_df = pd.DataFrame.from_dict(data)

    row = active_cell["row"]

    fig = go.Figure()

    try:
        single_cardprice = pd.DataFrame.from_dict(
            literal_eval(selected_df.iloc[row]["data"])["paper"]["cardmarket"]["retail"]
        )

        for version in single_cardprice.columns:
            fig.add_trace(
                go.Scatter(
                    x=single_cardprice.index, y=single_cardprice[version], name=version
                ),
            )

        fig.update_layout(legend_title_text="Version")

        fig.update_yaxes(ticksuffix=" €")

        return dcc.Graph(figure=fig)

    except KeyError:
        print("Card does not have paper pricing.")


@callback(
    Output("card-image", "src"),
    Input("current-data", "data"),
    Input("tbl", "active_cell"),
)
def show_cardimage(data, active_cell):
    if not data or not active_cell:
        return None

    selected_df = pd.DataFrame.from_dict(data)

    row = active_cell["row"]

    single_card = selected_df.iloc[row]

    img = get_card_image(single_card["name"], single_card["setCode"])["small"]

    return img


if __name__ == "__main__":
    app.run(debug=True)
