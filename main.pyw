import os

import config
import gui
import password_manager as pwm

if not os.path.exists(config.PASSWORD_FILE):
    with open(config.PASSWORD_FILE, "w") as f:
        f.write("website,username,password")

gui = gui.Gui(password_manager=pwm.PasswordManager())
gui.display()
