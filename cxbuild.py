import sys
from cx_Freeze import setup, Executable

buildOptions = dict(include_files = ['Penalty-Kick/', 'Archery/', 'Race_Game/', 'Support/', 'images/', 'music/', 'assets/', 'fonts/'])
setup(
         name = "Video Game Design",
         version = "1.0",
         description = "TSA 2018",
         author = "TJHSST TSA",
         options = dict(build_exe = buildOptions),
         executables = [Executable("main.py", base=None)])