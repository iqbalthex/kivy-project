from kivy.app import App
from kivy.uix.widget import Widget
from kivy.lang import Builder

Builder.load_file("../layout/login.kv")

class LoginPage(Widget):
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
