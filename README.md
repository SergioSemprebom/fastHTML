# FastHTML

COMO CRIAR WEBAPPS COM PYTHON – FASTHTML

Como Criar WebApps com Python – FastHTML
O FastHTML é um framework inovador, desenvolvido em Python, que simplifica a criação de aplicativos web sem a necessidade de escrever código em HTML, CSS ou JavaScript.
Assim, será possível construir uma aplicação web moderna utilizando apenas Python, tanto no back-end quanto no front-end.
Embora o FastHTML não exija a escrita direta de HTML e CSS, é importante que você tenha noções básicas dessas linguagens, para compreender as estruturas nos componentes que ele utiliza.

O que é o FastHTML?
O FastHTML é um framework em Python que facilita a criação de aplicativos web sem exigir o uso de HTML, CSS ou JavaScript diretamente, apenas utilizando Python.
Ele simplifica a construção de interfaces dinâmicas e componentes reutilizáveis, que podem ser manipulados diretamente no navegador sem precisar recarregar a página.
Isso é possível graças à sua integração com o HTMX, uma biblioteca que permite fazer requisições assíncronas para o servidor e atualizar partes específicas da página de forma dinâmica, sem recarregar todo o conteúdo.
 
Acesse o site oficial do FastHTML
Como Instalar o FastHTML?
Para começar a usar o FastHTML, basta instalar o framework utilizando o pip no terminal do seu editor de código.
pip install python-fasthtml
 
Após a instalação, o próximo passo é criar um arquivo Python chamado main.py, onde veremos a estrutura básica de um aplicativo desenvolvido com FastHTML.
 
Criando a Estrutura Básica de um Aplicativo
Agora que o FastHTML está instalado, podemos construir a estrutura básica de um aplicativo para que você entenda como o framework funciona. Esse processo é simples e direto.
Embora seja comum importar todas as funcionalidades do FastHTML de uma vez, vamos importar apenas o necessário, para que possamos entender detalhadamente cada funcionalidade.
Começamos importando o FastHTML e o serve. O FastHTML é responsável por criar o aplicativo, enquanto o serve inicia o servidor e coloca o site no ar.
Em seguida, criaremos uma instância da classe FastHTML, o que inicializa o aplicativo e prepara o ambiente para que possamos definir rotas e responder às requisições dos usuários.
from fasthtml.common import FastHTML, serve
app = FastHTML()
Criando uma Rota no FastHTML
Uma rota define o caminho que o navegador do usuário precisa acessar para visualizar uma página específica do site. Vamos começar criando a rota principal, acessada ao visitar a raiz do site (homepage).
Para definir essa rota, utilizamos o decorator @app.get(“/”). Esse decorator informa ao FastHTML que toda vez que alguém fizer uma requisição GET na URL principal, a função logo abaixo deverá ser executada.
No nosso caso, essa função, chamada homepage(), retornará um conteúdo HTML simples, com uma tag <h1> exibindo a mensagem “Bem-vindo ao meu site com FastHTML”.
from fasthtml.common import FastHTML, serve
app = FastHTML()
@app.get("/")
def homepage():
return "<h1>Bem vindo ao meu site com FastHTML</h1>"
Executando e Testando o Site
Por fim, para que o site funcione e seja acessível, precisamos colocar o servidor no ar utilizando a função serve().
from fasthtml.common import FastHTML, serve
app = FastHTML()
@app.get("/")
def homepage():
return "<h1>Bem vindo ao meu site com FastHTML</h1>"
serve()
Ao executar esse código, o servidor de desenvolvimento do FastHTML será iniciado, e você poderá acessar o aplicativo localmente pelo navegador.
  
Uma das grandes vantagens do FastHTML é o recarregamento automático. Isso significa que, enquanto desenvolve, você pode modificar o código e ver as mudanças no navegador sem precisar reiniciar o servidor.
Por exemplo, se alterarmos o texto dentro da tag <h1>, basta salvar o arquivo e atualizar a página no navegador para ver a mudança.
from fasthtml.common import FastHTML, serve
app = FastHTML()
@app.get("/")
def homepage():
return "<h1>Bem vindo ao meu site com FastHTML. Alterei.</h1>"
serve()
 
Esse é o exemplo mais básico de uma aplicação com FastHTML. A partir de agora, vamos explorar outros conceitos importantes desse framework e desenvolver nossa lista de tarefas com Python.
Componentes Reutilizáveis no FastHTML
Uma das grandes vantagens do FastHTML é sua abordagem baseada em componentes reutilizáveis.
Um componente é uma parte da página web que pode ser reaproveitada, como botões, caixas de texto ou listas, assim como acontece no React.
Esses componentes são criados utilizando classes do FastHTML, permitindo aos desenvolvedores definir a estrutura e o estilo de cada elemento.
Isso significa que, ao criar um componente, você pode utilizá-lo em diversas partes do site sem precisar repetir o código. Isso facilita a manutenção e torna o desenvolvimento mais ágil.
Criando o a Base do Aplicativo da Lista de Tarefas
Vamos explorar melhor a funcionalidade dos componentes construindo um aplicativo de lista de tarefas.
Para isso, criaremos dois arquivos: aplicativo.py, onde desenvolveremos a lógica da aplicação, e componentes.py, onde desenvolveremos os componentes reutilizáveis.
 
Para começar, no arquivo aplicativo.py, importaremos as funções essenciais do FastHTML que nos permitirão criar e executar o site.
Diferente do exemplo anterior, utilizaremos fast_app ao invés de FastHTML. Isso nos permite criar uma instância para a aplicação e outra para as rotas, proporcionando mais flexibilidade.
from fasthtml.common import fast_app, serve
app, routes = fast_app()
Agora, vamos definir a rota principal (homepage), da mesma forma que fizemos antes. Porém, desta vez, usaremos o decorator @routes, que, além de definir a URL, permite especificar o método HTTP (GET, POST, etc.) com o parâmetro methods.
from fasthtml.common import fast_app, serve
app, routes = fast_app()
@routes("/")
def homepage():
return "<h1>Bem vindo ao meu site com FastHTML.</h1>"
serve()
Executando esse código, o site estará disponível localmente, igual ao exemplo inicial dessa aula.
 
Criando e Utilizando o Primeiro Componente
Agora vamos aprender a criar componentes dinâmicos e reutilizáveis no FastHTML. Para isso, criaremos uma função que retorna um elemento HTML. O primeiro componente será responsável por gerar os títulos e subtítulos das páginas.
Esse componente será definido pela função gerar_titulo() que receberá como parâmetros o título e o subtítulo desejado.
Dentro dessa função retornaremos uma única <div> que envolverá todo o conteúdo exibido: um título em <h1>, um parágrafo <p> com o subtítulo e um segundo parágrafo <p> com um texto padrão.
Para utilizar esses elementos HTML, precisamos importá-los a partir do módulo fasthtml.common.
from fasthtml.common import Div, H1, P
def gerar_titulo(titulo, subtitulo):
return Div(
H1(titulo),
P(subtitulo),
P("Esse componente foi gerado com FastHTML")
)
Com isso, temos nosso primeiro componente criado e pronto para ser utilizado em diferentes páginas.
Por exemplo, dentro do arquivo aplicativo.py, vamos importar esse componente e adicioná-lo à função homepage() que havíamos declarado anteriormente.
Basta substituir a antiga tag <h1> que tínhamos por uma chamada à função gerar_titulo, passando para ela o título e o subtítulo que você deseja exibir.
Além disso, por se tratar de um componente reutilizável, podemos criar uma segunda rota chamada blog, na qual utilizaremos o mesmo componente para gerar um título e um subtítulo diferentes.
from fasthtml.common import fast_app, serve
from componentes import gerar_titulo
app, routes = fast_app()
@routes("/")
def homepage():
return gerar_titulo("Homepage", "Brincando com o FastHTML")
@routes("/blog")
def blog():
return gerar_titulo("Blog", "Blog com artigos para você aprender Python")
serve()
Agora, ao acessar o site, teremos duas páginas diferentes (homepage e blog), com o mesmo componente gerando os títulos e subtítulos.
  
Perceba que com o uso desses componentes podemos criar todo o HTML das páginas através do Python.
Por padrão o FastHTML inclui uma estilização padrão, mas você também pode personalizar e estilizar suas páginas com um CSS próprio.
Criando o Componente Formulário da Lista de Tarefas
Além do título, nosso aplicativo precisa de mais dois componentes: um formulário para adicionar tarefas e uma lista interativa de tarefas. Vamos começar pelo formulário.
No arquivo componentes.py, criaremos a função gerar_formulario(). Para isso, importaremos os elementos Form, Input e Button.
O Form() é o contêiner principal que envolverá todos os elementos do formulário, nosso formulário em si. É ele quem define como os dados serão enviados ao servidor e qual ação será tomada quando o usuário clicar no botão de envio.
Além de conter o campo de entrada (Input) e o botão de envio (Button), o Form() recebe os atributos method e action:
•	method=”post”: Define o método HTTP que será usado ao enviar o formulário. No caso, é o método POST, que é utilizado quando estamos enviando dados para o servidor.
•	action=”/adicionar_tarefa”: Especifica para onde os dados do formulário serão enviados. Nesse caso, ao submeter o formulário, os dados serão enviados para a rota /adicionar_tarefa.
O Input() é o campo onde o usuário digitará a nova tarefa. Ele recebe 3 argumentos:
•	type=”text”: Define que este campo de entrada é do tipo texto, permitindo ao usuário digitar qualquer texto livremente.
•	name=”tarefa”: O atributo name define o nome do campo de entrada. Esse nome será usado no servidor para identificar o valor enviado pelo usuário. No nosso caso, a tarefa digitada será enviada com o nome tarefa.
•	placeholder=”Insira a tarefa a ser adicionada”: O placeholder é um texto que aparece dentro do campo de texto antes de o usuário digitar algo. Funciona como uma dica visual que indica ao usuário o que ele deve fazer.
Por fim, o Button() é o botão de envio do formulário. Quando o usuário clica nele, os dados do formulário são enviados para a URL especificada no atributo action. Como parâmetro, passamos o texto que desejamos exibir no botão.
Essa função retornará o nosso componente formulário.
def gerar_formulario():
formulario = Form(
Input(type="text", name="tarefa", placeholder="Insira a tarefa a ser adicionada"),
Button("Enviar"),
method="post",
action="/adicionar_tarefa",
)
return formulário
Implementando o Formulário ao nosso Aplicativo
Agora, voltando ao arquivo aplicativo.py, vamos importar o componente do formulário e adicioná-lo dentro da página inicial.
Ao invés de termos o componente que gera o título, vamos ter o componente do formulário.
from fasthtml.common import fast_app, serve
from componentes import gerar_titulo, gerar_formulario
app, routes = fast_app()
@routes("/")
def homepage():
formulario = gerar_formulario()
return formulario
@routes("/blog")
def blog():
return gerar_titulo("Blog", "Blog com artigos para você aprender Python")
serve()
Salvando nosso arquivo e atualizando a página inicial do site, teremos agora a estrutura básica do formulário de lista de tarefas.
 
Componentes Prontos do FastHTML
O FastHTML oferece diversos componentes prontos que simplificam a criação de páginas. Um desses componentes é o Titled, que auxilia na estruturação de páginas ao exibir um título principal seguido por outros elementos.
Em vez de simplesmente exibir o formulário na nossa homepage, podemos utilizar a função Titled para apresentar um título na página, seguido do formulário.
Para isso, basta importar essa função do FastHTML e adicioná-la ao retorno da função homepage().
O primeiro argumento deve ser o título da página, e os argumentos seguintes serão os elementos que você deseja renderizar, que neste caso é o nosso formulário.
from fasthtml.common import fast_app, serve, Titled
from componentes import gerar_titulo, gerar_formulario
app, routes = fast_app()
@routes("/")
def homepage():
formulario = gerar_formulario()
return Titled("Lista de Tarefas", formulario)
@routes("/blog")
def blog():
return gerar_titulo("Blog", "Blog com artigos para você aprender Python")
serve()
Após atualizar o site, a página inicial exibirá o título e o formulário centralizados, com um espaçamento adequado.
 
Criando a Rota para Adicionar Tarefa
Dentro do formulário ao clicar no botão Enviar, as informações precisam ser enviadas para a rota /adicionar_tarefa, que ainda não existe. Precisamos criá-la.
Primeiro, vamos definir uma lista vazia chamada lista_tarefas, que armazenará as tarefas adicionadas pelo usuário. Em uma aplicação completa, você integraria o FastHTML a um banco de dados para registrar essas informações.
No entanto, como o foco desta aula é apresentar o FastHTML, não abordaremos a integração com o banco de dados. Portanto, as informações permanecerão apenas enquanto a página estiver aberta.
Com a lista de tarefas definida, vamos criar nossa rota /adicionar_tarefa. Essa rota aceitará requisições do tipo POST, que é como o navegador envia dados do formulário para o servidor.
Dentro dessa rota, teremos a função adicionar_tarefa, que receberá a tarefa como uma string. Se a tarefa não estiver vazia, ela será adicionada à lista de tarefas.
É necessário nomear a variável que receberá os dados do formulário, neste caso a variável tarefa e, além disso, especificar o tipo da variável (string).
Também precisamos importar o RedirectResponse, que nos permite redirecionar o usuário para uma URL específica após o envio do formulário e qual o código de status HTTP usar.
É importante utilizar um status de redirecionamento (303) para garantir que a operação ocorra corretamente.
Como a homepage só aceita requisições do tipo GET, não informar o código de redirecionamento pode causar problemas com a requisição do tipo POST da rota /adicionar_tarefa.
from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario
app, routes = fast_app()
lista_tarefas = []
@routes("/")
def homepage():
formulario = gerar_formulario()
return Titled("Lista de Tarefas", formulario)
@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
if tarefa:
lista_tarefas.append(tarefa)
return RedirectResponse(url="/", status_code=303)
@routes("/blog")
def blog():
return gerar_titulo("Blog", "Blog com artigos para você aprender Python")
serve()
Componente Lista de Tarefas
Com o formulário pronto e a lista de tarefas criada, precisamos exibir essa lista na página inicial para que o usuário possa visualizá-la e interagir. Para isso, criaremos o componente gerar_lista_tarefas.
Esse componente será responsável por exibir a lista de tarefas e fornecer uma opção para exclusão de itens. Para isso, precisaremos importar os elementos:
•	Ul() cria uma lista não ordenada (itens sem numeração sequencial).
•	Li() cria os elementos da lista.
•	A() cria uma tag de âncora, permitindo adicionar um link ao lado de cada item da lista para excluí-lo.
Após importar os elementos, definiremos a função gerar_lista_tarefas, que receberá a lista de tarefas que queremos exibir.
Dentro dessa função, criaremos uma variável chamada itens_lista. Para cada tarefa na lista de tarefas, geraremos um item de lista (Li).
Cada item incluirá o nome da tarefa e um link de exclusão ao lado, que será criado com a função A(). Esse link permitirá ao usuário clicar e remover a tarefa correspondente.
Para garantir que o link de exclusão funcione corretamente, precisaremos percorrer a lista de tarefas usando a função enumerate, que fornece tanto o índice da tarefa (armazenado na variável i) quanto o nome da tarefa (armazenado na variável tarefa).
Assim, para cada tarefa, criaremos um item de lista com a função Li(), contendo o nome da tarefa e um link “Excluir” ao lado. O link receberá o atributo href, que apontará para a rota de exclusão.
Para que o link de exclusão funcione dinamicamente e selecione a tarefa correta, utilizaremos o índice da tarefa. Isso significa que cada link “Excluir” apontará para uma URL específica associada à sua tarefa.
Após criar todos os itens da lista, o próximo passo é colocá-los dentro da nossa lista não ordenada, que aparece com marcadores ao lado e não com números. Para isso, utilizamos a função Ul().
A função Ul() recebe como argumento todos os itens da lista. O asterisco antes de itens_lista serve para “desempacotar” a lista, ou seja, passar cada item individualmente para dentro da função, em vez de enviar a lista inteira como um único item.
Dessa forma, o FastHTML entende que queremos que cada item apareça como um <li> separado dentro do <ul>.
Por fim, a função retornará a lista criada.
from fasthtml.common import Div, H1, P, Form, Input, Button, Ul, Li, A
def gerar_titulo(titulo, subtitulo):
return Div(
H1(titulo),
P(subtitulo),
P("Esse componente foi gerado com FastHTML")
)
def gerar_formulario():
formulario = Form(
Input(type="text", name="tarefa", placeholder="Insira a tarefa a ser adicionada"),
Button("Enviar"),
method="post",
action="/adicionar_tarefa",
)
return formulario
def gerar_lista_tarefas(lista_tarefas):
itens_lista = [Li(tarefa, " - ", A("Excluir", href=f"/deletar/{i}")) for i, tarefa in enumerate(lista_tarefas)]
lista = Ul(
*itens_lista
)
return lista
Exibindo a Lista de Tarefas
Para gerar e visualizar a lista de tarefas atual na nossa página inicial, precisamos integrar o componente gerar_lista_tarefas na função homepage(). Isso será feito passando a lista de tarefas atual como argumento para o componente.
Primeiro, importe o componente gerar_lista_tarefas no arquivo aplicativo.py. Em seguida, armazene o componente gerado na variável elemento_lista_tarefas e retorne essa variável dentro da função Titled().
from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefas
app, routes = fast_app()
lista_tarefas = []
@routes("/")
def homepage():
formulario = gerar_formulario()
elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)
Criando a Rota para Deletar os Itens
Para que o link “Excluir” remova itens da lista de tarefas, precisamos criar uma rota que nos permita remover esses itens. O decorator dessa rota será dinâmico, pois cada item terá sua própria rota de exclusão.
Na rota, usaremos a variável dinâmica {posicao} para capturar o índice da tarefa na URL e passá-lo para a função deletar(). Esse índice representa a posição da tarefa que desejamos remover da lista.
A função deletar(posicao: int) será chamada quando a rota for acessada. Ela recebe o parâmetro posicao, que indica qual item da lista deve ser deletado. O :int após posicao indica que esperamos que essa variável seja um número inteiro.
Dentro da função, primeiro verificamos se o valor de posicao é válido, ou seja, se corresponde a uma tarefa existente na lista. Fazemos isso verificando se o índice da tarefa (posicao) é menor que o tamanho da lista de tarefas.
Se o índice for maior ou igual ao tamanho da lista, significa que a posição não existe e a função não realizará nenhuma ação. Se a posição for válida, utilizamos o método pop(posicao) para remover a tarefa correspondente da lista.
Após a remoção, redirecionamos o usuário de volta para a página inicial com RedirectResponse.
from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefas
app, routes = fast_app()
lista_tarefas = []
@routes("/")
def homepage():
formulario = gerar_formulario()
elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)
@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
if tarefa:
lista_tarefas.append(tarefa)
return RedirectResponse(url="/", status_code=303)
@routes("/deletar/{posicao}")
def deletar(posicao: int):
if len(lista_tarefas) > posicao:
lista_tarefas.pop(posicao)
return RedirectResponse(url="/", status_code=303)
@routes("/blog")
def blog():
return gerar_titulo("Blog", "Blog com artigos para você aprender Python")
serve()
Salvando o código e acessando a página do aplicativo, você poderá adicionar e remover itens da lista de tarefas.
 
Com isso, nosso aplicativo web de lista de tarefas está completo. Porém, podemos implementar funcionalidades adicionais com HTMX para tornar a aplicação ainda mais dinâmica e eficiente, permitindo adicionar e excluir tarefas sem recarregar a página.
HTMX no FastHTML
O HTMX é uma ferramenta poderosa que permite atualizar partes da página de forma dinâmica, sem a necessidade de recarregar a página inteira. Isso melhora a experiência do usuário e torna a aplicação mais responsiva.
No nosso projeto, utilizaremos quatro atributos do HTMX:
•	HX-POST: Define o método HTTP para a requisição, semelhante ao método POST no HTML, mas com controle adicional sobre quais partes da página são atualizadas.
•	HX-GET: Define o método HTTP da requisição como GET, permitindo recuperar dados sem recarregar a página.
•	HX-TARGET: Especifica o elemento da página que será atualizado com a resposta do servidor. Em vez de atualizar o conteúdo completo, apenas a parte definida será modificada.
•	HX-SWAP: Define como a resposta do servidor será incorporada à página.
Repare que todos os atributos relacionados ao HTMX começam com a notação hx_.
Vamos implementar esses parâmetros em nossos componentes, começando pelo gerar_formulario().
Dentro da função Form(), podemos adicionar os atributos HTMX hx_post, hx_target e hx_swap. Esses atributos permitem que o formulário faça uma requisição sem recarregar a página quando for enviado.
O atributo hx_post=”/adicionar_tarefa” informa ao HTMX que, ao enviar o formulário, ele deve fazer uma requisição POST para a URL /adicionar_tarefa. A requisição será feita em segundo plano, sem recarregar a página.
O hx_target=”#lista-tarefas” define o alvo da atualização, ou seja, o elemento HTML que será substituído pelo conteúdo retornado pela requisição. Nesse caso, a lista de tarefas (identificada pelo id lista-tarefas) será atualizada.
Por fim, o atributo hx_swap=”outerHTML” diz ao HTMX que ele deve substituir todo o conteúdo da lista de tarefas pela nova lista gerada, em vez de apenas atualizar o conteúdo interno.
def gerar_formulario():
formulario = Form(
Input(type="text", name="tarefa", placeholder="Insira a tarefa a ser adicionada"),
Button("Enviar"),
method="post",
action="/adicionar_tarefa",
hx_post="/adicionar_tarefa",
hx_target="#lista-tarefas",
hx_swap="outerHTML"
)
return formulario
Agora, vamos ajustar o componente gerar_lista_tarefas. Adicionaremos o identificador id=”lista-tarefas” à nossa lista para garantir que o componente gerar_formulario() consiga identificar qual elemento deve ser atualizado.
Além disso, definiremos os atributos HTMX para o link de exclusão dos itens da lista criado com a função A().
Nesse componente teremos o atributo hx_get=f”/deletar/{i}” para informar que, ao clicar no link “Excluir”, uma requisição GET será feita para a URL /deletar/{i}, onde {i} é o índice da tarefa que estamos removendo.
Assim como no formulário, essa requisição acontece em segundo plano, sem recarregar a página.
O atributo hx_target=”#lista-tarefas” novamente indica o alvo da atualização, que é o elemento com o ID #lista-tarefas.
E por fim, novamente usaremos o hx_swap=”outerHTML” define que o conteúdo da lista de tarefas deve ser substituído pelo novo conteúdo retornado.
Agora, vamos modificar as rotas adicionar_tarefa e deletar. Essas rotas não devem mais redirecionar o usuário, mas sim retornar a nova lista gerada.
Portanto, ao invés de retornar RedirectResponse, as rotas agora retornarão a função gerar_lista_tarefas().
from fasthtml.common import fast_app, serve, Titled, RedirectResponse
from componentes import gerar_titulo, gerar_formulario, gerar_lista_tarefas
app, routes = fast_app()
lista_tarefas = []
@routes("/")
def homepage():
formulario = gerar_formulario()
elemento_lista_tarefas = gerar_lista_tarefas(lista_tarefas)
return Titled("Lista de Tarefas", formulario, elemento_lista_tarefas)
@routes("/adicionar_tarefa", methods=["post"])
def adicionar_tarefa(tarefa: str):
if tarefa:
lista_tarefas.append(tarefa)
return gerar_lista_tarefas(lista_tarefas)
@routes("/deletar/{posicao}")
def deletar(posicao: int):
if len(lista_tarefas) > posicao:
lista_tarefas.pop(posicao)
return gerar_lista_tarefas(lista_tarefas)
@routes("/blog")
def homepage():
return gerar_titulo("Blog", "Blog com artigos para você aprender Python")
serve()
Agora, ao adicionar ou excluir tarefas, a página não será recarregada completamente. Apenas a lista de tarefas será atualizada.
 
Conclusão – Como Criar WebApps com Python – FastHTML
Na aula de hoje, eu te mostrei como utilizar o FastHTML para criar WebApps com Python! Essa abordagem simples e eficaz facilita a criação de aplicativos web modernos utilizando Python.
A integração com HTMX proporciona um desenvolvimento front-end dinâmico e responsivo, melhorando tanto a experiência de desenvolvimento quanto a do usuário final.
Para desenvolvedores familiarizados com Python que procuram uma maneira de construir aplicativos web sem depender de múltiplas linguagens, o FastHTML é uma excelente escolha.
Embora não seja necessário escrever códigos em HTML e CSS, é importante ter conhecimento dessas tecnologias ao trabalhar com o FastHTML.
Por isso, caso você queira se tornar um desenvolvedor web completo, confira nossos cursos:

