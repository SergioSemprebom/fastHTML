from fasthtml.common import fast_app, serve, Titled, RedirectResponse  # type: ignore
from componentes import gerar_titulo, gerar_formulario

app, routes = fast_app()

lista_tarefas = []

@routes("/")
def homepage():
    formulario = gerar_formulario()
    print(lista_tarefas)
    return Titled("Lista de Tarefas", formulario)

@routes("/adicionar_tarefa", method=["post"])
def adicionar_tarefas(tarefa: str):
    if tarefa:
        lista_tarefas.append(tarefa)
        return RedirectResponse(url="/", status_code=303)


@routes("/blog")
def homepage():
    return gerar_titulo("Blog", "Blog com artigos para você aprender Python")

serve()
