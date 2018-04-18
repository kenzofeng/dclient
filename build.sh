#on windows
pyinstaller --add-binary venv/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll;PyQt5/Qt/plugins/style
s/  -F  main.py
#on linux or mac
pyinstaller --add-binary venv/Lib/site-packages/PyQt5/Qt/plugins/styles/qwindowsvistastyle.dll:PyQt5/Qt/plugins/style
s/  -F  main.py