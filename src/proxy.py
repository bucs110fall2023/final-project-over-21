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
        "X-RapidAPI-Key": "c5e6da7fa3mshe74d2afdf5f2e42p17c91ejsn75e152f9c5ed",
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