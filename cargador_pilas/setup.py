from cx_Freeze import setup
from cx_Freeze import Executable

exe = Executable(
        script="cargador.py",
        base="Win32GUI",

        compress = True,
        copyDependentFiles = True,
        appendScriptToExe = False,
        appendScriptToLibrary = False,
)

extra_options = {
    "packages": ["pilas"],
    "optimize" : 2,
    "compressed":True,
}

setup(
    name="Cargador",
    version="0.1",
    options = {"build_exe": extra_options},
    description="Un cargador de juegos",
    executables=[exe],
)
