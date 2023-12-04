import pygame
import pygame_menu
# from src.user import User
# from src.proxy import Proxy

# For testing mainloop() method within controller.py
from user import User
from proxy import Proxy


class Controller:
    '''
    To control the program
    '''
    def __init__(self, state = "START"):
        # For testing mainloop() method within controller.py
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.screen.fill("pink")

        self.state = state
        
        # Previous code
        # font = pygame.font.Font(None, 35)
        # text = font.render("Enter your birthday month, day to display your Zodiac info: ", True, "black")
        # self.screen.blit(text, (100, 100))

        # start_menu = pygame_menu.Menu("Read your horoscope for today", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
        # start_menu.add.text_input("Birth Month: ", default="January")
        # start_menu.add.button("Quit", pygame_menu.events.EXIT)
        # start_menu.mainloop(self.screen)

        # pygame.display.flip()


    def get_birthday(self):
        month = (input("What's your birthday month (january, february, etc.): "))
        # testing the entry if it is name of a month
        month_list = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
        while month not in month_list:
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

        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "INPUT":
                self.inputloop()
            elif self.state == "OUTPUT":
                self.outputloop()
        
        # Previous code
        # print("checkpoint -2")
        # controller = Controller()
        # print("checkpoint -1")
        # [month, day] = self.get_birthday()
        # print(month, day)
        # print("checkpoint 0")
        # user = User(month, day)
        # print("checkpoint 1")
        # user_zodiac = user.find_zodiac_sign() 
        # print("checkpoint 2")
        # print(user_zodiac)
        # print("checkpoint 3")
        # proxy = Proxy()
        # sign_info = proxy.get_sign_info(user_zodiac)
        # print(sign_info)

        # return sign_info
    
    def startloop(self):
        
        self.menu = pygame_menu.Menu("Read your horoscope for today", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
        # self.menu.add.button("Play", self.set_state("INPUT"))
        self.menu.add.button("Quit", pygame_menu.events.EXIT)
        
        # Do we still need an event loop if we are using pygame-menu? Because it is already listening for a click
        # while self.state == "START":
        #     for event in pygame.event.get():
        #         if event.type == pygame.MOUSEBUTTONDOWN:
        #             self.state == "INPUT"

        self.menu.update(pygame.event.get())
        
        self.menu.draw(self.screen)
        
        pygame.display.flip()
        
    
    # Created this function because Button in pygame-menu needs a Menu, a MenuAction (event), a function (callable), or None
    def set_state(self, state = "START"):
        self.state = state
        return None

    
    def inputloop(self):
        print("Input loop")

        self.menu = pygame_menu.Menu("Enter your birthday", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.month = self.menu.add.text_input("Birthday Month (e.g. January, February, etc.): ", default="January")
        self.day = self.menu.add.text_input("Birthday Day (e.g. 1, 2, etc.): ", default=1)
        self.menu.add.button("Return to Start Menu", self.set_state("START"))

        self.menu.update(pygame.event.get())
        
        self.menu.draw(self.screen)
        
        pygame.display.flip()

        # month = (input("What's your birthday month (january, february, etc.): "))
        # # testing the entry if it is name of a month
        # month_list = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
        # while month not in month_list:
        #         print("You were supposed to enter the name of one of the 12 months. Try again:")
        #         month = (input("What's your birthday month (january, february, etc.): "))
        # day = int(input("What's your birthday day: "))
        
        # #day_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ,16, 17, 18, 19, 20, 21, 22, 23,24, 25, 26, 27, 28, 29, 30,31]
        # while day not in day_list:
        #     print ("Your input needs to be an intiger betwen 1 and 31.")
        #     day = int(input("What's your birthday day (number between and 31): "))

        return self.month, self.day

    def outputloop(self):
        pass
        

# For testing mainloop() method within controller.py; when testing only controller.py need to remove src. from the imports
controller = Controller("START")
controller.mainloop()