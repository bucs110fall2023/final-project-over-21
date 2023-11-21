class Proxy():
    '''
    This class is to determine Zodiac sign based on
    the user's input and to make the API call to 
    get the horoscope for user
    '''
    
    # Takes user's input to see what 
    # Zodiac sign the person is:
    
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

   
    month = (input("What's your birthday month (january, february,.): "))
    day = int(input("What's your birthday day: "))


    def zodiac_sign(day, month): 
      
    # checks month and date within the valid range 
    # of a specified zodiac 
    # credit https://www.geeksforgeeks.org/program-display-astrological-sign-zodiac-sign-given-date-birth/
        if month == 'december': 
            astro_sign = 'Sagittarius' if (day < 22) else 'capricorn'
            
        elif month == 'january': 
            astro_sign = 'Capricorn' if (day < 20) else 'aquarius'
            
        elif month == 'february': 
            astro_sign = 'Aquarius' if (day < 19) else 'pisces'
            
        elif month == 'march': 
            astro_sign = 'Pisces' if (day < 21) else 'aries'
            
        elif month == 'april': 
            astro_sign = 'Aries' if (day < 20) else 'taurus'
            
        elif month == 'may': 
            astro_sign = 'Taurus' if (day < 21) else 'gemini'
            
        elif month == 'june': 
            astro_sign = 'Gemini' if (day < 21) else 'cancer'
            
        elif month == 'july': 
            astro_sign = 'Cancer' if (day < 23) else 'leo'
            
        elif month == 'august': 
            astro_sign = 'Leo' if (day < 23) else 'virgo'
            
        elif month == 'september': 
            astro_sign = 'Virgo' if (day < 23) else 'libra'
            
        elif month == 'october': 
            astro_sign = 'Libra' if (day < 23) else 'scorpio'
            
        elif month == 'november': 
            astro_sign = 'scorpio' if (day < 22) else 'sagittarius'
         
        print("Your Zodiac sign is: " + astro_sign) 
        return astro_sign
      
# Driver code  
    if __name__ == '__main__': 
        # day = 19
        # month = "may"
        zodiac_sign(day, month) 