"""
Author: RedFantom
License: GNU GPLv3
Copyright (c) 2017-2018 RedFantom
"""
from ttkthemes._utils import is_python_3
if is_python_3():
    import tkinter as tk
    from tkinter import ttk
else:
    import Tkinter as tk
    import ttk
