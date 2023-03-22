from kivy.uix.screenmanager import Screen


class Controller(Screen):
  def slide_to(self, direction):
    """
    Method untuk mengatur arah transisi.
    """
    self.manager.transition.direction = direction

