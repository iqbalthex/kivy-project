from kivy.lang import Builder
from kivy.properties import ObjectProperty
from .controller import Controller

tentang = """\
Tentangku
Nama: Dione
Asal: Indonesia<3
Hobi: Membaca dan Ngoding
"""
kontak = """\
Kontak
WhatsApp: +-628*******
"""

class Dione(Controller):
  title_label = ObjectProperty()
  icon = ObjectProperty()

  def about_me(self):
    self.title_label.text = tentang
    self.icon.source = "gh.jpg"
    self.icon.opacity = 1

  def my_contact(self):
    self.title_label.text = kontak
    self.icon.source = "wa.jpg"
    self.icon.opacity = 1


Builder.load_file("./views/dione.kv")
