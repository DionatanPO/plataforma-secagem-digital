from django.shortcuts import render

def index(request):
    return render(request, 'websites/index.html')
def portifolio(request):
    return render(request, 'websites/projects.html')
def equipe(request):
    return render(request, 'websites/equipe.html')
def sobre(request):
    return render(request, 'websites/sobre.html')
def contato(request):
    return render(request, 'websites/contato.html')
def cursos(request):
    return render(request, 'websites/cursos.html')
def servicos(request):
    return render(request, 'websites/servicos.html')
def politica_privacidade(request):
    return render(request, 'websites/politica_privacidade.html')
def centro(request):
    return render(request, 'websites/centro.html')
def iot(request):
    return render(request, 'websites/iot.html')

def politica_privacidade2(request):
    return render(request, 'websites/politica_privacidade2.html')

def politica_privacidade3(request):
    return render(request, 'websites/politica_privacidade3.html')

def page1(request):
    return render(request, 'websites/page1.html')

def page2(request, turno_id):

    context = {

        'turno_id': turno_id,
        'parent': 'index',
        'segment': 'index'
    }
    return render(request, 'websites/page2.html', context)


def page3(request):
    return render(request, 'websites/page3.html')

def documentario(request):
    return render(request, 'websites/documentario.html')

def dionatan(request):
    return render(request, 'websites/dionatan.html')