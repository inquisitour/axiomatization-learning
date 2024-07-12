# methodology.py

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def render_methodology():
    st.header("Methodology")
    
    st.subheader("Axiomatic Training Approach")
    st.write("""
    The axiomatic training approach involves the following steps:
    1. Express causal axioms as symbolic tuples: ⟨premise, hypothesis, result⟩
    2. Generate synthetic training data based on axiom demonstrations
    3. Train a transformer model on these demonstrations
    4. Evaluate generalization to new scenarios
    """)
    
    st.subheader("Causal Irrelevance Definition")
    st.latex(r"""
    \text{Causal Irrelevance: } (X \not\rightarrow Y |Z) \text{ iff: } P(y|z, do(X) = x) = P(y|z, do(X) = x'), \forall x, x', y, z
    """)
    st.write("This definition forms the basis for the axiomatic approach to causal reasoning.")
    
    st.subheader("Transitivity Axiom")
    st.latex(r"""
    (X \not\rightarrow Y |Z) \Rightarrow (A \not\rightarrow Y |Z) \lor (X \not\rightarrow A|Z) \forall A \notin X \cup Z \cup Y
    """)
    st.write("The transitivity axiom is used as the primary example for axiomatic training in this paper.")
    
    st.subheader("Synthetic Data Generation")
    st.write("""
    Synthetic data is generated based on the transitivity axiom:
    1. Create causal graphs with varying structures (chains, random flipping, etc.)
    2. Generate premise-hypothesis pairs based on the graph structure
    3. Label each pair as True or False based on the axiom
    """)
    
    # Visualization of synthetic data generation
    G = nx.DiGraph()
    G.add_edges_from([('X', 'A'), ('A', 'Y')])
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots()
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold', arrows=True, ax=ax)
    ax.set_title("Example: X → A → Y")
    st.pyplot(fig)
    
    st.write("""
    For the graph above:
    - Premise: "X causes A. A causes Y."
    - Hypothesis: "Does X cause Y?"
    - Label: Yes (True)
    """)
    
    st.subheader("Model Architecture")
    st.write("""
    - 67 million parameter transformer model
    - 12 attention layers, 8 attention heads, 512 embedding dimensions
    - Custom tokenizer for alphanumeric node names
    - Experiments with different positional encodings: None (NoPE), Learnable (LPE), Sinusoidal (SPE)
    """)
    
    st.subheader("Training Procedure")
    st.write("""
    - Loss function: Cross-entropy loss on the binary classification task (Yes/No)
    - Optimizer: AdamW with learning rate 1e-4
    - Training for 100 epochs
    - Batch size: 32
    - Gradient clipping: 1.0
    """)