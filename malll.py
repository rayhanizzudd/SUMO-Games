import pygame

pygame.init()
screen = pygame.display.set_mode((1000, 800))
img = pygame.image.load('game1/1.png')
done = False
bg = (120,120,120)
while not done:
   for event in pygame.event.get():
      screen.fill(bg)
      rect = img.get_rect()
      rect.center = 200, 100
      screen.blit(img, rect)
      if event.type == pygame.QUIT:
        done = True
   pygame.display.update()

