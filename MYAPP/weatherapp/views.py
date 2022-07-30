from django.shortcuts import render
import requests

def home(request):
    city=request.POST.get('city')
    ource = requests.get("http://api.weatherapi.com/v1/current.json?key=b5fef2042fbb497faeb182122220505&q="+city+"&aqi=no")
    fg=ource.json()
    datas = {
    "location": str(fg["location"]["name"]),
    "region":str( fg["location"]["region"]),
    "temp": str(fg["current"]["temp_c"]),
    "country": str(fg["location"]["country"]),
    }
    
    print(fg)
    return render(request,"index.html",datas)



