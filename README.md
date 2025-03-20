# 🧾 Personalized Invoice Generator

A user-friendly and customizable billing application designed for **Cotton and Maize Merchant**. Built using **Python (Tkinter)** with **MySQL** integration and **DOCX** invoice generation for offline billing needs.

---

## 📌 Features

- 🔢 **Auto Invoice Numbering** — Fetches next invoice number based on database records.
- 🗓️ **Auto Date Detection** — Automatically sets the current date and updates after midnight.
- 👤 **Buyer/Consignee Details** — Easily input party names, addresses, vehicle number, and destination.
- 🧮 **Live Total Calculation** — Automatically calculates total and displays amount in words.
- 🏦 **Bank Dropdown** — Select from pre-defined banks and fetch associated account details automatically.
- 📄 **DOCX Invoice Template** — Populates a professional invoice template with all details neatly arranged.
- 📂 **Bill Folder Saving** — Saves invoices in a structured folder `bills 2025/` with custom filename format.
- 🆕 **New Bill Option** — Reset the form and generate a fresh invoice.
- ❌ **Close Button** — Quickly exit the app.

---

## 🛠️ Tech Stack

- **Python 3.9+**
- **Tkinter** – GUI
- **MySQL** – Database backend
- **python-docx** – For invoice document creation
- **num2words** – For converting total amount to readable words

---

## 📁 Project Structure

```
Billing Application/
├── Config/
│   └── config.py             # Configuration file for database settings (DB_CONFIG dict)
│
├── db/
│   └── connection.py         # Handles MySQL DB connection using Config
│
├── templates/
│   └── invoice.docx          # Pre-designed invoice Word template
│
├── bills 2025/               # Folder to store all generated invoice DOCX files
│
├── Invoice.py                # Main Python Tkinter GUI application
├── README.md                 # Project documentation
└── requirements.txt          # Python dependencies

```

---


## 🚀 How to Run

1. Clone this repository  
   `git clone https://github.com/yourusername/invoice-generator.git`

2. Setup MySQL database:
   - Create a DB named `invoice`
   - Add `invoices` table with relevant columns (check `connection.py`)
   - Add your DB credentials in `db/connection.py`

3. Install required Python packages:
   ```bash
   pip install python-docx num2words mysql-connector-python
   ```

4. Run the application:
   ```bash
   python Invoice.py
   ```

---

## ✅ To-Do / Improvements

- PDF invoice export
- GST support
- Multi-item billing
- Print invoice directly
