from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages

import pandas as pd
import geopandas as gpd
from shapely.geometry import Point
from django.conf import settings
import os

from .forms import SignupForm

# Create your views here.
@login_required
def csv_to_shapefile(request):
    if request.method == 'POST':
        csv_file = request.FILES['csv_file']
        if not csv_file.name.endswith(".csv"):
            messages.error(request, 'File is not CSV type')
            return render(request, 'conv_csv/wrongFile.html')
        df = pd.read_csv(csv_file)
        geometry = [Point(xy) for xy in zip(df.Longitude, df.Latitude)]
        gdf = gpd.GeoDataFrame(df, geometry=geometry)
        shapefile_path = os.path.join(settings.MEDIA_ROOT, 'output.shp')
        gdf.to_file(shapefile_path, driver='ESRI Shapefile')
        return render(request, 'conv_csv/conversion_complete.html')
    else:
        return render(request, 'conv_csv/csv_to_shapefile.html')
    
def home(request):
    return render(request, 'conv_csv/home.html')

from django.shortcuts import render

# Create your views here.
def contact(request):
    return render(request, 'conv_csv/contact.html')

def signup(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        
        if form.is_valid():
            form.save()
            
            return redirect('/login/')
        
    form = SignupForm()
    context = {'form': form}
    return render(request, 'conv_csv/signup.html', context)