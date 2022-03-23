import arcade
import random
import time

NUMBER_OF_COINS = 50
SPRITE_SCALING_COIN = 1
NUMBER_OF_SPECIAL_COINS = 5


class Collectable(arcade.Sprite):

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

    def setup_coin(self, wall_list):

        for i in range(NUMBER_OF_COINS):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Collectable("Sprite\Blue_gem.png", SPRITE_SCALING_COIN)
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(200, 1200)
                coin.center_y = random.randrange(100, 700)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.coin_list.append(coin)

    def setup_special_coin(self, wall_list):
        for i in range(NUMBER_OF_SPECIAL_COINS):
            # Create the coin instance
            # Coin image from kenney.nl
            coin = Collectable("Sprite\Diamond.png", SPRITE_SCALING_COIN)
            coin_placed_successfully = False

            # Keep trying until success
            while not coin_placed_successfully:
                # Position the coin
                coin.center_x = random.randrange(200, 1000)
                coin.center_y = random.randrange(200, 700)

                # See if the coin is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(coin, wall_list)

                # See if the coin is hitting another coin
                coin_hit_list = arcade.check_for_collision_with_list(coin, self.special_coin_list)

                if len(wall_hit_list) == 0 and len(coin_hit_list) == 0:
                    # It is!
                    coin_placed_successfully = True

            # Add the coin to the lists
            self.special_coin_list.append(coin)

    def setup_green_gem(self, wall_list):
        green_gem = Collectable("Sprite\Green_gem.png", SPRITE_SCALING_COIN)
        green_gem_placed_successfully = False

        # Keep trying until success
        while not green_gem_placed_successfully:
            # Position the coin
            green_gem.center_x = random.randrange(200, 1000)
            green_gem.center_y = random.randrange(200, 700)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(green_gem, wall_list)

            if len(wall_hit_list) == 0:
                green_gem_placed_successfully = True

        # Add the coin to the lists
        self.green_gem_list.append(green_gem)

    def setup_red_gem(self, wall_list):
        red_gem = Collectable("Sprite\Red_gem.png", SPRITE_SCALING_COIN)
        red_gem_placed_successfully = False

        # Keep trying until success
        while not red_gem_placed_successfully:
            # Position the coin
            red_gem.center_x = random.randrange(200, 1000)
            red_gem.center_y = random.randrange(200, 700)

            # See if the coin is hitting a wall
            wall_hit_list = arcade.check_for_collision_with_list(red_gem, wall_list)

            if len(wall_hit_list) == 0:
                red_gem_placed_successfully = True

        # Add the coin to the lists
        self.red_gem_list.append(red_gem)
