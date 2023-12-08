class User:
    '''
    Determines the user's zodiac sign based on the user's birthday
    '''
    
    def __init__(self, month="March", day=14):
        '''
        The constructor (aka special method) that initializes the month and day of the User object
        Args: String month and int day are the month and day that was input by the user (presumably their birthday)
        Return: None
        '''
        self.day = day
        self.month = month
    
    
    def find_zodiac_sign(self):
        '''
        Takes the user's input for month and day and calculates their zodiac sign based 
        on the date ranges for each sign. This method is longer than 10 lines to check
        the date against all twelve zodiac signs.
        Args: None
        Return: String zodiac_sign is the user's zodiac sign based on the month and day they input
        ''' 
        day = self.day
        month = self.month
        
        if month == 'december':
            zodiac_sign = 'sagittarius' if (day < 22) else 'capricorn'
            
        elif month == 'january': 
            zodiac_sign = 'capricorn' if (day < 20) else 'aquarius'
            
        elif month == 'february': 
            zodiac_sign = 'aquarius' if (day < 19) else 'pisces'
            
        elif month == 'march': 
            zodiac_sign = 'pisces' if (day < 21) else 'aries'
            
        elif month == 'april': 
            zodiac_sign = 'aries' if (day < 20) else 'taurus'
            
        elif month == 'may': 
            zodiac_sign = 'taurus' if (day < 21) else 'gemini'
            
        elif month == 'june': 
            zodiac_sign = 'gemini' if (day < 21) else 'cancer'
            
        elif month == 'july': 
            zodiac_sign = 'cancer' if (day < 23) else 'leo'
            
        elif month == 'august': 
            zodiac_sign = 'leo' if (day < 23) else 'virgo'
            
        elif month == 'september': 
            zodiac_sign = 'virgo' if (day < 23) else 'libra'
            
        elif month == 'october': 
            zodiac_sign = 'libra' if (day < 23) else 'scorpio'
            
        elif month == 'november': 
            zodiac_sign = 'scorpio' if (day < 22) else 'sagittarius'
        
        print(f"The sign based on the input is {zodiac_sign}.")
        return zodiac_sign


# Testing the find_zodiac_sign() method within user.py
# user = User("january", 1)
# user.find_zodiac_sign()

# Western Astrology Star Sign Dates
# Aries (March 21-April 19)
# Taurus (April 20-May 20)
# Gemini (May 21-June 20)
# Cancer (June 21-July 22)
# Leo (July 23-August 22)
# Virgo (August 23-September 22)
# Libra (September 23-October 22)
# Scorpio (October 23-November 21)
# Sagittarius (November 22-December 21)
# Capricorn (December 22-January 19)
# Aquarius (January 20-February 18)
# Pisces (February 19-March 20)