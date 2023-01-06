import os
import sys

from flask import Flask

from app.static.database import main as database_routine
from app.models import main as models_func
from app.views import main as views_func


def main():
    # configura a aplicação e define as pastas onde ela deve procurar os itens
    current_path = os.sep.join(os.path.abspath(__file__).split(os.sep)[:-1])

    app = Flask(
        'Minha primeira aplicação Flask',
        template_folder='templates',
        static_folder='static',
        root_path=os.path.join(current_path, 'app'),
        instance_path=os.path.join(current_path, 'app', 'instance'),
        instance_relative_config=True
        # instance_relative_config=True
    )
    sys.path.append(os.path.join(current_path, 'app'))
    # configura os arquivos de definições, app/config.py e app/instance/config.py
    app.config.from_object('config')
    try:
        app.config.from_pyfile('config.py')
    except FileNotFoundError:
        print('--' * 55, file=sys.stderr)
        print(
            ' O arquivo app/instance/config.py não foi encontrado, '
            'então o arquivo app/config.py será usado no seu lugar.',
            file=sys.stderr
        )
        print('--' * 55, file=sys.stderr)

    # se
    #   GENERATE_DB = True
    # em app/instance/config.py ou em app/config.py, deleta o banco
    # de dados antigo e cria-o de novo
    if app.config["GENERATE_DB"]:
        database_routine()

    app = models_func(app)  # carrega as definições de funções ajax na aplicação
    app = views_func(app)  # carrega as definições de roteamento na aplicação

    # coloca o backend a rodar no modo debug; modificações feitas nos arquivos de código-fonte
    # se refletirão em tempo real nas páginas Web (basta dar um F5 no navegador)
    app.run(use_reloader=app.config["USE_REALODER"])


if __name__ == '__main__':
    main()
