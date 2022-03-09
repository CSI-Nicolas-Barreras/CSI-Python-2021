#imports the libary that we downloaded for games.
import pygame 
# initialize all imported pygame modules.
pygame.init()
# creates an instance of the pygame.
dis=pygame.display.set_mode((400,300))
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