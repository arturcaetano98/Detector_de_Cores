import sys
from cx_Freeze import setup, Executable

import numpy
import cv2

base = None
if sys.platform == "win32":
    base = "Win32GUI"

executables = [
        Executable("Detector.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = ["numpy","cv2"],
        include_files = [],
        excludes = []
)

setup(
    name = "Detector de Cores",
    version = "1.1",
    description = "Aplicativo escrito em Python para aula de Inteligencia Artificial",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
