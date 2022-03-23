import arcade
import Enemy

SPRITE_SCALING = 0.8


# Index of textures, first element faces left, second faces right
TEXTURE_LEFT = 0
TEXTURE_RIGHT = 1
TEXTURE_UP = 2
TEXTURE_DOWN = 3


class Player(arcade.Sprite):

    def __init__(self):
        super().__init__()

        self.scale = SPRITE_SCALING
        self.textures = []
        self.score = 0
        # Load a left facing texture and a right facing texture.
        # flipped_horizontally=True will mirror the image we load.
        texture = arcade.load_texture("Sprite/Player/PlayerLeft1.png")
        self.textures.append(texture)
        texture = arcade.load_texture("Sprite/Player/PlayerRight1.png")
        self.textures.append(texture)
        texture = arcade.load_texture("Sprite/Player/PlayerFront1.png")
        self.textures.append(texture)
        texture = arcade.load_texture("Sprite/Player/PlayerBack1.png")
        self.textures.append(texture)
        self.set_player_location()


        # By default, face right.
        self.texture = texture
    def set_player_location(self):
        self.center_x = 100
        self.center_y = 100
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        # Figure out if we should face left or right
        if self.change_x < 0:
            self.texture = self.textures[TEXTURE_LEFT]
        elif self.change_x > 0:
            self.texture = self.textures[TEXTURE_RIGHT]
        elif self.change_y < 0:
            self.texture = self.textures[TEXTURE_UP]
        elif self.change_y > 0:
            self.texture = self.textures[TEXTURE_DOWN]


