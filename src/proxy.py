from user import User
import requests

class Proxy():
    '''
    Proxy class makes API call for user's sign
    '''
    
    def __init__(self):
        pass
        # self.url = "https://horoscope-astrology.p.rapidapi.com/sign"


    # def get(self):
    #     querystring = {"s":"my_sign"}

    #     headers = {
    #     "X-RapidAPI-Key": 
    #     "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
    #      }

    #     response = requests.get(self.url, headers=headers, params=querystring)
    #     print(response.json())
        
    #     if response.get('results'):
    #         return response['results']
    #     else:
    #         return None
 

    #astro_sign = User().zodiac_sign(month,day)
    #astro_sign = User(month,day)
    url = "https://horoscope-astrology.p.rapidapi.com/sign"

    querystring = {"s":"my_sign"}

    headers = {
        "X-RapidAPI-Key": "39d1c4f37bmshcdfe6dac9622395p1dc660jsn6a4727b5182a",
        "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
    }

    response = requests.get(url, headers=headers, params=querystring)

    print(response.json())