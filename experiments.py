# experiments.py

import streamlit as st
import pandas as pd

def render_experiments():
    st.header("Experiments")
    
    st.subheader("Training Datasets")
    training_data = pd.DataFrame({
        "Setup": ["TS1", "TS2", "OCC"],
        "Sequential Chains": [101000, 132000, 175000],
        "Random Flipping": [73000, 42000, 0],
        "Completely Reversed": [12000, 0, 0],
        "Total Instances": [175000, 175000, 175000]
    })
    st.table(training_data)
    st.write("""
    - TS1: Balanced mix of sequential and randomly flipped chains
    - TS2: More sequential chains, fewer randomly flipped chains
    - OCC: Only sequential chains (Only Causal Chains)
    """)
    
    st.subheader("Evaluation Datasets")
    st.write("""
    1. Length Generalization:
       - Chains of length 7-15 (training only used 3-6)
       - Both sequential and randomly flipped chains
    
    2. Node Name Shift:
       - 8-10 character names (vs 1-3 in training)
       - Tests robustness to changes in variable representation
    
    3. Order of Causal Sequences:
       - Completely reversed chains
       - Shuffled sequences
       - Tests understanding of causal direction
    
    4. Branching:
       - Erdos-Renyi graphs with varying branching factors (1.4 and 2.0)
       - Tests generalization to complex graph structures
       - Graph sizes: 5, 8, 10, 12 nodes
    """)
    
    st.subheader("Data Perturbation Techniques")
    st.write("""
    1. Node names:
       - 1-3 character alphanumeric names in training
       - Randomly generated for each instance
    
    2. Causal Graph Topology:
       - Sequential: All edges point forward (e.g., X → Y → Z)
       - Random Flipping: Some edges randomly reversed (e.g., X → Y ← Z)
    
    3. Length:
       - 3-6 nodes in training set
       - Varied to test length generalization
    """)
    
    st.subheader("Baseline Models")
    st.write("""
    Large Language Models used as baselines:
    1. GPT-4 (gpt-4-32k)
    2. Gemini Pro (gemini-pro)
    3. Phi-3 (Phi-3-mini-128k-instruct)
    
    These models were evaluated using zero-shot prompting.
    """)
    
    st.subheader("Evaluation Metrics")
    st.write("""
    - Accuracy: Proportion of correct predictions
    - F1 Score: Harmonic mean of precision and recall
    - Precision: True positives / (True positives + False positives)
    - Recall: True positives / (True positives + False negatives)
    """)