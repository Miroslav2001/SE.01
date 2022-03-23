import datetime
import time

import arcade
import arcade.gui
from arcade.gui import UIManager

import Collectable
import Enemy
import Player01
import Statistics
import sceneTiles

SPRITE_SIZE = 25 * 1.5
SCREEN_WIDTH = 1420
SCREEN_HEIGHT = 800

OPENING_PAGE = 1
MENU_PAGE = 2
GAME_WINDOW_1 = 3
HIGH_SCORE_WINDOW = 4
GAME_OVER = 5
GAME_CHOOSER = 6
INTRODUCTION_PAGE = 7


class ArenaGame(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        print("CLICK")


class EndlessMode(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        mainWindow.change_game_state(INTRODUCTION_PAGE)


class StartGame(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        mainWindow.change_game_state(GAME_WINDOW_1)


class QuitButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        arcade.exit()


class MenuButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        mainWindow.change_game_state(MENU_PAGE)


class ScoreButton(arcade.gui.UIFlatButton):
    def on_click(self, event: arcade.gui.UIOnClickEvent):
        mainWindow.change_game_state(HIGH_SCORE_WINDOW)


class MyGameWindow(arcade.Window):
    player = Player01.Player()
    enemy = Enemy.Coin()
    collectable = Collectable.Collectable()
    statistics = Statistics.Statistics()

    def __init__(self, width, height):
        super().__init__(width, height)

        self.time_hit_enemy = 0
        self.time_hit_coin = 0
        self.coin_time = None
        self.manager = None
        self.physicsEngineCoin = None
        self.current_state = None
        self.physicsEngine = None

        self.ui_manager = UIManager()
        arcade.set_background_color([101, 216, 255])
        self.change_game_state(OPENING_PAGE)
        self.allSpritesList = arcade.SpriteList()
        self.levelOneList = arcade.SpriteList()
        self.enemy.coin_list = arcade.SpriteList()
        self.enemy.ghost_list = arcade.SpriteList()
        self.collectable.red_gem_list = arcade.SpriteList()
        self.collectable.green_gem_list = arcade.SpriteList()
        self.collectable.special_coin_list = arcade.SpriteList()
        self.kill_player = True
        self.wanted_timer = 0
        self.wanted_red_timer = 0
        self.wanted_green_timer = 0
        self.spawn_time_red = 0
        self.spawn_time_green = 0
        self.timer = 0
        self.enemy_information = False
        self.inputStr = ""
        self.user_name = None
        self.name_set = False
        self.gem_collected = 0
        self.enemy_killed = 0
        self.background = None

    def on_draw(self):
        self.clear()
        arcade.start_render()

        if self.current_state == OPENING_PAGE:
            self.draw_opening_page()
            self.manager.draw()

        elif self.current_state == MENU_PAGE:
            self.draw_menu_page()
            self.manager.draw()

        elif self.current_state == INTRODUCTION_PAGE:
            self.draw_introduction_page()
            self.manager.draw()

        elif self.current_state == GAME_WINDOW_1:
            self.draw_game_window_one()
            arcade.set_background_color(arcade.color.BLACK)

        elif self.current_state == GAME_OVER:
            arcade.set_background_color([101, 216, 255])
            self.draw_game_over()
            self.manager.draw()

        elif self.current_state == HIGH_SCORE_WINDOW:
            self.draw_score_page()
            self.manager.draw()

    def change_game_state(self, new_state):
        self.manager = arcade.gui.UIManager()
        self.manager.enable()
        self.current_state = new_state

        if self.current_state == OPENING_PAGE:
            self.background = arcade.load_texture("Sprite\Retro_image03.PNG")
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
            self.background = arcade.load_texture("Sprite\Retro_image02.PNG")

            start_game = EndlessMode(text="Endless Mode", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=0,
                    align_y=0,
                    child=start_game)
            )

            arena_game = ArenaGame(text="Arena Mode", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=-500,
                    align_y=0,
                    child=arena_game)
            )

            high_score = ScoreButton(text="High-Score Table", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=500,
                    align_y=0,
                    child=high_score)
            )

        elif self.current_state == GAME_WINDOW_1:
            self.setup()

        elif self.current_state == INTRODUCTION_PAGE:
            self.background = arcade.load_texture("Sprite\INTRODUCTION_IMAGE.PNG")
            skip_button = StartGame(text="SKIP", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=600,
                    align_y=350,
                    child=skip_button)
            )
        elif self.current_state == GAME_OVER:
            self.background = arcade.load_texture("Sprite\GAME_OVER.PNG")
            self.reset_variables()
            self.statistics.storeResult(self.user_name, self.player.score)
            menu_button = MenuButton(text="Menu", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=500,
                    align_y=250,
                    child=menu_button)
            )

        elif self.current_state == HIGH_SCORE_WINDOW:
            self.background = arcade.load_texture("Sprite\Retro_image03.PNG")
            menu_button = MenuButton(text="Menu", width=200)
            self.manager.add(
                arcade.gui.UIAnchorWidget(
                    align_x=500,
                    align_y=250,
                    child=menu_button)
            )

    def draw_score_page(self):
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)
        self.statistics.display_statistics()
    def draw_game_over(self):
        message = "GAME OVER"
        arcade.draw_text(message, SCREEN_WIDTH / 4, SCREEN_HEIGHT / 2, arcade.color.BLACK, 54)
        self.statistics.sort_table()
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

    def draw_introduction_page(self):
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

    def draw_game_window_one(self):

        self.allSpritesList.draw()
        self.player.draw()
        self.collectable.coin_list.draw()
        self.collectable.special_coin_list.draw()
        self.collectable.red_gem_list.draw()
        self.collectable.green_gem_list.draw()

        arcade.draw_text("Score: " + str(self.player.score), 1200, 760,
                         arcade.color.GREEN, font_name="Kenney Future")
        if self.enemy_information:
            arcade.draw_text("KILL", 700, 385,
                             arcade.color.RED_DEVIL, 20, font_name="Kenney Future")
        elif not self.enemy_information:
            arcade.draw_text("RUN", 700, 385,
                             arcade.color.BLUE, 20, font_name="Kenney Future")
        self.enemy.coin_list.draw()
        self.enemy.ghost_list.draw()


    def draw_opening_page(self):
        output = "Enter Your Username"
        arcade.draw_text(output, 200, 650, arcade.color.WHITE, 30)
        self.name_input()
        arcade.draw_rectangle_outline(590, 516, 600, 88, arcade.color.BRITISH_RACING_GREEN)
        output = "Press ENTER to lock in your Username"
        arcade.draw_text(output, 200, 400, arcade.color.WHITE, 30)
        if self.name_set:
            output = "Username Stored"
            arcade.draw_text(output, 200, 300, arcade.color.WHITE, 30)



    def draw_menu_page(self):
        message = "Not available for this beta"
        arcade.draw_text(message, 110, 210, arcade.color.BLACK)
        arcade.draw_lrwh_rectangle_textured(0, 0,
                                            SCREEN_WIDTH, SCREEN_HEIGHT,
                                            self.background)

    def setPlayerPhysics(self):
        self.physicsEngine = arcade.PhysicsEnginePlatformer(self.player, self.levelOneList, gravity_constant=0)

    def countdown(self):
        self.wanted_timer = (self.timer + 4)

    def name_input(self):
        output = self.inputStr
        arcade.draw_text(output, 300, 500, arcade.color.WHITE, 54)

    def reset_variables(self):
        self.gem_collected = 0
        self.enemy_killed = 0
        Collectable.NUMBER_OF_SPECIAL_COINS = 5
        Enemy.ENEMY_COUNT = 5
        self.collectable.green_gem_list.clear()  # Clear previous game green gems
        self.collectable.red_gem_list.clear()  # Clear previous game red gems

    def setup(self):
        if self.current_state == GAME_WINDOW_1:
            sceneTiles.sceneTiles.setupSceneOne(self)
            self.player.set_player_location()
            self.enemy.coin_list = arcade.SpriteList()
            self.enemy.ghost_list = arcade.SpriteList()
            self.collectable.coin_list = arcade.SpriteList()
            self.collectable.special_coin_list = arcade.SpriteList()
            self.enemy.setup(self.levelOneList)
            self.enemy.setup_ghost(self.levelOneList)
            self.collectable.setup_coin(self.levelOneList)
            self.collectable.setup_special_coin(self.levelOneList)
            self.collectable.setup_red_gem(self.levelOneList)
            self.collectable.setup_green_gem(self.levelOneList)

    def update(self, delta_time):

        if self.current_state == GAME_WINDOW_1:
            self.enemy.random_movement(self.levelOneList)
            self.setPlayerPhysics()
            self.player.update()
            self.player.update_animation()
            self.physicsEngine.update()
            self.timer = time.perf_counter()
            contact_enemy = arcade.check_for_collision_with_list(self.player, self.enemy.coin_list)
            scores = arcade.check_for_collision_with_list(self.player, self.collectable.coin_list)
            contact_gem = arcade.check_for_collision_with_list(self.player, self.collectable.special_coin_list)
            contact_ghost = arcade.check_for_collision_with_list(self.player, self.enemy.ghost_list)
            contact_red_gem = arcade.check_for_collision_with_list(self.player, self.collectable.red_gem_list)
            contact_green_gem = arcade.check_for_collision_with_list(self.player, self.collectable.green_gem_list)
            for ghost in self.enemy.ghost_list:
                ghost.follow_sprite(self.player)
            if self.wanted_timer > self.timer:
                self.enemy_information = True
            else:
                self.enemy_information = False

            if self.wanted_red_timer < self.timer:
                Player01.MOVEMENT_SPEED = 3
                Player01.MOVEMENT_SPEED_NEGATIVE = -3
            elif self.wanted_red_timer > self.timer:
                Player01.MOVEMENT_SPEED = 8
                Player01.MOVEMENT_SPEED_NEGATIVE = -8

            if self.spawn_time_red < self.timer:
                if self.spawn_time_red != 0:
                    self.spawn_time_red = 0
                    self.collectable.setup_red_gem(self.levelOneList)

            if self.spawn_time_green < self.timer:
                if self.spawn_time_green != 0:
                    self.spawn_time_green = 0
                    self.collectable.setup_green_gem(self.levelOneList)

            if self.wanted_green_timer < self.timer:
                self.player.scale = 0.8
            elif self.wanted_green_timer > self.timer:
                self.player.scale = 0.3

            for hit in contact_gem:
                self.countdown()
                hit.value = 100
                self.player.score += hit.value
                hit.kill()
                self.gem_collected = self.gem_collected + 1
                if self.gem_collected == Collectable.NUMBER_OF_SPECIAL_COINS:
                    self.gem_collected = 0
                    self.collectable.setup_special_coin(self.levelOneList)

            for hit in contact_enemy or contact_ghost:
                if self.wanted_timer < self.timer:
                    self.change_game_state(GAME_OVER)
                else:
                    hit.kill()
                    self.enemy_killed = self.enemy_killed + 1
                    if self.enemy_killed == Enemy.ENEMY_COUNT + Enemy.GHOST_COUNT:
                        self.enemy_killed = 0
                        Enemy.ENEMY_COUNT = Enemy.ENEMY_COUNT + 2
                        Enemy.GHOST_COUNT = Enemy.GHOST_COUNT + 1
                        self.enemy.setup(self.levelOneList)
                        self.enemy.setup_ghost(self.levelOneList)

            for hit in scores:
                self.player.score += 25
                hit.kill()

            for hit in contact_red_gem:
                self.wanted_red_timer = self.timer + 4
                self.spawn_time_red = self.timer + 5
                self.player.score += 75
                hit.kill()

            for hit in contact_green_gem:
                self.wanted_green_timer = self.timer + 4
                self.spawn_time_green = self.timer + 5
                self.player.score += 50
                hit.kill()

    def on_key_press(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.UP:
            self.player.change_y = Player01.MOVEMENT_SPEED
        elif key == arcade.key.S or key == arcade.key.DOWN:
            self.player.change_y = Player01.MOVEMENT_SPEED_NEGATIVE
        elif key == arcade.key.A or key == arcade.key.LEFT:
            self.player.change_x = Player01.MOVEMENT_SPEED_NEGATIVE
        elif key == arcade.key.D or key == arcade.key.RIGHT:
            self.player.change_x = Player01.MOVEMENT_SPEED
        if self.current_state == OPENING_PAGE:
            if arcade.key.A <= key <= arcade.key.Z:
                self.inputStr += chr(key)
            elif key == arcade.key.BACKSPACE:
                self.inputStr = self.inputStr[0: -1]
            elif key == arcade.key.SPACE:
                self.inputStr += (" ")
            elif key == arcade.key.ENTER:
                self.user_name = self.inputStr
                self.name_set = True

    def on_key_release(self, key, modifiers):
        if key == arcade.key.W or key == arcade.key.S or key == arcade.key.UP or key == arcade.key.DOWN:
            self.player.change_y = 0
        elif key == arcade.key.A or key == arcade.key.D or key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player.change_x = 0


mainWindow = MyGameWindow(SCREEN_WIDTH, SCREEN_HEIGHT)
arcade.run()
