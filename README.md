# Causal Reasoning Through Axiomatic Training: Interactive Dashboard

<p align="center">
[![Python](https://img.shields.io/badge/Python-3.7%2B-blue)](https://www.python.org/downloads/)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0%2B-FF4B4B)](https://streamlit.io/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0%2B-orange)](https://matplotlib.org/)
[![Pandas](https://img.shields.io/badge/Pandas-1.0%2B-150458)](https://pandas.pydata.org/)
[![NetworkX](https://img.shields.io/badge/NetworkX-2.0%2B-yellow)](https://networkx.org/)
[![Maintenance](https://img.shields.io/badge/Maintained%3F-yes-green.svg)](https://GitHub.com/Naereen/StrapDown.js/graphs/commit-activity)
</p>

This repository contains an interactive dashboard for the paper "Teaching Transformers Causal Reasoning through Axiomatic Training" by Vashishtha et al. (2024). Explore key findings on how transformers learn causal axioms, generalize to complex structures, and compare with large language models.

## 🚀 Features

- **Interactive Sections**: Navigate through Introduction, Methodology, Experiments, Results, and more.
- **Visualizations**: Explore graphs and charts illustrating key findings.
- **Comparative Analysis**: See how axiomatic training compares to large language models.
- **Causal Axioms**: Deep dive into the transitivity axiom and its applications.

## 📁 Project Structure

```
axiomatization-learning/
│
├── main_dashboard.py
├── introduction.py
├── methodology.py
├── experiments.py
├── results.py
├── discussion.py
├── models.py
├── data_generation.py
├── axioms.py
└── requirements.txt
```

## 🛠️ Installation

1. Clone this repository:
   ```
   git clone https://github.com/inquisitour/axiomatization-learning.git
   cd axiomatization-learning
   ```

2. Install the required packages:
   ```
   pip install -r requirements.txt
   ```

## 🖥️ Usage

Run the dashboard using Streamlit:

```
streamlit run main_dashboard.py
```

Navigate through different sections using the sidebar to explore various aspects of the paper.

## 📊 Dashboard Sections

- **Introduction**: Overview of the paper and key research questions.
- **Methodology**: Details on axiomatic training and model architecture.
- **Experiments**: Training datasets and evaluation setups.
- **Results**: Performance comparisons and generalization capabilities.
- **Discussion**: Key findings, implications, and future directions.
- **Model Details**: In-depth look at the transformer architecture used.
- **Data Generation**: Insights into synthetic data creation for training.
- **Causal Axioms**: Exploration of causal irrelevance and the transitivity axiom.

## 📚 Citation

If you use this dashboard in your research, please cite the original paper:

```bibtex
@article{vashishtha2024teaching,
  title={Teaching Transformers Causal Reasoning through Axiomatic Training},
  author={Vashishtha, Aniket and Kumar, Abhinav and Reddy, Abbavaram Gowtham and Balasubramanian, Vineeth N and Sharma, Amit},
  journal={arXiv preprint arXiv:2407.07612},
  year={2024}
}
```

## 📧 Contact

For any queries, please open an issue or contact [deshmukhpratik931@gmail.com](deshmukhpratik931@gmail.com).

---

Happy exploring! 🎉 Dive into the world of causal reasoning and transformer models with our interactive dashboard.
