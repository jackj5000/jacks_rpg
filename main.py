from main_character import MainCharacter
from food import Food
from currency import Currency
import pygame

class Game(object):
    def __init__(self):
        self.player = MainCharacter()
        self.apple = Food('APPLE', 0.50, 0.33, 1)
        self.all_sprites_list = pygame.sprite.Group()
        self.items_sprites_list = pygame.sprite.Group()
        self.all_sprites_list.add(self.player)
        self.all_sprites_list.add(self.apple)
        self.items_sprites_list.add(self.apple)

    def process_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if self.player.touching_item is not None and self.player.last_direction == 'RIGHT':
                        self.player.touching_item = None
                    self.player.change_x = -2
                if event.key == pygame.K_RIGHT:
                    self.player.change_x = 2
                    if self.player.touching_item is not None and self.player.last_direction == 'LEFT':
                        self.player.touching_item = None
                if event.key == pygame.K_UP:
                    self.player.change_y = -2
                    if self.player.touching_item is not None and self.player.last_direction == 'DOWN':
                        self.player.touching_item = None
                if event.key == pygame.K_DOWN:
                    self.player.change_y = 2
                    if self.player.touching_item is not None and self.player.last_direction == 'UP':
                        self.player.touching_item = None
                if event.key == pygame.K_SPACE and self.player.touching_item is not None:
                    self.player.add_item(self.player.touching_item)
                    self.player.touching_item.kill()
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT and self.player.change_x < 0:
                    self.player.change_x = 0
                if event.key == pygame.K_RIGHT and self.player.change_x > 0:
                    self.player.change_x = 0
                if event.key == pygame.K_UP and self.player.change_y < 0:
                    self.player.change_y = 0
                if event.key == pygame.K_DOWN and self.player.change_y > 0:
                    self.player.change_y = 0
        return False

    def run_logic(self):
        self.all_sprites_list.update()
        items_hit_list = pygame.sprite.spritecollide(self.player, self.items_sprites_list, False)
        for item in items_hit_list:
            self.player.touching_item = item
            if self.player.change_x > 0:
                self.player.rect.right = item.rect.left
                self.player.last_direction = 'RIGHT'
            elif self.player.change_x < 0:
                self.player.rect.left = item.rect.right
                self.player.last_direction = 'LEFT'
            elif self.player.change_y > 0:
                self.player.rect.bottom = item.rect.top
                self.player.last_direction = 'DOWN'
            elif self.player.change_y < 0:
                self.player.rect.top = item.rect.bottom
                self.player.last_direction = 'UP'

    def display_frame(self, screen):
        screen.fill((255, 255, 255))
        self.all_sprites_list.draw(screen)
        pygame.display.flip()

def main():
    pygame.init()
    size = [640, 480]
    screen = pygame.display.set_mode(size)
    pygame.display.set_caption('Jacks RPG')
    pygame.mouse.set_visible(False)
    game = Game()
    done = False
    clock = pygame.time.Clock()
    while not done:
        done = game.process_events()
        game.run_logic()
        game.display_frame(screen)
        clock.tick(60)
    pygame.quit()    

    
if __name__ == "__main__":
    main()
