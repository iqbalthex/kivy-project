from kivy.lang import Builder
from .controller import Controller


class Menu(Controller):
  pass


Builder.load_file("./views/menu.kv")
