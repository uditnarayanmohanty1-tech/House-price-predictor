# 🏠 House Price Predictor

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=streamlit&logoColor=white)
![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=for-the-badge&logo=scikit-learn&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=for-the-badge&logo=plotly&logoColor=white)
![Accuracy](https://img.shields.io/badge/Accuracy-95.43%25-brightgreen?style=for-the-badge)

> An ML-powered House Price Predictor that estimates property prices across 10 major Indian cities using Random Forest — built in 1 day as part of my 30-Day AI/ML Challenge!

---

## 🎯 What It Does

- 🏡 Enter house details — area, bedrooms, city, furnishing, age
- 💰 Get **instant price prediction** in ₹
- 📊 See **which factors affect price** the most
- 🌆 Compare prices **across all cities**
- 📐 Get **price per sq ft** breakdown

---

## 🖥️ Results Preview

| Detail | Value |
|--------|-------|
| 🎯 Model Accuracy (R²) | **95.43%** |
| 📊 Algorithm | Random Forest Regressor |
| 🏙️ Cities Covered | 10 Major Indian Cities |
| 🏘️ Training Data | 1000 house records |

### Sample Prediction — Delhi
| | Price |
|--|-------|
| 🏷️ Minimum | ₹8,726,229 |
| 🎯 Predicted | ₹9,695,810 |
| 🏷️ Maximum | ₹10,665,391 |
| 📐 Per sq ft | ₹8,080 |

---

## 🧠 How It Works

```
Enter House Details
        ↓
Label Encoding (City + Furnishing → Numbers)
        ↓
Random Forest Regressor (100 trees)
        ↓
Price Predicted in ₹
        ↓
±10% range shown (Min / Predicted / Max)
        ↓
Feature Importance + City Comparison Charts
```

---

## 🏙️ Cities Covered

| City | Price Level |
|------|------------|
| Mumbai | 🔴 Highest |
| Delhi | 🔴 Very High |
| Bangalore | 🟠 High |
| Hyderabad | 🟠 High |
| Chennai | 🟡 Medium-High |
| Pune | 🟡 Medium |
| Kolkata | 🟢 Medium |
| Jaipur | 🟢 Affordable |
| Ahmedabad | 🟢 Affordable |
| Lucknow | 🟢 Most Affordable |

---

## 🛠️ Tech Stack

| Tool | Purpose |
|------|---------|
| Python | Core language |
| Pandas | Data handling |
| NumPy | Data generation |
| scikit-learn | Random Forest model |
| Plotly | Interactive charts |
| Streamlit | Web interface |

---

## 📊 Features Used in Model

| Feature | Impact |
|---------|--------|
| City | 🔴 Very High |
| Area (sq ft) | 🔴 Very High |
| Furnishing | 🟠 High |
| Bedrooms | 🟡 Medium |
| Age | 🟡 Medium |
| Bathrooms | 🟢 Low-Medium |
| Floor | 🟢 Low |
| Parking | 🟢 Low |

---

## 🚀 How to Run Locally

**1. Clone the repository**
```bash
git clone https://github.com/uditnarayanmohanty1-tech/house-price-predictor.git
cd house-price-predictor
```

**2. Install dependencies**
```bash
pip install streamlit pandas scikit-learn plotly numpy
```

**3. Run the app**
```bash
python -m streamlit run app.py
```

**4. Open in browser**
```
http://localhost:8501
```

---

## 📁 Project Structure

```
house-price-predictor/
│
├── app.py              ← Main application + model + charts
├── requirements.txt    ← Python dependencies
├── .gitignore          ← Git ignore file
└── README.md           ← Project documentation
```

---

## 📅 30-Day AI/ML Challenge

This is **Day 6** of my 30-Day AI/ML Project Challenge!

| Day | Project | Tech |
|-----|---------|------|
| Day 1 | 📱 Spam SMS Detector | Naive Bayes + TF-IDF |
| Day 2 | 🎓 Student Grade Predictor | Linear Regression |
| Day 3 | 🧠 AI Quiz Generator | Groq API + LLaMA 3 |
| Day 4 | 🎬 Movie Recommender | Cosine Similarity |
| Day 5 | 📊 Data Dashboard | Plotly + Streamlit |
| Day 6 | 🏠 House Price Predictor | Random Forest ← You are here |

---

## 👨‍💻 Author

**Udit Narayan Mohanty**
- 🎓 BTech CSE (AI/ML)
- 🐙 GitHub: [@uditnarayanmohanty1-tech](https://github.com/uditnarayanmohanty1-tech)

---

⭐ **Star this repo if you found it helpful!**

> *"Every day is a new project. Every project is a new skill."*
