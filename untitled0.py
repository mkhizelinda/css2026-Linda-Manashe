# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 11:02:37 2026

@author: MKHIZEL
"""

import subprocess

#file = "temp1.py"
file = "untitled1.py"
subprocess.Popen(
    ["streamlit","run",file],shell=True
)