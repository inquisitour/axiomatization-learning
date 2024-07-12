# results.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def render_results():
    st.header("Results")
    
    st.subheader("Length Generalization")
    length_data = pd.DataFrame({
        "Length": [7, 8, 9, 10, 11, 12, 13, 14, 15],
        "TS2 NoPE": [1.00, 0.99, 0.92, 0.88, 0.86, 0.95, 0.96, 0.81, 0.85],
        "GPT-4": [0.95, 0.97, 0.87, 0.91, 0.90, 0.92, 0.85, 0.93, 0.89],
        "Gemini Pro": [0.63, 0.69, 0.64, 0.65, 0.72, 0.60, 0.59, 0.67, 0.61],
        "Phi-3": [0.81, 0.96, 0.85, 0.87, 0.90, 0.84, 0.91, 0.90, 0.78]
    })
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for model in ["TS2 NoPE", "GPT-4", "Gemini Pro", "Phi-3"]:
        ax.plot(length_data["Length"], length_data[model], marker='o', label=model)
    ax.set_xlabel("Chain Length")
    ax.set_ylabel("Accuracy")
    ax.set_title("Length Generalization Performance")
    ax.legend()
    st.pyplot(fig)
    
    st.write("""
    Key observations:
    1. TS2 NoPE model performs competitively with GPT-4, especially for chains of length 7-13.
    2. TS2 NoPE significantly outperforms Gemini Pro and Phi-3 across all lengths.
    3. Performance of TS2 NoPE decreases slightly for very long chains (14-15), but remains high.
    """)
    
    st.subheader("Reversal Generalization")
    reversal_data = pd.DataFrame({
        "Length": [3, 4, 5, 6],
        "TS2 NoPE": [0.99, 0.99, 0.95, 0.94],
        "GPT-4": [0.97, 0.99, 0.98, 0.92],
        "Gemini Pro": [0.61, 0.59, 0.66, 0.62],
        "Phi-3": [0.80, 0.69, 0.73, 0.69]
    })
    
    fig, ax = plt.subplots(figsize=(10, 6))
    for model in ["TS2 NoPE", "GPT-4", "Gemini Pro", "Phi-3"]:
        ax.plot(reversal_data["Length"], reversal_data[model], marker='o', label=model)
    ax.set_xlabel("Chain Length")
    ax.set_ylabel("Accuracy")
    ax.set_title("Reversal Generalization Performance")
    ax.legend()
    st.pyplot(fig)
    
    st.write("""
    Key observations:
    1. TS2 NoPE performs on par with or better than GPT-4 for reversed chains.
    2. TS2 NoPE significantly outperforms Gemini Pro and Phi-3 on this task.
    3. Performance remains high even for longer reversed chains.
    """)
    
    st.subheader("Branching Generalization")
    branching_data = pd.DataFrame({
        "Nodes": [5, 8, 10, 12],
        "TS2 NoPE (BF=1.4)": [0.86, 0.77, 0.74, 0.70],
        "TS2 NoPE (BF=2.0)": [0.83, 0.74, 0.69, 0.64],
        "GPT-4 (BF=1.4)": [0.95, 0.90, 0.88, 0.86],
        "GPT-4 (BF=2.0)": [0.98, 0.91, 0.84, 0.82],
        "Gemini Pro (BF=1.4)": [0.74, 0.76, 0.73, 0.71],
        "Gemini Pro (BF=2.0)": [0.77, 0.72, 0.71, 0.73]
    })
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for model in branching_data.columns[1:]:
        ax.plot(branching_data["Nodes"], branching_data[model], marker='o', label=model)
    ax.set_xlabel("Number of Nodes")
    ax.set_ylabel("Accuracy")
    ax.set_title("Branching Generalization Performance")
    ax.legend()
    st.pyplot(fig)
    
    st.write("""
    Key observations:
    1. TS2 NoPE performs well on branched graphs, despite being trained only on simple chains.
    2. Performance decreases with increasing graph size and branching factor, but remains significantly above random (50%).
    3. GPT-4 outperforms TS2 NoPE on this task, but TS2 NoPE is competitive with or better than Gemini Pro.
    """)
    
    st.subheader("Node Name Generalization")
    node_name_data = pd.DataFrame({
        "Length": [3, 4, 5, 6, 7, 8, 9],
        "TS2 NoPE": [1.00, 0.95, 0.87, 0.84, 0.79, 0.76, 0.73],
        "GPT-4": [0.99, 0.97, 0.89, 0.85, 0.95, 0.90, 0.90],
        "Gemini Pro": [0.75, 0.73, 0.72, 0.76, 0.71, 0.68, 0.74],
        "Phi-3": [0.88, 0.86, 0.82, 0.79, 0.76, 0.73, 0.79]
    })
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for model in ["TS2 NoPE", "GPT-4", "Gemini Pro", "Phi-3"]:
        ax.plot(node_name_data["Length"], node_name_data[model], marker='o', label=model)
    ax.set_xlabel("Chain Length")
    ax.set_ylabel("Accuracy")
    ax.set_title("Node Name Generalization Performance")
    ax.legend()
    st.pyplot(fig)
    
    st.write("""
    Key observations:
    1. TS2 NoPE shows robust performance when generalizing to longer node names.
    2. Performance is comparable to GPT-4 for shorter chains and outperforms Gemini Pro and Phi-3.
    3. There's a slight decrease in performance for longer chains, but it remains significantly above random.
    """)
    
    st.subheader("Impact of Positional Encoding")
    pe_data = pd.DataFrame({
        "Length": [7, 8, 9, 10, 11, 12, 13, 14, 15],
        "NoPE": [1.00, 0.99, 0.92, 0.88, 0.86, 0.95, 0.96, 0.81, 0.85],
        "LPE": [0.98, 0.92, 0.77, 0.59, 0.57, 0.57, 0.55, 0.51, 0.50],
        "SPE": [0.99, 0.95, 0.86, 0.80, 0.76, 0.84, 0.79, 0.85, 0.77]
    })
    
    fig, ax = plt.subplots(figsize=(12, 6))
    for pe in ["NoPE", "LPE", "SPE"]:
        ax.plot(pe_data["Length"], pe_data[pe], marker='o', label=pe)
    ax.set_xlabel("Chain Length")
    ax.set_ylabel("Accuracy")
    ax.set_title("Impact of Positional Encoding on Length Generalization")
    ax.legend()
    st.pyplot(fig)
    
    st.write("""
    Key observations:
    1. No Positional Encoding (NoPE) shows the best generalization to longer sequences.
    2. Learnable Positional Encoding (LPE) performs well for lengths seen during training but fails to generalize to longer sequences.
    3. Sinusoidal Positional Encoding (SPE) shows better generalization than LPE but still underperforms compared to NoPE.
    """)
    
    st.subheader("Correlation to Causation Task")
    corr_cause_data = pd.DataFrame({
        "Model": ["Ours", "GPT-4", "Gemini Pro", "Phi-3"],
        "Precision": [0.72, 0.59, 0.52, 0.52],
        "Recall": [0.50, 0.50, 0.59, 0.60],
        "F1 Score": [0.59, 0.54, 0.55, 0.56],
        "Accuracy": [0.64, 0.58, 0.52, 0.52]
    })
    
    st.table(corr_cause_data)
    
    st.write("""
    Key observations:
    1. Our axiomatic training approach outperforms larger language models on this task.
    2. The model shows a good balance between precision and recall.
    3. The performance demonstrates the effectiveness of axiomatic training for more complex causal reasoning tasks.
    """)