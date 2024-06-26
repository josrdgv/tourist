from django.contrib import messages
import requests
from django.shortcuts import render, redirect
from .models import *
from .serializers import *
from rest_framework import generics
from rest_framework.permissions import AllowAny
from .forms import touristform
from django.core.paginator import Paginator, EmptyPage, InvalidPage


# Create your views here.

# Create your views here.
class tourist_create(generics.ListCreateAPIView):
    queryset = tour_destinations.objects.all()
    serializer_class = tourist_serializer
    permission_classes = [AllowAny]


class tourist_detail(generics.RetrieveAPIView):
    queryset = tour_destinations.objects.all()
    serializer_class = tourist_serializer


class tourist_update(generics.RetrieveUpdateAPIView):
    queryset = tour_destinations.objects.all()
    serializer_class = tourist_serializer


class touristdelete(generics.DestroyAPIView):
    queryset = tour_destinations.objects.all()
    serializer_class = tourist_serializer


def create_tourist_places(request):
    if request.method == 'POST':

        name = request.POST.get('name')
        district = request.POST.get('district')
        state = request.POST.get('state')
        map_link = request.POST.get('map_link')
        weather = request.POST.get('weather')
        description = request.POST.get('description')

        tour = tour_destinations(name=name, district=district, state=state, map_link=map_link, weather=weather,
                                 description=description)

        if tour:
            try:

                tour.save()
                api_url = 'http://127.0.0.1:8000/create/'
                data = {
                    'name': name,
                    'district': district,
                    'state': state,
                    'map_link': map_link,
                    'weather': weather,
                    'description': description,

                }

                response = requests.post(api_url, data=data,
                                         files={'destination_img': request.FILES.get('destination_img')})

                if response.status_code == 400:
                    messages.success(request, 'Reciepe inserted successfully')
                else:
                    messages.error(request, f'Reciepe is not incerted')

            except requests.RequestException as e:

                messages.error(request, f'Error during API {str(e)}')
        else:
            messages.error(request, 'Form is not valid')
            return redirect('/')

    return render(request, 'create_tourist_place.html')

    # messages.success(request,'Successfully registered')


def tourist_details(request, id):
    api_url = f'http://127.0.0.1:8000/detail/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        place_description = data['description'].split('.')
        return render(request, 'tourist_place_detail.html', {'place_description': place_description, 'data': data})
    return render(request, 'tourist_place_detail.html')


def index(request):
    api_url = 'http://127.0.0.1:8000/create/'
    try:

        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            original_data = data
            paginator = Paginator(original_data, 6)
            try:
                page = int(request.GET.get('page', 1))
            except:
                page = 1
            try:
                tour = paginator.page(page)
            except(EmptyPage, InvalidPage):
                tour = Paginator.page(paginator.num_pages)
            context = {
                'original_data': original_data,
                'tour': tour}
            return render(request, 'index.html', context)
        else:
            return render(request, 'index.html', {'error_message': f'Error:{response.status_code}'})
    except requests.RequestException as e:

        return render(request, 'index.html', {'error_message': f'Error:{str(e)}'})

    return render(request, 'index.html')


def destination_updation_details(request, id):
    api_url = f'http://127.0.0.1:8000/detail/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data = response.json()
        place_description = data['description'].split('.')
    return render(request, 'update_tourist.html', {'place_description': place_description, 'data': data})


def destination_update(request,id):
    if request.method == 'POST':

        name = request.POST.get('name')
        district = request.POST.get('district')
        state = request.POST.get('state')
        map_link = request.POST.get('map_link')
        weather = request.POST.get('weather')
        description = request.POST.get('description')
        print('Img URL', request.FILES.get('destination_img'))

        api_url = f'http://127.0.0.1:8000/update/{id}/'

        data = {
            'name': name,
            'district': district,
            'state': state,
            'map_link': map_link,
            'weather': weather,
            'description': description,

        }

        files = {'destination_img': request.FILES.get('destination_img')}
        response = requests.put(api_user=api_url, data=data, files=files)
        if response.status_code == 200:
            messages.success(request, 'Updated successfully')
            return redirect('/')
        else:
            messages.error(request, f'Error submitting data in rest API:{response.status_code} ')

    return render(request,'update_tourist.html')


def destination_delete(request, id):
    api_url = f'http://127.0.0.1:8000/delete/{id}/'
    response = requests.get(api_url)
    if response.status_code == 200:
        data=response.json()
        return render(request, 'delete.html', {'data': data})

    return render(request, 'delete.html')


