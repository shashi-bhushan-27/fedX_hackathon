import pandas as pd
import joblib
from catboost import CatBoostClassifier, CatBoostRegressor
from sklearn.model_selection import train_test_split
from sklearn.metrics import roc_auc_score, mean_absolute_error

# Load data
df = pd.read_csv("/content/flex_dca_training_data.csv")

# Prepare X and y
X = df.drop(columns=["recovered","closure_days","dca_id"])
y_recovery = df["recovered"]
y_aging = (df["closure_days"] > 30).astype(int)
y_speed = df["closure_days"]

# --- CRITICAL FIX: Identify Categorical Columns ---
# This finds all columns that are objects (strings) or categories
cat_features = X.select_dtypes(include=['object', 'category']).columns.tolist()

# Fill NaN in categorical columns with a placeholder string as CatBoost requires
for col in cat_features:
    X[col] = X[col].fillna('None')

# -------- Split --------
# Note: Use the same random_state to ensure rows match across different y targets
X_train, X_test, yr_train, yr_test = train_test_split(X, y_recovery, test_size=0.2, random_state=42)
_, _, ya_train, ya_test = train_test_split(X, y_aging, test_size=0.2, random_state=42)
_, _, ys_train, ys_test = train_test_split(X, y_speed, test_size=0.2, random_state=42)

# -------- Models --------
# Tip: Adding task_type='GPU' here will speed up your 114MB training on Colab
recovery_model = CatBoostClassifier(verbose=False, task_type='CPU') # or 'GPU'
aging_model = CatBoostClassifier(verbose=False, task_type='CPU')
speed_model = CatBoostRegressor(verbose=False, task_type='CPU')

# --- Pass cat_features here ---
print("Training Recovery Model...")
recovery_model.fit(X_train, yr_train, cat_features=cat_features)

print("Training Aging Risk Model...")
aging_model.fit(X_train, ya_train, cat_features=cat_features)

print("Training Closure Speed Model...")
speed_model.fit(X_train, ys_train, cat_features=cat_features)

# -------- Evaluation --------
rec_auc = roc_auc_score(yr_test, recovery_model.predict_proba(X_test)[:,1])
aging_auc = roc_auc_score(ya_test, aging_model.predict_proba(X_test)[:,1])
speed_mae = mean_absolute_error(ys_test, speed_model.predict(X_test))

print(f"\nResults:")
print("Recovery AUC:", rec_auc)
print("Aging Risk AUC:", aging_auc)
print("Closure Speed MAE (Days):", speed_mae)

# -------- Save --------
# Ensure the directory exists before saving
import os
os.makedirs("backend/app/ml", exist_ok=True)
joblib.dump(recovery_model, "backend/app/ml/recovery.pkl")
joblib.dump(aging_model, "backend/app/ml/aging.pkl")
joblib.dump(speed_model, "backend/app/ml/speed.pkl")


# Training Recovery Model...
# Training Aging Risk Model...
# Training Closure Speed Model...

# Results:
# Recovery AUC: 1.0
# Aging Risk AUC: 0.532777223502318
# Closure Speed MAE (Days): 27.169656519688733
# ['backend/app/ml/speed.pkl']