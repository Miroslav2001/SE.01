import arcade

SPRITE_SCALING = 6
SPRITE_SIZE = 2


class Enemy(arcade.Sprite):
    enemy_list = None

    def setup_enemy(self):
        self.enemy_list = arcade.SpriteList()
        resource = ":resources:images/animated_characters/zombie/zombie_idle.png"
        enemy = arcade.Sprite(resource, SPRITE_SCALING)
        enemy.center_x = SPRITE_SIZE * 4
        enemy.center_y = SPRITE_SIZE * 7
        self.enemy_list.append(enemy)

