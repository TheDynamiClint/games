import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font('pygame_stuff/font/Pixeltype.ttf', 50)

sky_surface = pygame.image.load('pygame_stuff/graphics/Sky.png').convert()
ground_surface = pygame.image.load('pygame_stuff/graphics/ground.png').convert()

score_surf = test_font.render('My Game', False, '#FF22EE')
score_rect = score_surf.get_rect(center=(400, 50))

snail_surface = pygame.image.load('pygame_stuff/graphics/snail/snail1.png').convert_alpha()
snail_rect = snail_surface.get_rect(midbottom=(600, 300))

player_surface = pygame.image.load('pygame_stuff/graphics/player/player_walk_1.png')
player_rect = player_surface.get_rect(midbottom=(80, 300))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        # if event.type == pygame.MOUSEMOTION:
        #   if player_rect.collidepoint(event.pos):
        #       print('collision')

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    pygame.draw.rect(screen, 'Pink', score_rect)
    pygame.draw.rect(screen, 'Pink', score_rect, 10)
    # pygame.draw.line(screen, 'Gold', (0, 0), (800, 400), 10)
    screen.blit(score_surf, score_rect)
    # snail_x_position -= 4
    # if snail_x_position < -100:
    #    snail_x_position = 800

    # player_rect.left += 1
    snail_rect.x -= 4

    if snail_rect.right <= 0:
        snail_rect.left = 800

    screen.blit(player_surface, player_rect)
    screen.blit(snail_surface, snail_rect)

    if player_rect.colliderect(snail_rect):
        print('collision')

    # mouse_pos = pygame.mouse.get_pos()
    # if player_rect.collidepoint((mouse_pos)):
    #     print('collision')

    pygame.display.update()
    clock.tick(40)
