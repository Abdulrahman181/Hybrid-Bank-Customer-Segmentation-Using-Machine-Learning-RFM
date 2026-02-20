# 🏦 Hybrid Bank Customer Segmentation System  
### Machine Learning + RFM-Based Customer Intelligence Pipeline

---

## 📌 Project Overview

This project presents an **end-to-end customer segmentation pipeline** built using a real-world bank transactions dataset.

The goal is to segment customers into meaningful behavioral groups using:

- 🔹 Machine Learning Clustering (KMeans & DBSCAN)
- 🔹 Traditional RFM Analysis (Recency, Frequency, Monetary)
- 🔹 Dimensionality Reduction (PCA)
- 🔹 Business-Driven Interpretation

This hybrid approach combines **data-driven intelligence** with **business interpretability**, making the solution both technically robust and commercially practical.

---

## 🎯 Business Objective

Banks need to:

- Identify high-value customers (VIPs)
- Detect dormant or churn-risk customers
- Understand behavioral spending patterns
- Enable targeted marketing campaigns
- Reduce customer attrition

This project delivers a scalable segmentation system to achieve these goals.

---

## 📊 Dataset Overview

The dataset contains:

- 295,000+ transactions
- 280,000+ unique customers
- Demographics (Age, Gender, Location)
- Account balance information
- Transaction amount & timestamps

Each row represents a transaction.

---

## ⚙️ Project Pipeline

### 1️⃣ Data Understanding & Cleaning

- Date conversion & formatting
- Missing value handling
- Age correction & validation
- Gender normalization
- Feature extraction (Hour, ZeroBalanceFlag)

---

### 2️⃣ Feature Engineering

Transactions were aggregated at the **customer level**, generating:

- TotalTransactions
- TotalAmount
- AvgTransactionAmount
- AvgAccountBalance
- ZeroBalanceRatio
- Recency
- CustomerLifetimeDays
- Age

This transforms raw transactional data into structured customer behavioral profiles.

---

### 3️⃣ Feature Scaling & Transformation

- Log transformation for skewed financial features
- Median imputation
- Standard scaling
- PCA (95% variance retained)

Original Features: 8  
Reduced Components: 6  

This ensures stability and performance in clustering.

---

## 🤖 Machine Learning Segmentation

### 🔹 KMeans Clustering
- Optimal clusters selected via Elbow Method
- Final model: 4 clusters
- Silhouette Score: ~0.24

### 🔹 DBSCAN
- Density-based clustering
- Better separation score (~0.34)
- Detects noise/outliers

---

## 📈 Cluster Profiling

Clusters were interpreted based on:

- Spending behavior
- Account balance
- Recency
- Age distribution

Example segments:

- 🏆 High-Value Customers
- ⚠ Dormant Customers
- 💸 Low-Balance Risk Group
- 📉 Moderate Activity Segment

---

## 📊 Traditional RFM Segmentation

Customers were also segmented using:

- Recency
- Frequency
- Monetary

Generated:
- R_Score
- F_Score
- M_Score
- RFM Segment Labels (VIP, Loyal, At Risk, Lost, Regular)

---

## ⚖️ ML vs RFM Comparison

| RFM | ML Clustering |
|------|--------------|
| Rule-based | Data-driven |
| Easy to explain | Detects hidden patterns |
| Business friendly | Multi-dimensional |

### Best Practice:
Use RFM for business communication + ML for behavioral discovery.

---

## 📌 Key Insights

- ML segmentation revealed multi-dimensional customer behavior beyond simple monetary value.
- RFM was partially limited due to low transaction frequency variance.
- DBSCAN showed stronger separation quality than KMeans.
- PCA improved clustering stability and reduced noise.

---

## 🚀 Technical Stack

- Python
- Pandas / NumPy
- Seaborn / Matplotlib
- Scikit-learn
- PCA
- KMeans
- DBSCAN

---

## 📂 Project Structure

Bank-Customer-Segmentation/
│

├── Bank_Customer_Segmentation.ipynb

├── bank_transactions.csv

├── README.md


---

## 🧠 Why This Project Matters

This project demonstrates:

✔ End-to-end ML pipeline  
✔ Feature engineering expertise  
✔ Business-driven interpretation  
✔ Multiple clustering techniques  
✔ Model evaluation  
✔ Hybrid segmentation strategy  

It bridges the gap between **technical modeling** and **real-world business application**.

---

## 📈 Future Improvements

- Hyperparameter optimization
- Automated model selection
- Dashboard deployment (Streamlit / Power BI)
- Production pipeline integration
- Churn prediction extension

---

## 👤 Author

**Abdelrahman**  
Data Science & Machine Learning Enthusiast  

---

## ⭐ Final Outcome

A production-ready, scalable customer segmentation system combining traditional business logic with modern machine learning techniques.

---
