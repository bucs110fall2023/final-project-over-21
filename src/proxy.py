import requests

class Proxy:
    '''
    Sends and receives the API request for info about zodiac sign's personality
    '''
    
    def __init__(self):
        '''
        The constructor (aka special method) that initializes the Proxy object with the API's link
        Args: None
        Return: None
        '''
        self.url = "https://horoscope-astrology.p.rapidapi.com/sign"
    
    
    def get_sign_info(self, users_sign=None):
        '''
        Sends a request to the API for the personlity of the specified zodiac sign
        Args: String users_sign is the zodiac sign that was calculated in the User class based on the month and day that the user input
        Return: String sign_personality is the info about the sign's personality that was requested from the API
        '''
        querystring = {"s": users_sign}

        headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
        response = requests.get(self.url, headers=headers, params=querystring)
        sign_personality = response.json()['nature']
        # print(f"The sign being sent to the API is {users_sign}.")
        # print(sign_personality)
        
        return sign_personality

       
# Testing the get_sign_info() method within proxy.py
# proxy = Proxy()
# proxy.get_sign_info("taurus")