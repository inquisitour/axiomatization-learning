# models.py

import streamlit as st

def render_models():
    st.header("Model Details")
    
    st.subheader("Transformer Architecture")
    st.write("""
    The model used in this study is based on the GPT-2 architecture with the following specifications:
    - Total parameters: 67 million
    - Number of layers: 12
    - Number of attention heads: 8
    - Embedding dimension: 512
    """)
    
    st.subheader("Tokenizer")
    st.write("""
    A custom tokenizer was developed for this task:
    - Alphanumeric node names are tokenized at the character level
    - Special terms (e.g., 'causes', 'Does', 'cause', 'Yes', 'No') are tokenized at the word level
    - Total vocabulary size: 69 tokens
    """)
    
    st.subheader("Positional Encoding Variants")
    st.write("""
    Three variants of positional encoding were tested:
    1. No Positional Encoding (NoPE): No explicit positional information is added to the input embeddings.
    2. Learnable Positional Encoding (LPE): Trainable position embeddings are added to the input embeddings.
    3. Sinusoidal Positional Encoding (SPE): Fixed sinusoidal functions are used to encode position information.
    """)
    
    st.subheader("Training Details")
    st.write("""
    - Optimizer: AdamW
    - Learning rate: 1e-4
    - Number of epochs: 100
    - Batch size: 32
    - Gradient clipping: 1.0
    - Loss function: Cross-entropy loss for binary classification (Yes/No)
    """)
    
    st.subheader("Baseline Models")
    st.write("""
    Large Language Models used as baselines:
    1. GPT-4 (gpt-4-32k):
       - Developed by OpenAI
       - Estimated parameters: Over 1 trillion
    
    2. Gemini Pro (gemini-pro):
       - Developed by Google
       - Estimated parameters: Not publicly disclosed, but likely in the hundreds of billions
    
    3. Phi-3 (Phi-3-mini-128k-instruct):
       - Developed by Microsoft
       - Parameters: 3.8 billion
    
    These models were evaluated using zero-shot prompting, without any fine-tuning for the causal reasoning tasks.
    """)