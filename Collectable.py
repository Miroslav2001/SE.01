import arcade
import random

NUMBER_OF_BLUE_GEMS = 50
SPRITE_SCALING_GEM = 1
NUMBER_OF_DIAMONDS = 5


class Collectable(arcade.Sprite):

    def __init__(self,
                 filename: str = None,
                 scale: float = 1):

        super().__init__(filename, scale)

    def setup_blue_gem(self, wall_list):

        for i in range(NUMBER_OF_BLUE_GEMS):
            # Create the blue gems instance
            gem = Collectable("Sprite\Blue_gem.png", SPRITE_SCALING_GEM)
            gem_placed_successfully = False

            # Keep trying until success
            while not gem_placed_successfully:
                # Position the gem
                gem.center_x = random.randrange(200, 1200)
                gem.center_y = random.randrange(100, 700)

                # See if the gem is hitting a wall
                wall_hit_list = arcade.check_for_collision_with_list(gem, wall_list)

                # See if the gem is hitting another gem
                gem_hit_list = arcade.check_for_collision_with_list(gem, self.blue_gem_list)

                if len(wall_hit_list) == 0 and len(gem_hit_list) == 0:
                    # It is!
                    gem_placed_successfully = True

            # Add the gem to the lists
            self.blue_gem_list.append(gem)

    def setup_diamond(self, wall_list):
        for i in range(NUMBER_OF_DIAMONDS):
            # Create the Diamond instance
            diamond = Collectable("Sprite\Diamond.png", SPRITE_SCALING_GEM)
            diamond_placed_successfully = False

            while not diamond_placed_successfully:
                diamond.center_x = random.randrange(200, 1000)
                diamond.center_y = random.randrange(200, 700)
                wall_hit_list = arcade.check_for_collision_with_list(diamond, wall_list)
                diamond_hit_list = arcade.check_for_collision_with_list(diamond, self.diamond_list)
                if len(wall_hit_list) == 0 and len(diamond_hit_list) == 0:
                    diamond_placed_successfully = True
            self.diamond_list.append(diamond)

    def setup_green_gem(self, wall_list):
        green_gem = Collectable("Sprite\Green_gem.png", SPRITE_SCALING_GEM)
        green_gem_placed_successfully = False

        while not green_gem_placed_successfully:
            green_gem.center_x = random.randrange(200, 1000)
            green_gem.center_y = random.randrange(200, 700)
            wall_hit_list = arcade.check_for_collision_with_list(green_gem, wall_list)
            if len(wall_hit_list) == 0:
                green_gem_placed_successfully = True
        self.green_gem_list.append(green_gem)

    def setup_red_gem(self, wall_list):
        red_gem = Collectable("Sprite\Red_gem.png", SPRITE_SCALING_GEM)
        red_gem_placed_successfully = False
        while not red_gem_placed_successfully:
            red_gem.center_x = random.randrange(200, 1000)
            red_gem.center_y = random.randrange(200, 700)
            wall_hit_list = arcade.check_for_collision_with_list(red_gem, wall_list)
            if len(wall_hit_list) == 0:
                red_gem_placed_successfully = True
        self.red_gem_list.append(red_gem)
