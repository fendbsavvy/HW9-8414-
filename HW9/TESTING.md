# DGA Detection Tool: Manual Testing Guide

## Test Setup

### Create and activate virtual environment
  - (inside project directory)
  - python3 -m venv venv
  - source venv/bin/activate

### Install all necessary dependencies
- pip install h2o
- sudo apt install default-jre -y
- pip install shap matplotlib
- pip install -q google-generativeai
- pip install aiohttp
- export GOOGLE_API_KEY='AIza...'

## Execute project files

### Generate Dataset
- python3 1_generate_dga_data.py

Check that dga_dataset_train.csv was created
**Output:*** dga_dataset_train.csv created successfully.

### Train AutoML Model
- python3 2_run_automl.py
check that ./models/best_dga_model is created
check for MOJO artifact 

### Verify SHAP Explanations
- python3 3_explain_model.py
Verify shap_summary.png and shap_force.png is generated 


### Generate Prescriptive Playbook
- python3 4_generate_prescriptive_playbook.py

### Run test script
- verify expected output for domains "google.com", "ulmrl7vh5kweramdilp0q3hnd.com"


Parse progress: |████████████████████████████████████████████████████████████████████████████████████ (done)| 100%
xgboost prediction progress: |███████████████████████████████████████████████████████████████████████ (done)| 100%
predict          dga      legit
legit      0.0711842  0.928816
dga        0.931661   0.0683391
[2 rows x 3 columns]

Closing connection _sid_9f02 at exit
H2O session _sid_9f02 closed.




verify expected output for dga 
