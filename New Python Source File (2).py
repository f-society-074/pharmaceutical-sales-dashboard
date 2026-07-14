import pandas as pd
from pathlib import Path

# نفس الفولدر الموجود فيه ملف Python
folder = Path(__file__).parent

# البحث عن ملف الداتا تلقائيًا
files = list(folder.glob("pharma_sales_perfect*"))

if not files:
    raise FileNotFoundError("ملف pharma_sales_perfect غير موجود في نفس الفولدر")

file_path = files[0]

print("File found:", file_path.name)

# قراءة الملف حسب نوعه
if file_path.suffix.lower() == ".csv":
    df = pd.read_csv(file_path)
elif file_path.suffix.lower() in [".xlsx", ".xls"]:
    df = pd.read_excel(file_path)
else:
    raise ValueError(f"نوع الملف غير مدعوم: {file_path.suffix}")

print("\n=== SHAPE ===")
print("Rows:", df.shape[0])
print("Columns:", df.shape[1])

print("\n=== COLUMN NAMES ===")
for i, col in enumerate(df.columns, 1):
    print(f"{i}. {col}")

print("\n=== DATA TYPES ===")
print(df.dtypes)

print("\n=== FIRST 10 ROWS ===")
print(df.head(10).to_string())

print("\n=== MISSING VALUES ===")
print(df.isnull().sum())

print("\n=== UNIQUE VALUES PER COLUMN ===")
print(df.nunique())