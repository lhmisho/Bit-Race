import pygame

pygame.init()

display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('A bit racing')

black = (0, 0, 0)
white = (255,255,255)

clock = pygame.time.Clock()
crushed = False
carImg = pygame.image.load('racecar.png')

def car(x,y):
    gameDisplay.blit(carImg, (x,y))

x = (display_width * 0.45)
y = (display_height * 0.8)

while not crushed:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            crushed = True
    
    gameDisplay.fill(white)
    car(x,y)

    pygame.display.update()
    clock.tick(60)

pygame.quit()
quit()