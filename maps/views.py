from django.test import TestCase

# Create your tests here.

from django.shortcuts import render
from maps.models import project
from pathlib import Path
import pandas as pd

import requests
from pprint import pprint
import folium

from django.http import HttpResponse
import csv


from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas

def index(request):
    
    BASE_URL = 'https://nominatim.openstreetmap.org/search?format=json'
    m = folium.Map(zoom_start=4, width=800, height=400)
    city_between=None
    if request.method=='POST':
        zipcode_start = request.POST.get('zipcode_start')
        zipcode_end = request.POST.get('zipcode_end')
        city_start = request.POST.get('city_start')
        city_end = request.POST.get('city_end')
        city_between = request.POST.get('city_between')
        
        response = requests.get(f"{BASE_URL}&postalcode={zipcode_start}")
        response = requests.get(f"{BASE_URL}&city={city_start}")
        
        data = response.json()
        print('data',data)
        response = requests.get(f"{BASE_URL}&postalcode={zipcode_end}")
        response = requests.get(f"{BASE_URL}&city={city_end}")
        data1 = response.json()
        print(data1)

        latitude = data[0].get('lat')
        longitude = data[0].get('lon')
        
        name=data[0].get('display_name')
        print(latitude, longitude)

        latitude2 = data1[0].get('lat')
        longitude2 = data1[0].get('lon')

        name1=data1[0].get('display_name')
        print(latitude2, longitude2)
        print(name1)
           

        location = float(latitude), float(longitude)
        location2 = float(latitude2), float(longitude2)
        

        # create a Folium map centred at the above location
        # add markers at the locations
        folium.Marker(location, tooltip=name,icon=folium.Icon(color='green')).add_to(m)
        folium.Marker(location2, tooltip=name1, icon=folium.Icon(color='red')).add_to(m)

        if city_between:
            response = requests.get(f"{BASE_URL}&city={city_between}")
            data2 = response.json()
            latitude3 = data2[0].get('lat')
            longitude3 = data2[0].get('lon')
            name2=data2[0].get('display_name')
            location3 = float(latitude3), float(longitude3) 
            folium.Marker(location3, tooltip=name2, icon=folium.Icon(color='black')).add_to(m)
            line = folium.PolyLine(locations=[location, location2,location3], color='blue')
        else:
            line = folium.PolyLine(locations=[location, location2], color='blue')
        line.add_to(m)
        newdoc = project(city_start=city_start,city_end=city_end,city_between=city_between) 
        newdoc.save()
        
    return render(request, 'maps.html',{'m':m._repr_html_()})



def download_data_csv(request):
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachment; filename="data.csv"'

    writer = csv.writer(response)
    writer.writerow(['city_start', 'city_end', 'city_between'])  

    data = project.objects.all()
    for item in data:
        writer.writerow([item.city_start, item.city_end, item.city_between])  
    return response

def download_data(request):
    response = HttpResponse(content_type='application/pdf')
    response['Content-Disposition'] = 'attachment; filename="data.pdf"'

    pdf = canvas.Canvas(response, pagesize=letter)

    data = project.objects.all()  

   
    table_header = ['City Start', 'City End', 'City Between']
    y_position = 700  

  
    for header in table_header:
        pdf.drawString(100, y_position, header)
        y_position -= 20

  
    for item in data:
        row = [item.city_start, item.city_end, item.city_between]
        y_position -= 20

        for column in row:
            pdf.drawString(100, y_position, str(column))
            y_position -= 20

    pdf.showPage()
    pdf.save()

    return response
