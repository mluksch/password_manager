import gui
import password_manager as pwm

gui = gui.Gui(password_manager=pwm.PasswordManager())

m = pwm.PasswordManager()
m.upsert_entry("https://google.com", "123")
m.delete_entry("https://amazon.de")
gui.display()
