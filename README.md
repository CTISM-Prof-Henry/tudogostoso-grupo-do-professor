# flaskNeles

Seu objetivo neste trabalho é programar um site. O trabalho está dividido entre duas etapas, frontend e backend.
Você usará este repositório para as duas etapas, pois a segunda depende da primeira para funcionar. 

## Sumário

* [Dicas para o desenvolvimento do trabalho](#dicas-para-o-desenvolvimento-do-trabalho)
  * [Usando recursos disponíveis](#usando-recursos-disponíveis)
  * [Resolvendo problemas](#resolvendo-problemas)
* [Instalação](#instalação)
  * [Importando um banco de dados existente](#importando-um-banco-de-dados-existente)
* [Checklist das atividades - frontend](#checklist-das-atividades---frontend)
  * [HTML](#html)
  * [CSS](#css)
  * [Javascript](#javascript)
  * [Modelagem do Banco](#modelagem-do-Banco)
  * [Outros requisitos](#outros-requisitos)
* [Checklist das atividades - backend](#checklist-das-atividades---backend)
  * [Banco de Dados](#banco-de-dados)
  * [Páginas e Roteamento](#páginas-e-roteamento)

## Dicas para o desenvolvimento do trabalho

### Usando recursos disponíveis

Utilize os repositórios [pythonSqlite](https://github.com/CTISM-Prof-Henry/pythonSqlite), 
[pythonFlask](https://github.com/CTISM-Prof-Henry/pythonFlask) e [webEssentials](https://github.com/CTISM-Prof-Henry/webEssentials)
para auxiliá-lo no desenvolvimento deste trabalho. A seção Referências do 
[pythonFlask](https://github.com/CTISM-Prof-Henry/pythonFlask) será excepcionalmente útil. Faça os exercícios do 
[pythonSqlite](https://github.com/CTISM-Prof-Henry/pythonSqlite) para uma melhor compreensão do banco de dados. Se
você se esquecer dos comandos ou conceitos do git+Github, use o conhecimento disponível no 
[gitEssentials](https://github.com/CTISM-Prof-Henry/gitEssentials).

### Resolvendo problemas

É muito provável (praticamente certo) que, durante o desenvolvimento deste trabalho, você encontre dificuldades - o 
aplicativo por algum motivo parou de funcionar; o arquivo HTML está com os elementos mal-organizados; o banco de dados
não quer ser gerado; o testador está dando um erro bizarro; dentre outras tantas coisas. Talvez você perceba estes 
erros durante o desenvolvimento, ou só depois quando executar um dos dois testadores disponíveis.

Uma boa (ótima) prática de programação é criar um commit **antes** de você fazer modificações que potencialmente irão
fazer o seu trabalho parar de funcionar. Por exemplo, o aplicativo disponibilizado na pasta [app](app) é fornecido de 
maneira que ele funcione (ele não apresenta nenhum bug), e desde o primeiro momento ele passa em 7 dos 11 testes do 
testador [test_frontend](test_frontend.py), e em todos os testes do [test_database](test_database.py). 

Portanto, **verifique o que funciona** antes de você começar a mexer no código-fonte. Se algum problema ocorrer, 
os testadores lhe auxiliarão a encontrar o erro.

Caso esteja fazendo o trabalho em grupo, leia a seção 
[Resolvendo conflitos](https://github.com/CTISM-Prof-Henry/gitEssentials/blob/main/chapters/resolvendo_conflitos.md)
do repositório [gitEssentials](https://github.com/CTISM-Prof-Henry/gitEssentials).

## Instalação

Siga as instruções que estão disponíveis na seção 
[Instalação](https://github.com/CTISM-Prof-Henry/pythonFlask#instala%C3%A7%C3%A3o) do repositório 
[pythonFlask](https://github.com/CTISM-Prof-Henry/pythonFlask).

### Importando um banco de dados existente

Caso você já tenha um banco de dados que queira reaproveitar neste trabalho, siga o seguinte passo-a-passo:

1. Pelo prompt de comando, navegue até a pasta do seu arquivo `.db`
2. Execute o comando
   
   ```bash
   sqlite3 <nome do banco>.db .dump > script.sql
   ```
   
   Onde `<nome do banco>` é o nome do seu banco de dados. Por exemplo, se o nome dele for `banco.db`, o comando será
   
   ```bash
   sqlite3 banco.db .dump > script.sql
   ```
   
3. Copie o arquivo `script.sql` que foi gerado para a pasta [app/static/database](app/static/database).


## Checklist das atividades - frontend

**Dica 1:** Para marcar um dos checkboxes abaixo, edite o arquivo em Markdown e troque de `[ ]` para `[x]`.

**Dica 2:** itens marcados por 🤖 estão inclusos nos testes dos testadores automáticos.

**Dica 3:** itens marcados por 🖥️ só aparecerão corretamente se você rodar o script [app/\_\_main\_\_.py](app/__main__.py)
e abrir a URL que aparecer na tela: http://127.0.0.1:5000 

### HTML

* [ ] **(0.5 pt)** 🤖 No mínimo três templates HTML
* [ ] **(1 pt)** 🤖 No mínimo 20 tags HTML em alguma página
  * `<html>`, `<body>`, `<h1>`, `<p>`, `<img>`, etc
* [ ] **(1 pt)** 🤖 Alguma página faz uso de [formulários](https://www.w3schools.com/html/html_forms.asp)
* [ ] **(1 pt)** 🤖 Alguma página tem uma funcionalidade que faz uso de código-fonte Javascript
  * Por exemplo, clicar em um botão e abrir um [modal](https://getbootstrap.com/docs/4.0/components/modal/), ou então
    abrir um [menu lateral](https://bootstrapious.com/p/bootstrap-sidebar), etc
  * Você pode implementar qualquer funcionalidade. Seja criativo!
  * 🖥 Exemplo (botão alerta): [app/templates/template_1.html](app/templates/template_1.html)
* [ ] **(1 pt)** Uma página inicial (bonita)
  * Por exemplo, se o tema do seu trabalho for de receitas culinárias, você pode se inspirar na página inicial do site
    Tudo Gostoso: https://www.tudogostoso.com.br
  * Exemplo no projeto: [app/templates/pagina_inicial.html](app/templates/pagina_inicial.html)
* [ ] **(1 pt)** Uma página de erro 404 (bonita)
  * Exemplo no projeto: [app/templates/404.html](app/templates/404.html)

### CSS

* [ ] **(0.5 pt)** 🤖 No máximo um arquivo CSS
  * Deve ser adicionado externamente à todas as páginas HTML
* [ ] **(1 pt)** 🤖 No mínimo 15 definições CSS
  * O arquivo [app/static/css/main.css](app/static/css/main.css) possui 8 definições.
* [ ] **(0.5 pt)** 🤖 Pelo menos uma fonte é do [Google Fonts](https://fonts.google.com/)
  * O repositório [pythonFlask](https://github.com/CTISM-Prof-Henry/pythonFlask/blob/main/tutoriais/fontes/como_inserir_fontes.md) 
    possui um tutorial na seção de referências
* [ ] (opcional) O site possui uma paleta de cores 
  * Você pode usar os sites [Coolors](https://coolors.co/) e [Viz Palette](https://projects.susielu.com/viz-palette)
    para montar uma paleta de cores.
  * A paleta de cores influencia na beleza da página inicial e na página de erros.

### Javascript

* [ ] **(1 pt)** 🤖 No mínimo um arquivo JS
  * Pode ser usado para colocar o código-fonte AJAX da segunda parte (opcional e mais difícil), ou então algum código 
    Javascript pertinente (recomendado e mais fácil) 
  * Por exemplo, se o tema do seu trabalho for de receitas culinárias, você pode colocar neste arquivo o código-fonte
    Javascript que faz a conversão de medidas

### Modelagem do Banco 

* [ ] **(1 pt)** Modelagem do banco de dados feita utilizando a biblioteca 
  [mermaid](https://mermaid-js.github.io/mermaid/#/), e escrita no arquivo [diagrama.md](diagrama.md).
  * [ ] Pelo menos 3 tabelas
  * [ ] No mínimo 2 colunas por tabela 
  * [ ] Pelo menos uma tabela com 4 colunas 
  * [ ] Pelo menos 2 tuplas por tabela
  * [ ] Uma tabela com 10 tuplas
  * [ ] Todas as tabelas possuem chave primária (primary key, PK)
  * [ ] Pelo menos uma tabela possui chave primária composta (e.g. duas colunas)
  * [ ] Pelo menos duas tabelas possuem chave estrangeira (foreign key, FK)
  * [ ] O banco de dados é original. Nenhum outro grupo pegou o mesmo tema que o tema do seu grupo
  * Confira o [exemplo pré-pronto](diagrama.md) que está disponibilizado neste arquivo. Você pode usar o site 
    [mermaid.live](mermaid.live) para fazer o diagrama, e depois copiar-e-colar o código no arquivo 
    [diagrama.md](diagrama.md).

### Outros requisitos

* [ ] **(0.5 pt)** 🤖 um favicon personalizado
  * favicon é o logo do site, que é mostrado na barra de endereços do navegador
  * Veja o exemplo em [app/static/img/favicon.ico](app/static/img/favicon.ico)

## Checklist das atividades - backend

### Banco de Dados

* [ ] **(2 pts)** 🤖 Banco de dados (pronto), com um arquivo de nome `script.sql` na pasta 
  [app/static/database](app/static/database) 
  * [ ] 🤖 Pelo menos 3 tabelas
  * [ ] 🤖 No mínimo 2 colunas por tabela 
  * [ ] 🤖 Pelo menos uma tabela com 4 colunas 
  * [ ] 🤖 Pelo menos 2 tuplas por tabela
  * [ ] 🤖 Uma tabela com 10 tuplas
  * [ ] 🤖 Todas as tabelas possuem chave primária (primary key, PK)
  * [ ] 🤖 Pelo menos uma tabela possui chave primária composta (e.g. duas colunas)
  * [ ] 🤖 Pelo menos duas tabelas possuem chave estrangeira (foreign key, FK)
  * [ ] 🤖 O banco de dados é original. Nenhum outro grupo pegou o mesmo tema que o tema do seu grupo

### Páginas e Roteamento

* [ ] **(2 pts)** Alguma página possui informações que são atualizadas pelo servidor
  * Template (abra no navegador): [app/templates/template_2.html](app/templates/template_2.html)
  * 🖥️ Página renderizada: [http://127.0.0.1:5000/server_generated_page](http://127.0.0.1:5000/server_generated_page)
  * Código-fonte: [app/views.py](app/views.py) (método `server_generated_page`)   
* [ ] **(2 pts)** Alguma página, no código de roteamento, faz consultas ao banco de dados
  * Template: [app/templates/pagina_inicial.html](app/templates/pagina_inicial.html)
  * 🖥️ Página renderizada: [http://127.0.0.1:5000](http://127.0.0.1:5000)
  * Código-fonte: [app/views.py](app/views.py) (método `initial_page`)
* [ ] **(2 pts)** Alguma página faz uso de código-fonte AJAX
  * Template: [app/templates/template_1.html](app/templates/template_1.html)
  * 🖥️ Página renderizada: [http://127.0.0.1:5000/ajax_generated_table](http://127.0.0.1:5000/ajax_generated_table)
  * Código-fonte: [app/views.py](app/views.py) (método `ajax_generated_page`) e [app/models.py](app/models.py) (método
    `generate_table`)
* [ ] **(2 pt)** Todos os templates HTML foram atualizados para usar `url_for`, para links, imagens, CSS, Javascript, etc
  * Todos os templates em [app/templates](app/templates) estão configurados para funcionar tanto estaticamente quanto 
    dinamicamente
  
