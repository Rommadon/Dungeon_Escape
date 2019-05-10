import arcade
import os

SPRITE_SCALING = 1
SPRITE_NATIVE_SIZE = 128
SPRITE_SIZE = int(SPRITE_NATIVE_SIZE * SPRITE_SCALING)

SCREEN_WIDTH = 1250
SCREEN_HEIGHT = 650
SCREEN_TITLE = "Dungeon Escape"

# How many pixels to keep as a minimum margin between the character
# and the edge of the screen.
VIEWPORT_MARGIN = 40
RIGHT_MARGIN = 150

# Physics
MOVEMENT_SPEED = 5
JUMP_SPEED = 14
GRAVITY = 0.5


class MyGame(arcade.Window):
    """ Main application class. """

    def __init__(self):
        """
        Initializer
        """
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        file_path = os.path.dirname(os.path.abspath(__file__))
        os.chdir(file_path)

        # Sprite lists
        self.wall_list = None
        self.wall_list_2 = None
        self.enemy_list = None
        self.enemy_list_2 = None
        self.player_list = None
        self.door_list = None
        self.trophy_list = None

        # Set up the player
        self.player_sprite = None
        self.physics_engine = None
        self.view_left = 0
        self.view_bottom = 0

        #Set up state
        self.game_over = False
        self.go_to_stage_2 = False
        self.winner = False
        self.start = True

    def setup(self):
        """ Set up the game and initialize the variables. """

        # Sprite lists
        self.wall_list = arcade.SpriteList()
        self.enemy_list = arcade.SpriteList()
        self.player_list = arcade.SpriteList()
        self.door_list = arcade.SpriteList()
        self.trophy_list = arcade.SpriteList()

        if self.go_to_stage_2:
          # Draw the walls on the bottom
          for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
              wall = arcade.Sprite("images/wall.png", 1)

              wall.bottom = 0
              wall.left = x/2
              self.wall_list.append(wall)

          # Draw the platform
          for x in range(SPRITE_SIZE * 5, SPRITE_SIZE* 6, SPRITE_SIZE):
              wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

              wall.bottom = SPRITE_SIZE * 2
              wall.left = x
              self.wall_list.append(wall)
          
        
          for x in range(SPRITE_SIZE * 2, SPRITE_SIZE* 4, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 1
            wall.left = x
            self.wall_list.append(wall)

                
          for x in range(SPRITE_SIZE * 6, SPRITE_SIZE* 8, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 1
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 8, SPRITE_SIZE* 9, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 2
            wall.left = x
            self.wall_list.append(wall)

          
          for x in range(SPRITE_SIZE * 1, SPRITE_SIZE* 2, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 2
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 2, SPRITE_SIZE* 4, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

        if not self.go_to_stage_2:
          # Draw the walls on the bottom
          for x in range(0, SCREEN_WIDTH, SPRITE_SIZE):
              wall = arcade.Sprite("images/wall.png", 1)

              wall.bottom = 0
              wall.left = x/5
              self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 1, SPRITE_SIZE* 2, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 1
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 2, SPRITE_SIZE* 3, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 2
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 1, SPRITE_SIZE* 2, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 3, SPRITE_SIZE* 5, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 5, SPRITE_SIZE* 6, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 1
            wall.left = x
            self.wall_list.append(wall)

          for x in range(SPRITE_SIZE * 7, SPRITE_SIZE* 8, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = 0 
            wall.left = x
            self.wall_list.append(wall)
          
          for x in range(SPRITE_SIZE * 8, SPRITE_SIZE* 9, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 1
            wall.left = x
            self.wall_list.append(wall)
          
          for x in range(SPRITE_SIZE * 9, SPRITE_SIZE* 10, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 2
            wall.left = x
            self.wall_list.append(wall)
          
          for x in range(SPRITE_SIZE * 8, SPRITE_SIZE* 9, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 3
            wall.left = x
            self.wall_list.append(wall)
          for x in range(SPRITE_SIZE * 9, SPRITE_SIZE* 10, SPRITE_SIZE):
            wall = arcade.Sprite("images/wall.png", SPRITE_SCALING)

            wall.bottom = SPRITE_SIZE * 4
            wall.left = x
            self.wall_list.append(wall)

        # -- Draw an enemy on the ground
        if self.go_to_stage_2:
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 1.5
          enemy.left = SPRITE_SIZE * 2

          # Set enemy initial speed
          enemy.boundary_right = SPRITE_SIZE * 3.5
          enemy.boundary_left = SPRITE_SIZE * 2
          enemy.change_x = 4
          self.enemy_list.append(enemy)

          # -- Draw a enemy on the platform
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 2.5
          enemy.left = SPRITE_SIZE * 4

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 6
          enemy.boundary_left = SPRITE_SIZE * 3
          enemy.change_x = 4
          self.enemy_list.append(enemy)


          # -- Draw a enemy on the platform
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 1.5
          enemy.left = SPRITE_SIZE * 6

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 7.5
          enemy.boundary_left = SPRITE_SIZE * 6
          enemy.change_x = 4
          self.enemy_list.append(enemy)

          # -- Draw a enemy on the platform
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 0.5
          enemy.left = SPRITE_SIZE * 1

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 6
          enemy.boundary_left = SPRITE_SIZE * 0.5
          enemy.change_x = 4
          self.enemy_list.append(enemy)

          # -- Draw a enemy on the platform
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 3.5
          enemy.left = SPRITE_SIZE * 1

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 5
          enemy.boundary_left = SPRITE_SIZE * 0.5
          enemy.change_x = 4
          self.enemy_list.append(enemy)

        if not self.go_to_stage_2:
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 0.5
          enemy.left = SPRITE_SIZE * 1

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 3
          enemy.boundary_left = SPRITE_SIZE * 1
          enemy.change_x = 4
          self.enemy_list.append(enemy)

          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 3.5
          enemy.left = SPRITE_SIZE * 1

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 5
          enemy.boundary_left = SPRITE_SIZE * 0.5
          enemy.change_x = 4
          self.enemy_list.append(enemy)

          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 3.5
          enemy.left = SPRITE_SIZE * 7

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 9
          enemy.boundary_left = SPRITE_SIZE * 7
          enemy.change_x = 4
          self.enemy_list.append(enemy)

          
          enemy = arcade.Sprite("images/monster.png", 0.2)

          enemy.bottom = SPRITE_SIZE * 2
          enemy.left = SPRITE_SIZE * 4

          # Set boundaries on the left/right the enemy can't cross
          enemy.boundary_right = SPRITE_SIZE * 7
          enemy.boundary_left = SPRITE_SIZE * 4
          enemy.change_x = 4
          self.enemy_list.append(enemy)
    
        # Trophy
        if not self.go_to_stage_2:
          trophy = arcade.Sprite("images/door.png", 1.5)

          trophy.bottom = SPRITE_SIZE * 4.5
          trophy.left = SPRITE_SIZE * 9.1
          self.door_list.append(trophy)

        if self.go_to_stage_2:
          trophy = arcade.Sprite("images/trophy.png", 1)

          trophy.bottom = SPRITE_SIZE * 2.5
          trophy.left = SPRITE_SIZE * 8.15
          self.trophy_list.append(trophy)

        # -- Set up the player
        self.player_sprite = arcade.Sprite("images/player.png", SPRITE_SCALING)
        self.player_list.append(self.player_sprite)

        # Starting position of the player
        self.player_sprite.center_x = 70
        self.player_sprite.center_y = 270

        self.physics_engine = arcade.PhysicsEnginePlatformer(self.player_sprite,
                                                             self.wall_list,
                                                             gravity_constant=GRAVITY)

        # Set the background color
        arcade.set_background_color(arcade.color.BLACK)

    def on_draw(self):
        arcade.start_render()
        
        if self.start:
          arcade.draw_text("Dungeon Escape", 375, 400, arcade.color.WHITE, 50)
          arcade.draw_text("Press Enter To Start", 550, 350, arcade.color.WHITE, 12)

        if not self.game_over and not self.winner and not self.start:
          self.player_list.draw()
          self.wall_list.draw()
          self.enemy_list.draw()
          self.door_list.draw()
          self.trophy_list.draw()

        if self.winner:
          arcade.draw_text("You Winner", 470, 400, arcade.color.YELLOW, 50)
          arcade.draw_text("Press spacebar To Try Again Kid", 525, 350, arcade.color.WHITE, 12)
          
        if self.game_over:
          arcade.draw_text("You died", 500, 400, arcade.color.RED, 50)
          arcade.draw_text("Press Spacebar To Try Again Kid", 520, 350, arcade.color.WHITE, 12)

    def on_key_press(self, key, modifiers):
        """
        Called whenever the mouse moves.
        """
        if key == arcade.key.UP:
            if self.physics_engine.can_jump():
                self.player_sprite.change_y = JUMP_SPEED
        elif key == arcade.key.LEFT:
            self.player_sprite.change_x = -MOVEMENT_SPEED
        elif key == arcade.key.RIGHT:
            self.player_sprite.change_x = MOVEMENT_SPEED
        elif key == arcade.key.SPACE:
            self.game_over = False
            self.go_to_stage_2 = False
            self.winner = False
            self.setup()
        elif key == arcade.key.ENTER:
            self.start = False
            self.setup()
            

    def on_key_release(self, key, modifiers):
        """
        Called when the user presses a mouse button.
        """
        if key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player_sprite.change_x = 0

    def update(self, delta_time):
        """ Movement and game logic """

        if not self.game_over:
            self.enemy_list.update()

            for enemy in self.enemy_list:
                if len(arcade.check_for_collision_with_list(enemy, self.wall_list)) > 0:
                    enemy.change_x *= -1
                elif enemy.boundary_left is not None and enemy.left < enemy.boundary_left:
                    enemy.change_x *= -1
                elif enemy.boundary_right is not None and enemy.right > enemy.boundary_right:
                    enemy.change_x *= -1

            self.physics_engine.update()

            if len(arcade.check_for_collision_with_list(self.player_sprite, self.enemy_list)) > 0:
              self.game_over = True

            if self.player_sprite.center_y < 0:
              self.game_over = True

            if len(arcade.check_for_collision_with_list(self.player_sprite, self.door_list)) > 0:
              self.go_to_stage_2 = True
              self.setup()

            
            if len(arcade.check_for_collision_with_list(self.player_sprite, self.trophy_list)) > 0:
              self.winner = True
              self.setup()

def main():
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()