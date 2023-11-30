import pygame
from src.user import User
from src.proxy import Proxy

# For testing mainloop() method within controller.py
# from user import User
# from proxy import Proxy


class Controller:
    '''
    To control the program
    '''
    def __init__(self):
        pass
        screen = pygame.display.set_mode()
        screen.fill("pink")
        
        font = pygame.font.Font(None, 35)
        text = font.render("Enter your birthday month, day to display your Zodiac info: ", True, "black")
        screen.blit(text, (100, 100))
        pygame.display.flip()

    def get_birthday(self):
        month = (input("What's your birthday month (january, february, etc.): "))
        # testing the entry if it is name of a month
        month_list = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
        while month not in month_list :
                print("You were supposed to enter the name of one of the 12 months. Try again:")
                month = (input("What's your birthday month (january, february, etc.): "))
        day = int(input("What's your birthday day: "))
        
        # #day_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ,16, 17, 18, 19, 20, 21, 22, 23,24, 25, 26, 27, 28, 29, 30,31]
        # while day not in day_list:
        #     print ("Your input needs to be an intiger betwen 1 and 31.")
        #     day = int(input("What's your birthday day (number between and 31): "))
            
        print(month, day)
        return month, day
    
    def mainloop(self):
        print("checkpoint -2")
        controller = Controller()
        print("checkpoint -1")
        [month, day] = controller.get_birthday()
        print(month, day)
        print("checkpoint 0")
        user = User(month, day)
        print("checkpoint 1")
        user_zodiac = user.find_zodiac_sign() 
        print("checkpoint 2")
        print(user_zodiac)
        print("checkpoint 3")
        proxy = Proxy()
        sign_info = proxy.get_sign_info(user_zodiac)
        print(sign_info)
        return sign_info

# Testing the mainloop() method; when testing only controller.py need to remove src. from the imports
# controller = Controller()
# controller.mainloop()


# in a method in Controller class
# p = Proxy()
# horo = p.get_horo()