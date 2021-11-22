# (HID-65) Projeto CATALAN

Projeto CATALAN: **C**oimbra **A**drisson **T**oso **A**lynne **L**ucas **A**lexa**N**dre

<p align="center">
  <img src="./data/logo-small.png" />
</p>

<!--
Mals pelo HTML ae galera, mas era pq eu queria alinhar a imagem no centro da tela =/

Código original sem HTML (imagem alinhada na esquerda):
![Catalan Logo](./data/logo-small.png)

-->

Projeto desenvolvido para a matéria de HID-65: Engenharia para o Ambiente e Sustentabilidade do Instituto Tecnológico de Aeronáutica (ITA) para os cursos de Engenharia Eletrônica e Engenharia de Computação.

## Proposta

Toda a documentação relevante do projeto encontra-se dentro do diretório `docs/`. A proposta do projeto pode ser acessada pelo link: [Documento de Proposta](<./docs/Grupo 1 - Projeto CATALAN.pdf>)

## Uso da API da TecSUS

Documentação de uso da APIs utilizadas: [API](./docs/API.md)

## Executando o código inicial (Prova de Conceito)

Instale as dependências (sugestão: Usar um ambiente virtual no Python):
```bash
pip install -r requirements.txt
```

Configure as variáveis de ambiente necessárias (e.g.: chaves de API) no seu environment. Por exemplo:

```bash
export TECSUS_API_KEY=SUBSTITUIR_CHAVE_DA_API_AQUI
```

Execute a prova de conceito:
```bash
python src/poc.py
```

## Valores de tarifa utilizados

As tarifas e o horário dos períodos para o cálculo da tarifa branca foram retirados de uma consulta feita ao site da ANEEL ([https://www.aneel.gov.br/tarifa-branca](https://www.aneel.gov.br/tarifa-branca)) no dia 21/11/2021, com os valores referentes à distribuidora EDP SP (São José dos Campos).

Valores obtidos na consulta:
- Tarifa convencional: 0,636 [R$ / kWh]
- Tarifa Branca:
  - Ponta: 0,512 [R$ / kWh]
  - Intermediário: 0,721 [R$ / kWh]
  - Fora Ponta: 1,113 [R$ / kWh]
 
Períodos da Tarifa Branca:
- Ponta: (00:00 - 16:30); (21:30 - 00:00)
- Intermediário: (16:30 - 17:30); (20:30 - 21:30)
- Fora Ponta: (17:30 - 20:30)

<!-- Para os cálculos do custo de consumo, dado que este projeto é apenas uma prova de conceito, foram utilizados valores estáticos para as tarifas. Os valores foram retirados de uma tabela com valores da empresa EDP (São José dos Campos). Foi considerado para cálculo valores referentes a bandeira verde. A tabela de tarifas utilizada pode ser conferida no link: [Tarifas de SP](./docs/tarifa_SP.pdf) -->