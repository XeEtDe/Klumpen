import pygame

pygame.init()
sreen = pygame.display.set_mode((1000, 900))
done = False

while done == False:
        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                        done = True

        pygame.display.flip()
