import h2o
h2o.init()
model = h2o.load_model("./models/best_dga_model")

domains = ["google.com", "ulmrl7vh5kweramdilp0q3hnd.com"]

def get_entropy(s):
    import math
    p, lns = {}, float(len(s))
    for c in s:
        p[c] = p.get(c, 0) + 1
    return -sum(count/lns * math.log(count/lns, 2) for count in p.values())

X = [[len(d), get_entropy(d)] for d in domains]

import pandas as pd
h2o_df = h2o.H2OFrame(pd.DataFrame(X, columns=["length", "entropy"]))
preds = model.predict(h2o_df)
print(preds)

