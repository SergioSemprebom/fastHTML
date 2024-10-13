from fasthtml.common import fast_app, serve

app, routes = fast_app()


@routes("/")
def homepage():
    return "<h1>Bem vindo JESUS</h1>"

serve()
