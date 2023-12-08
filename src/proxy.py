import requests

class Proxy:
    '''
    Sends and receives the API request for the daily horoscope
    '''
    
    def __init__(self):
        '''
        The constructor (aka special method) that initializes the Proxy object with the API's link
        Args: None
        Return: None
        '''
        self.url = "https://horoscope-astrology.p.rapidapi.com/horoscope"
        

    def get_daily_horoscope(self, users_sign=None):
        '''
        Sends a request to the API for the user's daily horoscope
        Args: String users_sign is the zodiac sign that was calculated in the User class based on the month and day that the user input
        Return: String daily_horoscope is the user's horoscope for the current day that was requested from the API
        '''
        querystring = {"day":"today","sunsign": users_sign}

        headers = {
        "X-RapidAPI-Key": "",
        "X-RapidAPI-Host": "horoscope-astrology.p.rapidapi.com"
        }
        response = requests.get(self.url, headers=headers, params=querystring)
        daily_horoscope = response.json()
        print(f"The sign being sent to the API is {users_sign}.")
        print(daily_horoscope)
        
        return daily_horoscope
        
# Testing the get_daily_horoscope() method within proxy.py
proxy = Proxy()
proxy.get_daily_horoscope("taurus")