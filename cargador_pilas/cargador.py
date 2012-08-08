import tkMessageBox
import Tkinter
import imp
import sys
import os

window = Tkinter.Tk()
window.wm_withdraw()

if not os.path.exists('run.py'):
    tkMessageBox.showerror("Error", "No se encuentra el archivo run.py")
    sys.exit(1)

try:
    imp.load_source("__main__", "run.py")
except Exception, e:

    tkMessageBox.showerror("Error", e)
