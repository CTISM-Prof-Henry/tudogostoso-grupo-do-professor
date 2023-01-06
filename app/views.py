"""
Arquivo com definições de roteamento para a aplicação.

É uma boa prática de programação colocar o mesmo nome do roteamento, da função e do arquivo HTML.
"""

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
        try:
            materias = query_function('''SELECT id_materia, nome FROM materias''')
            texto_lista_materias = ''
            for materia in materias:
                id_materia = materia[0]
                nome_materia = materia[1]
                rota = 'materias/{0}'.format(id_materia)
                texto_lista_materias += '<li class="no-marker"><a href="{0}">{1}</a></li>\n'.format(rota, nome_materia)

            shia = '''
            <div class="center">
            <h2 class="center" style="width:100%">Shia está pistolaço com você >:(</h1>
            <br/>
            <iframe src="https://www.youtube.com/embed/Alt0SKEL84M"
                title="YouTube video player" frameborder="0"
                allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture"
                allowfullscreen style="width: 100%;resize: horizontal;aspect-ratio: 16 / 9;">
            </iframe>
            </div>
            '''

            return flask.render_template('pagina_inicial.html', lista_materias=texto_lista_materias, shia=shia)
        except Exception:
            return flask.render_template(
                '404.html'
            )

    @app.route('/materias/<id_materia>', methods=['GET'])
    def materias(id_materia):
        try:
            nome_materia = query_function('''SELECT nome FROM materias WHERE id_materia = {0}'''.format(id_materia))[0][0]

            texto_paragrafos = '<p class="center">Esta é a página da matéria <b>{0}!</b></p><br/>\n'.format(nome_materia)
            texto_paragrafos += '<p class="center">Veja abaixo os professores que ministraram-na:</p><br/>\n'

            professores = query_function('''
                SELECT p.nome
                FROM professores p
                INNER JOIN professores_para_materias ppm on p.id_professor = ppm.id_professor
                INNER JOIN materias m on ppm.id_materia = m.id_materia
                WHERE m.id_materia = '{0}';
            '''.format(id_materia))

            texto_paragrafos += '<ul class="center">\n'
            for prof in professores:
                texto_paragrafos += '\t<li>{0}</li>\n'.format(prof[0])
            texto_paragrafos += '</ul>'

            return flask.render_template(
                'template_2.html',
                paragrafo=texto_paragrafos,
                imagem=''
            )
        except Exception:
            return flask.render_template(
                '404.html'
            )

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
