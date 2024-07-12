# discussion.py

import streamlit as st

def render_discussion():
    st.header("Discussion and Conclusion")
    
    st.subheader("Key Findings")
    st.write("""
    1. Transformers can learn causal axioms through axiomatic training.
    2. Models generalize to longer and more complex graph structures not seen during training.
    3. Performance often matches or exceeds larger language models on causal reasoning tasks.
    4. No positional encoding (NoPE) performs best for generalization across different tasks.
    5. Data diversity through edge-level perturbations aids generalization to complex structures.
    """)
    
    st.subheader("Implications")
    st.write("""
    1. Axiomatic training provides a new paradigm for teaching causal reasoning to AI systems.
    2. Small, specialized models can perform competitively with large language models on specific reasoning tasks.
    3. The approach demonstrates the potential for learning abstract reasoning principles from symbolic demonstrations.
    4. The success of NoPE suggests that explicit positional information may hinder generalization in some reasoning tasks.
    """)
    
    st.subheader("Limitations")
    st.write("""
    1. The study focuses primarily on the transitivity axiom; generalization to other axioms needs further investigation.
    2. The approach requires carefully crafted synthetic data, which may not always be feasible for more complex domains.
    3. The model's performance on very large graphs (>15 nodes) or extremely dense networks was not extensively tested.
    4. The approach has not been tested on real-world causal inference problems with noisy or incomplete data.
    """)
    
    st.subheader("Future Directions")
    st.write("""
    1. Extend the axiomatic training approach to other causal axioms and more complex causal reasoning tasks.
    2. Investigate the potential of combining axiomatic training with other learning approaches, such as few-shot learning or meta-learning.
    3. Explore applications of axiomatically trained models in downstream tasks like effect estimation or counterfactual reasoning.
    4. Study the interpretability of axiomatically trained models to understand how they represent and apply causal knowledge.
    5. Investigate the potential of axiomatic training for other forms of abstract reasoning, such as mathematical or logical reasoning.
    """)

    st.subheader("Broader Impact")
    st.write("""
    1. Improved causal reasoning capabilities in AI systems could lead to more reliable decision-making in critical domains like healthcare, policy-making, and scientific research.
    2. The approach demonstrates a way to imbue AI systems with formal reasoning capabilities, which could be extended to other domains requiring rigorous logical thinking.
    3. By showing that smaller, specialized models can perform well on specific reasoning tasks, this work may encourage more efficient and targeted AI development.
    4. The success of axiomatic training highlights the importance of incorporating domain knowledge and formal theories into machine learning approaches.
    """)