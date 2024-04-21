from django.shortcuts import render, HttpResponse

html_base = """
    <h1>Mi Web Personal</h1>
    <ul>
        <li><a href="/">Portada</a></li>
        <li><a href="/about">Acerca de</a></li>
        <li><a href="/portfolio">Portafolio</a></li>
        <li><a href="/contact">Contacto</a></li>
    </ul>

"""

def home(request):
    return HttpResponse(html_base + """
        <h2>Bienvenidos</h2>
        <p>Esta es la portada</p>
    """)

def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Tavo y le estoy dando duro a Django desde hace tiempo. Ya lo entiendo!</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portafolio</h2>
        <p>Aquí te muestro mi producción profesional</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>Tienes mis cuentas electrónicas</p>
    """)    