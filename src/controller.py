import pygame
from src.user import User
from src.proxy import Proxy
import sys

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
        
        # credit: YouTube tutorial: Python/Pygame tutorial: Getting text input by Clear Code
        # steps for creating text input:
        # 1 . create a text font, 2. render text with the font 3, display rendered text

        #set up
        #pygame.init()
        # clock = pygame.time.Clock()
        # screen = pygame.display.set_mode()
        # screen.fill("pink")
        # base_font = pygame.font.Font(None,42)
        # user_text = ""

        # # Creating a rectangle for input
        # input_rect = pygame.Rect(200, 200, 240,50)
        # #color = pygame.Color("yellow")
        # # creating variables that will be used for selecting and disselecting the rectangle
        # color_active = pygame.Color("yellow")
        # color_passive = pygame.Color("blue")
        # color = color_passive

        # active = False
    
        # while True:
        #     for event in pygame.event.get():
        #         if event.type == pygame.QUIT:
        #             pygame.quit()
        #             sys.exit()
                
        #         # checking if user's mouse is inside the box/rectangle    
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             if input_rect.collidepoint(event.pos):
        #                 active = True
        #             else:
        #                 active = False
                
        #         # getting input from the user, BACKSPACE IS NOT WORKING!    
        #         if event.type == pygame.KEYDOWN:
        #             if active == True:
        #                 if event.key == pygame.K_BACKSPACE:
        #                     user_text = user_text[:-1]
        #                 else:
        #                     user_text += event.unicode
        #                     print(user_text)
        #                     return user_text
        #     if active:
        #         color = color_active
        #     else:
        #         color = color_passive
            
        #     pygame.draw.rect(screen,color,input_rect,2)
            
        #     # rendering text on its own surface   
        #     text_surface = base_font.render(user_text,True,(255,255,255))
        #     screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
                
        #     pygame.display.flip()
        #     clock.tick(60)        
        
    def get_birthday(self):
        month = (input("What's your birthday month (january, february, etc.): "))
        # testing the entry if it is name of a month
        month_list = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
        while month not in month_list :
                print("You were supposed to enter the name of one of the 12 months. Try again:")
                month = (input("What's your birthday month (january, february, etc.): "))
        day = int(input("What's your birthday day: "))
        
        while day not in range(0,32):
             print ("Your input needs to be an intiger betwen 1 and 31.")
             day = int(input("What's your birthday day (number between and 31): "))
            
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