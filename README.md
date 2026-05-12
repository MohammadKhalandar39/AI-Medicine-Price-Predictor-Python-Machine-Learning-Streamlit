# 💊 AI Medicine Price Predictor

## 📑 Table of Contents

* [Features](#-features)
* [Technologies Used](#-technologies-used)
* [Installation](#-installation)
* [Usage](#-usage)
* [Important Notes](#-important-notes)
* [Security Warning](#-security-warning)
* [Project Structure](#-project-structure)
* [Future Improvements](#-future-improvements)
* [Project Overview](#-project-overview)
* [Dataset Information](#-dataset-information)
* [Machine Learning Workflow](#-machine-learning-workflow)
* [Exploratory Data Analysis-eda](#-exploratory-data-analysis-eda)
* [Models Used](#-models-used)
* [Streamlit-Web-Application](#-streamlit-web-application)
* [Author](#-author)
* [Support](#-support)

An end-to-end Machine Learning project that predicts the **price category of medicines** using medicine composition, manufacturer, and medicine type.

This project uses a large Indian medicines dataset, multiple ML models, and a Streamlit web application for interactive predictions.

---

# ✨ Features

* AI-powered medicine price category prediction
* Interactive Streamlit web interface
* NLP-based medicine composition analysis
* Multiple machine learning model comparison
* Real-world Indian medicines dataset
* Automated preprocessing pipeline
* Category-based prediction output
* Clean and responsive UI

---

# 🛠️ Technologies Used

## Programming Language

* Python

## Machine Learning

* Scikit-learn
* TF-IDF Vectorizer
* Random Forest
* Gradient Boosting
* Logistic Regression

## Data Analysis

* Pandas
* NumPy
* Matplotlib

## Web Framework

* Streamlit

## Model Storage

* Pickle

---

# 📥 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/medicine-price-predictor.git
cd medicine-price-predictor
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Jupyter Notebook

Train the model and generate:

```bash
best_model.pkl
```

## 4. Run Streamlit Application

```bash
streamlit run app.py
```

---

# ▶️ Usage

1. Open the Streamlit application in your browser.
2. Select the medicine manufacturer.
3. Choose the medicine type.
4. Enter or select the composition.
5. Click the predict button.
6. View the predicted medicine price category.

---

# 📌 Important Notes

* The model predicts only price categories, not exact prices.
* Prediction accuracy depends on dataset quality.
* Ensure the trained model file (`best_model.pkl`) exists before running the app.
* Some medicine compositions may not exist in the training dataset.
* Large datasets may require additional system memory.

---

# 🔐 Security Warning

* Never upload sensitive or private medical records.
* This project is for educational and research purposes only.
* Predictions should not be considered medical or financial advice.
* Avoid exposing trained model files publicly in production environments.
* Always validate user input before deployment.

---

# 📁 Project Structure

```text
medicine-price-predictor/
│
├── Extensive_A_Z_medicines_dataset_of_India.csv
├── medicines predicts ML (1).ipynb
├── app.py
├── best_model.pkl
├── requirements.txt
└── README.md
```

---

# 🚀 Future Improvements

* Deep Learning integration
* Real-time medicine API support
* Exact price prediction using regression
* Cloud deployment support
* User authentication system
* Dashboard analytics
* Multi-language support
* Medicine recommendation engine

---

# 📌 Project Overview

The system analyzes medicine-related information and predicts whether a medicine belongs to a:

* 💰 Low Price Range
* ⚠️ Medium Price Range
* 🔥 High Price Range

The project includes:

* Data Cleaning & Preprocessing
* Exploratory Data Analysis (EDA)
* Feature Engineering
* Machine Learning Model Training
* Model Comparison
* Streamlit Web App Deployment

---

# 📂 Project Files

| File                                           | Description                                                       |
| ---------------------------------------------- | ----------------------------------------------------------------- |
| `Extensive_A_Z_medicines_dataset_of_India.csv` | Main dataset containing Indian medicine details                   |
| `medicines predicts ML (1).ipynb`              | Jupyter Notebook for preprocessing, EDA, training, and evaluation |
| `app (1).py`                                   | Streamlit web application for predictions                         |
| `best_model.pkl`                               | Saved trained machine learning model                              |

---

# 📊 Dataset Information

The dataset contains more than **250,000 medicine records** with features such as:

* Medicine Name
* Manufacturer
* Medicine Type
* Composition
* Side Effects
* Uses
* Therapeutic Class
* Price
* Substitutes

### Dataset Shape

* Rows: ~256,000+
* Columns: 24

---

# ⚙️ Technologies Used

## Programming Language

* Python

## Libraries

* Pandas
* NumPy
* Scikit-learn
* Matplotlib
* Streamlit
* Pickle

---

# 🧠 Machine Learning Workflow

## 1. Data Cleaning

* Removed duplicate records
* Standardized column names
* Converted price column into numeric format
* Handled missing values

## 2. Feature Engineering

Created a new `composition` feature by combining:

* `short_composition1`
* `short_composition2`

Created target variable:

* `price_category`

  * Low
  * Medium
  * High

---

# 📈 Exploratory Data Analysis (EDA)

The notebook includes:

* Price Distribution
* Price Category Distribution
* Average Price by Medicine Type
* Top Manufacturers Analysis
* Smart Insights using GroupBy Analysis

---

# 🤖 Models Used

The following ML models were trained and compared:

| Model                        | Purpose                |
| ---------------------------- | ---------------------- |
| Random Forest Classifier     | Main prediction model  |
| Gradient Boosting Classifier | Performance comparison |
| Logistic Regression          | Baseline model         |

The best-performing model is automatically selected and saved as:

```python
best_model.pkl
```

---

# 🔄 ML Pipeline

The preprocessing pipeline includes:

* OneHotEncoder for categorical features
* TF-IDF Vectorizer for composition text
* ColumnTransformer
* Scikit-learn Pipeline

Features used for prediction:

```python
manufacturer_name
type
composition
```

---

# 🖥️ Streamlit Web Application

The project includes a modern Streamlit interface with:

✅ Sidebar Input Controls
✅ Manufacturer Dropdown
✅ Medicine Type Selection
✅ Composition Selection/Input
✅ Real-Time Predictions
✅ Premium UI Styling

Prediction Output:

* LOW Price Range
* MEDIUM Price Range
* HIGH Price Range

---

# 🚀 How to Run the Project

## 1. Clone Repository

```bash
git clone https://github.com/your-username/medicine-price-predictor.git
cd medicine-price-predictor
```

## 2. Install Dependencies

```bash
pip install -r requirements.txt
```

## 3. Run Jupyter Notebook

Train the model and generate:

```bash
best_model.pkl
```

---

## 4. Run Streamlit App

```bash
streamlit run app.py
```

---

# 📦 Suggested Requirements

Create a `requirements.txt` file with:

```txt
streamlit
pandas
numpy
scikit-learn
matplotlib
```

---

# 📸 Application Features

![image alt](https://github.com/MohammadKhalandar39/AI-Medicine-Price-Predictor-Python-Machine-Learning-Streamlit/blob/ccb5e8bb3f1695cdc0eb0abb67a3783173e31ada/Dashboards/Screenshot%20(31).png)

## User Inputs

* Manufacturer
* Medicine Type
* Composition

## AI Prediction

The model predicts medicine pricing category based on the selected inputs.

---

# 📌 Example Prediction

### Input

* Manufacturer: Sun Pharma
* Type: Tablet
* Composition: Paracetamol + Caffeine

### Output

```text
MEDIUM Price Range
```

---

# 🔮 Future Improvements

Potential upgrades for the project:

* Deep Learning Models
* Medicine Recommendation System
* Price Regression Prediction
* Deployment on Cloud (AWS/Render/Streamlit Cloud)
* User Authentication
* Real-Time API Integration
* Advanced Dashboard Analytics

---

# 🏆 Project Highlights

✅ Large Real-World Dataset
✅ NLP-Based Composition Processing
✅ Multiple ML Algorithms
✅ Interactive Web App
✅ End-to-End AI Workflow

---

# 👨‍💻 Author

Developed as an AI & Machine Learning project using Python, Scikit-learn, and Streamlit.

---

# ⭐ Support

If you like this project:

⭐ Star the repository
🍴 Fork the project
📢 Share with others

