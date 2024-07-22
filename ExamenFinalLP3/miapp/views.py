from django.shortcuts import render, HttpResponse

layout = """
    <h1> Proyecto Web (LP3 - 2024) | Flor Cerdán </h1>
    <hr/>
    <ul>
        <li>

            EXAMEN FINAL
            <br>
            <a href="/inicio"> Inicio</a>
        </li>
        <li>
            <a href="/personas"> Mensaje de Saludo</a>
        </li>
    </ul>
    <hr/>
    """

def index(request):
    return render(request, "index.html")

def personas(request):
    return render(request, "personas.html")
