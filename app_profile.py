# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 13:36:39 2025

@author: mulau
"""

import streamlit as st
import pandas as pd

st.title("Researcher Profile Page")
name = "Musiwalo Samuel Mulaudzi"
field = "Biochemistry"
institution = "University of Johannesburg"

st.header("Researcher Overview")
st.write(f"  Name: {name}") 
st.write(f"  Field of Research:  {field}")
st.write(f" Institution:  {institution}")
st.header("Publications")
uploaded_file = st.file_uploader("Upload a CSV of Publications", type="csv")
if uploaded_file:
    publications = pd.read_csv(uploaded_file)
    st.dataframe(publications)
    keyword = st.text_input("Filter by keyword", "")
    if keyword:
        filtered = publications[
            publications.apply(lambda row: keyword.lower() in row.astype(str).str.lower().values, axis=1)
        ]
        st.write(f"Filtered Results for '{keyword}':")
        st.dataframe(filtered)
    else:
        st.write("Showing all publications")
st.header("Publication Trends")
if uploaded_file:
    if "Year" in publications.columns:
        year_counts = publications["Year"].value_counts().sort_index()
        st.bar_chart(year_counts)
    else:
        st.write("The CSV does not have a 'Year' column to visualize trends.")
st.header("Contact Information")
email = "mulaudzimusiwalo6@gmail.com"
st.write(f"You can reach {name} at {email}.")       