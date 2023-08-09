from django.http import HttpResponse
from django.shortcuts import render
from app1.models import Question,Answer,Level

def index(request):
    html="""<!DOCTYPE html>
            <html lang="en">
            <head>
                <meta charset="UTF-8">
                <meta name="viewport" content="width=device-width, initial-scale=1.0">
                <title>Document</title>
            </head>
            <body>
                <ul>
                    <li><a href='app1/tablas'>Tablas</a></li>
                    <li><a href='mostrar/'>Mostrar</a></li>
                    <li><a href='https://www.google.com' target='_blank'k>Google</a></li>
                </ul>
            </body>
            </html>
    """
    return HttpResponse(html)

def mostrar(request, id):
    ##lista=["Juan", "Pedro", "José", "Ana", "Luis","Andrés","Carlos","Jonás"]
    lista=[{"id":0,"nombre": "Jonnathan","correo":"jonnathan@gmail.com", "contrasena":"abc123"},
           {"id":1,"nombre": "Juan","correo":"juan@gmail.com", "contrasena":"def456"},
           {"id":2,"nombre": "Pedro","correo":"pedro@gmail.com", "contrasena":"hif789"},
           {"id":3,"nombre": "Luis","correo":"luis@gmail.com", "contrasena":"ghi123"}]
    print(len(lista))
    data={}
    ##data["id"]=lista[id]
    ##data["nombre"]=nombre
    data["persona"]=lista[id]
    data["len"]=len(lista)-1
    return render(request, "index.html",data)

def home(request):
    data={}
    hobbies=["caminar", "bailar", "reir", "correr", "cantar", "dibujar"]
    data["lista"]=hobbies
    data["title"]="Bienvenido a mi página"
    return render(request, "home.html", data)

def proyectos(request):
    return render(request, "proyectos.html", {"title":"Mis Proyectos"})

def contactame(request):
    return render(request, "contactame.html", {"title":"Contáctame"})

def formulario1(request):
    data={}
    if request.method=="POST":
        print("Peticion: ",request.POST)
        name = request.POST["name"]
        age = request.POST.get("age")
        print(name,age)
    if request.method=="GET":
        data["title"]="Formulario GET"
    return render(request, "forms/form_user.html",data)

def formulario2(request):
    return render(request, "forms/form_post.html", {"title":"Formulario2"})

def formulario3(request):
    return render(request, "forms/form_employee.html", {"title":"Formulario3"})

def pregunta(request, id):    
    data={}
    data["questions"] = p = Question.objects.filter(level= id)    
    data["answers"] = Answer.objects.filter(question_id__in=data["questions"])
    print(data["answers"])
    data["valor"] = id        
    return render(request, "questions/pregunta.html",data)

def principal(request):    
    data={}
    niveles= Level.objects.all()
    data["niveles"]= niveles
    return render(request, "questions/principal.html",data)

def resultados(request):
    data={}
    if request.method=="POST":
        valor = request.POST.get("valor_form")        
        data["valor"] = valor
    return render(request, "questions/resultados.html",data)