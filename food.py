from item import Item
import pygame

class Food(Item):
    def __init__(self, name, value, weight, hp):
        super().__init__(name, value, weight)
        self.image = pygame.Surface([10, 10])
        self.image.fill((255, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = (640//3)
        self.rect.centery = (480//3)
        self.hp = hp
