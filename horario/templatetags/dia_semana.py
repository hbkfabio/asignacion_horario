from django.template.defaulttags import register
from django.template.defaultfilters import linebreaksbr, urlize
...
@register.filter(is_safe=True, needs_autoescape=True)
def get_item(dictionary, key, autoescape=True):
    return dictionary.get(key)

@register.filter(is_safe=True)
def get_type(a, value):
    return type(value).__name__

@register.filter(is_safe=True, needs_autoescape=True)
def get_cursos_grupo(dictionary, key, autoescape=True):
    """
    Funcion que retorna en formato de texto los CursosGrupo obtenidos desde
    Horario.
    El formato del diccionario que recibe es:
    {
        codigo_periodo: [CursosGrupo, CursosGrupo, ...]
    }

    Retorna:
        * String, cadena de texto con resultados concatenados.
    """

    a = dictionary.get(key)
    txt = ""
    p = True

    for i in a:
        if p is True:
            txt += i.modulo.nombre + " / "
            p = False
        txt += i.curso_grupo.nombre + " / "

    return txt
