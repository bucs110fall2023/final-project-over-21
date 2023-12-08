import pygame
import pygame_menu
import textwrap
# from src.user import User
# from src.proxy import Proxy

# For testing mainloop() method within controller.py
from user import User
from proxy import Proxy


class Controller:
    '''
    Displays the GUI, receives input from the user, creates a User object to calculate 
    the user's zodiac sign, creates a Proxy object to send a request to the API for the 
    user's horoscope based on their zodiac sign, displays the horoscope to the user
    '''
    
    def __init__(self):
        '''
        The constructor (aka special method) that initializes the Controller object which creates the display and sets the state
        Args: None
        Return: None
        '''
        # For testing mainloop() method within controller.py
        pygame.init()

        self.screen = pygame.display.set_mode()
        self.screen.fill("pink")

        self.state = "START"
        print(f"This is the init() method of the Controller class and the state should be 'START'. The actual state is {self.state}.")
    
    
    def mainloop(self):
        '''
        Runs the relevant method for each state
        Args: None
        Return: None
        '''
        print(f"This is the mainloop() method of the Controller class and the current state is {self.state}.")

        while True:
            if self.state == "START":
                self.startloop()
            elif self.state == "INPUT":
                self.inputloop()
            elif self.state == "OUTPUT":
                self.outputloop()
    
    
    def startloop(self):
        '''
        Displays the START state where the user can choose to play or quit the program
        Args: None
        Return: None
        '''
        print(f"This is the startloop() method of the Controller class and the current state is {self.state}.")
        
        self.menu = pygame_menu.Menu(
            "Read Your Horoscope",
            width=500, 
            height=300, 
            theme=pygame_menu.themes.THEME_SOLARIZED,
            onclose=pygame_menu.events.EXIT
        )

        self.menu.add.button("Play", self.set_state, "INPUT")
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

        while self.state == "START":
            if self.menu.is_enabled():
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
            pygame.display.flip()
        
    
    def set_state(self, state="START"):
        '''
        Changes the state when a button in pygame-menu is clicked
        Args: String state is the state that will be set when the button is clicked
        Return: None
        '''
        self.state = state
    
    
    def send_input(self):
        '''
        Creates a User object based on the input, runs the method to determine the user's 
        zodiac sign, creates a Proxy object, sends a request to the API for the daily horoscope
        Args: None
        Return: None
        '''
        month = self.month.get_value()
        day = int(self.day.get_value())
        user = User(month, day)
        self.users_sign = user.find_zodiac_sign() 
        proxy = Proxy()
        self.daily_horoscope = proxy.get_daily_horoscope(self.users_sign)
        self.state = "OUTPUT"
    
    
    def inputloop(self):
        '''
        Displays the pygame-menu where the user can input their birthday
        Args: None
        Return: None
        '''
        print(f"This is the inputloop() method of the Controller class and the current state is {self.state}.")
        
        self.screen.fill("pink")
        
        self.menu = pygame_menu.Menu(
            "Enter your birthday", 
            width=500, 
            height=300, 
            theme=pygame_menu.themes.THEME_SOLARIZED,
            onclose=pygame_menu.events.EXIT
        )
        
        self.month = self.menu.add.text_input("Month: ", default="")
        self.day = self.menu.add.text_input("Day: ", default="")
        self.menu.add.button("Submit", self.send_input)
        self.menu.add.button("Quit", pygame_menu.events.EXIT)
        
        while self.state == "INPUT":
            if self.menu.is_enabled():
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
            pygame.display.flip()
    
    
    def display_horoscope(self):
        '''
        Takes the response from the API, cuts the string into a list of strings 
        to wrap the text, renders the text to the user with blit
        Args: None
        Return: None
        '''
        font = pygame.font.Font(None, 30)
        horoscope_wrap = textwrap.wrap(self.daily_horoscope, width=70)
        # print(horoscope_wrap, type(horoscope_wrap))
             
        line_y = 200
        for line in range(len(horoscope_wrap)):
            horoscope = font.render(horoscope_wrap[line], True, "black")
            self.screen.blit(horoscope, (400, line_y))
            line_y = line_y + 30   
        pygame.display.flip()
      
    
    def outputloop(self):
        '''
        Displays the daily horoscope that was sent through the API request
        Args: None
        Return: None
        '''
        print(f"This is the outputloop() method of the Controller class and the current state is {self.state}.")
        
        self.screen.fill("pink")
        self.display_horoscope()
        
        self.menu = pygame_menu.Menu(
            "", 
            width=400, 
            height=300, 
            theme=pygame_menu.themes.THEME_SOLARIZED,
            onclose=pygame_menu.events.EXIT
        )
        self.menu.add.button("Play Again", self.set_state, "INPUT")
        self.menu.add.button("Quit", pygame_menu.events.EXIT)

        while self.state == "OUTPUT":
            if self.menu.is_enabled():
                self.menu.update(pygame.event.get())
                self.menu.draw(self.screen)
            pygame.display.flip()

# For testing mainloop() method within controller.py; when testing only controller.py need to remove src. from the imports
controller = Controller()
controller.mainloop()