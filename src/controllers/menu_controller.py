from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Menu(Screen):
  def slide_to(self, direction):
    """
    Method untuk mengatur arah transisi.
    """
    self.manager.transition.direction = direction


Builder.load_file("./views/menu.kv")
