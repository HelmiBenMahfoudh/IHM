from django.shortcuts import render, redirect
import json
from django.contrib import messages
from django.contrib.auth.models import User, auth


from travello.form import *
from .models import *

# Create your views here.

def index(request):
    form = SearchForm()
    dests = Destination.objects.all()
    hotels = Hotel.objects.all()

    


    return render(request, 'index.html', {'dests': dests, 'hotels' : hotels, 'form': form})

def search(request):

    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid(): 
            destination = form.cleaned_data['destination']
            num_nights = form.cleaned_data['num_nights']
            budget = form.cleaned_data['budget']
            typeOfRoom = form.cleaned_data['typeOfRoom']

            hotelsByDest = Hotel.objects.filter(dest__name=destination)
            valid_hotels = []

            for hotel in hotelsByDest:
                room_price = Room.objects.filter(hotelRoom=hotel, typeOfRoom=typeOfRoom, availability=True).values('price').first()
                if room_price and (room_price['price'] * num_nights <= budget):
                    valid_hotels.append({"hotel":hotel,"price":room_price['price']  * num_nights})

            request.session['valid_hotels']=json.dumps([{"hotel":h["hotel"].to_dict(),"price":h["price"] }for h in valid_hotels])

            
        filter=FilterForm(request.POST)   
        if filter.is_valid():
            serialized_list = request.session.get('valid_hotels')
            if serialized_list:
                valid_hotels = json.loads(serialized_list)  # Deserialize the list using JSON
                
                stars = filter.cleaned_data['stars']
                rate = filter.cleaned_data['rate']
                offer = filter.cleaned_data['offer']

                filtered_hotels = []
                for hotel in valid_hotels:
                    hotel_data = hotel["hotel"]
                    if stars and hotel_data["stars"] <= stars:
                        continue
                    if rate and hotel_data["rate"] <= rate:
                        continue
                    if offer and not hotel_data["offer"]:
                        continue    
                    filtered_hotels.append(hotel)
                    valid_hotels = filtered_hotels

        sort=SortForm(request.POST)   
        if sort.is_valid():
            serialized_list = request.session.get('valid_hotels')
            if serialized_list:
                valid_hotels = json.loads(serialized_list)

                sort_by=sort.cleaned_data['sort_by']
                
                if sort_by == 'lowest_rating':
                     valid_hotels = sorted(valid_hotels, key=lambda hotel: hotel["hotel"]["rate"])
                elif sort_by == 'highest_rating':
                    valid_hotels = sorted(valid_hotels, key=lambda hotel: hotel["hotel"]["rate"],reverse=True)
                elif sort_by == 'highest_stars':
                    valid_hotels = sorted(valid_hotels, key=lambda hotel: hotel["hotel"]["stars"], reverse=True)
                elif sort_by == 'lowest_stars':
                    valid_hotels = sorted(valid_hotels, key=lambda hotel: hotel["hotel"]["stars"])
                elif sort_by == 'lowest_price':
                    valid_hotels = sorted(valid_hotels, key=lambda hotel: hotel["price"])
                elif sort_by == 'highest_price':
                    valid_hotels = sorted(valid_hotels, key=lambda hotel: hotel["price"], reverse=True)
        return render(request, 'search.html', {'hotelsByDest': valid_hotels,'form': sort, 'filter':filter})
    return render(request, 'index.html', {'form': form})

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'invalid credentials...')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, "username taken...")
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request, "email taken...")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password1, email=email, first_name=first_name, last_name=last_name)
                user.save()
                messages.info(request, "user created...")
                return redirect('login')
        else:
            messages.info(request, "password not matched...")
            return redirect('register')
        return redirect('/')
    else:
        return render(request, 'register.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def contact(request):
    return render(request, 'contact.html')

def about(request):
    return render(request, 'about.html')

def news(request):
    return render(request, 'news.html')

def destinations(request):
    return render(request, 'destinations.html')