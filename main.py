import pygame
from src.controller import Controller

def main():
    pygame.init()
    controller = Controller()
    controller.mainloop()

if __name__ == '__main__':
    main()