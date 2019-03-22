import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dungeon Escape"


class DungeonEscape(arcade.Window):
  def __init__(self, width, height, title):
    super().__init__(width, height, title)

    arcade.set_background_color(arcade.color.AMAZON)

    # If you have sprite lists, you should create them here,
    # and set them to None

  def setup(self):
    # Create your sprites and sprite lists here
    pass

  def on_draw(self):
    """
    Render the screen.
    """

    # This command should happen before we start drawing. It will clear
    # the screen to the background color, and erase what we drew last frame.
    arcade.start_render()

    # Call draw() on all your sprite lists below

  def update(self, delta_time):
    """
    All the logic to move, and the game logic goes here.
    Normally, you'll call update() on the sprite lists that
    need it.
    """
    pass

  def on_key_press(self, key, key_modifiers):
    """
    Called whenever a key on the keyboard is pressed.

    For a full list of keys, see:
    http://arcade.academy/arcade.key.html
    """
    pass

  def on_key_release(self, key, key_modifiers):
    """
    Called whenever the user lets off a previously pressed key.
    """
    pass

def main():
  game = MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
  game.setup()
  arcade.run()

if __name__ == "__main__":
  main()