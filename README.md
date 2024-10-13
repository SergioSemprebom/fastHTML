# FastHTML

FastHTML: Crie Web Apps Modernas com Python
Construa aplicações web dinâmicas e responsivas sem escrever HTML, CSS ou JavaScript!

Este guia apresenta o FastHTML, um framework Python inovador que simplifica o desenvolvimento web, permitindo a criação de interfaces complexas e interativas utilizando apenas Python.

O que é FastHTML?

O FastHTML é um framework que permite criar aplicações web sem escrever código HTML, CSS ou JavaScript diretamente. Ele se integra ao HTMX, uma biblioteca que possibilita a atualização dinâmica de partes da página, sem recarregamento completo, proporcionando uma experiência de usuário mais fluida.

Instalação:

Bash
pip install python-fasthtml
Use code with caution.

Estrutura Básica:

Python
from fasthtml.common import FastHTML, serve

app = FastHTML()

@app.get("/")
def homepage():
  return "<h1>Bem-vindo ao meu site com FastHTML</h1>"

serve()
Use code with caution.

Componentes Reutilizáveis:

Crie componentes reutilizáveis para estruturar sua aplicação de forma modular e eficiente.

Python
from fasthtml.common import Div, H1, P

def gerar_titulo(titulo, subtitulo):
  return Div(
    H1(titulo),
    P(subtitulo),
    P("Esse componente foi gerado com FastHTML")
  )
Use code with caution.

Exemplo: Lista de Tarefas:

Construa uma aplicação de lista de tarefas com formulário para adicionar novas tarefas e funcionalidade de exclusão.

Python
from fasthtml.common import fast_app, serve, Titled
from componentes import gerar_formulario, gerar_lista_tarefas

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

serve()
Use code with caution.

HTMX para Interatividade:

Utilize atributos HTMX para adicionar interatividade sem recarregar a página, proporcionando uma experiência de usuário mais fluida.

Python
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
Use code with caution.

Conclusão:

O FastHTML oferece uma abordagem moderna e eficiente para o desenvolvimento web com Python. Sua integração com HTMX permite a criação de aplicações dinâmicas e responsivas, simplificando o processo de desenvolvimento e proporcionando uma experiência de usuário aprimorada.

Recursos Adicionais:

Site oficial do FastHTML
Documentação do HTMX
Observação: Conhecimento básico de HTML e CSS é recomendado para melhor compreensão e utilização do FastHTML.