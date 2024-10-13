from fasthtml.common import Div, H1, P, Form, Input, Button # type: ignore

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P("Esse componente foi criado com FastHTML")
    )

def gerar_formulario():
    formulario = Form(
        Input(type="text", name="tarefa", placeholder="Insira a tarefa a ser adicionada"),
        Button("Enviar"),
        method="post",
        action="/adicionar_tarefa"
    )
    return formulario

def gerar_lista_tarefas():
    pass