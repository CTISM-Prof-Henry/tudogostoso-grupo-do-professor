"""
Arquivo com definições de roteamento para a aplicação.

É uma boa prática de programação colocar o mesmo nome do roteamento, da função e do arquivo HTML.
"""
import sqlite3

import flask

try:
    # esse bloco de código roda se o código for executado pelo Pycharm
    folder = ''
    from app.models import query_function
except ModuleNotFoundError:
    # esse bloco de código roda se o código for executado pela linha de comando
    from models import query_function


def main(app: flask.app.Flask) -> flask.app.Flask:

    @app.route('/')
    def initial_page():
        # eu quero recuperar a lista de memes que estão na tabela memes
        results = query_function('''SELECT id, nome FROM memes;''')

        # results =
        # [
        #   ('DJ André Marques manda AQUELE ao vivo', 'https://youtube.com/'),
        #   ('Rei do Camarote', 'https://youtube.com/'
        # ]

        lista_materias = '<ul>'
        for result in results:
            lista_materias += '<li><a href="{1}">{0}</a></li>'.format(result[1], flask.url_for('memes', id_meme=result[0]))
        lista_materias += '</ul>'

        return flask.render_template(
            'pagina_inicial.html',
            lista_materias=lista_materias
        )

    @app.route('/memes/<id_meme>', methods=['GET'])
    def memes(id_meme):
        try:
            results = query_function('''SELECT nome, link FROM memes WHERE id = {0};'''.format(id_meme))

            # results = [(nome, link)]

            return flask.render_template(
                'pagina_meme.html',
                nome='<p>{0}</p>'.format(results[0][0]),
                link='<p>{0}</p>'.format(results[0][1])
            )
        except:
            return flask.render_template('404.html')

    @app.route('/server_generated_page', methods=['GET'])
    def server_generated_page():
        return flask.render_template(
            'template_2.html',
            paragrafo='<p class="center">Este parágrafo foi renderizado pelo servidor!</p>',
            imagem='<img class="center" src="' + flask.url_for('static', filename='img/ye_smiling.jpg') + '">'
        )

    @app.route('/ajax_generated_table', methods=['GET'])
    def ajax_generated_table():
        return flask.render_template('template_1.html')

    @app.errorhandler(404)
    def page_not_found(page):
        return flask.render_template('404.html'), 404

    app.register_error_handler(404, page_not_found)

    return app
