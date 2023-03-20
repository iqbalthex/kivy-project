from kivy.app import App
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager
from kivy.lang import Builder


class Main(ScreenManager):
  """
  Kelas untuk membungkus halaman aplikasi (semacam pagination).
  """

  def to(self, page):
    """
    Method untuk berpindah halaman.
    """
    self.current = page


class GabutApp(App):
  def build(self):
    return Main()


# memuat view utama dan style/propertinya
Builder.load_file("./main.kv")
Window.size = (400, 600)

if __name__ == "__main__":
  GabutApp().run()
