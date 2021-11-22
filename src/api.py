import os
import requests
import logging

logger = logging.getLogger(__name__)

import plotly.express as px
from datetime import datetime
from datetime import timedelta

url = 'https://api.tecsus.com.br/v0/smartmeter/get_simple_data'

headers = {
    'x-api-key': os.environ['TECSUS_API_KEY']
}

def get_consumption(device_id, dt_start, dt_end):
    params_array = break_daterange_in_periods(device_id, dt_start, dt_end)

    measures = []
    measures_time = []
    measures_accumulated = []

    for params in params_array:
        # Send request
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
        for raw_measure in raw_measures:
            measures.append(raw_measure['measure'])
            measures_time.append(datetime.fromtimestamp(raw_measure['measure_unixtime']))
            measures_accumulated.append(raw_measure['measure_accumulated'])

    (consumo_conv, custo_conv) = custo_convencional(measures)
    (consumo_branca, custo_branca) = custo_tarifa_branca(measures, measures_time)

    # Suaviza Intervalos (deixar consumo mais constante)
    measures_smooth = []
    measures_time_smooth = []
    measures_accumulated_smooth = []

    measures_smooth.append(measures[0])
    measures_time_smooth.append(measures_time[0])
    measures_accumulated_smooth.append(measures_accumulated[0])

    for i in range(1,len(measures)):
        delta_time_minutes = round((measures_time[i] - measures_time[i-1]).total_seconds() / 60)
        
        if delta_time_minutes > 5:
            multiplier = round(delta_time_minutes / 5)
            for j in range(multiplier):
                measures_smooth.append(measures[i] / multiplier)
                measures_time_smooth.append(measures_time[i-1] + timedelta(minutes=(j+1)*5))
            pass
        else:
            measures_smooth.append(measures[i])
            measures_time_smooth.append(measures_time[i])

    # Média Móvel
    mm_range = 5
    measures_mm = []
    for idx in range(len(measures_smooth) - mm_range):
        measures_range = measures_smooth[idx:idx+mm_range]
        #print(f'{measures_range} - {len(measures_range)}')
        measures_mm.append( sum(measures_range) / len(measures_range) )
    measures_time_mm = measures_time_smooth[mm_range:]

    fig = px.line(x=measures_time_smooth, y=measures_smooth, title=f'Dispositivo: {req["device_name"]}')
    fig.update_xaxes(title="Data")
    fig.update_yaxes(title="Consumo [Wh]")
    return (consumo_conv, custo_conv, consumo_branca, custo_branca, fig)

def seleciona_tarifa(hours, minutes):
    total_minutes = hours*60 + minutes
    
    if total_minutes <= 16*60 + 30 or total_minutes >= 21*60 + 30:
        return 'ponta'
    elif total_minutes <= 17*60 + 30 or total_minutes >= 20*60 + 30:
        return 'intermediario'
    else:
        return 'foraponta'

def custo_convencional(measures):
    # Tarifa normal (fácil de calcular)
    taxa = 0.636
    custo = 0
    consumo = 0
    for i in range(len(measures)):
        consumo += measures[i] / 1000
        custo += measures[i] / 1000 * taxa
    
    return (consumo, custo)

def custo_tarifa_branca(measures, measures_time):
    # Tarifa branca (mais suga)
    taxa = {}
    taxa['ponta'] = 0.512
    taxa['intermediario'] = 0.721
    taxa['foraponta'] = 1.113

    custo = 0
    consumo = 0
    for i in range(len(measures)):
        tarifa = seleciona_tarifa(measures_time[i].minute, measures_time[i].hour)
        consumo += measures[i] / 1000
        custo += measures[i] / 1000 * taxa[tarifa]
    
    return (consumo, custo)

def break_daterange_in_periods(device_id, dt_start, dt_end):
    MAX_DAYS_REQUEST = 3
    date_format_str = '%Y-%m-%d %H:%M:%S'

    start_date = datetime.strptime(dt_start, date_format_str)
    end_date = datetime.strptime(dt_end, date_format_str)

    params_array = []

    delta_days = round((end_date - start_date).total_seconds() / (3600 * 24))
    if delta_days > MAX_DAYS_REQUEST:
        temp_start_date = start_date
        temp_end_date = start_date + timedelta(days=MAX_DAYS_REQUEST)
        while temp_end_date < end_date:
            params_array.append({
                'device_id': device_id,
                'dt_start': temp_start_date.strftime(date_format_str),
                'dt_end': temp_end_date.strftime(date_format_str)
            })
            temp_start_date = temp_end_date + timedelta(seconds=1)
            temp_end_date += timedelta(days=MAX_DAYS_REQUEST)
        
        temp_end_date += timedelta(seconds=1)
        params_array.append({
            'device_id': device_id,
            'dt_start': temp_end_date.strftime(date_format_str),
            'dt_end': end_date.strftime(date_format_str)
        })
    else:
        params_array.append({
            'device_id': device_id,
            'dt_start': start_date.strftime(date_format_str),
            'dt_end': end_date.strftime(date_format_str)
        })

    return params_array