import os
import sqlite3

import flask
from flask import request, jsonify

from datetime import datetime as dt


def data_para_string(data: dt) -> str:
    """
    Converte uma data para uma string, no formato ANO-MÊS-DIA.
    """
    string = data.strftime('%Y-%m-%d')
    return string


def string_para_data(string: str) -> dt:
    """
    Converte uma string no formato ANO-MÊS-DIA para uma data.
    """
    data = dt.strptime(string, '%Y-%m-%d')
    return data


def query_function(query: str = None, database_path: str = None) -> list:
    """
    Função para fazer pesquisas no banco de dados.

    :param query: A string de consulta sqlite.
    :param database_path: Caminho do banco de dados. Caso não seja provido, irá assumir que o banco é um arquivo
                          test.db na pasta deste script.
    :return: Uma lista de tuplas, onde cada tupla é uma tupla do banco de dados.
    """
    # pega o caminho absoluto do arquivo do banco de dados
    # por exemplo, se o test.db estiver na pasta C:\Users\aluno,
    # database_path vai ser C:\Users\aluno\test.db
    if database_path is None:
        database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'static', 'database', 'test.db')

    if query is None:
        raise ValueError('query não pode ser None!')

    # se conecta ao arquivo do banco
    with sqlite3.connect(database_path) as con:
        # pega um cursor para executar as operações
        # um cursor é uma conexão para o banco de dados (e.g. cria, deleta, insere, etc)
        cur = con.cursor()

        answer = cur.execute(query).fetchall()
        return answer


def main(app: flask.app.Flask) -> flask.app.Flask:
    @app.route('/generate_table', methods=['POST'])
    def generate_table():
        table_name = request.form['opcao_selecionada']
        # pega o nome das colunas
        table_columns = query_function('''select name from pragma_table_info("{0}");'''.format(table_name))
        table_columns = tuple([x[0] for x in table_columns])  # transforma a lista de tuplas numa tupla
        # pega os dados
        answer = query_function('''SELECT * FROM {0}'''.format(table_name))
        # transforma os dados
        new_answer = []
        for line in answer:
            new_answer.append({k: v for k, v in zip(table_columns, line)})
        # monta a resposta
        response = jsonify(new_answer)
        response.headers.add('Access-Control-Allow-Origin', '*')  # Essa linha é necessária. Requisição dos navegadores
        return response  # retorna resposta para a página Web

    return app
