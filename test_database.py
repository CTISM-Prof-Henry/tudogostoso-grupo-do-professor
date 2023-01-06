import os
import sqlite3
import unittest


def __get_tables_fields__(cursor: sqlite3.Cursor) -> dict:
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = [x['name'] for x in cursor.execute("PRAGMA table_info(%s)" % table_name).fetchall()]

    return data


def __get_table_number_of_rows__(cursor: sqlite3.Cursor) -> dict:
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = cursor.execute("SELECT COUNT(*) FROM %s" % table_name).fetchone()['COUNT(*)']

    return data


def __get_primary_keys__(cursor: sqlite3.Cursor):
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = [
            {'name': x['name'], 'is_pk': x['pk']}
            for x in cursor.execute("PRAGMA table_info(%s)" % table_name).fetchall()
        ]

    return data


def __get_foreign_key_count__(cursor: sqlite3.Cursor):
    obj_tables = cursor.execute("SELECT * FROM sqlite_master WHERE type='table'").fetchall()
    data = {}
    for table in obj_tables:  # type: sqlite3.Row
        table_name = table['name']
        data[table_name] = len(cursor.execute("PRAGMA foreign_key_list(%s)" % table_name).fetchall())

    return data


class DatabaseTester(unittest.TestCase):

    @staticmethod
    def get_database_path():
        _current_folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
        _database_folder = os.path.join(_current_folder, 'app', 'static', 'database')
        _matches = [x for x in os.listdir(_database_folder) if x.split('.')[-1].lower() == 'db']
        if len(_matches) == 1:
            database_path = os.path.join(_database_folder, _matches[0])
        elif len(_matches) == 0:
            database_path = os.path.join(_database_folder, 'test.db')
            try:
                from app.static.database import main as database_routine
            except ModuleNotFoundError:
                from static.database import main as database_routine

            database_routine(database_path)
        else:
            raise ValueError(
                'foram encontrados mais que um banco de dados na pasta {0}! '
                '(apenas um arquivo .db deve existir)'.format(_database_folder)
            )

        return database_path

    def test_number_tables(self):
        """
        Checa o número de tabelas
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            fields = __get_tables_fields__(cursor)  # type: dict

            self.assertGreaterEqual(len(fields), 3, "O banco de dados precisa ter ao menos cinco tabelas!")

    def test_minimum_columns(self):
        """
        Checa o número de colunas por tabelas
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            tables = __get_tables_fields__(cursor)  # type: dict

            for k, v in tables.items():
                self.assertGreaterEqual(len(v), 2, "O banco de dados precisa ter ao menos duas colunas por tabela!")

    def test_optimal_columns(self):
        """
        Checa se ao menos uma tabela tem 4 colunas
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            tables = __get_tables_fields__(cursor)  # type: dict

            max_columns = 0
            for k, v in tables.items():
                max_columns = max(max_columns, len(v))

            self.assertGreaterEqual(max_columns, 4, "Pelo menos uma tabela precisa ter quatro colunas!")

    def test_minimum_tuples(self):
        """
        Checa se as tabelas possuem ao menos duas tuplas
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            rows = __get_table_number_of_rows__(cursor)  # type: dict

            for k, v in rows.items():
                self.assertGreaterEqual(v, 2, "Todas as tabelas do banco precisam ter ao menos duas tuplas!")

    def test_optimal_tuples(self):
        """
        Checa se ao menos uma tabela possui 10 tuplas
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            rows = __get_table_number_of_rows__(cursor)  # type: dict

            max_tuples = 0
            for k, v in rows.items():
                max_tuples = max(max_tuples, v)

            self.assertGreaterEqual(max_tuples, 10, "Pelo menos uma tabela precisa ter 10 tuplas!")

    def test_primary_keys(self):
        """
        Testa se todas as tabelas possuem primary keys.
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            pks = __get_primary_keys__(cursor)

            for k, v in pks.items():
                found = False
                for field in v:
                    if field['is_pk'] > 0:
                        found = True
                        break
                self.assertTrue(found, "Todas as tabelas precisam ter ao menos uma primary key!")

    def test_composite_primary_keys(self):
        """
        Testa se ao menos uma tabela possui chave primária composta.
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            pks = __get_primary_keys__(cursor)

            found = False
            for k, v in pks.items():
                for field in v:
                    if field['is_pk'] > 1:
                        found = True
                        break
                if found:
                    break
            self.assertTrue(found, "Pelo menos uma tabela precisa ter chave primária composta!")

    def test_foreign_keys(self):
        """
        Testa se ao menos uma tabela possui chave estrangeira
        """

        with sqlite3.connect(self.get_database_path()) as con:
            con.row_factory = sqlite3.Row
            cursor = con.cursor()
            pks = __get_foreign_key_count__(cursor)

            count = 0
            for k, v in pks.items():
                count += v
            self.assertGreaterEqual(count, 2, "Pelo menos duas tabelas precisa ter chave estrangeira!")


if __name__ == '__main__':
    unittest.main()
