from kivy.lang import Builder
from kivy.properties import ObjectProperty
from .controller import Controller


class Login(Controller):
  username_input = ObjectProperty()
  password_input = ObjectProperty()

  def login(self, app):
    '''
    from mysql.connector import connect
    conn = connect(
      host="localhost",
      user="root",
      password="",
      database="komin"
    )
    c = conn.cursor()

    c.execute("""SELECT * FROM admin""")
    users = c.fetchall()

    for user in users:
      if self.username_input.text == user[1] and self.password_input.text == user[3]:
    '''
    if self.username_input.text == "admin" and self.password_input.text == "123":
        # jika user ditemukan, redirect ke halaman menu
        app.root.to("menu")
        return None

    print("Login failed.")


Builder.load_file("./views/login.kv")
