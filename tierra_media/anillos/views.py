from django.shortcuts import render
from .models import Usuario, Post 
from django.contrib.auth import authenticate, login 

def index(request):
    return render(request, 'index.html')

def registro(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password'] 
        user = User.objects.create_user(username=username, password=password)
        login(request, user)
        return redirect('index')

    return render(request, 'registro.html')
         
def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, 'login.html', {'error':'Usuario o contraseña inválido'})

    return render(request, 'login.html')

def logout(request):
     # Lógica de cierre de sesión

 def lista_posts(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {'posts': posts})

def post_detalle(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post.html', {'post': post})
