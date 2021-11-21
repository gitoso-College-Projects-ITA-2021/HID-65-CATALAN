from datetime import datetime
import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)

import dash
import dash_bootstrap_components as dbc

import api, layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])
app.title = 'Projeto CATALAN'

# Default: Actual Month Consumption
date_format_str = '%Y-%m-%d %H:%M:%S'
today = datetime.today()
first_day_month = today.replace(day=1)

params = {
    'device_id': '198762435721298897478401',
    'dt_start': first_day_month.strftime(date_format_str),
    'dt_end': today.strftime(date_format_str)
}

fig = api.get_consumption(params['device_id'], params['dt_start'], params['dt_end'])
app.layout = layout.build_layout(fig)

if __name__ == '__main__':
    app.run_server(debug=True)
