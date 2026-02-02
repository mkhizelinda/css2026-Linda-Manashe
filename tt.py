# -*- coding: utf-8 -*-
"""
Created on Mon Feb  2 14:41:45 2026

@author: MKHIZEL
"""

import streamlit as st
import pandas as pd
import numpy as np

st.sidebar.title("Menu")
menue = st.sidebar.radio("Menu:", ["My Profile","Publication","Contact"])