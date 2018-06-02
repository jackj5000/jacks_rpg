from currency import Currency
from food import Food
import pygame

class MainCharacter(pygame.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.image = pygame.Surface([20, 20])
        self.image.fill((0, 0, 0))
        self.rect = self.image.get_rect()
        self.rect.centerx = (640//2)
        self.rect.centery = (480//2)
        self.change_x = 0
        self.change_y = 0
        self.max_hp = 10
        self.hp = 10
        self.level = 1
        self.xp = 0
        self.currency = 0.00
        self.inventory_weight = 0.00
        self.inventory = {}
        self.touching_item = None
        self.last_direction = None

    def update(self):
##  mouse movement        
##        pos = pygame.mouse.get_pos()
##        self.rect.centerx = pos[0]
##        self.rect.centery = pos[1]        
        self.rect.x += self.change_x
        self.rect.y += self.change_y

    def __str__(self):
        string = "HP: {}\nLEVEL: {}\nXP: {}\nCURRENCY: {}\nINVENTORY_WEIGHT: {}\nINVENTORY:\n"
        i = 1
        for key, value in self.inventory.items():
            string += "    {}. {} - VALUE: {} WEIGHT: {}\n".format(i, key, value.value, value.weight)
            i += 1
        return string.format(self.hp, self.level, self.xp, self.currency, self.inventory_weight)

    def add_item(self, item):        
        if type(item) is Currency:
            self.currency += item.instant_value
        else:
            self.inventory_weight += item.weight
            self.inventory[item.name] = item

    def use_item(self, name):
        item = self.inventory[name]
        self.inventory_weight -= item.weight
        if type(item) is Food:
            self.hp += item.hp
            if self.hp > self.max_hp:
                self.hp = self.max_hp        
        del self.inventory[name]
            
