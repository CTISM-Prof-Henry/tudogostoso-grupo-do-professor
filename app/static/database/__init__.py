"""
Arquivo que deleta o banco de dados (se ele existir) e recria as tabelas e tuplas.
"""

import os
import sqlite3


def main(database_path: str = None, script_sql_path: str = None):
    print('---------- rotina do banco de dados ----------')

    # pega o caminho absoluto do arquivo do banco de dados
    # por exemplo, se o test.db estiver na pasta C:\Users\aluno,
    # database_path vai ser C:\Users\aluno\test.db
    if database_path is None:
        database_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'test.db')

    if script_sql_path is None:
        script_sql_path = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'script.sql')

        if not os.path.exists(script_sql_path):
            raise FileNotFoundError('Precisa haver um arquivo script.sql na pasta app/static/database, '
                                    'com as rotinas de criação de tabelas e inserção de tuplas!')

    # se o banco de dados existir, deleta-o
    # isso facilita a vida na hora que formos re-gerar o banco, pois evita que tuplas
    # com ID repetido sejam inseridas novamente
    if os.path.exists(database_path):
        print('removendo banco de dados antigo encontrado...')
        os.remove(database_path)
        print('banco de dados antigo removido!')

    # cria o arquivo do banco se ele não existe
    # ou se conecta ao arquivo se existir
    with sqlite3.connect(database_path) as con:
        print('banco de dados criado!')
        # pega um cursor para executar as operações
        # um cursor é uma conexão para o banco de dados (e.g. cria, deleta, insere, etc)
        cur = con.cursor()

        with open(script_sql_path, 'r', encoding='utf-8') as script_sql:
            lines = '\n'.join(script_sql.readlines())
            cur.executescript(lines)

        print('tabelas criadas!')
        print('tuplas inseridas!')

        # salva as modificações feitas no banco
        con.commit()
        print('banco de dados salvo!')

    print('---------- rotina do banco de dados ----------')


if __name__ == '__main__':
    main()
