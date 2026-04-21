### 🏠 House Price Prediction using Machine Learning



### 📌 Project Overview

This project is a Machine Learning-based web application that predicts house prices based on various property features. It demonstrates an end-to-end workflow including data preprocessing, exploratory data analysis (EDA), model training, evaluation, and deployment using Streamlit.



The goal is to build an intelligent system that can estimate house prices accurately using historical housing data.



---



### 🎯 Problem Statement

House prices depend on multiple factors such as area, number of bedrooms, bathrooms, furnishing status, and location-related features. Manual estimation can be inaccurate and inconsistent.



This project aims to:

- Analyze housing data

- Identify key factors affecting price

- Build a predictive machine learning model

- Provide a user-friendly web interface for predictions



---



### 📊 Model Performance



- 🤖 Best Model: Random Forest Regressor 
- 📈 R² Score: 0.6529242642153184
- 📉 Mean Absolute Error (MAE): 970043.403920164



✔ The Random Forest model performed better than Linear Regression by capturing complex non-linear relationships in the dataset.



---



### 🧠 How the Model Works



- The model uses a \*\*Random Forest Regressor\*\*, which is an ensemble of multiple decision trees.

- Each tree predicts a house price independently.

- The final prediction is obtained by averaging all tree outputs.

- This improves accuracy and reduces overfitting.



---



### 📂 Dataset Information

The dataset contains housing attributes such as:



- Area

- Number of bedrooms

- Number of bathrooms

- Stories

- Parking

- Furnishing status

- Air conditioning

- Guestroom

- Basement

- Price (target variable)



---



### ⚙️ Project Workflow



#### 1. Data Collection

- Loaded dataset using Pandas



#### 2. Data Preprocessing

- Handled missing values

- Converted categorical variables using One-Hot Encoding

- Feature selection



#### 3. Exploratory Data Analysis (EDA)

- Visualized relationships between features and price

- Identified key influencing factors



#### 4. Model Training

- Random Forest Regressor

- Trained on processed dataset



#### 5. Model Evaluation

- R² Score

- Mean Absolute Error (MAE)



#### 6. Deployment

- Built interactive web app using Streamlit



---



### 🚀 Streamlit Web App



This project includes an interactive web application where users can input house details and get instant price predictions.



---



### ▶️ How to Run Locally


streamlit run app.py



---



### 🎯 Features



- User-friendly interface

- Real-time predictions

- Dropdowns for categorical inputs

- Numeric inputs for house features



---



### 🛠️ Technologies Used



- Python 🐍

- Pandas \& NumPy

- Scikit-learn

- Matplotlib \& Seaborn

- Streamlit

- Joblib



---



### 📁 Project Structure



house-price-prediction-ml/

│

├── data/                  # Dataset files

├── notebooks/             # Jupyter notebooks

├── images/                # Visualizations

├── src/                   # Python scripts

├── app.py                 # Streamlit application

├── model.pkl             # Trained ML model

├── columns.pkl           # Feature columns

├── requirements.txt

├── README.md



---



### 📈 Key Insights



- House area is the most important factor affecting price

- Furnishing status significantly impacts property value

- Additional features like air conditioning and parking increase price

- Random Forest performs better than Linear Regression for this dataset



---



### 🚀 Future Improvements



- Hyperparameter tuning for better accuracy

- Try advanced models (XGBoost, Gradient Boosting)

- Deploy the Streamlit app online (Streamlit Cloud / Render)

- Add real-time database integration

- Improve UI with advanced design components



---



### 👩‍💻 Author



Methmi Weerathunga

BSc in Data Science.



GitHub: https://github.com/methmi2004



LinkedIn: www.linkedin.com/in/methmi-weerathunga-47a121333



---



### ⭐ Acknowledgements



This project was built as part of my learning journey in Machine Learning and Data Science, focusing on real-world predictive modeling and deployment practices.