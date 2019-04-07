import pygame, time, random

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
green = (0,155,0)
display_width = 800
display_height = 600

gameDisplay = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snaky Snake')

img = pygame.image.load('snakehead.png')
apple = pygame.image.load('apple.png')


clock = pygame.time.Clock()

block_size = 20
FPS = 20
direct = "right"
font = pygame.font.SysFont(None, 25)
def snake(snakelist, block_size):
    if direct == "right":
        head = pygame.transform.rotate(img, 270)
    if direct == "left":
        head = pygame.transform.rotate(img, 90)
    if direct == "up":
        head = img
    if direct == "down":
        head = pygame.transform.rotate(img, 180)
    gameDisplay.blit(head, (snakelist[-1][0], snakelist[-1][1]))
    for XnY in snakelist[:-1]:
        pygame.draw.rect(gameDisplay, green, [XnY[0], XnY[1], block_size, block_size])

def text_objects(text, color):
    textSurface = font.render(text, True, color)
    return textSurface, textSurface.get_rect()

def message_to_screen(msg, color):
    textSurf, textRect = text_objects(msg,color)
    #screen_text = font.render(msg, True, color)
    #gameDisplay.blit(screen_text, [display_width/2, display_height/2])
    textRect.center = (display_width /2), (display_height / 2)
    gameDisplay.blit(textSurf, textRect)

def gameLoop():
    global direct
    gameExit = False
    gameOver = False
    lead_x = display_width/2
    lead_y = display_height/2
    lead_x_change = 10
    lead_y_change = 0
    snakelist = []
    snakelength = 1
    randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0

    while not gameExit: # while gameExit is False
        while gameOver ==True:
            gameDisplay.fill(white)
            message_to_screen("Game over, Press C to play again or Q to quit", red)
            pygame.display.update()
            for event in pygame.event.get():

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        gameExit = True
                        gameOver = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                gameExit = True
                gameOver = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    lead_x_change = -block_size
                    lead_y_change = 0
                    direct = "left"
                elif event.key == pygame.K_RIGHT:
                    lead_x_change = block_size
                    lead_y_change = 0
                    direct = "right"
                elif event.key == pygame.K_UP:
                    lead_y_change = -block_size
                    lead_x_change = 0
                    direct = "up"
                elif event.key == pygame.K_DOWN:
                    lead_y_change = block_size
                    lead_x_change = 0
                    direct = "down"
        if lead_x >= display_width or lead_x<0 or lead_y >= display_height or lead_y<0:
            gameOver = True

    #        if event.type == pygame.KEYUP:
    #            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
    #                lead_x_change = 0
        lead_x += lead_x_change
        lead_y += lead_y_change

        gameDisplay.fill(white)
        applethickness = 20
        #pygame.draw.rect(gameDisplay, red, [randAppleX, randAppleY, applethickness, applethickness])
        gameDisplay.blit(apple, [randAppleX, randAppleY, applethickness, applethickness])
        snakehead = []
        snakehead.append(lead_x)
        snakehead.append(lead_y)
        snakelist.append(snakehead)
        if len(snakelist) > snakelength:
            del snakelist[0]
        for eachSegment in snakelist[:-1]:
            if eachSegment == snakehead:
                gameOver = True

        snake(snakelist, block_size)
        pygame.display.update()
        clock.tick(FPS)
        #if lead_x == randAppleX and lead_y == randAppleY:
        #    randAppleX = round(random.randrange(0,display_width-block_size))#/10.0)*10.0
        #    randAppleY = round(random.randrange(0,display_height-block_size))#/10.0)*10.0
        #    snakelength +=1

        #if lead_x >= randAppleX and lead_x <= randAppleX + applethickness:
        #    if lead_y >= randAppleY and lead_y <= randAppleY + applethickness:
        #        randAppleX = round(random.randrange(0, display_width-block_size))
        #        randAppleY = round(random.randrange(0, display_height-block_size))
        #        snakelength += 1
        if lead_x > randAppleX and lead_x < randAppleX + applethickness or lead_x + block_size > randAppleX and lead_x + block_size < randAppleX + applethickness:

            if lead_y > randAppleY and lead_y < randAppleY + applethickness:
                randAppleX = round(random.randrange(0, display_width-block_size))
                randAppleY = round(random.randrange(0, display_height-block_size))
                snakelength+=1
            elif lead_y + block_size > randAppleY and lead_y + block_size < randAppleY + applethickness:
                randAppleX = round(random.randrange(0, display_width-block_size))
                randAppleY = round(random.randrange(0, display_height-block_size))
                snakelength+=1


    pygame.quit()
    quit()

gameLoop()