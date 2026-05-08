# store-sales-forecasting

📊 Rossmann Store Sales Forecasting System
🚀 Project Overview

This project is an end-to-end Machine Learning solution designed to predict daily sales for Rossmann, one of Europe’s largest drugstore chains.

By leveraging historical data from 1,115 stores (1M+ rows), the system generates accurate forecasts and provides insights into how promotions, holidays, and store types impact revenue.

✨ Key Features
📦 Big Data Processing
Efficiently handled and processed 1M+ rows of retail data using MySQL.
🤖 AI Prediction Engine
Built using XGBoost Regressor to capture complex sales patterns and seasonality.
📊 Interactive Dashboard
Developed a professional UI using Streamlit for real-time predictions.
📈 Business Intelligence Insights
Provides recommendations for:
Staffing optimization
Inventory planning
Promotion strategies
🛠️ Tech Stack
Language: Python 3.x
Database: MySQL
Machine Learning: XGBoost, Scikit-learn
Data Processing: Pandas, NumPy
Web Framework: Streamlit
Database Connectivity: SQLAlchemy, PyMySQL

📂 Project Structure

sales-prediction-system/
├── app/
│   └── main.py              # Streamlit Dashboard (UI)
├── data/
│   ├── train.csv            # Historical Sales Data
│   └── store.csv            # Store Metadata
├── models/
│   └── sales_model.pkl      # Trained ML Model
├── src/
│   ├── database_handler.py  # MySQL Data Pipeline
│   └── model_trainer.py     # Model Training Script
├── requirements.txt         # Dependencies
└── README.md                # Documentation
