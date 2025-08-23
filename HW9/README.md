# The Prescriptive DGA Detector

## Goals
The goal of this lab is to develop an end-to-end Python application that integrates **AutoML**, **Explainable AI (XAI)**, and **Generative AI** into a powerful workflow. The tool will:

1. **Build a high-performance model**  
   Rapidly train a model to distinguish between legitimate and DGA domains using AutoML.

2. **Explain model predictions**  
   Use Explainable AI techniques like SHAP to provide insight into the model's decisions.

3. **Generate actionable response**  
   Translate those explanations into actionable instructions using Generative AI.

---


## Architecture

### 1. Data Generation using file`1_generate_dga_data.py`
**Purpose:** Generate synthetic dataset for model training and testing.  
**Steps:**
- Create domain samples from list of popular domains.
- Generate DGA domains with random alphanumeric characters.
- Calculate entropy and length features for each domain.
- Label data as legit or dga and save to `dga_dataset_train.csv`.

**Output:** training dataset `dga_dataset_train.csv` 

---

### 2. Model Training with AutoML using file `2_run_automl.py`
**Purpose:** Automatically train and select the best classification model.  
**Steps:**
- Load dataset using H2O.
- Define features length, entropy and target class.
- Run H2O AutoML to train multiple models and select the best one.
- Save the best model as a MOJO artifact.

**Output:**  
- H2O model: `./models/best_dga_model`  
- MOJO artifact: `XGBoost_2_AutoML_1_20250820_00141.zip`

---

### 3. Model Explanation using file `3_explain_model.py`
**Purpose:** Provide insight for the model’s predictions.  
**Steps:**
- Load the trained model and test dataset.
- Use SHAP to generate explanations.
- Save plots for visualization.

**Output:**  SHAP visualizations `shap_summary.png` and `shap_force.png`.

---

### 4. Actionable Instructions using file `4_generate_prescriptive_playbook.py`
**Purpose:** Translate model explanations into actionable instructions.  
**Steps:**
- Accept XAI findings as input.
- Send prompt to Google Generative AI (Gemini API) to create a step-by-step playbook.
- Generate clear instructions 
- Display the AI-generated playbook.

**Output:** Playbook.



## Usage:
### Create and activate virtual environment
  - (inside project directory)
  - python3 -m venv venv
  - source venv/bin/activate

### Install necessary packages
- pip install h2o
- sudo apt install default-jre -y
- pip install shap matplotlib
- pip install -q google-generativeai
- pip install aiohttp
- export GOOGLE_API_KEY='AIza...'

### Execute project files
- python3 1_generate_dga_data.py
- python3 2_run_automl.py
- python3 3_explain_model.py
- python3 4_generate_prescriptive_playbook.py


### Expected Output
- Findings for playbook
- AI-Generated Playbook 


