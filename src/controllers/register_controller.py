from kivy.lang import Builder
from kivy.properties import ObjectProperty
from .controller import Controller


class Register(Controller):
  username_input = ObjectProperty()
  password_input = ObjectProperty()

  def register(self):
    print(self.username_input.text)
    print(self.password_input.text)

    # if self.username.text != "admin" or self.password.text != "password":
      # return self.add_widget(Label(text="Login failed."))

    # self.add_widget(Label(text="Register success."))


Builder.load_file("./views/register.kv")
