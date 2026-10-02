# Hybrid Bank Customer Segmentation

This repository contains a Jupyter notebook prototype for customer-level RFM and clustering analysis. The notebook describes a bank-transactions workflow using K-Means, DBSCAN, PCA, and RFM scoring. It is not a validated or production-ready system.

## Contents

- `Bank_Customer_Segmentation.ipynb` — analysis workflow.
- `requirements.txt` — pinned Python dependencies.

The transaction dataset is **not included**. No customer data is needed to inspect or syntax-check the notebook, but executing its analysis requires an authorized dataset copy.

## Run locally

Use Python 3.10–3.12, then install the pinned dependencies and launch JupyterLab:

```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
python -m pip install -r requirements.txt
jupyter lab
```

Place an authorized `bank_transactions.csv` file in the repository root (next to the notebook), then run the notebook from top to bottom. The notebook checks for the file and reports its expected location if it is missing. The analysis expects these columns: `TransactionID`, `CustomerID`, `TransactionAmount (INR)`, `CustAccountBalance`, `CustomerDOB`, `TransactionDate`, `TransactionTime`, `CustLocation`, and `CustGender`.

Do not commit the CSV or other customer-level exports. Check that your copy is appropriately licensed and that you are permitted to process it; remove or anonymize identifying data where required by your policies.

## Reproducibility and limitations

The DBSCAN sample selection uses a fixed seed. The notebook's previously saved cell outputs and execution counts have been cleared so old data previews, plots, or scores are not presented as fresh results. DBSCAN is fit on a sample of at most 5,000 customers; its silhouette score is calculated only on non-noise points in that sample and is omitted when fewer than two non-noise clusters are found.

The dataset is absent from this repository, so the notebook has not been executed end to end here. Any scores or business interpretations previously stated for this project are unverified in this checkout and should not be treated as reproduced results. Clustering quality and segment meaning depend on the authorized input data and require independent validation before business use.
