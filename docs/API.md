# Documentação de uso da APIs

## API da TecSUS

### Parâmetros
- **SERVIDOR:** https://api.tecsus.com.br
- **SERVIÇO:** /v0/smartmeter/get_simple_data
- **PARÂMETROS:**
    - `device_id`: ID do dispositivo (Dispositivo: Geladeira: 198762435721298897478401)
    - `dt_end`: Data e hora final para requisição dos dados
    - `dt_start`: Data e hora inicial para requisição dos dados
- **API-KEY:** `REDIGIDO` (No caso aqui para o desenvolvimento usaremos uma variável de ambiente chamada `TECSUS-API-KEY`)

### Exemplo de aplicação:
```bash
curl --location --request GET
'https://api.tecsus.com.br/v0/smartmeter/get_simple_data?device_id=198762435721298897478401&dt_start=2021-08-01
00:00:00&dt_end=2021-08-30 00:00:00' \
--header 'x-api-key: $TECSUS-API-KEY'
```

### Exemplo de resposta:
```json
{
  "error": false,
  "msg": "Ok",
  "data": [
    {
      "name": "Energia",
      "measures": [
        {
          "measure_unixtime": 1627776024,
          "measure": 3,
          "measure_accumulated": 61710
        },
        {
          "measure_unixtime": 1627776324,
          "measure": 3,
          "measure_accumulated": 61713
        },
        ...
      ]
    }
  ],
  "quantity": 1000,
  "device_id": "198762435721298897478401",
  "device_name": "Energia D1 - C2 Geladeira"
}

```