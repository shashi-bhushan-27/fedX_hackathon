import pandas as pd
import numpy as np

# Load Kaggle datasets
uci = pd.read_csv("raw/UCI_Credit_Card.csv")
lc  = pd.read_csv("raw/loan.csv")

# =======================
# UCI TRANSFORMATION
# =======================

uci["amount"] = uci["LIMIT_BAL"]
uci["due_days"] = uci[["PAY_0","PAY_2","PAY_3","PAY_4","PAY_5","PAY_6"]].mean(axis=1)
uci["invoice_count"] = (uci["BILL_AMT1"] > 0).astype(int) + (uci["BILL_AMT2"] > 0).astype(int)
uci["credit_score"] = 750 - (uci["PAY_0"] * 20)
uci["previous_collections"] = uci["PAY_AMT1"]
uci["historical_default_rate"] = uci["default.payment.next.month"]
uci["recovered"] = 1 - uci["default.payment.next.month"]
uci["closure_days"] = (uci["PAY_0"] + 1) * 5
uci["region"] = np.random.choice(["US","EU","APAC"], size=len(uci))
uci["specialization"] = np.random.choice(["B2B","B2C"], size=len(uci))
uci["dca_id"] = np.random.choice(["DCA001","DCA002","DCA003"], size=len(uci))

uci_final = uci[[
    "amount","due_days","invoice_count","credit_score","previous_collections",
    "historical_default_rate","recovered","closure_days","region","specialization","dca_id"
]]

# =======================
# LENDING CLUB TRANSFORMATION
# =======================

lc["amount"] = lc["loan_amnt"]
lc["due_days"] = np.random.randint(10, 90, size=len(lc))
lc["invoice_count"] = np.random.randint(1,5,size=len(lc))
lc["credit_score"] = lc["grade"].astype("category").cat.codes * 100 + 600
lc["previous_collections"] = lc["total_pymnt"]
lc["historical_default_rate"] = (lc["loan_status"]!="Fully Paid").astype(int)
lc["recovered"] = (lc["loan_status"]=="Fully Paid").astype(int)
lc["closure_days"] = np.random.randint(10,120,size=len(lc))
lc["region"] = lc["addr_state"]
lc["specialization"] = np.random.choice(["B2B","B2C"], size=len(lc))
lc["dca_id"] = np.random.choice(["DCA001","DCA002","DCA003"], size=len(lc))

lc_final = lc[uci_final.columns]

# =======================
# FINAL DATASET
# =======================

final_df = pd.concat([uci_final, lc_final]).sample(frac=1).reset_index(drop=True)
final_df.to_csv("flex_dca_training_data.csv", index=False)

print("FLEX-DCA training dataset created.")
