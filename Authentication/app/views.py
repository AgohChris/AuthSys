from django.shortcuts import redirect, render
from django.shortcuts import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.


def home(request):
        
    return render(request, 'app/index.html')


def register(request):
    if request.method == "POST":
        username = request.POST['username']
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        email = request.POST['email']
        password = request.POST['password']
        password1 = request.POST['password1']
        
        if password1 != password:
            messages.error(request, "les mots de passes ne corresponde pas")
        
        mon_utilisateur = User.objects.create_user(username, email, password)
        mon_utilisateur.firt_name = firstname
        mon_utilisateur.last_name = lastname
        
        mon_utilisateur.save()
        messages.success(request, 'Votre compte à été créé aec succès hein')
        return redirect('login')
    
    return render(request, 'app/register.html')


def login(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        
        if user is not None:
            login(request, user)
            firstname = user.firstname
            # messages.success(request, f"Bienvenue {username}")
            return render(request, 'app/index.html', {'firstame':firstname})
        else:
            messages.error(request, 'Username ou password incorrect')
            return redirect('lgoin')
    return render(request, 'app/index.html', {'firstame':firstname})


def logout(request):
    
    pass