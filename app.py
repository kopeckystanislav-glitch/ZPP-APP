# -*- coding: utf-8 -*-
import streamlit as st
import pandas as pd
from datetime import datetime

# Načíst data
modules = pd.read_csv('data/modules.csv')  
submodules = pd.read_csv('data/submodules.csv')
checklist_items = pd.read_csv('data/checklist_items.csv')
try:
    reports = pd.read_csv('data/reports.csv')
except FileNotFoundError:
    reports = pd.DataFrame(columns=['report_id','user_email','sub_id','timestamp','notes','photo_url'])

# --- DEBUG: výpis sloupců -------------
st.write("Columns in modules:", modules.columns.tolist())
st.write("Columns in submodules:", submodules.columns.tolist())
# ------------------------------------

# Přihlášení uživatele
st.sidebar.title("Uživatel")
user_email = st.sidebar.text_input("Zadej svůj email:", "")

# Výběr modulu
st.title("Aplikace pro vyšetřovatele požárů")
module_choice = st.radio("Vyber modul:", modules['name'])
module_id = modules.loc[modules['name'] == module_choice, 'module_id'].iloc[0]

# Zobrazení podmodulů
st.header(f"Podmoduly pro {module_choice}")
# Filtrujeme submodules podle module_id
subs = submodules[submodules['module_id'] == module_id]
for _, row in subs.iterrows():
    st.subheader(row['name'])
    if row['type'] == 'info':
        st.info(f"Info sekce pro {row['name']}.")
    elif row['type'] == 'form':
        if st.button(f"Otevřít {row['name']}"):
            if row['name'] == 'Checklist':
                st.write("Zde bude formulář pro Checklist.")
            elif row['name'] == 'Report':
                st.write("Zde bude formulář pro Report.")

