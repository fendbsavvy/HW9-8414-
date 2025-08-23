# Filename: 3_explain_model.py
import h2o
import shap
import pandas as pd
import matplotlib.pyplot as plt
import math


def get_entropy(s):
    p, lns = {}, float(len(s))
    for c in s:
        p[c] = p.get(c, 0) + 1
    return -sum(count/lns * math.log(count/lns, 2) for count in p.values())


h2o.init()
model_path = "./models/best_dga_model"
best_model = h2o.load_model(model_path)


TEST_DOMAIN = "kq3v9z7j1x5f8g2h.info"

X_test = pd.DataFrame([[len(TEST_DOMAIN), get_entropy(TEST_DOMAIN)]],
                      columns=['length', 'entropy'])

h2o_df = h2o.H2OFrame(X_test)
pred = best_model.predict(h2o_df)
pred_label = pred.as_data_frame()['predict'][0]
pred_probs = pred.as_data_frame().iloc[0][1:]
confidence = max(pred_probs) * 100
print(f"Prediction: {pred_label}, Confidence: {confidence:.2f}%")


def predict_wrapper(data):
    h2o_df = h2o.H2OFrame(pd.DataFrame(data, columns=X_test.columns))
    predictions = best_model.predict(h2o_df)
    return predictions.as_data_frame()['dga']

explainer = shap.KernelExplainer(predict_wrapper, X_test)
shap_values = explainer.shap_values(X_test)

print("Displaying SHAP Summary Plot (Global Explanation)...")
shap.summary_plot(shap_values, X_test, show=False)
plt.savefig("shap_summary.png")
plt.close()

print("Displaying SHAP Force Plot (Local Explanation for first instance)...")
shap.force_plot(explainer.expected_value, shap_values[0,:], X_test.iloc[0,:], show=False, matplotlib=True)
plt.savefig("shap_force.png")
plt.close()



findings = {
    "domain": TEST_DOMAIN,
    "prediction": pred_label,
    "confidence": confidence,
    "entropy": X_test.iloc[0]['entropy'],
    "length": X_test.iloc[0]['length']
}

print("Findings prepared for playbook:")
print(findings)

h2o.shutdown()
