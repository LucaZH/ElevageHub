from django.shortcuts import render,redirect

from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.db import connection
from django.contrib import messages

from elevagehub_app.models import Animal,Activite
@login_required
def mesanimaux(request):
    if request.method == 'POST':
        nom = request.POST.get('nom')
        espece = request.POST.get('espece')
        date = request.POST.get('date')
        poids_initial = request.POST.get('poids_initial')
        notes = request.POST.get('notes')
        photo = request.FILES.get('image')
        user = request.user
        animal = Animal(nom=nom, espece=espece, date=date, poids_initial=poids_initial, notes=notes, photo=photo, user=user)
        animal.save()
    user = request.user
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM elevagehub_app_animal WHERE user_id=%s", [user.id])
        animals = cursor.fetchall()
    animal_list = []
    for animal in animals:
        animal_dict = {
            'id': animal[0],
            'nom': animal[1],
            'espece': animal[2],
            'date': animal[3],
            'poids_initial': animal[4],
            'note': animal[5],
            'photo': animal[6],
            'user':animal[7]

        }
        animal_list.append(animal_dict)
    print(animal_list)
    context = {'animal_list': animal_list}
    return render(request, 'mesanimaux.html', context)
@login_required
def delete_animal(request,animal_id):
    with connection.cursor() as cursor:
        cursor.execute("DELETE FROM elevagehub_app_animal WHERE id = %s", [animal_id])
    return redirect('mesanimaux')

@login_required
def ajouter_animal(request):
    if request.method == 'POST':
        nom = request.POST['nom']
        espece = request.POST['espece']
        date = request.POST['date']
        poids_initial = request.POST['poids_initial']
        notes = request.POST['notes']
        photo = request.FILES.get('photo')
        user = request.user
        cursor = connection.cursor()
        cursor.execute("INSERT INTO elevagehub_app_animal (nom, espece, date, poids_initial, notes, photo, user_id) VALUES (%s, %s, %s, %s, %s, %s, %s)", [nom, espece, date, poids_initial, notes, photo, user.id])
        messages.success(request, 'Animal ajouté avec succès')
        return redirect('mesanimaux')
    return render(request, 'mesanimaux.html')


def home(request):
    return render(request, 'index.html')

@login_required
def activites(request):
    if request.method == 'POST':
        type_activite = request.POST.get('type_activite')
        espece = request.POST.get('espece')
        date = request.POST.get('date')
        notes = request.POST.get('notes')
        photo = request.FILES.get('image')
        animal = request.POST.get('animal')
        user = request.user
        activites = Activite(type_activite=type_activite, animal=animal, date_activite=date, notes=notes, photo=photo, user=user)
        activites.save()
    user = request.user
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM elevagehub_app_activite WHERE user_id=%s", [user.id])
        activites = cursor.fetchall()
    activite_list = []
    for activite in activites:
        activite_dict = {
            'id': activite[0],
            'user': activite[1],
            'animal': activite[2],
            'type_activite': activite[3],
            'date_activite': activite[4],
            'notes': activite[5],
            'photo': activite[6],

        }
        activite_list.append(activite_dict)
        user = request.user
    with connection.cursor() as cursor:
        cursor.execute("SELECT * FROM elevagehub_app_animal WHERE user_id=%s", [user.id])
        animals = cursor.fetchall()
    animal_list = []
    for animal in animals:
        animal_dict = {
            'id': animal[0],
            'nom': animal[1],
            'espece': animal[2],
            'date': animal[3],
            'poids_initial': animal[4],
            'note': animal[5],
            'photo': animal[6],
            'user':animal[7]

        }
        animal_list.append(animal_dict)
    print(activite_list)
    context = {'activite_list': activite_list,"animal_list":animal_list}
    return render(request, 'activites.html', context)

@login_required
def stocks(request):
    return render(request, 'stocks.html')

def signup(request):
    return render(request,'signup.html')

@login_required
def animal_list(request):
    user = request.user
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM elevagehub_app_animal WHERE user_id=%s", [user.id])
    animals = cursor.fetchall()
    animal_list = []
    for animal in animals:
        animal_dict = {
            'id': animal[0],
            'name': animal[1],
            'species': animal[2],
            'breed': animal[3],
            'gender': animal[4],
            'birthdate': animal[5],
            'weight': animal[6],
            'user_id': animal[7]
        }
        animal_list.append(animal_dict)
    context = {'animal_list': animal_list}
    return render(request, 'animal_list.html', context)
