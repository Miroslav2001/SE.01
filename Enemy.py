import arcade
import random  # For generating random numbers for enemy movement.

ENEMY1_SCALING = 1
enemyScaling = 1
SPRITE_SPEED = 1
ENEMY_COUNT = 5
RUN_ENEMY = 1
GHOST_SPEED = 0.5
GHOST_COUNT = 0


class Coin(arcade.Sprite):


    def __init__(
            self,
            filename: str = None,
            scale: float = 1,
            image_x: float = 0,
            image_y: float = 0,
            image_width: float = 0,
            image_height: float = 0,
            center_x: float = 0,
            center_y: float = 0,
            repeat_count_x: int = 1,  # Unused
            repeat_count_y: int = 1,  # Unused
            flipped_horizontally: bool = False,
            flipped_vertically: bool = False,
            flipped_diagonally: bool = False,
            hit_box_algorithm: str = "Simple",
            hit_box_detail: float = 4.5,
            angle: float = 0,
    ):
        super().__init__(filename, scale, image_x, image_y, image_width, image_height, center_x, center_y,
                         repeat_count_x, repeat_count_y, flipped_horizontally, flipped_vertically, flipped_diagonally,
                         hit_box_algorithm, hit_box_detail, angle)
        self.ghost_list = arcade.SpriteList()
        self.imageSprite = None
        self.physicsEngine = None
        self.speed = None
        self.dir_x = 0
        self.dir_y = 0
        self.counter = 1
        self.coin_list = None
        self.counter = 1

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
        self.coin_list = arcade.SpriteList()
        self.update()

        for i in range(ENEMY_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Coin("Sprite\Skeleton.png", ENEMY1_SCALING)
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(200, 1200)
                coin.center_y = random.randrange(100, 700)
                while coin.change_x == 0 and coin.change_y == 0:
                    coin.change_x = random.randrange(-4, 5)
                    coin.change_y = random.randrange(-4, 5)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists

            # Add the coin to the lists
            self.coin_list.append(coin)

    def setup_ghost(self, wall_list):
        self.ghost_list = arcade.SpriteList()
        for i in range(GHOST_COUNT):
            # Create the coin instance
            # Coin image from kenney.nl
            ghost = Coin("Sprite\Ghost.png", ENEMY1_SCALING)
            ghost_placed_successfully = False

            while not ghost_placed_successfully:
                # Position the coin
                ghost.center_x = random.randrange(200, 1200)
                ghost.center_y = random.randrange(100, 700)
                while ghost.change_x == 0 and ghost.change_y == 0:
                    ghost.change_x = random.randrange(-4, 5)
                    ghost.change_y = random.randrange(-4, 5)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(ghost, wall_list)

                # See if the coin is hitting another coin
                ghost_hit_list = arcade.check_for_collision_with_list(ghost, self.coin_list)

                if len(wall_hit_list) == 0 and len(ghost_hit_list) == 0:
                    # It is!
                    ghost_placed_successfully = True

            # Add the coin to the lists

            # Add the coin to the lists
            self.ghost_list.append(ghost)


    def random_movement(self, wall_list):

        for coin in self.coin_list:

            coin.center_x += coin.change_x
            collide = arcade.check_for_collision_with_list(coin, wall_list)
            for wall in collide:
                if coin.change_x > 0:
                    coin.right = wall.left
                elif coin.change_x < 0:
                    coin.left = wall.right
            if len(collide) > 0:
                coin.change_x *= -1

            coin.center_y += coin.change_y
            walls_hit = arcade.check_for_collision_with_list(coin, wall_list)
            for wall in walls_hit:
                if coin.change_y > 0:
                    coin.top = wall.bottom
                elif coin.change_y < 0:
                    coin.bottom = wall.top
            if len(walls_hit) > 0:
                coin.change_y *= -1
