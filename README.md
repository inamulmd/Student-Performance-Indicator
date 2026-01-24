
# 🎯 Student Performance Indicator

An **end-to-end Machine Learning project** that predicts students' exam performance based on demographic and academic features. The project includes **data processing, model training, evaluation, and a Flask-based web application** for real-time predictions.

---

## 📌 Problem Statement

Student academic performance depends on multiple factors such as study habits, parental background, and socio-economic conditions. Early prediction of performance helps educators and institutions:

* Identify at-risk students
* Provide timely academic interventions
* Improve overall learning outcomes

This project builds a **machine learning pipeline** to accurately predict student scores and provides a **user-friendly web interface** for real-world usage.

---
## Demo Link :: https://drive.google.com/drive/folders/1bHD559sqKy2LYlZyql985K91C36yGWj9

## 📊 Dataset Information

* **Source:** Kaggle – Student Performance Dataset
* **Records:** ~1000 samples
* **Features:**

  * Gender
  * Race/Ethnicity
  * Parental Level of Education
  * Lunch Type
  * Test Preparation Course
  * Reading Score
  * Writing Score
* **Target Variable:** Math Score

---

## ⚙️ Project Workflow

1. Data Ingestion
2. Data Cleaning & Preprocessing
3. Exploratory Data Analysis (EDA)
4. Feature Engineering
5. Model Training
6. Model Evaluation
7. Model Selection
8. Prediction Pipeline
9. Flask Web Application
10. Deployment

---

## 🏗️ Project Architecture

This project follows a **modular ML pipeline architecture**, ensuring scalability, maintainability, and clean separation of concerns:

* Data Ingestion Module
* Data Transformation Module
* Model Trainer Module
* Prediction Pipeline
* Web Interface Layer

---

## 📂 Project Structure

```
Student-Performance-Indicator/
│
├── artifacts/              # Saved models, preprocessors, datasets
├── notebook/               # EDA and experiments
├── src/
│   ├── components/         # Data ingestion, transformation, training modules
│   ├── pipeline/           # Training & prediction pipelines
│   ├── exception.py        # Custom exception handling
│   └── logger.py           # Logging configuration
│
├── templates/              # HTML templates (Flask UI)
├── application.py          # Flask app configuration
├── app.py                  # Entry point
├── requirements.txt        # Dependencies
├── setup.py                # Package setup
└── README.md
```

---

## 🛠️ Tech Stack

* **Python**
* **NumPy** – Numerical computation
* **Pandas** – Data manipulation
* **Scikit-learn** – Machine learning models
* **Matplotlib / Seaborn** – Visualization
* **Flask** – Web framework
* **HTML / CSS** – Frontend

---

## 🤖 Machine Learning Models Used

* Linear Regression
* Decision Tree
* Random Forest
* Gradient Boosting
* CatBoost
* XGBoost
* K-Nearest Neighbors (KNN)
* Support Vector Machine (SVM)

**Best Model Selected:** Gradient Boosting / Random Forest (based on evaluation metrics)

---

## 📈 Model Performance

* **R² Score:** ~0.88 – 0.92
* **RMSE:** Low error rate

The model demonstrates **high predictive accuracy and robustness**.

---

## 🖥️ Web Application Preview

The project includes a **Flask-based web application** where users can input student data and instantly receive predicted exam scores.

**Features:**

* Clean UI
* Real-time predictions
* Easy input form

---

## 🚀 How To Run Locally

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/inamulmd/Student-Performance-Indicator.git
```

### 2️⃣ Navigate to Project Directory

```bash
cd Student-Performance-Indicator
```

### 3️⃣ Create Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate   # Windows
source venv/bin/activate # Linux/Mac
```

### 4️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 5️⃣ Run the Application

```bash
python app.py
```

### 6️⃣ Open Browser

```
http://127.0.0.1:5000
```

---

## 🌍 Deployment

* Flask web application
* Deployable on **AWS / Heroku / Render / Railway**

---

## 📌 Future Improvements

* Hyperparameter tuning
* Deep Learning models
* Docker containerization
* CI/CD pipeline
* Cloud deployment
* Interactive dashboards

---

## 👨‍💻 Author

**Inamul Md**

* 🔗 GitHub: [https://github.com/inamulmd](https://github.com/inamulmd)
* 🔗 LinkedIn: [https://www.linkedin.com/in/inamulmd/](https://www.linkedin.com/in/inamulmd/)

---

## ⭐ Support

If you found this project helpful, please consider giving it a ⭐ — it motivates me to build more high-quality projects!

---


