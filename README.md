
# Projeto de ETL com FastAPI
Este projeto demonstra uma aplicação simples de ETL (Extract, Transform, Load) utilizando as bibliotecas pandas, SQLAlchemy, FastAPI e requests em Python.

## Requisitos

Certifique-se de ter o Python 3.x instalado no seu sistema. Além disso, instale as dependências listadas no arquivo `requirements.txt` utilizando o gerenciador de pacotes pip:

```
pip install -r requirements.txt
```

## Configuração

Antes de executar a aplicação, é necessário realizar algumas configurações:

1. Abra o arquivo `config.py` e ajuste as configurações conforme necessário. Por exemplo, defina a URL da API que será consultada.

2. Certifique-se de ter um banco de dados SQLite criado. O projeto irá utilizar um arquivo chamado `my_lite_store.db`. Você pode criar um novo arquivo vazio ou fornecer um caminho personalizado para o arquivo do banco de dados.

## Executando a aplicação

Para executar a aplicação, use o seguinte comando:

```
uvicorn src.main:app --reload
```

Isso iniciará o servidor FastAPI e você poderá acessar a documentação da API e os endpoints disponíveis em `http://localhost:8000/docs`.

## Endpoints

A aplicação possui os seguintes endpoints:

### `/etl`

- Descrição: Executa o processo de ETL.
- Método: GET
- Parâmetros:
  - Nenhum parâmetro necessário.
- Resposta:
  - Status code 200 (OK) se o processo de ETL for concluído com sucesso.
  - Status code 500 (Erro do servidor) em caso de falha no processo de ETL.

## Observações

- O endpoint `/etl` executa a extração dos dados de uma API, realiza a transformação desses dados utilizando o pandas e, em seguida, carrega os dados transformados em um banco de dados SQLite.
- A configuração da API a ser consultada e outras configurações relevantes podem ser ajustadas no arquivo `config.py`.
- Certifique-se de fornecer as dependências necessárias (como o SQLAlchemy) e importar os módulos corretamente nos arquivos do projeto.

## Contribuição

Fique à vontade para contribuir com melhorias para este projeto. Sinta-se à vontade para abrir issues relatando problemas ou sugerindo novas funcionalidades.

Espero que isso possa ajudar a iniciar seu projeto! Lembre-se de ajustar o conteúdo conforme necessário e adicionar informações adicionais, como informações de instalação, uso avançado, etc.