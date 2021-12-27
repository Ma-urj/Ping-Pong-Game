import pygame
import sys
import time
import random


def ball_animation():
    global ball_speed_x, ball_speed_y, player_score, opponent_score
    ball.x += ball_speed_x
    ball.y += ball_speed_y
    if ball.y <= 0 or ball.y >= dis_height:
        ball_speed_y = -ball_speed_y
    if ball.colliderect(player) or ball.colliderect(opponent):
        ball_speed_x = -ball_speed_x
    if ball.x <= 0 or ball.x >= dis_width:
        if ball.x <= 0:
            player_score += 1
        else:
            opponent_score += 1
        ball_speed_x *= random.choice((1, -1))
        ball_speed_y *= random.choice((1, -1))
        GameLoop()


def player_animation():
    player.y += player_speed
    if player.top <= 0:
        player.top = 0
    if player.bottom >= dis_height:
        player.bottom = dis_height


def opponent_ai():
    if opponent.y < ball.y:
        opponent.y += opponent_speed
    if opponent.y > ball.y:
        opponent.y -= opponent_speed

    if opponent.top <= 0:
        opponent.top = 0
    if opponent.bottom >= dis_height:
        opponent.bottom = dis_height


pygame.init()

clock = pygame.time.Clock()

# RGB colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
bg_color = pygame.Color('grey12')
light_grey = (200, 200, 200)


# Window Dimensions
dis_width = 1280
dis_height = 960


# Font styles
game_font = pygame.font.SysFont("bahnschrift", 32)

# Function for keeping score
player_score = 0
opponent_score = 0


screen = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption("Pong Game by Maurj")

# Game Rectangles
ball = pygame.Rect(dis_width/2-15, dis_height/2-15, 30, 30)
player = pygame.Rect(dis_width-20, dis_height/2-70, 10, 140)
opponent = pygame.Rect(20, dis_height/2-70, 10, 140)
ball_speed_x = 7
ball_speed_y = 7
player_speed = 0
opponent_speed = 6


def GameLoop():
    global player_speed
    ball.x = dis_width/2-15
    ball.y = dis_height/2-15

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Movement
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    player_speed += 6
                elif event.key == pygame.K_UP:
                    player_speed -= 6
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_DOWN:
                    player_speed -= 6
                elif event.key == pygame.K_UP:
                    player_speed += 6

        player_animation()

        ball_animation()

        opponent_ai()

        screen.fill(bg_color)
        pygame.draw.rect(screen, light_grey, player)
        pygame.draw.rect(screen, light_grey, opponent)
        pygame.draw.ellipse(screen, light_grey, ball)
        pygame.draw.aaline(screen, light_grey, (dis_width/2, 0),
                           (dis_width/2, dis_height))
        player_text = game_font.render(f"{player_score}", False, light_grey)
        screen.blit(player_text, (660, 470))
        opponent_text = game_font.render(
            f"{opponent_score}", False, light_grey)
        screen.blit(opponent_text, (600, 470))
        pygame.display.flip()
        clock.tick(60)


GameLoop()
