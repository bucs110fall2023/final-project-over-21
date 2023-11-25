from user import User
import requests

class Proxy:
    '''
    Proxy class makes API call for user's sign
    '''
    
    def __init__(self):
        self.url = "https://horoscope-astrology.p.rapidapi.com/sign"


    def get(self):
        querystring = {"s":"taurus"}

        headers = {
        "X-RapidAPI-Key": ,
        "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
        response = requests.get(self.url, headers=headers, params=querystring)
        print(response.json())
        
proxy = Proxy()
proxy.get()
 
    #astro_sign = User().zodiac_sign(month,day)
    #astro_sign = User(month,day)
    