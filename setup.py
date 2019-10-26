import sys
from cx_Freeze import setup, Executable
from tkinter import *
import pandas as pd
from random import randint
from time import time
from time import sleep



executables = [
        Executable("Hangman-beta.py", base=None)
]

buildOptions = dict(
        packages = [],
        includes = ["tkinter","pandas", "time", "random"],
        include_files = [],
        excludes = []
)




setup(
    name = "HangMan",
    version = "1.0",
    description = "Criado por Accioly",
    options = dict(build_exe = buildOptions),
    executables = executables
 )
