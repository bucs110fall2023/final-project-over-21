import pygame
import sys

class Data:
      
        # credit: YouTube tutorial: Python/Pygame tutorial: Getting text input by Clear Code
        # steps for creating text input:
        # 1 . create a text font, 2. render text with the font 3, display rendered text

        #set up
        pygame.init()
        clock = pygame.time.Clock()
        screen = pygame.display.set_mode()
        screen.fill("pink")
        font = pygame.font.Font(None, 35)
        text = font.render(
                        "Enter your birthday month in a first box and birthday day in second box:", True, "black"
                    )
        screen.blit(text, (100, 100))
        pygame.display.flip()
        pygame.time.wait(1000)
        base_font = pygame.font.Font(None,42)
        user_text = ""
        user_day = ""

        # Creating a rectangle for input
        input_rect = pygame.Rect(200, 200, 240,50)
        input_rect2 = pygame.Rect(200, 300,240,50)
        #color = pygame.Color("yellow")
        # creating variables that will be used for selecting and disselecting the rectangle
        color_active = pygame.Color("yellow")
        color_passive = pygame.Color("blue")
        color = color_passive

        active = False
    
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                
                # checking if user's mouse is inside the box/rectangle    
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                
                # getting input from the user, BACKSPACE IS NOT WORKING!    
                if event.type == pygame.KEYDOWN:
                    if active == True:
                        if event.key == pygame.K_BACKSPACE:
                            user_text = user_text[:-1]
                        else:
                            user_text += event.unicode
                            print(user_text)
                            
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if input_rect2.collidepoint(event.pos):
                        active = True
                    else:
                        active = False
                            
                if event.type == pygame.KEYDOWN:
                    if active == True:
                            #return user_text
                        if event.key == pygame.K_BACKSPACE:
                                user_day = user_day[:-1]
                        else:
                                user_day += event.unicode
                                print(user_day)
            if active:
                color = color_active
            else:
                color = color_passive
            
            pygame.draw.rect(screen,color,input_rect,2)
            pygame.draw.rect(screen,color,input_rect2,2)
            
            
            # rendering text on its own surface   
            text_surface = base_font.render(user_text,True,(255,255,255))
            screen.blit(text_surface,(input_rect.x + 5, input_rect.y + 5))
            day_surface = base_font.render(user_day,True,(255,255,255))
            screen.blit(day_surface,(input_rect2.x + 5, input_rect2.y + 5))
                
            pygame.display.flip()
            clock.tick(60)        
        