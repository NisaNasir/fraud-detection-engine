# 🛡️ Real-Time Fintech Transaction Monitoring & Fraud Detection Engine

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://YOUR-STREAMLIT-APP-URL.streamlit.app)
*(Replace the URL above with your actual live Streamlit app link)*

## Executive Summary
This project delivers an end-to-end Machine Learning Fraud Detection Engine built for digital banks, payment gateways, and e-wallets (e.g., Touch 'n Go Digital, GXBank, Boost Bank). The pipeline processes highly imbalanced transaction data (~284k records with a 0.17% fraud ratio), handles noise via data sanitization, benchmarks unsupervised anomaly detection (**Isolation Forest**) against cost-sensitive supervised models (**XGBoost**), and provides operational **precision-recall threshold tuning**.

To comply with **Bank Negara Malaysia (BNM)** standards on Model Governance and Anti-Money Laundering (AML) transparency, the framework integrates **SHAP (SHapley Additive exPlanations)** to generate audit trails explaining why specific transactions trigger risk flags.

---

## 📊 Key Results & Business Metrics
* **Extreme Class Imbalance Resolution:** Managed 1:580 fraud-to-normal ratio using `scale_pos_weight` and stratified sampling.
* **Model Performance:** Achieved a **Precision-Recall AUC (PR-AUC) of ~0.85** and **ROC-AUC of ~0.97**, drastically outperforming unsupervised baselines.
* **Threshold Tuning & Operational Trade-offs:** Engineered custom risk thresholds (e.g., 0.30 cutoff) to optimize the balance between catching fraudulent transfers and preventing excessive false alarms for legitimate users.
* **Real-Time Deployment:** Built an interactive risk ops dashboard deployed live on Streamlit Cloud for step-up authentication routing (OTP/2FA) and auto-blocking.

---

## 🛠️ Tech Stack & Methodology
* **Core Stack:** Python, Pandas, NumPy, Scikit-Learn
* **Machine Learning:** XGBoost Classifier, Isolation Forest (Anomaly Baseline)
* **Model Explainability:** SHAP (TreeExplainer summary & waterfall plots)
* **Evaluation Metrics:** PR-AUC, ROC-AUC, Precision, Recall, Confusion Matrix
* **Deployment:** Streamlit Cloud

---

## 💡 System Architecture

```text
[Raw Transaction Stream] 
       │
       ▼
[Data Cleaning & Deduplication] ────► (Duplicate transaction removal, PCA feature scaling audit)
       │
       ▼
[Imbalance & Anomaly Modeling] ────► (Isolation Forest Baseline vs. Cost-Sensitive XGBoost)
       │
       ▼
[Threshold Optimization] ─────────► (Risk-ops decision matrix: Auto-Approve, 2FA Step-up, Auto-Block)
       │
       ▼
[Regulatory Compliance Engine] ───► (SHAP-driven feature attribution for AML compliance audits)
       │
       ▼
[Live Production Dashboard] ─────► (Streamlit real-time risk control panel)
```

## 📁 Repository Structure
```text
malaysia-fraud-detection-engine/
├── app/
│   └── app.py               <- Streamlit transaction monitoring dashboard
├── notebooks/
│   └── fraud_detection.ipynb <- Data audit, EDA, modeling, PR-AUC evaluation & SHAP
├── requirements.txt         <- Project dependencies
└── README.md                <- Technical & executive documentation
```
