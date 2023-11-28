class User:
    '''
    The class is to collect user's information
    and to determine Zodiac sign based on
    the user's input 
    '''
    
    #def __init__(self):
        
    # self.month = (input("What's your birthday month (january, february,.): "))
    # self.day = int(input("What's your birthday day: "))
      
    def __init__(self, month, day):
        self.day = day
        self.month = month
    
    
    def find_zodiac_sign(self):
        '''
        Takes the user's birthday to determine their zodiac sign
        '''
        
        day = self.day
        month = self.month
        
        # I will put credit in README later
        # credit https://www.geeksforgeeks.org/program-display-astrological-sign-zodiac-sign-given-date-birth/
        # astro_sign = "foo"
        #print(month)
        
        if month == 'december':
            astro_sign = 'sagittarius' if (day < 22) else 'capricorn'
            
        elif month == 'january': 
            astro_sign = 'capricorn' if (day < 20) else 'aquarius'
            
        elif month == 'february': 
            astro_sign = 'aquarius' if (day < 19) else 'pisces'
            
        elif month == 'march': 
            astro_sign = 'pisces' if (day < 21) else 'aries'
            
        elif month == 'april': 
            astro_sign = 'aries' if (day < 20) else 'taurus'
            
        elif month == 'may': 
            astro_sign = 'taurus' if (day < 21) else 'gemini'
            
        elif month == 'june': 
            astro_sign = 'gemini' if (day < 21) else 'cancer'
            
        elif month == 'july': 
            astro_sign = 'cancer' if (day < 23) else 'leo'
            
        elif month == 'august': 
            astro_sign = 'leo' if (day < 23) else 'virgo'
            
        elif month == 'september': 
            astro_sign = 'virgo' if (day < 23) else 'libra'
            
        elif month == 'october': 
            astro_sign = 'libra' if (day < 23) else 'scorpio'
            
        elif month == 'november': 
            astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
         
        print("Your zodiac sign is " + astro_sign)
        return astro_sign
    
#user = User()      
# Driver code  
#if __name__ == '__main__': 
    # day = 19
    # month = "may"
#    user.find_zodiac_sign()



# Testing the find_zodiac_sign() method
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