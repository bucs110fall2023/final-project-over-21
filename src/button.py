import pygame

class Button(pygame.sprite.Sprite):
    '''
    Button class to create a Submit button and a Play Again button
    '''
    def __init__(self, x=0, y=0, width=150, height=150, color="red", text="Submit"):
        super().__init__()
        self.image = pygame.Surface(width, height)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.color = color
        self.image.fill(self.color)

        self.text = pygame.font.SysFont(None, 36).render(text, True, "black")

        self.image.blit(self.message, (20, 20))


    def button_hover(self, color):
        self.color = color
        self.image.fill(self.color)


    def button_click(self):
        pass