from dash import dcc, html
import dash_bootstrap_components as dbc
from datetime import date


def build_layout(fig):
    layout = html.Div(
        [
            _build_title(),

            _build_options(),

            _build_options2(),

            dcc.Graph(
                id='consumo-no-tempo',
                figure=fig
            )
        ],
        className="bg-light",
    )
    return layout


def _build_title():
    return html.Div(
        dbc.Container(
            [
                html.H1('Monitor de Tarifa Branca', className="display-3"),
                html.Hr(className="my-2"),
            ],
            fluid=True,
            className="py-3",
        ),
        className="p-3 bg-light rounded-3",
    )
    return dbc.Jumbotron(
            children='Monitor de Tarifa Branca',
            style={
                'textAlign': 'center'
            }
    )


def _build_options():
    return dbc.Container(
        [
            dbc.ButtonGroup([
                dbc.Button(
                    "Último Mês", 
                    color="secondary", 
                    className="me-1"
                ),
                dbc.Button(
                    "Última Semana", 
                    color="secondary", 
                    className="me-1"
                ),
                dbc.Button(
                    "Últimas 24h", 
                    color="secondary", 
                    className="me-1"
                ),
                dbc.Button(
                    "Últimas 12h", 
                    color="secondary", 
                    className="me-1",
                ),
                dbc.Button(
                    "Última Hora", 
                    color="secondary", 
                    className="me-1"
                ),
            ]),
        ]
    )

def _build_options2():
    return dbc.Container(
        [
            dbc.ButtonGroup([
                dcc.DatePickerRange(
                    id='date-picker-range',
                    start_date=date(1997, 5, 3),
                    end_date_placeholder_text='Select a date!'
                )
            ]),
            dbc.Button(
                "Intervalo Personalizado", 
                color="secondary", 
                className="me-1"
            ),
        ]
    )