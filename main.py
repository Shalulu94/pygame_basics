import pygame
from sys import exit

pygame.init()
screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption("Runner")
clock = pygame.time.Clock()
test_font = pygame.font.Font("font/Pixeltype.ttf", 50)

sky_surface = pygame.image.load("graphics/Sky.png")
ground_surface = pygame.image.load("graphics/ground.png")
text_surface = test_font.render("My game", False, "Black")

snail_x_pos = 600
snail_y_pos = 250

snail_surf = pygame.image.load("graphics/snail/snail1.png").convert_alpha()
snail_rect = snail_surf.get_rect(midbottom=(800, 300))


player_surf = pygame.image.load("graphics/Player/player_walk_1.png").convert_alpha()
player_rect = player_surf.get_rect(midbottom=(80, 300))


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

    screen.blit(sky_surface, (0, 0))
    screen.blit(ground_surface, (0, 300))
    screen.blit(text_surface, (300, 50))

    snail_rect.left -= 4
    if snail_rect.right <= 0:
        snail_rect.left = 800
    screen.blit(snail_surf, snail_rect)
    screen.blit(player_surf, player_rect)

    player_rect.colliderect(snail_rect)

    pygame.display.update()
    clock.tick(60)