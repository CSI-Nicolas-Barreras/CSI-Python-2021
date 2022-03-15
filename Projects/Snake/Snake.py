#imports the libary that we downloaded for games.
import pygame 
# initialize all imported pygame modules.
pygame.init()
# creates an instance of the pygame.
dis=pygame.display.set_mode((400,300))
#colors
blue=(0,0,255)
red=(255,0,0)
# updates the entire Surface, only if no argument is passed. 
pygame.display.update()
# Snake Game By Nicolas Barreras
pygame.display.set_caption('Snake game by Edureka')
#created a variable game over that is a bolean that is false
game_over=False
#loop run while the game is not over
while not game_over:
    #no c
    for event in pygame.event.get():
        #no c
        if event.type==pygame.QUIT:
             # variable game over that is a bolean that is true
             game_over=True
        #prints out all the actions that take place on the screen
        #print(event)   
# shut down pygame.
pygame.quit()
# it terminates the execution of the program completely.
quit()



import pygame
 
pygame.init()
 
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
 
dis = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Snake Game by Edureka')
 
game_over = False
 
x1 = 300
y1 = 300
 
x1_change = 0       
y1_change = 0
 
clock = pygame.time.Clock()
 
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
 
    x1 += x1_change
    y1 += y1_change
    dis.fill(white)
    pygame.draw.rect(dis, black, [x1, y1, 10, 10])
 
    pygame.display.update()
 
    clock.tick(30)
 
pygame.quit()
quit()
