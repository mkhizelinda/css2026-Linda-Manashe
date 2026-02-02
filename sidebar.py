# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:45:12 2026

@author: MKHIZEL
"""

import subprocess

file = "tt.py"

subprocess.Popen(
    ["streamlit","run",file], shell = True
)