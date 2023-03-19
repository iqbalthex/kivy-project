from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.widget import Widget

class LoginPage(Widget):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

  def login(self):
    username = self.username
    password = self.password

    # if username.text != "admin" or password.text != "password":
      # return self.add_widget(Label(text="Login failed."))

    # self.add_widget(Label(text="Login success."))


class GabutApp(App):
  def build(self):
    return LoginPage()


if __name__ == "__main__":
  GabutApp().run()
