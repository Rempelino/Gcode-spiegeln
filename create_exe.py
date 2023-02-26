import os
ROOT_DIR = os.path.dirname(os.path.abspath(__file__)) # This is your Project Root
os.system('start /wait cmd /c "cd {} & pyinstaller --onefile main.py"'.format(ROOT_DIR))
print('FERTIG')