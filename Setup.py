import sys
from cx_Freeze import setup, Executable

base = None
if sys.platform == "win32":
    base = "Win32GUI"

setup(
    name="Time_Display",
    version="1.0",
    description="Displays US Timezones",
    executables=[Executable("Time_Display.py", base=base)],)
