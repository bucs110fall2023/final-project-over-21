
import requests

class Proxy:
    '''
    Proxy class makes API call for user's sign
    '''
    
    def __init__(self):
        self.url = "https://horoscope-astrology.p.rapidapi.com/sign"


    def get_sign_info(self,z):
        querystring = {"s":"z"}

        headers = {
        "X-RapidAPI-Key": "39d1c4f37bmshcdfe6dac9622395p1dc660jsn6a4727b5182a",
        "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
        response = requests.get(self.url, headers=headers, params=querystring)
        facts = response.json()['symbol']
        print("Your sign's symbol is " + str(facts) + ".")
        #print(response.json())
        return facts
        


    #astro_sign = User(month,day)
    