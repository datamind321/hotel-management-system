import cx_Freeze
import os
import sys
base = None

if sys.platform == 'win32':
    base = "Win32GUI"

os.environ['TCL_LIBRARY'] = r"C:\Users\rajsi\AppData\Local\Programs\Python\Python39\tcl\tcl8.6"
os.environ['TK_LIBRARY'] = r"C:\Users\rajsi\AppData\Local\Programs\Python\Python39\tcl\tk8.6"

executables = [cx_Freeze.Executable("Hotel_Management_System.py", base=base, icon="hotel.ico")]


cx_Freeze.setup(
    name = "HOTEL MANAGEMENT SYSTEM",
    options = {"build_exe": {"packages":["tkinter","os"], "include_files":["hotel.ico",'tcl86t.dll','tk86t.dll', 'images','db']}},
    version = "1.0",
    description = "HOTEL MANAGEMENT SOFTWARE| Developed By DataMind Platform",
    executables = executables 
    )

