
# 🧾 Synthetic Accounting Journal Entries Dataset

This project contains a synthetic dataset of accounting journal entries, generated for educational, analytical, and machine learning use in the domain of **Accounting and Finance**.

## 📌 Purpose

The goal of this dataset is to:
- Provide a **realistic but fictional** set of accounting entries.
- Support **research and model development** in bookkeeping automation, NLP-based financial analysis, and AI-assisted audit tools.
- Offer a clean, structured dataset for **students, developers, and analysts** to work on classification, error detection, or data visualization tasks.

## 📁 Dataset Overview

The dataset is generated using a Python script (`generate_journal_entries.py`) and exported as a CSV file:

**Filename**: `synthetic_journal_entries.csv`

### 🧾 Columns

| Column Name         | Description                                                                 |
|---------------------|-----------------------------------------------------------------------------|
| Entry ID            | Unique identifier for each journal entry                                    |
| Date                | Date of the transaction (YYYY-MM-DD)                                        |
| Transaction Type    | Type/category of transaction (e.g., Sales, Purchase, Rent, etc.)            |
| Account Debited     | Account that has been debited                                                |
| Account Credited    | Account that has been credited                                               |
| Amount              | Transaction amount in monetary units (e.g., BDT, USD)                       |
| Narration           | Short description of the transaction                                         |

### 📊 Sample Record

```
Entry ID: 1001  
Date: 2024-01-01  
Transaction Type: Sales  
Account Debited: Accounts Receivable  
Account Credited: Sales Revenue  
Amount: 15000.00  
Narration: Credit sale to customer ABC Pvt. Ltd.
```

## ⚙️ How the Data is Generated

The Python script (`generate_journal_entries.py`) generates synthetic data by:
- Randomly selecting transaction types and entity names.
- Assigning realistic debit/credit account pairs.
- Generating random amounts between 1,000 and 20,000.
- Creating one entry per day starting from `2024-01-01`.

To generate your own dataset:

```bash
python generate_journal_entries.py
```

## 🧠 Potential Uses

- 📚 Accounting practice for students and educators
- 🔍 NLP tasks like **narration classification**
- 🧾 Transaction classification or **fraud detection models**
- 📊 Dashboard/ERP prototype testing
- 🤖 Bookkeeping automation system training

## 📎 License

This dataset is synthetic and created for public educational and research use. No real company or financial data is involved.

## ✍️ Author

Created by Towhid Abrar  
Generated with Python and Pandas.
