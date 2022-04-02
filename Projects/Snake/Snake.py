#imports the libary that we downloaded for games.
import random
import pygame 
# initialize all imported pygame modules.
pygame.init()
#colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

dis_width = 800
dis_height  = 600
# creates an instance of the pygame.
dis=pygame.display.set_mode((800,600))
#colors
# blue=(0,0,255)
# red=(255,0,0)
# updates the entire Surface, only if no argument is passed. 
pygame.display.update()
# Snake Game By Nicolas Barreras
pygame.display.set_caption('Snake game by Edureka')
#created a variable game over that is a bolean that is false
game_over=False

# x1 = dis_width/2
# y1 = dis_height/2
 
snake_block=10

x1 = 300
y1 = 300
 
# x1_change = 0       
# y1_change = 0

clock = pygame.time.Clock()
snake_speed=30

font_style = pygame.font.SysFont(None, 50)
 
def message(msg,color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width/2, dis_height/2])

def gameLoop():  # creating a function
        game_over = False
        game_close = False
    
        x1 = dis_width / 2
        y1 = dis_height / 2
    
        x1_change = 0
        y1_change = 0
    
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_width - snake_block) / 10.0) 
    #loop run while the game is not over
        while not game_over:
            while game_close == True:
                dis.fill(white)
                message("You Lost! Press Q-Quit or C-Play Again", red)
                pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()
        #no c
            for event in pygame.event.get():
            #no c
                if event.type==pygame.QUIT:
                # variable game over that is a bolean that is true
                    game_over=True
                # snake game rules 
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

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(white)
        #prints out all the actions that take place on the screen
        pygame.draw.rect(dis, black, [x1, y1, 10, 10])
        pygame.draw.rect(dis, black, [x1, y1, snake_block, snake_block])
        # pygame.draw.rect(dis,blue,[200,150,10,10])
        #print(event)
        pygame.display.update() 

        clock.tick(30)

# message("You lost",red)
        pygame.display.update()
    # time.sleep(2)

        if x1 == foodx and y1 == foody:
            print("Yummy!!")
        clock.tick(snake_speed)
        # shut down pygame.
        pygame.quit()
        # it terminates the execution of the program completely.
        quit()

gameLoop()








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
