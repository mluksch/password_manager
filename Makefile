build: main.pyw gui.py config.py password_manager.py
	pyinstaller --name=Pass --clean --onefile --icon=password.ico .\main.pyw