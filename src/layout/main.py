from dash import dcc, html
import dash_bootstrap_components as dbc
from datetime import date
from datetime import datetime


def build_layout(dt_start, dt_end, consumo_conv, custo_conv, consumo_branca, custo_branca, fig):

    layout = html.Div(
        [
            _build_title(),

            _build_options(),

            _build_header(dt_start, dt_end, consumo_conv, custo_conv, consumo_branca, custo_branca),
            
            _build_graph(fig)
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
                    "Últimos 3 Meses", 
                    color="secondary", 
                    className="me-1",
                    id='btn-last-3months',
                    n_clicks=0
                ),
                dbc.Button(
                    "Últimos 2 Meses", 
                    color="secondary", 
                    className="me-1",
                    id='btn-last-2months',
                    n_clicks=0
                ),
                dbc.Button(
                    "Último Mês", 
                    color="secondary", 
                    className="me-1",
                    id='btn-last-month',
                    n_clicks=0
                ),
            ]),
        ]
    )

def _build_header(dt_start, dt_end, consumo_conv, custo_conv, consumo_branca, custo_branca):
    if dt_start == None or dt_end == None or consumo_conv == None or custo_conv == None or consumo_branca == None or custo_branca == None:
        return html.Div([
                    html.Hr(className="my-2"),
                    html.H6(f'Selecione um período para realizar o cálculo das tarifas', className="display-5", id='range'),
                    html.Br(),
                    html.H6("", id='consumo', className="display-6"),
                    html.H6("", id='custo-conv', className="display-6"),
                    html.H6("", id='custo-branca', className="display-6"),
                ],
                className="bg-light",
                style = {
                    'textAlign': 'center'
                }
            )
    
    in_date_format_str = '%Y-%m-%d %H:%M:%S'
    start_date = datetime.strptime(dt_start, in_date_format_str)
    end_date = datetime.strptime(dt_end, in_date_format_str)

    out_date_format_str = '%d/%m/%Y'
    start_date = start_date.strftime(out_date_format_str)
    end_date = end_date.strftime(out_date_format_str)

    return html.Div([
                    html.Hr(className="my-2"),
                    html.H6(f'Datas: {start_date} a {end_date}', className="display-5", id='range'),
                    html.Br(),
                    html.H6(f"Consumo: {consumo_conv:.2f} kWh", id='consumo', className="display-6"),
                    html.H6(f"Tarifa Convencional: R$ {custo_conv:.2f}", id='custo-conv', className="display-6"),
                    html.H6(f"Tarifa Branca: R$ {custo_branca:.2f}", id='custo-branca', className="display-6"),
                ],
                className="bg-light",
                style = {
                    'textAlign': 'center'
                }
            )

def _build_graph(fig):
    if fig == None:
        return dcc.Graph(
                id='consumo-no-tempo',
                figure = {
                    'data': []
                }
            )
    
    return dcc.Graph(
                id='consumo-no-tempo',
                figure=fig
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

