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