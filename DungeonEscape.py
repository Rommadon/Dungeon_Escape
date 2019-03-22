import arcade

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Dungeon Escape"


class DungeonEscape(arcade.Window):
  def __init__(self, width, height, title):
    super().__init__(width, height, title)
    self.background = None

  def setup(self):
    self.background = arcade.load_texture("images/background.jpg")

  def on_draw(self):
    arcade.start_render()
    arcade.draw_texture_rectangle(SCREEN_WIDTH // 2, SCREEN_HEIGHT // 2, SCREEN_WIDTH, SCREEN_HEIGHT, self.background)

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
  game = DungeonEscape(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
  game.setup()
  arcade.run()

if __name__ == "__main__":
  main()