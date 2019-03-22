import arcade
import os

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dungeon Escape"
SPRITE_SCALING = 0.9


MOVEMENT_SPEED = 5

class Player(arcade.Sprite):
  def update(self):
    self.center_x += self.change_x
    self.center_y += self.change_y

    if self.left < 0:
        self.left = 0
    elif self.right > SCREEN_WIDTH - 1:
        self.right = SCREEN_WIDTH - 1

    if self.bottom < 0:
        self.bottom = 0
    elif self.top > SCREEN_HEIGHT - 1:
        self.top = SCREEN_HEIGHT - 1

class DungeonEscape(arcade.Window):
  def __init__(self, width, height, title):
    super().__init__(width, height, title)
    file_path = os.path.dirname(os.path.abspath(__file__))
    os.chdir(file_path)

    # Variables that will hold sprite lists
    self.player_list = None

    # Set up the player info
    self.player_sprite = None


  def setup(self):
    # Sprite lists
    self.player_list = arcade.SpriteList()

    # Set up the player
    self.player_sprite = Player("images/player.png", SPRITE_SCALING)
    self.player_sprite.center_x = 50
    self.player_sprite.center_y = 50
    self.player_list.append(self.player_sprite)

    arcade.set_background_color(arcade.color.REDWOOD)

  def on_draw(self):
    arcade.start_render()
    self.player_list.draw()

  def update(self, delta_time):
    self.player_list.update()

  def on_key_press(self, key, modifiers):
    if key == arcade.key.UP:
        self.player_sprite.change_y = MOVEMENT_SPEED
    elif key == arcade.key.DOWN:
        self.player_sprite.change_y = -MOVEMENT_SPEED
    elif key == arcade.key.LEFT:
        self.player_sprite.change_x = -MOVEMENT_SPEED
    elif key == arcade.key.RIGHT:
        self.player_sprite.change_x = MOVEMENT_SPEED

  def on_key_release(self, key, modifiers):
    if key == arcade.key.UP or key == arcade.key.DOWN:
        self.player_sprite.change_y = 0
    elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
          self.player_sprite.change_x = 0

def main():
  game = DungeonEscape(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
  game.setup()
  arcade.run()

if __name__ == "__main__":
  main()