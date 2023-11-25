from src.user import User
#from proxy import Proxy
#from button import Button
import pygame

class Controller:
    '''
    To control the program
    '''
    def __init__(self):
        #screen = pygame.display.get_mode()
        pass
        

    def get_user(self):
        month = (input("What's your birthday month (january, february,.): "))
        day = int(input("What's your birthday day: "))
        #print(month,day)
        return month,day
    
    def mainloop(self):
        print("checkpoint -2")
        cont = Controller()
        print("checkpoint -1")
        [month,day] = cont.get_user()
        print(month,day)
        print("checkpoint 0")
        user = User(month, day)
        print("checkpoint 1")
        z = user.zodiac_sign() 
        print("checkpoint 2")
        print(z)
        print("checkpoint 3")

#Controller.mainloop()

# in a method in Controller class
# need to create User object before
# p = Proxy()
# horo = p.get_horo()
# a = user.zodiac_sign() 