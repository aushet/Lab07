import pygame
import sys
import math
from datetime import datetime

pygame.init()
WIDTH, HEIGHT = 800, 600
CENTER = (WIDTH // 2, HEIGHT // 2)
FPS = 60

background = pygame.image.load(r"C:\Users\асер\Pictures\clock.png")
min_hand = pygame.image.load(r"C:\Users\асер\Pictures\min_hand.png")
sec_hand = pygame.image.load(r"C:\Users\асер\Pictures\sec_hand.png")

def rot_center(image, angle,center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

screen = pygame.display.set_mode((WIDTH,HEIGHT))
pygame.display.set_caption("Mikki Maus Clock")

clock = pygame.time.Clock()
while True:
    screen.fill((255,255,255))
    screen.blit(background,(0,0))
    now = datetime.now()
    minutes = now.minute
    seconds = now.second
    minute_angle = -(minutes * 6)
    second_angle = -(seconds * 6)
    rotate_minute_hand,min_rect = rot_center(min_hand,minute_angle,CENTER)
    rotate_second_hand,sec_rect = rot_center(sec_hand,second_angle,CENTER)
    screen.blit(rotate_minute_hand,min_rect.topleft)
    screen.blit(rotate_second_hand,sec_rect.topleft)
    pygame.display.flip()
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()