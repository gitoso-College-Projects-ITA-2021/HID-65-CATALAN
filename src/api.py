import os
import requests
import logging

logger = logging.getLogger(__name__)

import plotly.express as px
from datetime import datetime

url = 'https://api.tecsus.com.br/v0/smartmeter/get_simple_data'

headers = {
    'x-api-key': os.environ['TECSUS_API_KEY']
}

def get_consumption(device_id, dt_start, dt_end):
    params = {
        'device_id': device_id,
        'dt_start' : dt_start,
        'dt_end': dt_end
    }

    req = requests.get(url, headers=headers, params=params).json()

    if req['error']:
        logger.error(f"Request failed with messsage: { req['msg'] }")
        exit

    data = [d['name'] for d in req['data']]

    logger.info("Request info:")
    logger.info("msg     = {}".format(req['msg']))
    logger.info("device  = {}".format(req["device_name"]))
    logger.info("data    = {}".format(data))

    raw_measures = req['data'][0]['measures']

    measures = []
    measures_time = []
    measures_accumulated = []

    for raw_measure in raw_measures:
        measures.append(raw_measure['measure'])
        measures_time.append(datetime.fromtimestamp(raw_measure['measure_unixtime']))
        measures_accumulated.append(raw_measure['measure_accumulated'])

    # Média Móvel
    mm_range = 10
    measures_mm = []
    for idx in range(len(measures) - mm_range):
        measures_range = measures[idx:idx+mm_range]
        measures_mm.append( sum(measures_range) / len(measures_range) )
    measures_time_mm = measures_time[mm_range:]

    fig = px.line(x=measures_time_mm, y=measures_mm, title=f'Consumo: {req["device_name"]}')
    fig.update_xaxes(title="Data")
    fig.update_yaxes(title="Consumo [???]")
    return fig
