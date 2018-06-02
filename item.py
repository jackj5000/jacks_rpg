import pygame

class Item(pygame.sprite.Sprite):
    def __init__(self, name, value, weight):
        super().__init__()        
        self.name = name
        self.value = value
        self.weight = weight
