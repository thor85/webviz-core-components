import dash
import dash_html_components as html
import webviz_core_components


def test_colorscale(dash_duo):

    app = dash.Dash(__name__)

    app.layout = html.Div(
        [
            webviz_core_components.ColorScales(
                id="colorscale",
                colorscale=["red", "blue"],
                nSwatches=12,
                fixSwatches=False,
            ),
        ]
    )

    dash_duo.start_server(app)

    assert dash_duo.get_logs() == [], "browser console should contain no error"
