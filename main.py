import pygame
from src.controller import Controller
from dotenv import load_dotenv
load_dotenv()

def main():
    pygame.init()
    #Create an instance on your controller object
    #Call your mainloop
    controller = Controller()
    controller.mainloop()
    
    ###### NOTHING ELSE SHOULD GO IN main(), JUST THE ABOVE 3 LINES OF CODE ######

# https://codefather.tech/blog/if-name-main-python/
if __name__ == '__main__':
    main()