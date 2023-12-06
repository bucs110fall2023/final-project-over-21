import pygame
import pygame_menu
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
        # For testing mainloop() method within controller.py
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.screen.fill("pink")

        self.state = "START"
        print("Is this even running?!")
        print(self.state)
        
        # Previous code
        # font = pygame.font.Font(None, 35)
        # text = font.render("Enter your birthday month, day to display your Zodiac info: ", True, "black")
        # self.screen.blit(text, (100, 100))

        # start_menu = pygame_menu.Menu("Read your horoscope for today", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
        # start_menu.add.text_input("Birth Month: ", default="January")
        # start_menu.add.button("Quit", pygame_menu.events.EXIT)
        # start_menu.mainloop(self.screen)

        # pygame.display.flip()


    # def get_birthday(self):
    #     month = (input("What's your birthday month (january, february, etc.): "))
    #     # testing the entry if it is name of a month
    #     month_list = ["january", "february", "march", "april", "may", "june","july", "august", "september", "october", "november", "december"]
    #     while month not in month_list:
    #             print("You were supposed to enter the name of one of the 12 months. Try again:")
    #             month = (input("What's your birthday month (january, february, etc.): "))
    #     day = int(input("What's your birthday day: "))
        
    #     # #day_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, ,16, 17, 18, 19, 20, 21, 22, 23,24, 25, 26, 27, 28, 29, 30,31]
    #     # while day not in day_list:
    #     #     print ("Your input needs to be an intiger betwen 1 and 31.")
    #     #     day = int(input("What's your birthday day (number between and 31): "))
            
    #     print(month, day)
    #     return month, day
    

    def mainloop(self):
        
        print("This is mainloop")
        print(self.state)
        counter = 0
        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "INPUT":
                self.inputloop()
            elif self.state == "OUTPUT":
                self.outputloop()
                counter +=1
                if counter == 3:
                    break
                #self.endloop()

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
    
    # def endloop(self):
    #     self.menu = pygame_menu.Menu("End", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
    #     self.menu.add.button("Quit", pygame_menu.events.EXIT)
            
    #     while self.state == "OUTPUT":

    #         if self.menu.is_enabled():
    #             self.menu.update(pygame.event.get())
    #             self.menu.draw(self.screen)
        
    #         pygame.display.flip()
        
    def startloop(self):
        
        print("This is the beginning of the startloop")
        print(self.state)
        print("what is it doing now?")
        self.menu = pygame_menu.Menu(
            "Know Your Weaknesses",
            width=500, 
            height=300, 
            theme=pygame_menu.themes.THEME_SOLARIZED, 
            onclose=pygame_menu.events.EXIT
        )
        # self.test_menu = pygame_menu.Menu(
        #     "TEST MENU",
        #     width=400, 
        #     height=300, 
        #     theme=pygame_menu.themes.THEME_BLUE, 
        #     onclose=pygame_menu.events.EXIT
        # )
        # The method set_state() keeps running without the button being pressed and subsequently runs the inputloop() infinitely
        # Have to write functions that don't take parameters for pygame-menu
        # Callbacks - Usually the function you are calling followed by the parameters that will be passed
        self.menu.add.button("Play", self.set_state, "INPUT")
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

        while self.state == "START":

            if self.menu.is_enabled():
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
        
            pygame.display.flip()
        
    
    # Created this function because Button in pygame-menu needs a Menu, a MenuAction (event), a function (callable), or None
    def set_state(self, state = "START"):
        self.state = state
        return None
    
    def send_input(self):
        # Previous code
        # print("checkpoint -2")
        # controller = Controller()
        # print("checkpoint -1")
        # [month, day] = self.get_birthday()
        # Callback - Passing a function as a parameter
        month = self.month.get_value()
        day = int(self.day.get_value())
        user = User(month, day)
        user_zodiac = user.find_zodiac_sign() 
        proxy = Proxy()
        self.sign_info = proxy.get_sign_info(user_zodiac)
        print(self.sign_info)
        #return sign_info
        print("This is the send_input() method")
        self.state = "OUTPUT"
        print(self.state)
        
        # REMOVE API KEY BEFORE PUSHING

    
    def inputloop(self):
        self.screen.fill("pink")
        
        self.menu = pygame_menu.Menu("Enter your birthday", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
        self.month = self.menu.add.text_input("Month: ", default="")
        self.day = self.menu.add.text_input("Day: ", default="")
        
        self.menu.add.button("Submit", self.send_input) # Send info to user to find zodiac
        self.menu.add.button("Quit", pygame_menu.events.EXIT)
        
        print("Inputloop is working!!")
        
        
        while self.state == "INPUT":

            if self.menu.is_enabled():
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)

                # This line is in an infinite loop until the user clicks Submit!!
                print("Menu in eventloop is enabled!!!")
            
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

            # return self.month, self.day

    # we need to create a variable at the object level
    
    def outputloop(self):
        self.screen.fill("pink")
        print("starting running outpoot loop")
        font = pygame.font.Font(None, 30)
        text_info = "Your weakensses are " + self.sign_info + "."
        #text = font.render(self.sign_info, True, "black")
        text = font.render(text_info, True, "black")
        self.screen.blit(text, (400, 100 ))
    
        pygame.display.flip()
        #pygame.time.wait(500)
        
        self.menu = pygame_menu.Menu("", width=400, height=300, theme=pygame_menu.themes.THEME_SOLARIZED)
        # FORTUNE = self.sign_info
        # self.menu.add.label(FORTUNE, max_char = 0, selectable=False)
        self.menu.add.button("Play Again", self.set_state, "INPUT")
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

        # print("This is the outputloop")
        
        while self.state == "OUTPUT":
            if self.menu.is_enabled():
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
                #print("You will see output!")
                print("You should be now seeing output on screen")
                print("waiting for the mouse event")
            
            pygame.display.flip()

# For testing mainloop() method within controller.py; when testing only controller.py need to remove src. from the imports
# controller = Controller()
# controller.mainloop()