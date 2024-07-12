# data_generation.py

import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt

def render_data_generation():
    st.header("Data Generation")
    
    st.subheader("Synthetic Data Generation Process")
    st.write("""
    The synthetic data generation process involves the following steps:
    1. Generate causal graph structures
    2. Create natural language representations of the graphs
    3. Generate premise-hypothesis pairs
    4. Label the pairs based on the causal axiom
    """)
    
    st.subheader("Graph Generation")
    st.write("""
    1. Linear chains:
       - Create a directed path of length n (3 ≤ n ≤ 6 for training)
    2. Chains with random flipping:
       - Start with a linear chain
       - For each edge, flip its direction with probability 0.5
    3. Branching graphs (for evaluation):
       - Use Erdős-Rényi model to generate random graphs
       - Control density using branching factor (edges / nodes)
    """)
    
    # Visualize different graph types
    fig, (ax1, ax2, ax3) = plt.subplots(1, 3, figsize=(15, 5))
    
    # Linear chain
    G1 = nx.DiGraph([(0,1), (1,2), (2,3)])
    nx.draw(G1, ax=ax1, with_labels=True, node_color='lightblue', node_size=500, arrows=True)
    ax1.set_title("Linear Chain")
    
    # Chain with random flipping
    G2 = nx.DiGraph([(0,1), (2,1), (2,3)])
    nx.draw(G2, ax=ax2, with_labels=True, node_color='lightgreen', node_size=500, arrows=True)
    ax2.set_title("Chain with Random Flipping")
    
    # Branching graph
    G3 = nx.erdos_renyi_graph(5, 0.4, directed=True)
    nx.draw(G3, ax=ax3, with_labels=True, node_color='lightsalmon', node_size=500, arrows=True)
    ax3.set_title("Branching Graph")
    
    st.pyplot(fig)
    
    st.subheader("Natural Language Representation")
    st.write("""
    For each graph:
    1. Assign random alphanumeric names to nodes (1-3 characters for training, 8-10 for node name shift evaluation)
    2. Convert edges to natural language statements (e.g., "A causes B")
    3. Concatenate statements to form the premise
    """)
    
    st.subheader("Premise-Hypothesis Generation")
    st.write("""
    For each graph:
    1. Generate all possible pairs of nodes (X, Y)
    2. Create a hypothesis for each pair: "Does X cause Y?"
    3. Label the hypothesis:
       - "Yes" if there's a directed path from X to Y
       - "No" otherwise
    """)
    
    st.subheader("Data Augmentation Techniques")
    st.write("""
    1. Shuffling:
       - Randomly permute the order of causal statements in the premise
    2. Reversal:
       - Create completely reversed chains by flipping all edges
    3. Length variation:
       - Generate chains of different lengths (3-6 for training, up to 15 for evaluation)
    4. Node name variation:
       - Use different alphanumeric names for nodes across instances
    5. Branching factor variation:
       - For evaluation, create graphs with different branching factors (1.4 and 2.0)
    """)

    st.subheader("Training Data Composition")
    st.write("""
    Three main training datasets were created:
    1. TS1 (Training Set 1):
       - 101,000 sequential chains
       - 73,000 chains with random flipping
       - 12,000 completely reversed chains
    2. TS2 (Training Set 2):
       - 132,000 sequential chains
       - 42,000 chains with random flipping
       - No completely reversed chains
    3. OCC (Only Causal Chains):
       - 175,000 sequential chains
       - No random flipping or reversed chains
    """)

    st.subheader("Evaluation Data")
    st.write("""
    Several evaluation datasets were created to test different aspects of generalization:
    1. Length generalization:
       - Chains of length 7-15
       - Both sequential and randomly flipped
    2. Node name shift:
       - 8-10 character node names
       - Chains of length 3-9
    3. Reversal:
       - Completely reversed chains of length 3-6
    4. Branching:
       - Erdős-Rényi graphs with 5, 8, 10, and 12 nodes
       - Branching factors of 1.4 and 2.0
    5. MultiEval_SLR:
       - Shuffled, randomly flipped chains
       - Lengths up to 9 nodes
    """)

    st.subheader("Example Data Instance")
    st.code("""
    Premise: "A causes B. B causes C. D causes B."
    Hypothesis: "Does A cause C?"
    Label: "Yes"
    """, language="python")

    st.subheader("Data Balance")
    st.write("""
    - All training and evaluation datasets are balanced with equal numbers of "Yes" and "No" instances.
    - This ensures that the model cannot achieve high accuracy by simply guessing one class.
    """)