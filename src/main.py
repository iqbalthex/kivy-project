# from database import users
from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class Main(ScreenManager):
  pass


class GabutApp(App):
  def build(self):
    return Main()


Window.size = (400, 600)
Builder.load_file("./main.kv")

if __name__ == "__main__":
  GabutApp().run()
