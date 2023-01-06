import os
import unittest

import cssutils
from cssutils.css import CSSStyleSheet, CSSComment, CSSImportRule
from html.parser import HTMLParser


class MyHTMLParser(HTMLParser):

    def __init__(self, *, convert_charrefs: bool = ...) -> None:
        super().__init__(convert_charrefs=convert_charrefs)
        self.tags = dict()
        self.form_tag = False
        self.script_tag = False
        self.exclusive_css = True

    def handle_starttag(self, tag, attrs):
        try:
            self.tags[tag] += 1
        except KeyError:
            self.tags[tag] = 1

        if tag == 'style':
            self.exclusive_css = False
        elif tag == 'form':
            self.form_tag = True
        elif tag == 'script':
            dict_attrs = dict(attrs)
            if 'src' in dict_attrs:
                self.script_tag = True

    def handle_endtag(self, tag):
        pass


class FrontendTester(unittest.TestCase):
    @staticmethod
    def get_js_path():
        _current_folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
        path = os.path.join(_current_folder, 'app', 'static', 'js')
        return path

    @staticmethod
    def get_css_path():
        _current_folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
        path = os.path.join(_current_folder, 'app', 'static', 'css')
        return path

    @staticmethod
    def get_img_path():
        _current_folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
        path = os.path.join(_current_folder, 'app', 'static', 'img')
        return path

    @staticmethod
    def get_html_path():
        _current_folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
        path = os.path.join(_current_folder, 'app', 'templates')
        return path

    @staticmethod
    def get_database_path():
        _current_folder = os.sep.join(os.path.dirname(os.path.abspath(__file__)).split(os.sep))
        path = os.path.join(_current_folder, 'app', 'static', 'database')
        return path

    def test_number_js_files(self):
        js_path = self.get_js_path()
        files = [x for x in os.listdir(js_path) if x.split('.')[-1].lower() == 'js']
        self.assertGreaterEqual(len(files), 1, 'O aplicativo deve ter no mínimo um arquivo .js!')

    def test_number_html_files(self):
        html_path = self.get_html_path()
        files = [x for x in os.listdir(html_path) if x.split('.')[-1].lower() == 'html']
        self.assertGreaterEqual(len(files), 3, 'O aplicativo deve ter no mínimo três arquivos .html!')

    def test_number_css_files(self):
        css_path = self.get_css_path()

        files = [x for x in os.listdir(css_path) if x.split('.')[-1].lower() == 'css']
        self.assertEqual(len(files), 1, 'O aplicativo deve ter no máximo um arquivo .css!')

    def test_css_number_rules(self):
        css_path = self.get_css_path()
        css_filename = [x for x in os.listdir(css_path) if x.split('.')[-1].lower() == 'css'][0]
        stylesheet = cssutils.parseFile(os.path.join(css_path, css_filename))  # type: CSSStyleSheet
        n_rules = len([rule for rule in stylesheet.cssRules if not isinstance(rule, CSSComment)])
        self.assertGreaterEqual(n_rules, 15, 'O arquivo .css deve ter no mínimo 15 definições de regras!')

    def test_css_google_font(self):
        css_path = self.get_css_path()
        css_filename = [x for x in os.listdir(css_path) if x.split('.')[-1].lower() == 'css'][0]
        stylesheet = cssutils.parseFile(os.path.join(css_path, css_filename))  # type: CSSStyleSheet
        passing = []
        for rule in stylesheet.cssRules:
            passing += [isinstance(rule, CSSImportRule) and 'font' in rule.href and 'google' in rule.href]

        self.assertTrue(
            any(passing),
            'Você deve usar um comando @import no .css para importar uma fonte do Google Fonts!'
        )

    def test_css_exclusive_external_file(self):
        html_path = self.get_html_path()
        files = [x for x in os.listdir(html_path) if x.split('.')[-1].lower() == 'html']

        passing = []

        for some_file in files:
            with open(os.path.join(html_path, some_file), 'r', encoding='utf-8') as html_file:
                document = '\n'.join(html_file.readlines())

                parser = MyHTMLParser()
                parser.feed(document)
                self.assertTrue(parser.exclusive_css, 'Você não deve usar tags <style> nos seus arquivos .html!')

    def test_is_sql_file_present(self):
        database_path = self.get_database_path()
        found = False
        for some_file in os.listdir(database_path):
            if some_file.lower() == 'script.sql':
                found = True
                break

        self.assertTrue(found, 'A aplicação deve possuir um arquivo de nome script.sql na pasta app/static/database!')

    def test_is_favicon_present(self):
        img_path = self.get_img_path()
        found = False
        for some_img in os.listdir(img_path):
            if some_img.lower() == 'favicon.ico':
                found = True
                break

        self.assertTrue(found, 'Seu site deve ter um arquivo favicon.ico na pasta app/static/img!')

    def test_html_number_tags(self):
        html_path = self.get_html_path()
        files = [x for x in os.listdir(html_path) if x.split('.')[-1].lower() == 'html']

        passing = []
        counts = dict()

        for some_file in files:
            with open(os.path.join(html_path, some_file), 'r', encoding='utf-8') as html_file:
                document = '\n'.join(html_file.readlines())

                parser = MyHTMLParser()
                parser.feed(document)
                counts[some_file] = len(parser.tags)
                passing += [len(parser.tags) >= 20]

        contagem_str = '\n'.join(['{0}: {1}'.format(k, v) for k, v in counts.items()])

        self.assertTrue(any(passing), 'Alguma página HTML deve ter no mínimo 20 tags!\n' + contagem_str)

    def test_html_form_tag(self):
        html_path = self.get_html_path()
        files = [x for x in os.listdir(html_path) if x.split('.')[-1].lower() == 'html']

        passing = []

        for some_file in files:
            with open(os.path.join(html_path, some_file), 'r', encoding='utf-8') as html_file:
                document = '\n'.join(html_file.readlines())

                parser = MyHTMLParser()
                parser.feed(document)
                passing += [parser.form_tag]

        self.assertTrue(any(passing), 'Pelo menos alguma página HTML deve ter uma tag <form>!')

    def test_html_script_tag(self):
        html_path = self.get_html_path()
        files = [x for x in os.listdir(html_path) if x.split('.')[-1].lower() == 'html']

        passing = []

        for some_file in files:
            with open(os.path.join(html_path, some_file), 'r', encoding='utf-8') as html_file:
                document = '\n'.join(html_file.readlines())

                parser = MyHTMLParser()
                parser.feed(document)
                passing += [parser.script_tag]

        self.assertTrue(any(passing), 'Pelo menos alguma página HTML deve conter uma tag <script> com src definido para'
                                      ' um arquivo local!')


if __name__ == '__main__':
    unittest.main()
