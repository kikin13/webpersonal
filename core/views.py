from django.shortcuts import render, HttpResponse

html_base = """
<h1>Mi web personal</h1>
<ul>
    <li> <a href="/">Portada</a> </li>
    <li> <a href="/about-me/">Acerca de</a> </li>
    <li> <a href="/portfolio/">Portafolio</a> </li>
    <li> <a href="/contact/">Contacto</a> </li>
</ul>
"""

# Create your views here.
def home(request):
    return HttpResponse(html_base + """
        <h2>Portada</h2>
        <p>Esto es la portada</p>
    """)
    
def about(request):
    return HttpResponse(html_base + """
        <h2>Acerca de</h2>
        <p>Me llamo Luis Enrique Cervantes Caute y aprendo Django</p>
    """)

def portfolio(request):
    return HttpResponse(html_base + """
        <h2>Portafolio</h2>
        <p>Aqui se muestran todos los proyectos o trabajos realizados</p>
    """)

def contact(request):
    return HttpResponse(html_base + """
        <h2>Contacto</h2>
        <p>WhatsApp: 276-133-54-90<br>
        correo electronico: cervtsluis13@gmail.com</p>
    """)