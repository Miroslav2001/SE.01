import arcade
import random  # For generating random numbers for enemy movement.

ENEMY1_SCALING = 1 # Scale of Sprite enemies
SPRITE_SPEED = 1 # speed of skeletons
ENEMY_COUNT = 5 # initial number of skeletons to be displayed
GHOST_SPEED = 0.5 # speed of ghost
GHOST_COUNT = 0 # initial number of ghosts


class Enemy(arcade.Sprite):

    def __init__(
            self,
            filename: str = None,
            scale: float = 1):
        super().__init__(filename, scale)


    def follow_sprite(self, player_sprite):
        if self.center_y < player_sprite.center_y:
            self.center_y += min(GHOST_SPEED, player_sprite.center_y - self.center_y)
        elif self.center_y > player_sprite.center_y:
            self.center_y -= min(GHOST_SPEED, self.center_y - player_sprite.center_y)

        if self.center_x < player_sprite.center_x:
            self.center_x += min(GHOST_SPEED, player_sprite.center_x - self.center_x)
        elif self.center_x > player_sprite.center_x:
            self.center_x -= min(GHOST_SPEED, self.center_x - player_sprite.center_x)

    def setup(self, wall_list):

        for i in range(ENEMY_COUNT):
            # Create the enemy instance
            enemy = Enemy("Sprite\Skeleton.png", ENEMY1_SCALING)
            enemy_placed_successfully = False
            while not enemy_placed_successfully:
                enemy.center_x = random.randrange(200, 1200)
                enemy.center_y = random.randrange(100, 700)
                while enemy.change_x == 0 and enemy.change_y == 0:
                    enemy.change_x = random.randrange(-4, 5)
                    enemy.change_y = random.randrange(-4, 5)
                wall_hit_list = arcade.check_for_collision_with_list(enemy, wall_list)
                coin_hit_list = arcade.check_for_collision_with_list(enemy, self.enemy_list)
                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    enemy_placed_successfully = True

            self.enemy_list.append(enemy)

    def setup_ghost(self, wall_list):
        self.ghost_list = arcade.SpriteList()
        for i in range(GHOST_COUNT):
            # Create the ghost instance
            ghost = Enemy("Sprite\Ghost.png", ENEMY1_SCALING)
            ghost_placed_successfully = False

            while not ghost_placed_successfully:
                # Position the coin
                ghost.center_x = random.randrange(200, 1200)
                ghost.center_y = random.randrange(100, 700)
                while ghost.change_x == 0 and ghost.change_y == 0:
                    ghost.change_x = random.randrange(-4, 5)
                    ghost.change_y = random.randrange(-4, 5)

                wall_hit_list = arcade.check_for_collision_with_list(ghost, wall_list)
                ghost_hit_list = arcade.check_for_collision_with_list(ghost, self.ghost_list)
                if len(wall_hit_list) == 0 and len(ghost_hit_list) == 0:
                    # It is!
                    ghost_placed_successfully = True

            self.ghost_list.append(ghost)

    def random_movement(self, wall_list):
        for enemy in self.enemy_list:
            enemy.center_x += enemy.change_x
            collide = arcade.check_for_collision_with_list(enemy, wall_list)
            for wall in collide:
                if enemy.change_x > 0:
                    enemy.right = wall.left
                elif enemy.change_x < 0:
                    enemy.left = wall.right
            if len(collide) > 0:
                enemy.change_x *= -1

            enemy.center_y += enemy.change_y
            walls_hit = arcade.check_for_collision_with_list(enemy, wall_list)
            for wall in walls_hit:
                if enemy.change_y > 0:
                    enemy.top = wall.bottom
                elif enemy.change_y < 0:
                    enemy.bottom = wall.top
            if len(walls_hit) > 0:
                enemy.change_y *= -1
