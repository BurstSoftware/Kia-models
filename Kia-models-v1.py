import streamlit as st
import pandas as pd

# Page config
st.set_page_config(page_title="Kia Car Models Explorer", layout="wide")

st.title("🚗 Kia Car Models Explorer (2025–2026)")
st.markdown("Browse Kia's latest lineup by category, powertrain, and type.")

# Data
data = [
    # SUVs & Crossovers
    ["Telluride", "SUV", "Gas"],
    ["Sorento", "SUV", "Gas/Hybrid/PHEV"],
    ["Sportage", "SUV", "Gas/Hybrid/PHEV"],
    ["Seltos", "SUV", "Gas"],
    ["Soul", "Crossover", "Gas"],

    # Electric SUVs
    ["EV9", "Electric SUV", "Electric"],
    ["EV6", "Electric Crossover", "Electric"],
    ["EV5", "Electric SUV", "Electric"],
    ["EV3", "Electric SUV", "Electric"],

    # Sedans
    ["K5", "Sedan", "Gas"],
    ["K4", "Sedan", "Gas"],

    # Electric Sedan
    ["EV4", "Electric Sedan", "Electric"],

    # Minivan
    ["Carnival", "Minivan", "Gas/Hybrid"],

    # Electrified
    ["Niro Hybrid", "Crossover", "Hybrid"],
    ["Niro Plug-in Hybrid", "Crossover", "PHEV"],
    ["Niro EV", "Crossover", "Electric"],
]

df = pd.DataFrame(data, columns=["Model", "Category", "Powertrain"])

# Sidebar filters
st.sidebar.header("🔍 Filter Options")

category_filter = st.sidebar.multiselect(
    "Select Category",
    options=df["Category"].unique(),
    default=df["Category"].unique()
)

powertrain_filter = st.sidebar.multiselect(
    "Select Powertrain",
    options=df["Powertrain"].unique(),
    default=df["Powertrain"].unique()
)

# Filter data
filtered_df = df[
    (df["Category"].isin(category_filter)) &
    (df["Powertrain"].isin(powertrain_filter))
]

# Display metrics
st.metric("Total Models", len(filtered_df))

# Table
st.dataframe(filtered_df, use_container_width=True)

# Grouped view
st.subheader("📊 Models by Category")
grouped = filtered_df.groupby("Category")["Model"].apply(list)

for category, models in grouped.items():
    st.markdown(f"### {category}")
    st.write(", ".join(models))

# Search
st.subheader("🔎 Search Model")
search = st.text_input("Type a model name")

if search:
    results = df[df["Model"].str.contains(search, case=False)]
    st.write(results if not results.empty else "No results found.")

# Footer
st.markdown("---")
st.caption("Data based on Kia 2025–2026 global lineup.")
