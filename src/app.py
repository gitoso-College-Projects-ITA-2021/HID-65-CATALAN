from datetime import datetime, timedelta
from dateutil import relativedelta
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)

import dash
import dash_bootstrap_components as dbc
from dash.dependencies import Input, Output

import api, layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Projeto CATALAN'

# Default: Actual Month Consumption
date_format_str = '%Y-%m-%d %H:%M:%S'
today = datetime.today()
first_day_month = today.replace(day=15)
#first_day_month = today.replace(day=1)

params = {
    'device_id': '198762435721298897478401',
    'dt_start': first_day_month.strftime(date_format_str),
    'dt_end': today.strftime(date_format_str)
}

#(consumo_conv, custo_conv, consumo_branca, custo_branca, fig) = api.get_consumption(params['device_id'], params['dt_start'], params['dt_end'])
(consumo_conv, custo_conv, consumo_branca, custo_branca, fig) = (None, None, None, None, None)
app.layout = layout.build_layout(params['dt_start'], params['dt_end'], consumo_conv, custo_conv, consumo_branca, custo_branca, fig)

@app.callback(
    [Output('custo-conv', 'style'), Output('custo-branca', 'style'), Output('range', 'children'), Output('consumo', 'children'), Output('custo-conv', 'children'), Output('custo-branca', 'children'), Output('consumo-no-tempo', 'figure')],
    Input('btn-last-3months', 'n_clicks'),
    Input('btn-last-2months', 'n_clicks'),
    Input('btn-last-month', 'n_clicks'),
)
def calculate_3months(btn3months, btn2months, btn1month):
    changed_id = [p['prop_id'] for p in dash.callback_context.triggered][0]

    if 'btn-last-3months' in changed_id:
        first_day = datetime.today() - relativedelta.relativedelta(months=3)
        last_day = datetime.today()
    elif 'btn-last-2months' in changed_id:
        first_day = datetime.today() - relativedelta.relativedelta(months=2)
        last_day = datetime.today()
    elif 'btn-last-month' in changed_id:
        first_day = datetime.today().replace(day=1)
        last_day = datetime.today()
    else:
        return

    out_date_format_str = '%d/%m/%Y'
    start_date = first_day.strftime(out_date_format_str)
    end_date = last_day.strftime(out_date_format_str)
    range_str = f'Consumo de {start_date} a {end_date}'
    (consumo_conv_style, consumo_branca_style, consumo_str, custo_conv_str, custo_branca_str, fig) =  calculate_for_period(first_day, last_day)
    
    return [consumo_conv_style, consumo_branca_style, range_str, consumo_str, custo_conv_str, custo_branca_str, fig]


def calculate_for_period(first_day, last_day):
    params = {
        'device_id': '198762435721298897478401',
        'dt_start': first_day.strftime(date_format_str),
        'dt_end': last_day.strftime(date_format_str)
    }
    (consumo_conv, custo_conv, consumo_branca, custo_branca, fig) = api.get_consumption(params['device_id'], params['dt_start'], params['dt_end'])
    
    if float(consumo_conv) < float(consumo_branca):
        consumo_conv_style = {'color': 'green'}
        consumo_branca_style = {'color': 'red'}
    else:
        consumo_conv_style = {'color': 'red'}
        consumo_branca_style = {'color': 'green'}


    consumo_str = f"Consumo: {consumo_conv:.2f} kWh"
    custo_conv_str = f"Tarifa Convencional: R$ {custo_conv:.2f}"
    custo_branca_str = f"Tarifa Branca: R$ {custo_branca:.2f}"
    return (consumo_conv_style, consumo_branca_style, consumo_str, custo_conv_str, custo_branca_str, fig)

if __name__ == '__main__':
    app.run_server(host='0.0.0.0', debug=False)
