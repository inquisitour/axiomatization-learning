# axioms.py

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def render_axioms():
    st.header("Causal Axioms")
    
    st.subheader("Axiomatization of Causal Relevance")
    st.write("""
    The study is based on the axiomatization of causal relevance by Galles and Pearl (1997). 
    Under the stability assumption, causal irrelevance can be completely characterized by six axioms.
    """)
    
    st.subheader("Causal Irrelevance Definition")
    st.latex(r"""
    \text{Causal Irrelevance: } (X \not\rightarrow Y |Z) \text{ iff: } P(y|z, do(X) = x) = P(y|z, do(X) = x'), \forall x, x', y, z
    """)
    st.write("""
    This definition states that X is causally irrelevant to Y given Z if intervening on X does not change the probability of Y, given Z.
    """)
    
    st.subheader("Transitivity Axiom")
    st.latex(r"""
    (X \not\rightarrow Y |Z) \Rightarrow (A \not\rightarrow Y |Z) \lor (X \not\rightarrow A|Z) \forall A \notin X \cup Z \cup Y
    """)
    st.write("""
    The transitivity axiom is the primary focus of this study. It can be interpreted as follows:
    If X does not cause Y given Z, then for any variable A not in X, Y, or Z, either:
    1. A does not cause Y given Z, or
    2. X does not cause A given Z
    """)
    
    # Visualize transitivity
    G = nx.DiGraph()
    G.add_edges_from([('X', 'A'), ('A', 'Y')])
    pos = nx.spring_layout(G)
    fig, ax = plt.subplots(figsize=(8, 6))
    nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=3000, font_size=16, font_weight='bold', arrows=True, ax=ax)
    nx.draw_networkx_edge_labels(G, pos, edge_labels={('X', 'A'): 'causes', ('A', 'Y'): 'causes'}, font_size=14)
    ax.text(0.5, -0.1, "X causes Y (by transitivity)", ha='center', va='center', transform=ax.transAxes, fontsize=14, fontweight='bold')
    st.pyplot(fig)
    
    st.subheader("Other Axioms")
    st.write("""
    While not the focus of this study, the complete axiomatization includes five other axioms:
    1. Symmetry
    2. Decomposition
    3. Weak Union
    4. Contraction
    5. Weak Transitivity
    
    These axioms, together with transitivity, completely characterize causal irrelevance in stable causal models.
    """)
    
    st.subheader("Axiomatic Training Approach")
    st.write("""
    The study's novel contribution is the axiomatic training approach:
    1. Express causal axioms as symbolic tuples: ⟨premise, hypothesis, result⟩
    2. Generate synthetic data based on axiom demonstrations
    3. Train a transformer model on these demonstrations
    4. Evaluate the model's ability to apply the axiom to new, unseen causal structures
    
    This approach allows the model to learn causal reasoning principles directly from symbolic representations, 
    rather than inferring them from observational or interventional data.
    """)
    
    st.subheader("Extending to Other Axioms")
    st.write("""
    While this study focuses on the transitivity axiom, the axiomatic training approach could potentially be extended to other causal axioms:
    1. Generate synthetic data demonstrating each axiom
    2. Train models on individual axioms or combinations of axioms
    3. Evaluate the models' ability to perform more complex causal reasoning tasks
    
    This extension could lead to AI systems with a more complete understanding of causal principles, 
    enabling more sophisticated causal inference and decision-making capabilities.
    """)