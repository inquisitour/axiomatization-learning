# introduction.py

import streamlit as st

def render_introduction():
    st.header("Introduction")
    
    st.write("""
    This paper explores teaching causal reasoning to transformers through axiomatic training. 
    The key motivation is to enable AI systems to perform causal reasoning, which is essential for real-world interactions.
    """)
    
    st.subheader("Key Points")
    st.write("""
    1. Causal reasoning is crucial for AI systems interacting with the real world.
    2. The study focuses on learning causal reasoning from passive data.
    3. Axiomatic training involves learning from demonstrations of causal axioms.
    4. The paper investigates whether transformers can generalize from axiom demonstrations to new scenarios.
    5. The approach is based on Pearl's ladder of causation and the axiomatization of causal relevance by Galles and Pearl.
    """)
    
    st.subheader("Research Questions")
    st.write("""
    1. Can transformers learn causal axioms directly from symbolic demonstrations?
    2. How well do axiomatically trained models generalize to unseen, complex causal structures?
    3. How does the performance of axiomatically trained models compare to large language models on causal reasoning tasks?
    """)
    
    st.subheader("Contributions")
    st.write("""
    1. A novel axiomatic training framework for teaching causal reasoning to transformers.
    2. Empirical evidence that small transformers can learn and apply causal axioms.
    3. Demonstration of generalization to complex causal structures not seen during training.
    4. Comparative analysis with large language models on causal reasoning tasks.
    5. Insights into the role of positional encoding and data diversity in causal learning.
    """)

    st.subheader("Background: Pearl's Ladder of Causation")
    st.write("""
    Pearl's ladder of causation defines three levels of causal reasoning:
    
    1. Association (Seeing):
       - Observing correlations and patterns in data
       - Example: P(y|x) - The probability of Y given X
       - Typical question: What does a symptom tell me about disease?
    
    2. Intervention (Doing):
       - Predicting the effects of deliberate actions or interventions
       - Example: P(y|do(x)) - The probability of Y if we intervene to set X to a specific value
       - Typical question: What will happen if I take this drug?
    
    3. Counterfactuals (Imagining):
       - Reasoning about what could have happened under different circumstances
       - Example: P(y_x|x', y') - The probability of Y if X had been x, given that we observed X=x' and Y=y'
       - Typical question: Would I have avoided the disease if I had taken the drug?
    
    This paper focuses on teaching models to reason at the intervention level, which is crucial for understanding cause-and-effect relationships and making informed decisions in real-world scenarios.
    """)