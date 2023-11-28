import requests

class Proxy:
    '''
    Proxy class makes API call for user's sign
    '''
    
    def __init__(self):
        self.url = "https://horoscope-astrology.p.rapidapi.com/sign"
        

    def get_sign_info(self, users_sign):
        #self.z = z
        querystring = {"s": users_sign}

        headers = {
        "X-RapidAPI-Key": "4c0a3b9861mshb444707240507efp14c2e1jsnc99b8d23906a",
        "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
        response = requests.get(self.url, headers=headers, params=querystring)
        # facts = response.json()['symbol']
        # print("Your sign's symbol is " + str(facts) + ".")
        print(response.json())
        # return facts
        
# Testing API requests with the get_sign_info() method
# proxy = Proxy()
# proxy.get_sign_info("cancer")