from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

class LoginPage(BoxLayout):
  def __init__(self, **kwargs):
    super().__init__(**kwargs)

    self.username_input = TextInput(multiline=False)
    self.password_input = TextInput(multiline=False, password=True)
    self.login_btn = Button(text="Login")
    self.login_btn.bind(on_press=self.login)

    self.add_widget(Label(text="Username: "))
    self.add_widget(self.username_input)
    self.add_widget(Label(text="Password: "))
    self.add_widget(self.password_input)

  def login(self, instance):
    print(instance)
    if self.username_input.text != "admin" or self.password_input.text != "password":
      return self.add_widget(Label(text="Login failed."))

    self.add_widget(Label(text="Login success."))


class MyApp(App):
  def build(self):
    return LoginPage()


if __name__ == "__main__":
  my_app = MyApp()
  my_app.run()
