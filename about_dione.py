from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.image import Image

class HomePage(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
        self.orientation = 'vertical'
        
        header = BoxLayout(size_hint=(1, 0.1))
        header.add_widget(Label(text='HOME PAGE', font_size=30))
        self.add_widget(header)
        
 
        img = Image(source='background1.png', allow_stretch=True, keep_ratio=False, size_hint=(1,1))
        self.content_text = Label(text="Selamat datang di\n home page sedehanaku!!!", size_hint=(0, 0), pos_hint={'center_x': 0.5, 'center_y': 0.5}, bold=True, italic= True, font_size= 40)
        content = AnchorLayout()
        content.add_widget(img)
        content.add_widget(self.content_text)
        
        self.add_widget(content)
        

        footer = BoxLayout(size_hint=(1, 0.1))
        self.tentang = Button(text='Tentang', font_size=15, background_color=(1,1,0,1))
        self.tentang.bind(on_press= self.tentangku)
        self.kontak = Button(text='Kontak', font_size=15, background_color=(1,1,0,1))
        self.kontak.bind(on_press= self.kontakku)
        footer.add_widget(self.tentang)
        footer.add_widget(self.kontak)
        self.add_widget(footer)
        
    def tentangku(self, instance):
	       self.content_text.text = "Tentangku\n\nNama : Dione\nAsal: Indonesia<3\nHobi: Membaca dan Ngoding"
	       self.content_text.bold = False
    def kontakku(self, instance):
	       self.content_text.text = "Kontak\n\nWhatApp: +628*********"
        
class HomePageApp(App):
    def build(self):
        return HomePage()

if __name__ == '__main__':
    HomePageApp().run()
