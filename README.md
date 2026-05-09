# 💸 Expense Tracker App (Streamlit)

A modern, AI-powered Expense Tracker built using **Python + Streamlit + SQLite**, designed to help users manage daily expenses, track budgets, and visualize spending patterns.

---

## 🚀 Features

- ➕ Add daily expenses with category detection  
- 🤖 AI-based auto categorization of expenses  
- 📊 Interactive dashboard with insights & charts  
- 💰 Budget tracking system  
- 🗂️ SQLite database integration  
- 🌐 Deployable via Streamlit Cloud  

---

## 🛠️ Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **Database:** SQLite  

---

## 📁 Project Structure

```
expense-tracker/
│── app.py
│── requirements.txt
│── README.md
│
├── src/
│   ├── db.py
│   ├── utils.py
│   │
│   └── pages/
│       ├── dashboard.py
│       ├── add_expense.py
│       └── budget.py
```

---

## ⚙️ Installation & Setup

### 1. Clone Repository

```
git clone https://github.com/your-username/expense-tracker.git
cd expense-tracker
```

### 2. Create Virtual Environment

```
python -m venv venv
```

Activate it:

- Windows:
```
venv\Scripts\activate
```

- Mac/Linux:
```
source venv/bin/activate
```

### 3. Install Dependencies

```
pip install -r requirements.txt
```

### 4. Run the App

```
streamlit run app.py
```

---

## 🌍 Deployment (Streamlit Cloud)

1. Push project to GitHub  
2. Go to Streamlit Cloud  
3. Select your repo  
4. Set main file: `app.py`  
5. Deploy 🚀  

---

## ⚠️ Common Errors & Fixes

### ImportError (conn, cursor not found)

Fix in `src/db.py`:

```python
import sqlite3

conn = sqlite3.connect("expenses.db", check_same_thread=False)
cursor = conn.cursor()
```

---

### Module Not Found (src)

Add this in `app.py`:

```python
import sys
import os
sys.path.append(os.path.abspath(os.path.dirname(__file__)))
```

---

## 📊 Future Improvements

- 🔐 User authentication system  
- ☁️ Cloud database (Firebase / PostgreSQL)  
- 📱 Mobile responsive UI  
- 📈 Advanced analytics  
- 🤖 AI financial advisor  

---

## 👨‍💻 Author

**Dhananjay Bhaskar**

---

## 🙌 Acknowledgment

Special thanks to **Indian Institute of Placement** and my mentor for guidance and support.

---

## ⭐ Support

If you like this project:

- ⭐ Star the repo  
- 🍴 Fork it  
- 📢 Share it  
