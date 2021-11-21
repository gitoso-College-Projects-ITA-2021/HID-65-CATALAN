import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', 
    datefmt='%m/%d/%Y %I:%M:%S %p',
    level=logging.INFO
)

import dash
import dash_bootstrap_components as dbc

import api, layout

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

params = {
    'device_id': '198762435721298897478401',
    'dt_start': '2021-10-01 00:00:00',
    'dt_end': '2021-10-30 00:00:00'
}

fig = api.get_consumption(params['device_id'], params['dt_start'], params['dt_end'])
app.layout = layout.build_layout(fig)

if __name__ == '__main__':
    app.run_server(debug=True)
