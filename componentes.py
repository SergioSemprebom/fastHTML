from fasthtml.common import Div, H1, P # type: ignore

def gerar_titulo(titulo, subtitulo):
    return Div(
        H1(titulo),
        P(subtitulo),
        P("Esse componente foi criado com FastHTML")
    )