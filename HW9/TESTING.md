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

- Check that dga_dataset_train.csv was created
- **Output:** dga_dataset_train.csv created successfully.

### Train AutoML Model
- python3 2_run_automl.py
- check that ./models/best_dga_model is created
- check for MOJO artifact 

### Verify SHAP Explanations
- python3 3_explain_model.py
- Verify shap_summary.png and shap_force.png is generated
- Check for findings
Findings prepared for playbook:
{'domain': 'kq3v9z7j1x5f8g2h.info', 'prediction': 'dga', 'confidence': np.int64(100), 'entropy': np.float64(4.297079327540665), 'length': np.float64(21.0)}


### Generate Prescriptive Playbook
- python3 4_generate_prescriptive_playbook.py

- Check from generated playbook
--- AI-Generated Playbook ---
1. **Isolate:** Immediately block the domain `kq3v9z7j1x5f8g2h.info` at the firewall and DNS level.

2. **Investigate:** Perform a WHOIS lookup on the domain to identify registrant information and potentially associated infrastructure.

3. **Report:**  Document the incident in the ticketing system, including the alert details, actions taken, and findings from the WHOIS lookup.

4. **Monitor:**  Continuously monitor network traffic for any further communication attempts related to `kq3v9z7j1x5f8g2h.info` or similar suspicious domains.

### Generate findings for benign url
- replace URL in 3_explain_model.py --> TEST_DOMAIN = "google.com"
- Rerun script
- Check findings and play book

Findings prepared for playbook:
{'domain': 'google.com', 'prediction': 'legit', 'confidence': np.int64(100), 'entropy': np.float64(2.6464393446710157), 'length': np.float64(10.0)}

--- AI-Generated Playbook ---
1. **Verify Alert:** Confirm the alert source and ensure the alert details (domain: google.com, length: 10) match the information in your SIEM/monitoring system.

2. **Close the Alert:** Given the AI prediction of "legit" with 100% confidence, and the benign characteristics (low entropy), close the alert in the ticketing system.

3. **Document Closure:** Briefly note the reason for closure (AI prediction: legit, 100% confidence) in the alert's comment section.

4. **Review & Improve:**  Periodically review closed alerts to ensure the AI model's accuracy and adjust response playbooks as needed.





