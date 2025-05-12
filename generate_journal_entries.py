
import random
import pandas as pd
from datetime import datetime, timedelta

# Sample data for generation
transaction_types = {
    "Sales": ("Accounts Receivable", "Sales Revenue", "Credit sale to customer {}"),
    "Purchase": ("Inventory", "Accounts Payable", "Raw materials purchased from supplier {}"),
    "Payroll": ("Salaries Expense", "Bank Account", "Salary paid to employees"),
    "Depreciation": ("Depreciation Expense", "Accumulated Depreciation", "Monthly depreciation for asset"),
    "Loan Repayment": ("Loan Payable", "Bank Account", "Loan repayment to bank"),
    "Rent": ("Rent Expense", "Bank Account", "Monthly rent paid for office space"),
    "Cash Sale": ("Cash Account", "Sales Revenue", "Cash sale to customer"),
    "Interest Income": ("Bank Account", "Interest Income", "Interest received from bank"),
}

entities = ["ABC Pvt. Ltd.", "XYZ Corp.", "BrightTech", "Nova Enterprises", "Global Suppliers", "Unity Inc."]

def generate_journal_entries(num_entries=1000, start_date="2024-01-01"):
    entries = []
    base_date = datetime.strptime(start_date, "%Y-%m-%d")

    for i in range(num_entries):
        entry_id = 1001 + i
        date = base_date + timedelta(days=i)
        transaction_type = random.choice(list(transaction_types.keys()))
        debit, credit, narration_template = transaction_types[transaction_type]
        entity = random.choice(entities)
        narration = narration_template.format(entity) if "{}" in narration_template else narration_template
        amount = round(random.uniform(1000, 20000), 2)

        entries.append({
            "Entry ID": entry_id,
            "Date": date.strftime('%Y-%m-%d'),
            "Transaction Type": transaction_type,
            "Account Debited": debit,
            "Account Credited": credit,
            "Amount": amount,
            "Narration": narration
        })

    return pd.DataFrame(entries)

if __name__ == "__main__":
    df = generate_journal_entries()
    df.to_csv("synthetic_journal_entries.csv", index=False)
    print("1000 synthetic journal entries saved to 'synthetic_journal_entries.csv'")
