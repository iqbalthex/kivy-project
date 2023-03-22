from kivy.lang import Builder
from .controller import Controller


class Home(Controller):
  pass


Builder.load_file("./views/home.kv")
