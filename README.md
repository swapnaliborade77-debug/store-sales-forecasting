# 📊 Rossmann Store Sales Forecasting System 🚀

![Python](https://img.shields.io/badge/Python-3.9+-blue.svg)
![Streamlit](https://img.shields.io/badge/Frontend-Streamlit-red.svg)
![MySQL](https://img.shields.io/badge/Database-MySQL-orange.svg)
![XGBoost](https://img.shields.io/badge/ML-XGBoost-green.svg)

## 📌 Project Overview
This is an end-to-end Machine Learning solution designed to predict daily sales for **Rossmann**, one of Europe’s largest drugstore chains. By analyzing historical data from 1,115 stores (over 1M rows), the system generates accurate forecasts to help store managers plan ahead.

> **The Problem:** Rossmann store managers are tasked with predicting daily sales up to six weeks in advance. Store sales are influenced by many factors, including promotions, competition, school and state holidays, seasonality, and locality.

---

## ✨ Key Features
* **📦 Big Data Pipeline:** Efficiently handles 1M+ rows of retail data using **MySQL** for structured storage and retrieval.
* **🤖 AI Prediction Engine:** Powered by the **XGBoost Regressor**, capturing complex non-linear patterns like seasonality and holiday trends.
* **📊 Interactive Dashboard:** A **Streamlit** web interface that allows users to input store parameters and receive instant sales predictions.
* **📉 Insight-Driven:** Analyzes the impact of promotions and competition distance on total revenue.

---

## 🛠️ Tech Stack
| Category | Technology |
| :--- | :--- |
| **Language** | Python 3.10+ |
| **Database** | MySQL |
| **Machine Learning** | XGBoost, Scikit-learn |
| **Data Processing** | Pandas, NumPy |
| **Web Framework** | Streamlit |
| **ORM/Connectivity** | SQLAlchemy, PyMySQL |

---

## 📂 Project Structure
```text
sales-prediction-system/
├── app/
│   └── main.py              # Streamlit Dashboard (UI)
├── data/
│   ├── train.csv            # Historical Sales Data (raw)
│   └── store.csv            # Store Metadata
├── models/
│   └── sales_model.pkl      # Trained XGBoost Model
├── src/
│   ├── database_handler.py  # MySQL Data Pipeline & Queries
│   └── model_trainer.py     # Model Training & Evaluation Script
├── requirements.txt         # Project Dependencies
└── README.md                # Project Documentation
