import pilas
import tkMessageBox
import Tkinter
import imp

try:
    imp.load_source("__main__", "run.py")
except Exception, e:
    root = Tkinter.Tk()
    root.withdraw()

    MENSAJE_ERROR = "Lo siento, no se encuentra el archivo run.py"
    tkMessageBox.showerror("Error", e)
