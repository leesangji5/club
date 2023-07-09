import pygame
import random
import time

pygame.init()

screenWidth = 800
screenHeight = 600

screen = pygame.display.set_mode((screenWidth, screenHeight))
pygame.display.set_caption("game")
font = pygame.font.Font('freesansbold.ttf', 32)

def reactionSpeedTest():
    backgroundColour = (0, 0, 0)
    ballColour = (255, 255, 255)
    pointColour = (255, 255, 255)
    initailRadius = 10
    maxRadius = 30
    deltaR = 0.01
    maxBalls = 10
    timeInterval = 0.5
    point = 0
    pointx = 15
    pointy = 20
    deltaPoint = 1

    ballx = []
    bally = []
    ballr = []
    ballvisible = []

    st = time.time()

    run = True
    while run:
        pygame.time.delay(1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                mousex, mousey = pygame.mouse.get_pos()
                for i in range(len(ballx)):
                    if ballvisible[i] and (ballx[i]-ballr[i] < mousex) and (ballx[i]+ballr[i] > mousex) and (bally[i]-ballr[i] < mousey) and (bally[i]+ballr[i] > mousey):
                        ballvisible[i] = False
                        point += deltaPoint

        if time.time() - st > timeInterval and len(ballx) < maxBalls:
            ballx.append(random.randint(initailRadius, screenWidth - initailRadius))
            bally.append(random.randint(initailRadius, screenHeight - initailRadius))
            ballr.append(initailRadius)
            ballvisible.append(True)
            st = time.time()

        screen.fill(backgroundColour)
        for i in range(len(ballx)):
            ballr[i] += deltaR
            if ballr[i] > maxRadius:
                ballx[i] = random.randint(maxRadius, screenHeight - maxRadius)
                bally[i] = random.randint(maxRadius, screenHeight - maxRadius)
                ballr[i] = initailRadius
                ballvisible[i] = True
            if ballvisible[i]:
                pygame.draw.circle(screen, ballColour, (ballx[i], bally[i]), int(ballr[i]))
        
        text = font.render(str(point), True, pointColour, backgroundColour)
        textRect = text.get_rect()
        textRect.center = (pointx, pointy)
        screen.blit(text, textRect)

        pygame.display.update()

    pygame.quit()

def main():
    run = True
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
        
        text = font.render("reactionSpeedTest", True, (255, 255, 255), (100, 100, 100))
        textRect = text.get_rect()
        textRect.center = (screenWidth/2, screenHeight/2)
        screen.blit(text, textRect)

        pygame.display.update()

    pygame.quit()


reactionSpeedTest()
