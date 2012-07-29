from cx_Freeze import setup
from cx_Freeze import Executable

exe = Executable(
        script="cargador.py",
        base="Win32GUI",
)

setup(
    name="Cargador",
    version="0.1",
    description="Un cargador de juegos",
    executables=[exe],
)
