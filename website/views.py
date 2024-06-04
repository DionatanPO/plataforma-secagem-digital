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