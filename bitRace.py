import pygame
import time

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit racing')

red = (255,0,0)
black = (0, 0, 0)
white = (255,255,255)

car_width = 73

clock = pygame.time.Clock()
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

def text_object(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf', 115)
    textSurf, textRect = text_object(text, largeText)
    textRect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textSurf, textRect)
    pygame.display.update()

    time.sleep(2)
    game_loop()


def crash():
    message_display("You Crashed!")

def game_loop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0
    y_change = 0
    car_speed = 0
    game_exit = False

    while not game_exit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        # determining key press
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
                elif event.key == pygame.K_UP:
                    y_change = -5
                elif event.key == pygame.K_DOWN:
                    y_change = 5

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
                if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    y_change = 0
        x += x_change
        y += y_change

        gameDisplay.fill(white)
        car(x,y)

        if x < 0:
            # x_change = 1
            crash()
        if x > display_width - car_width:
            x_change = -1
        if y < 0:
            y_change = 1
        if y > display_height - car_width:
            y_change = -1

        pygame.display.update()
        clock.tick(100)


game_loop()
pygame.quit()
quit()