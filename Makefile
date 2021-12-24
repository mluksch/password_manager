build: main.pyw gui.py config.py password_manager.py
	pipenv install -d appdirs pandas && pyinstaller --name=Pass --clean --onefile --paths=venv/Lib/site-packages --icon=password.ico .\main.pyw