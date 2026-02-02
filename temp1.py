# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import streamlit as st

# Page configuration
st.set_page_config(
    page_title="Researcher Profile",
    page_icon="📚",
    layout="centered"
)

# Title section
st.title("Dr Linda Mkhize-Manashe")
st.subheader("Education and Technology Researcher")

st.write(
    """
    Welcome to my researcher profile page.  
    This page showcases my research interests, current projects, and academic work.
    """
)

st.divider()

# Research interests
st.header("Research Interests")
st.write(
    """
    • Digital storytelling in education  
    • Multilingual pedagogies and translanguaging  
    • Teaching and learning design in higher education  
    • Educational technology for social justice  
    • Student voices and participatory research
    """
)

st.divider()

# Current projects
st.header("Current Research Projects")
st.write(
    """
    **Enhancing Teaching and Learning Design Through Digital Storytelling and Multilingual Glossaries**  
    This PhD research explores how technology mediated and language responsive pedagogies can improve
    conceptual understanding and inclusive learning in a South African university context.
    """
)

st.divider()

# Publications
st.header("Publications and Academic Work")
st.write(
    """
    • Mkhize-Manashe, L. (2024). Exploring student voices in access to quality higher education.  
    • Mkhize-Manashe, L. (2025). Digital storytelling as a pedagogical tool in multilingual classrooms.  
    """
)

st.caption("Publication list for demonstration purposes")

st.divider()

# Skills and methods
st.header("Research Methods and Skills")
st.write(
    """
    • Mixed methods research  
    • Case study methodology  
    • Qualitative data analysis  
    • Curriculum and courseware design  
    • Use of AI tools in academic research
    """
)

st.divider()

# Contact section
st.header("Contact and Academic Profiles")
st.write(
    """
    📧 Email: your.mkhizelinda@gmail.com  
    🔗 Google Scholar: https://scholar.google.com/citations?user=5-3N5qsAAAAJ&hl=en  
    🔗 ORCID: https://orcid.org/0000-0003-4996-6159  
    🔗 LinkedIn: https://www.linkedin.com/in/linda-mkhize-manashe-00068439a/  
    """
)

st.success("Thank you for visiting my research profile")





