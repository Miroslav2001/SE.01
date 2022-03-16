import arcade
import arcade.gui
from arcade.gui import UIManager
import sceneTiles
import Player01
import Enemy


SPRITE_SIZE = 25 * 1.5
MOVEMENT_SPEED = 5
SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 800


OPENING_PAGE = 1
MENU_PAGE = 2
GAME_WINDOW_1 = 3


class StartGame(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        mainWindow.change_game_state(GAME_WINDOW_1)


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class MenuButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        mainWindow.current_state = MENU_PAGE


class MyGameWindow(arcade.Window):
    player = Player01.Player()
    enemy = Enemy.Coin(position_list)

    def __init__(self, width, height):
        super().__init__(width, height)
        self.physicsEngineCoin = None
        self.current_state = None
        self.physicsEngine = None

        self.ui_manager = UIManager()
        arcade.set_background_color([101, 216, 255])
        self.change_game_state(OPENING_PAGE)
        self.allSpritesList = arcade.SpriteList()
        self.levelOneList = arcade.SpriteList()
        self.enemy.coin_list = arcade.SpriteList()


    def on_draw(self):
        sceneTiles.levelOneList = arcade.SpriteList()
        arcade.start_render()
        self.manager.draw()

        if self.current_state == OPENING_PAGE:
            self.draw_opening_page()

        if self.current_state == MENU_PAGE:
            self.draw_menu_page()

        if self.current_state == GAME_WINDOW_1:
            self.clear()
            sceneTiles.sceneTiles.setupSceneOne(self)
            self.draw_game_window_one()



    def change_game_state(self, new_state):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.current_state = new_state

        if self.current_state == OPENING_PAGE:
            menu_button = MenuButton(text="Menu", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=500,
                    align_y=250,
                    child=menu_button)
            )

            quit_button = QuitButton(text="Quit", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=500,
                    align_y=-250,
                    child=quit_button)
            )

        elif self.current_state == MENU_PAGE:
            start_game = StartGame(text="Start Game", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=100,
                    align_y=-100,
                    child=start_game)
            )

        elif self.current_state == GAME_WINDOW_1:
            mainWindow.setup()

    def draw_game_window_one(self):
        self.allSpritesList.draw()
        self.player.draw()
        self.enemy.coin_list.draw()

    def draw_opening_page(self):
        message = "Opening Page"
        arcade.draw_text(message, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, arcade.color.BLACK, 54)

    def draw_menu_page(self):
        self.change_game_state(MENU_PAGE)
        message = "Menu Page"
        arcade.draw_text(message, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, arcade.color.BLACK, 54)

    def setPlayerPhysics(self):
        self.physicsEngine = arcade.PhysicsEnginePlatformer(self.player, self.levelOneList, gravity_constant=0)


    def setup(self):
        if self.current_state == GAME_WINDOW_1:
            self.allSpritesList = arcade.SpriteList()
            self.enemy.coin_list = arcade.SpriteList()
            self.enemy.setup()





    def update(self, delta_time):

        if self.current_state == GAME_WINDOW_1:
            #for coin in self.enemy.coin_list:
              #  coin.follow_sprite(self.player)""
            self.setPlayerPhysics()
            self.player.update()
            self.player.update_animation()
            self.physicsEngine.update()
            enemy = self.enemy.coin_list[0]
            self.enemy.update()
            self.enemy.random_update()





    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.player.change_y = MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player.change_y = -MOVEMENT_SPEED
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.player.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.player.change_x = MOVEMENT_SPEED


    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S or key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D or key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


mainWindow = MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
mainWindow.setup()
arcade.run()
