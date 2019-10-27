import sys
from cx_Freeze import setup, Executable
from tkinter import *
import pandas as pd
from random import randint
from time import time
from time import sleep


base = None
if sys.platform == "win32":
    base = "Win32GUI"
    
executables = [
        Executable("Hangman-beta.py", base=base)
]

buildOptions = dict(
        packages = [],
        includes = [],
        include_files = ["Forca-imagens", "Tabela"],
        excludes = []
)




setup(
    name = "HangMan",
    version = "1.0",
    description = "Criado por Accioly",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
