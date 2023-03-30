import pygame
import time
import random

pygame.init()
display_width = 750
display_height = 600
gray = (119, 119, 119)
gamedisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Need For Sleep")
scale_factor = 1.2
car_width = 70
######################
carimg = pygame.transform.scale(pygame.image.load("Race/pics/blue1.png"), (int(car_width * scale_factor), int(car_width * scale_factor)))
######################
clock = pygame.time.Clock()

background_images = [ #road-track 
    pygame.image.load("Race/pics/road3.png"),
    pygame.image.load("Race/pics/road1.png"),
    pygame.image.load("Race/pics/road1.png"),    
    pygame.image.load("Race/pics/road2.png"),    
    pygame.image.load("Race/pics/road1.png"),    
    pygame.image.load("Race/pics/road2.png"),    
    pygame.image.load("Race/pics/road1.png"),    
    pygame.image.load("Race/pics/road2.png"),    
    pygame.image.load("Race/pics/road1.png"),
    pygame.image.load("Race/pics/road3.png"),

    ]
background_index = 0
background_height = background_images[0].get_height()
myfont = pygame.font.SysFont("None", 100)
render_text = myfont.render("CAR CRASHED", 20, (0, 0, 0))
level_text = myfont.render("Level-", 1, (0, 0, 0))
#############
background_speed = 2
#############

def score_system(passed, score):
    font = pygame.font.SysFont(None, 25)
    text = font.render("Passed = "+str(passed), True, (0, 0, 0))
    score = font.render("Score = "+str(score), True, (255, 0, 0))
    gamedisplay.blit(text, (2, 20))
    gamedisplay.blit(score, (2, 2))



def background():
    global background_y, background_index, background_speed
    background_y += background_speed
    if background_y >= background_height:
        background_y = 0
        background_index = (background_index + 1) % len(background_images)
        if background_index == len(background_images) - 1:
            background_speed = 0
    background_image = background_images[background_index]
    gamedisplay.blit(background_image, (0, background_y))
    next_background_index = (background_index + 1) % len(background_images)
    next_background_image = background_images[next_background_index]
    gamedisplay.blit(next_background_image, (0, background_y - background_height))



def car(x, y):
    gamedisplay.blit(carimg, (x, y))



def game_loop():
    global background_y,background_speed
    background_y = 200-display_height
    x = 340
    y = 320
    x_change = 0
    passed = 0
    level = 0
    score = 0
    bumped = False
    while not bumped:
        for event in pygame.event.get():
            gamedisplay.fill(gray)
            background()
            if event.type == pygame.QUIT:
                pygame.quit()
                bumped = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                if event.key == pygame.K_RIGHT:
                    x_change = 5
                if event.key == pygame.K_UP:
                    background_speed += 2
                if event.key == pygame.K_DOWN:
                    background_speed -= 1
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0
        x += x_change
        gamedisplay.fill(gray)
        background()
        car(x, y)
        score_system(passed, score)
        pygame.display.update()
        clock.tick(90)
        if x > 520-car_width or x < 290-car_width:
            gamedisplay.blit(render_text, (130, 200))
            pygame.display.update()
            time.sleep(3)
            game_loop()
        if passed > 0 and passed % 10 == 0:
            level += 1
            background_speed += 2

def main_menu():
    menu_font = pygame.font.SysFont(None, 25)
    menu_title = pygame.font.SysFont(None, 50)
    title = menu_title.render("Welcome to 'Need For Sleep' Game", True, (255, 152, 255))
    start = menu_font.render("Press SPACE to start", True, (255, 255, 255))
    quit = menu_font.render("Press Esc to quit", True, (255, 255, 255))
    title_rect = title.get_rect(center=(display_width/2, display_height/2 - 200))
    start_rect = start.get_rect(center=(display_width/2, display_height/2 + 1))
    quit_rect = quit.get_rect(center=(display_width/2, display_height/2 + 30))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    game_loop()
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    quit()

        gamedisplay.fill(gray)
        gamedisplay.blit(title, title_rect)
        gamedisplay.blit(start, start_rect)
        gamedisplay.blit(quit, quit_rect)
        pygame.display.update()
        clock.tick(90)
  
main_menu()
pygame.quit()
quit()
