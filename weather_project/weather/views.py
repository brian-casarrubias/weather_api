from django.shortcuts import render
import requests
import http
import os


# Create your views here.
DESKTOP_PATH = os.path.join('C://Users//Brian//Desktop')


#were retriving our API key currently its in my desktop
with open(os.path.join(DESKTOP_PATH, 'API KEY.txt'), 'r') as f:
    API_KEY = f.read()


def home(request):
   
    
    if request.method == 'GET':
        CITY =  request.GET.get('q', 'None') #the value were retriveing from our website search bar
        if CITY == 'None':
            CITY = 'Las Vegas'
            BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='
            COMBINED_URL = BASE_URL + CITY + '&units=imperial&appid=' + API_KEY 

        elif CITY.isdigit():
             ZIP_CODE = str(CITY)
             BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?zip='
             COMBINED_URL = BASE_URL + ZIP_CODE + '&units=imperial&appid=' + API_KEY
        else:
             
            BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='
            COMBINED_URL = BASE_URL + CITY + '&units=imperial&appid=' + API_KEY 
            
        WEATHER = requests.get(COMBINED_URL).json()
        
           

        try:
            if 'Rain'  in WEATHER['weather'][0]['main']:
                weather_image = 'weather/images/rain1.png'
               
        except:
            CITY = 'Las vegas'
            BASE_URL = 'https://api.openweathermap.org/data/2.5/weather?q='
            COMBINED_URL = BASE_URL + CITY + '&units=imperial&appid=' + API_KEY 
        
            WEATHER = requests.get(COMBINED_URL).json()
        if 'Rain'  in WEATHER['weather'][0]['main']:
            weather_image = 'weather/images/rain2.png'
            print(WEATHER['weather'][0]['main'])

        elif 'Clouds' in  WEATHER['weather'][0]['main']:
                weather_image = 'weather/images/cloudy.png'
               
              
        elif 'Clear' in  WEATHER['weather'][0]['main']:
                weather_image = 'weather/images/sunny.png'
                
            
        elif 'Haze' in  WEATHER['weather'][0]['main']:
                weather_image = 'weather/images/cloudy.png'
               
        elif 'Snow' in  WEATHER['weather'][0]['main']:
                weather_image = 'weather/images/snow.png'
                
        elif 'Mist' in WEATHER['weather'][0]['main']:
             weather_image = 'weather/images/rain4.png'   
        elif 'Wind' in WEATHER['weather'][0]['main']:
             weather_image = 'weather/images/windy1.png'  
             
        else:
                weather_image = 'weather/images/cloudy.png'
      

    context = {
            'current_temperature':WEATHER['main']['temp'],
            'temp_max':WEATHER['main']['temp_max'],
            'temp_min':WEATHER['main']['temp_min'],
            'temp_feels_like':WEATHER['main']['feels_like'],
            'description':WEATHER['weather'][0]['description'],
            'wind_speed':WEATHER['wind']['speed'],
            'humidity':WEATHER['main']['humidity'],
            'City':CITY,
            'weather_image':weather_image,
            

        }
       
    

    return render(request, 'weather/index.html', context)


