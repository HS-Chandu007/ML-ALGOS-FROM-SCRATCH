<div align="center">

```
███╗   ███╗██╗         ███████╗██████╗  ██████╗ ███╗   ███╗    ███████╗ ██████╗██████╗  █████╗ ████████╗ ██████╗██╗  ██╗
████╗ ████║██║         ██╔════╝██╔══██╗██╔═══██╗████╗ ████║    ██╔════╝██╔════╝██╔══██╗██╔══██╗╚══██╔══╝██╔════╝██║  ██║
██╔████╔██║██║         █████╗  ██████╔╝██║   ██║██╔████╔██║    ███████╗██║     ██████╔╝███████║   ██║   ██║     ███████║
██║╚██╔╝██║██║         ██╔══╝  ██╔══██╗██║   ██║██║╚██╔╝██║    ╚════██║██║     ██╔══██╗██╔══██║   ██║   ██║     ██╔══██║
██║ ╚═╝ ██║███████╗    ██║     ██║  ██║╚██████╔╝██║ ╚═╝ ██║    ███████║╚██████╗██║  ██║██║  ██║   ██║   ╚██████╗██║  ██║
╚═╝     ╚═╝╚══════╝    ╚═╝     ╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝    ╚══════╝ ╚═════╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝    ╚═════╝╚═╝  ╚═╝
```

# 🧠 ML From Scratch

### *No sklearn. No PyTorch. No shortcuts — just pure Python & NumPy.*

<br>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-Only-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Algorithms](https://img.shields.io/badge/Algorithms-1_and_counting-22c55e?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Actively_Growing-f59e0b?style=for-the-badge)
![License](https://img.shields.io/badge/License-MIT-a855f7?style=for-the-badge)

<br>

> **"The best way to understand an algorithm is to build it with your own hands."**

</div>

---

## ⚡ What Is This?

This is a collection of **Machine Learning algorithms implemented entirely from scratch** — no high-level ML libraries, no `.fit()` magic, no black boxes.

Every algorithm here is:
- 🔢 **Built with pure Python + NumPy only**
- 📐 **Grounded in the math** — gradients, loss functions, and update rules are all coded explicitly
- 📖 **Readable and documented** — written to be understood, not just to run
- 🌱 **Actively growing** — new algorithms added regularly

This repo exists because *calling a library function* and *truly understanding how it works* are two very different things.

---

## 🗺️ Roadmap

> Every algorithm will be implemented from the ground up. Here's the plan:

```
SUPERVISED LEARNING
├── ✅  Linear Regression         — Gradient Descent, MSE Loss
├── 🔜  Logistic Regression       — Sigmoid, Binary Cross-Entropy
├── 🔜  K-Nearest Neighbors       — Euclidean Distance, Majority Voting
├── 🔜  Decision Trees            — Gini Impurity, Information Gain
├── 🔜  Naive Bayes               — Bayes Theorem, Gaussian Likelihood
├── 🔜  Support Vector Machine    — Hinge Loss, Kernel Trick
├── 🔜  Random Forest             — Bagging, Feature Sampling
└── 🔜  Gradient Boosting         — Residual Fitting, Weak Learners

UNSUPERVISED LEARNING
└── 🔜  K-Means Clustering        — Centroid Init, Inertia, Elbow Method
```

---

## 📦 Algorithms

| Algorithm | Status | Concepts Covered |
|-----------|--------|-----------------|
| [Linear Regression](./linear_regression/) | ✅ Done | Gradient Descent, MSE, Vectorized Gradients |
| Logistic Regression | 🔜 Soon | Sigmoid, Cross-Entropy |
| K-Nearest Neighbors | 🔜 Soon | Distance Metrics, Voting |
| Decision Tree | 🔜 Soon | Gini, Info Gain, Splitting |
| Naive Bayes | 🔜 Soon | Bayes Theorem, Likelihood |
| SVM | 🔜 Soon | Hinge Loss, Hyperplane |
| Random Forest | 🔜 Soon | Ensembling, Bagging |
| K-Means | 🔜 Soon | Clustering, Centroids |

---

## 🏗️ Repo Structure

```
ml-from-scratch/
│
├── 📁 linear_regression/
│   └── linear_regression.py     # Implementation
│
├── 📁 logistic_regression/      # 🔜 Coming soon
├── 📁 knn/                      # 🔜 Coming soon
├── 📁 decision_tree/            # 🔜 Coming soon
├── 📁 naive_bayes/              # 🔜 Coming soon
├── 📁 svm/                      # 🔜 Coming soon
├── 📁 random_forest/            # 🔜 Coming soon
├── 📁 kmeans/                   # 🔜 Coming soon
│
└── README.md
```

Each folder contains the implementation for that algorithm. As the repo grows, each will also include a dedicated README with the math and explanation.

---

## 🚀 Getting Started

**1. Clone the repo**
```bash
git clone https://github.com/yourusername/ml-from-scratch.git
cd ml-from-scratch
```

**2. Install the only dependency**
```bash
pip install numpy
```

**3. Try an algorithm**
```python
import numpy as np
from linear_regression.linear_regression import LinearRegression

model = LinearRegression(learning_rate=0.01, max_iter=1000)
model.fit(X_train, y_train)
predictions = model.predict(X_test)
print(f"MSE: {model.loss(y_test, predictions):.4f}")
```

---

## 🧰 Stack

| | |
|--|--|
| **Language** | Python 3.10+ |
| **Only Library** | NumPy |
| **No** | sklearn, PyTorch, TensorFlow, or any ML framework |

---

## 🎯 Why Build From Scratch?

Most ML courses teach you to use tools. This repo is about understanding what those tools actually do.

When you implement gradient descent by hand, you stop thinking of it as a function call and start thinking of it as a process — one that you can debug, modify, and improve.

That's the whole point.

---

## 📬 Connect

<div align="center">

[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github)]([https://github.com/yourusername](https://github.com/HS-Chandu007))
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin)]([https://linkedin.com/in/yourusername](https://www.linkedin.com/in/chandra-shekhar-b10196329/))

<br>

**If this repo helped you, drop a ⭐ — it keeps the motivation going!**

<br>

---

*Built with curiosity, NumPy, and zero `.fit()` calls from sklearn.*

</div>
