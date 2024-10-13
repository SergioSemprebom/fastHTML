from fasthtml.common import FastHTML, serve # type: ignore

app = FastHTML()

@app.get("/")
def homepage():
    return "<h1>Bem vindo ao meu Site com FastHTMl</h1>"

serve()