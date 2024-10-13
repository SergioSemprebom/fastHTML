from fasthtml.common import fast_app, serve # type: ignore
from componentes import gerar_titulo


app, routes = fast_app()

@routes("/")
def homepage():
    return gerar_titulo("Homepage", "Brincando de FastHTML")

@routes("blog")
def homepage():
    return gerar_titulo("Blog", "Blog com artigos para você aprender Python")

serve()
