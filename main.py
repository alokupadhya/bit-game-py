import pygame
import time
import random

pygame.init()

display_width = 700
display_height = 700
game_display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Pikachu(Bit Game)")
clock = pygame.time.Clock()
char_image = pygame.image.load("pikachu.PNG")
bg_image = pygame.image.load("bg.jpeg")
dpoke_image = pygame.image.load("devil.PNG")
fireball = pygame.image.load("fb.png")
char_width = 65


def display_text(text, size, x, y, color, type):
    largetext = pygame.font.Font("freesansbold.ttf", size)
    textsurf, textArea = text_object(text, largetext, color)
    textArea.center = (x, y)
    game_display.blit(textsurf, textArea)
    pygame.display.update()
    if type is "GOOUT":
        time.sleep(4)
        game_loop()


def text_object(text, font, color):
    textsurface = font.render(text, True, color)
    return textsurface, textsurface.get_rect()


def set_char(x, y):
    game_display.blit(char_image, (x, y))


def game_loop():
    char_x = int(display_width * 0.45)
    char_y = int(display_height * 0.7)
    enemypos_x = random.randrange(0, display_width - 75)
    enemypos_y = 1
    fireball_x = enemypos_x + 10
    fireball_y = 50
    scorecount = 0
    level = 1
    level_inc = 5
    lcount = 2
    agility = 5
    fbspeed = 5
    x_change = 0
    game_crash = False
    flag = 0
    text_at = ""
    p_pow = 100
    attack = 0
    while game_crash is False:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_a:
                    x_change = -agility
                if event.key == pygame.K_d:
                    x_change = agility
                if event.key == pygame.K_RSHIFT:
                    attack += 1

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_a or event.key == pygame.K_d:
                    x_change = 0

        char_x += x_change
        if attack > 10 and fireball_x <= char_x + 20 <= fireball_x + 40:
            p_pow = p_pow + 5
            enemypos_x = random.randrange(0, display_width - 75)
            fireball_x = enemypos_x + 10
            fireball_y = 50
            attack = 0

        if char_x <= 0 or char_x >= (display_width - char_width):
            display_text("Pickachu don't go out", 50, (display_width / 2), (display_height / 2), (0, 0, 0), "GOOUT")
        # background color
        game_display.blit(bg_image, (0, 0))
        game_display.blit(dpoke_image, (enemypos_x, enemypos_y))
        game_display.blit(fireball, (fireball_x, fireball_y))
        fireball_y += fbspeed
        text_scr = "Score: " + str(scorecount)
        text_lvl = "Level: " + str(level)
        display_text(text_scr, 20, (display_width * 0.2), (display_height * 0.87), (255, 0, 0), "NULL")
        display_text(text_lvl, 20, (display_width * 0.7), (display_height * 0.87), (255, 0, 0), "NULL")
        if fireball_y >= display_height * 0.7:
            scorecount += 1
            enemypos_x = random.randrange(0, display_width - 75)
            fireball_x = enemypos_x + 10
            fireball_y = 50
            attack = 0
        if scorecount > level_inc * lcount and level < 20:
            lcount += 2
            level += 1
            fbspeed += 1
        if level >= 10 and flag == 0:
            flag = 1
            agility += 15
            text_at = "Pickachu learn agility"
        if level >= 15 and flag == 1:
            flag = 0
            agility -= 15
            text_at = "Pickachu forgot agility"
        display_text(text_at, 20, (display_width * 0.46), (display_height * 0.95), (255, 0, 0), "NULL")
        # set_char pos (user def)
        set_char(char_x, char_y)
        if fireball_y + 40 >= char_y:
            if (fireball_x <= char_x + 50 <= fireball_x + 40) or (fireball_x <= char_x - 10 <= fireball_x + 40):
                p_pow = p_pow - 10
                enemypos_x = random.randrange(0, display_width - 75)
                fireball_x = enemypos_x + 10
                fireball_y = 50
            elif fireball_x <= char_x + 20 <= fireball_x + 40:
                p_pow = p_pow - 20
                enemypos_x = random.randrange(0, display_width - 75)
                fireball_x = enemypos_x + 10
                fireball_y = 50
        text_pow = "Energy level: " + str(p_pow) + "%"
        display_text(text_pow, 20, (display_width * 0.46), (display_height * 0.87), (255, 0, 0), "NULL")
        if p_pow <= 0:
            display_text("Pickachu fainted", 50, (display_width / 2), (display_height / 2), (0, 0, 0), "GOOUT")
        # update frames
        pygame.display.update()
        # frame visible or in motion 40 milisec
        clock.tick(30)


game_loop()
pygame.quit()
quit()
