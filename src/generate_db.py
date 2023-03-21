from mysql.connector import connect

conn = connect(
  host="localhost",
  user="root",
  password=""
)
c = conn.cursor()

c.execute("CREATE DATABASE IF NOT EXISTS kivy")
c.execute("USE kivy")

c.execute("""CREATE TABLE IF NOT EXISTS users(
  id       SMALLINT NOT NULL PRIMARY KEY AUTO_INCREMENT,
  name     VARCHAR(100),
  password VARCHAR(255)
)""")

c.execute("INSERT INTO users (name, password) VALUES ('admin', '123')")

conn.commit()
