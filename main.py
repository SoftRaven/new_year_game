import pygame
import const
import chars
import map
import random
from datetime import datetime

random.seed(datetime.now())

def take_random_pos(posList):
    numPos = len(posList)
    pos = random.randint(0, numPos-1)
    position = posList.pop(pos)
    x = position[1]*const.TILE + const.TILE/2
    y = position[0] * const.TILE + const.TILE / 2
    return x, y

pygame.init()
screen = pygame.display.set_mode((const.WIDTH, const.HEIGHT))
pygame.display.set_caption("Game")
clock = pygame.time.Clock()

trees_pos, freeSpaces = map.draw_trees()
all_sprites = pygame.sprite.Group()
trees = pygame.sprite.Group()
char = pygame.sprite.Group()
xPlayer, yPlayer = take_random_pos(freeSpaces)
player = chars.Player(xPlayer, yPlayer)
char.add(player)
for tree in trees_pos:
    all_sprites.add(tree)
    trees.add(tree)

running = True
while running:
    clock.tick(const.FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    char.update(trees)
    all_sprites.update()

    screen.fill(const.BLACK)
    all_sprites.draw(screen)
    char.draw(screen)
    pygame.display.flip()

pygame.quit()
