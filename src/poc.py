import requests
import os
import plotly.express as px
from datetime import datetime

url = 'https://api.tecsus.com.br/v0/smartmeter/get_simple_data'
headers = {'x-api-key': os.environ['TECSUS-API-KEY']}
params = {'device_id': '198762435721298897478401',
           'dt_start': '2021-08-01 00:00:00',
           'dt_end': '2021-08-30 00:00:00'}

r = requests.get(url, headers=headers, params=params)

data = r.json()

if data == None or data['error']:
    print('Request Error')
    exit

raw_measures = data['data'][0]['measures']

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
    print(f'{measures_range} - {len(measures_range)}')
    measures_mm.append( sum(measures_range) / len(measures_range) )
measures_time_mm = measures_time[mm_range:]

fig = px.line(x=measures_time_mm, y=measures_mm, title=f'Consumo: {data["device_name"]}')
fig.update_xaxes(title="Data")
fig.update_yaxes(title="Consumo [???]")
fig.show()