# Disease Prediction System

A Beginner-Friendly Python Project (Without Pandas/Scikit-Learn)

# Overview

This project is a simple, rule-based Disease Prediction System built using pure Python.
Instead of using machine-learning libraries (like Pandas, NumPy, or Scikit-Learn), this project uses a structured symptoms-database and logical matching to predict possible diseases.

It’s perfect for 1st-year engineering students, Python beginners, or anyone learning how to design a real-world mini-project.


---

# Features

 Predicts diseases based on user-entered symptoms

 Rule-based logic (no external libraries required)

 Clean & modular Python code

 Supports multiple symptoms

 Beginner-friendly

 Ready for college project submission



---

# Project Structure

Disease-Prediction/
│── data/
│   └── symptoms_db.py        # Symptom-disease dataset
│
│── src/
│   ├── predictor.py          # Core prediction logic
│   └── main.py               # User interface (CLI)
│
│── docs/
│   └── Project_Report.pdf    # Full report (auto-generated)
│
│── README.md                 # This file


---

# How It Works

1. User enters symptoms

Example:

["fever", "headache", "fatigue"]

2. The system compares these symptoms

…with the predefined database of diseases (stored in symptoms_db.py).

3. A match score is calculated

The disease with the highest similarity score is selected.

4. The predicted disease is displayed

With probability and possible causes.


---

# Installation

No special modules required — only Python.

Step 1: Clone Repository

git clone https://github.com/YOUR-USERNAME/disease-prediction.git
cd disease-prediction

Step 2: Run the Program

python src/main.py


---

# Example Output

Enter symptoms (comma separated): fever, cough, tiredness

Most Probable Disease: Influenza (Flu)

Matching Symptoms: 3/4
Confidence Level: 75%

Recommended Action:
- Rest and hydration
- Paracetamol for fever
- Seek medical help if symptoms persist


---

# Customization

You can easily extend the system:

# Add more diseases

Open:

data/symptoms_db.py

Add:

"dengue": ["fever", "rash", "vomiting", "joint pain"],

# Add a GUI (Tkinter)

Future versions may include a user interface.


---

# Future Enhancements

AI/ML model using scikit-learn

GUI using Tkinter / PyQt

API version (Flask/FastAPI)

Integration with real health datasets
