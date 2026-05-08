# store-sales-forecasting

📊 Rossmann Store Sales Forecasting System
Project Overview
This project is an end-to-end Machine Learning solution designed to predict daily sales for Rossmann, one of Europe's largest drugstore chains. By leveraging historical data from 1,115 stores, the system provides actionable insights into how promotions, holidays, and store types influence revenue.

✨ Key Features
Big Data Processing: Successfully handled and uploaded over 1 million rows of retail data into a MySQL database.

AI Engine: Powered by the XGBoost Regressor, optimized to understand complex retail patterns and seasonality.

Executive Dashboard: A professional, interactive Streamlit web interface for real-time sales forecasting.

Business Intelligence: Beyond just numbers, the system provides staffing and inventory recommendations based on predicted demand.

🛠️ Tech Stack
Language: Python 3.x

Database: MySQL (Storage & Retrieval)

Machine Learning: XGBoost, Scikit-learn, Pandas, NumPy

Web Framework: Streamlit (Custom HTML/CSS UI)

Database Connectivity: SQLAlchemy, PyMySQL

📂 Project Structure
Plaintext
sales-prediction-system/
├── app/
│   └── main.py              # Streamlit Dashboard (UI)
├── data/
│   ├── train.csv            # Historical Sales Data
│   └── store.csv            # Store Metadata
├── models/
│   └── sales_model.pkl      # Trained XGBoost Model
├── src/
│   ├── database_handler.py  # MySQL Data Upload Pipeline
│   └── model_trainer.py     # ML Training Script
├── requirements.txt         # Project Dependencies
└── README.md                # Documentation
🚀 How to Run
1. Clone the repository

Bash
git clone https://github.com/YourUsername/sales-prediction-system.git
cd sales-prediction-system
2. Install Dependencies

Bash
pip install -r requirements.txt
3. Setup Database & Train Model

Ensure your MySQL server is running.

Update credentials in src/database_handler.py.

Run the pipeline:

Bash
python src/database_handler.py
python src/model_trainer.py
4. Launch Dashboard

Bash
streamlit run app/main.py
📈 Business Impact
Optimized Staffing: Helps managers reduce labor costs on low-volume days.

Inventory Accuracy: Reduces "out-of-stock" scenarios during high-promotion periods.

Strategic Planning: Allows executives to test "What-If" scenarios for future promotions.

🔗 About the Developer
Developed by Swapnali. Feel free to connect for collaborations in Data Science and Machine Learning!

Pro-Tips for GitHub:
Short Description (About section): Use: "An end-to-end retail sales forecasting system using XGBoost, MySQL, and Streamlit to predict daily drugstore revenue with 1.1M+ data points."

Topics/Tags: Add these tags to your repo: machine-learning, python, data-science, sales-forecasting, mysql, streamlit, xgboost.

Screenshot: Take a screenshot of your beautiful new UI and add it to the top of the README!
