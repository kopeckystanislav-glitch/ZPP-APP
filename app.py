
import streamlit as st
import pandas as pd

st.set_page_config(page_title="ZPP - Vyšetřovatel požárů", layout="wide")
st.title("🔥 Aplikace pro vyšetřovatele požárů")

# Načtení modulů
try:
    modules = pd.read_csv("modules.csv", sep=";")
except FileNotFoundError:
    st.error("Soubor 'modules.csv' nebyl nalezen.")
    st.stop()

# Zobrazení sloupců pro debug
st.sidebar.header("📁 Sloupce v modules.csv:")
st.sidebar.write(list(modules.columns))

# Kontrola přítomnosti potřebných sloupců
required_columns = {"module_id", "name", "icon", "type"}
if not required_columns.issubset(modules.columns):
    st.error(f"Soubor 'modules.csv' musí obsahovat sloupce: {required_columns}")
    st.stop()

# Výběr modulu
modules["label"] = modules["icon"] + " " + modules["name"]
selected_label = st.radio("🧭 Vyber modul:", modules["label"])

# Zobrazení zvoleného modulu podle module_id
selected_row = modules[modules["label"] == selected_label].iloc[0]
selected_module_id = selected_row["module_id"]

st.success(f"✅ Vybral jsi modul: {selected_row['name']} (ID: {selected_module_id})")

# Pro budoucí rozšíření (např. výběr submodulů nebo formulář)
st.info("Zde může následovat formulář nebo detailní rozpad podle vybraného modulu.")
