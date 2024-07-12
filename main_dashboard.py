# main_dashboard.py

import streamlit as st
from introduction import render_introduction
from methodology import render_methodology
from experiments import render_experiments
from results import render_results
from discussion import render_discussion
from models import render_models
from data_generation import render_data_generation
from axioms import render_axioms

st.set_page_config(page_title="axiomatization-learning", layout="wide")

st.title("Teaching Transformers Causal Reasoning through Axiomatic Training")

# Enhanced author display with dark theme compatibility
st.markdown("""
<div style="background-color: #2c3e50; padding: 10px; border-radius: 5px; margin-bottom: 20px;">
    <h3 style="text-align: center; color: #3498db;">Authors</h3>
    <div style="display: flex; justify-content: space-around; flex-wrap: wrap;">
        <div style="text-align: center; margin: 10px; color: #ecf0f1;">
            <strong>Aniket Vashishtha</strong><br>Microsoft Research, India
        </div>
        <div style="text-align: center; margin: 10px; color: #ecf0f1;">
            <strong>Abhinav Kumar</strong><br>Massachusetts Institute of Technology, USA
        </div>
        <div style="text-align: center; margin: 10px; color: #ecf0f1;">
            <strong>Abbavaram Gowtham Reddy</strong><br>IIT Hyderabad, India
        </div>
        <div style="text-align: center; margin: 10px; color: #ecf0f1;">
            <strong>Vineeth N Balasubramanian</strong><br>IIT Hyderabad, India
        </div>
        <div style="text-align: center; margin: 10px; color: #ecf0f1;">
            <strong>Amit Sharma</strong><br>Microsoft Research, India
        </div>
    </div>
</div>
""", unsafe_allow_html=True)

sections = {
    "Introduction": render_introduction,
    "Methodology": render_methodology,
    "Experiments": render_experiments,
    "Results": render_results,
    "Discussion": render_discussion,
    "Model Details": render_models,
    "Data Generation": render_data_generation,
    "Causal Axioms": render_axioms
}

section = st.sidebar.radio("Navigate to:", list(sections.keys()))
sections[section]()

st.markdown("---")
st.write("Dashboard created based on the paper by Vashishtha et al., 2024")