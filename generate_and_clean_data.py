import numpy as np
import pandas as pd
import datetime
import random

np.random.seed(42)
random.seed(42)

print("توليد بيانات مبيعات أدوية مصرية واقعية على سنتين (2024-2025) ...")

# ---
# Products (50)
# ---
product_names = [
    "Panadol Extra", "Amoxicillin 500mg", "Lipitor 20mg", "Metformin 850mg", "Voltaren Emulgel",
    "Catafast 50mg", "Augmentin 1g", "Concor 5mg", "Zyrtec 10mg", "Brufen 400mg",
    "Nexium 40mg", "Plavix 75mg", "Ventolin Inhaler", "Claritin 10mg", "Grown-Up Vitamins",
    "Baby Aspirin", "Paracetamol Drops", "Omega 3 Fish Oil", "Vitamin C 1000mg", "Glucophage 1000mg",
    "Gaviscon Liquid", "Panadol Joint", "Zantac 150mg", "Provel 400mg", "Strepsils Honey",
    "Clexane 40mg", "Exforge 5/160mg", "Ator 20mg", "Keppra 500mg", "Januvia 100mg",
    "Tramadol 50mg", "Enalapril 10mg", "Furosemide 40mg", "Salbutamol Nebule", "Cetirizine 10mg",
    "Omeprazole 20mg", "Warfarin 5mg", "Insulin Pen", "Multivitamin Syrup", "Calcium + D3",
    "Miconazole Cream", "Clotrimazole", "Diclofenac Gel", "Paracetamol Suppository", "Amoxiclav 625mg",
    "Azithromycin 500mg", "Ciprofloxacin 500mg", "Metronidazole 500mg", "Loratadine 10mg", "Domperidone 10mg"
]
categories = [
    "Analgesic", "Antibiotic", "Cardiovascular", "Antipyretic", "Anti-inflammatory",
    "Analgesic", "Antibiotic", "Cardiovascular", "Antihistamine", "Anti-inflammatory",
    "Gastrointestinal", "Cardiovascular", "Respiratory", "Antihistamine", "Vitamins",
    "Cardiovascular", "Analgesic", "Vitamins", "Vitamins", "Antidiabetic",
    "Gastrointestinal", "Analgesic", "Gastrointestinal", "Anti-inflammatory", "Respiratory",
    "Cardiovascular", "Cardiovascular", "Cardiovascular", "Neurology", "Antidiabetic",
    "Analgesic", "Cardiovascular", "Cardiovascular", "Respiratory", "Antihistamine",
    "Gastrointestinal", "Cardiovascular", "Antidiabetic", "Vitamins", "Vitamins",
    "Dermatology", "Dermatology", "Anti-inflammatory", "Antipyretic", "Antibiotic",
    "Antibiotic", "Antibiotic", "Antibiotic", "Antihistamine", "Gastrointestinal"
]
# Check count
assert len(product_names) == 50
assert len(categories) == 50

cost_prices = np.round(np.random.uniform(5, 200, 50), 2)
stock_levels = np.random.randint(200, 8000, 50)

# Price setup
our_prices = np.round(cost_prices * np.random.uniform(1.3, 1.6, 50), 2)
competitor_prices = np.round(our_prices * np.random.uniform(0.85, 1.15, 50), 2)

df_products = pd.DataFrame({
    "product_id": [f"PROD_{i:03d}" for i in range(1, 51)],
    "product_name": product_names,
    "category": categories,
    "cost_price": cost_prices,
    "stock_level": stock_levels,
    "our_price": our_prices,
    "competitor_price": competitor_prices
})

# ---
# Reps (15)
# ---
rep_names = [
    "Ahmed Ali", "Mariam Saad", "Sarah John", "Youssef Zayed", "Omar Hassan",
    "Fatma Amro", "Khaled Nour", "Amr Ezat", "Hoda Kamel", "Mostafa Tarek",
    "Nadia Ibrahim", "Sami Mansour", "Rania El-Shazly", "Hassan Fathy", "Laila Ahmed"
]
primary_cities = [
    "Cairo", "Alexandria", "Giza", "Tanta", "Mansoura",
    "Asyut", "Port Said", "Ismailia", "Cairo", "Alexandria",
    "Hurghada", "Luxor", "Aswan", "Suez", "Tanta"
]
performance_factors = [1.6, 1.4, 1.2, 1.0, 0.9, 0.8, 0.7, 0.65, 1.3, 0.85, 1.1, 0.95, 0.75, 0.6, 0.9]

df_reps = pd.DataFrame({
    "rep_id": [f"REP_{i:02d}" for i in range(1, 16)],
    "rep_name": rep_names,
    "primary_city": primary_cities,
    "performance_factor": performance_factors
})
# Drop fields before export
df_reps_export = df_reps.drop(columns=["primary_city", "performance_factor"])

# ---
# Customers (50)
# ---
egyptian_cities = [
    "Cairo", "Giza", "Alexandria", "Tanta", "Mansoura",
    "Asyut", "Port Said", "Ismailia", "Hurghada", "Luxor", "Aswan", "Suez"
]
customers = []
for i in range(1, 51):
    city = np.random.choice(egyptian_cities)
    reliability = np.random.choice(["High", "Medium", "Low"], p=[0.5, 0.3, 0.2])
    customers.append({
        "customer_id": f"CUST_{i:03d}",
        "pharmacy_name": f"Pharmacy Branch {i}",
        "location_city": city,
        "payment_reliability": reliability
    })
df_customers = pd.DataFrame(customers)

# ---
# Sales transactions (100k, ~50k/year)
# ---
n_sales = 100000  # Two years
sales_list = []

# Start date: 2024-01-01
start_date = datetime.datetime(2024, 1, 1, 8, 0)

# Reps and products for selection
reps_list = df_reps.to_dict('records')
products_list = df_products.to_dict('records')

# Helper: random time across the day
def random_time_of_day(base_date):
    # Add a random hour between 8 and 22
    hour = np.random.randint(8, 22)
    minute = np.random.randint(0, 60)
    return base_date.replace(hour=hour, minute=minute, second=0)

# Monthly seasonality
# Simulate higher demand in some months
month_factor = {
    1: 1.2,  # Jan
    2: 1.1,
    3: 1.0,
    4: 0.9,
    5: 0.9,
    6: 1.0,
    7: 0.8,  # Summer
    8: 0.8,
    9: 1.0,
    10: 1.1,
    11: 1.2,  # Late fall
    12: 1.3   # Dec
}

# Weekly pattern
day_factor = {0: 1.0, 1: 1.0, 2: 1.0, 3: 1.0, 4: 1.0, 5: 0.7, 6: 1.0}  # 5 = Friday

print("محاكاة 100,000 معاملة على سنتين ...")
for i in range(n_sales):
    # Choose rep (weighted by performance)
    rep = np.random.choice(reps_list, p=df_reps["performance_factor"] / df_reps["performance_factor"].sum())
    
    # Choose city: 80% from rep city, else random
    if np.random.random() < 0.80:
        target_city = rep["primary_city"]
    else:
        target_city = np.random.choice(egyptian_cities)
    
    # Choose a pharmacy in that city
    city_pharmacies = df_customers[df_customers["location_city"] == target_city]
    if city_pharmacies.empty:
        cust_id = np.random.choice(df_customers["customer_id"])
    else:
        cust_id = np.random.choice(city_pharmacies["customer_id"])
    
    # Pick product (seasonal)
    # Set product weights by category and month
    # Simple random choice, with extra weight for some categories
    # Apply this later to quantity
    prod = np.random.choice(products_list)
    
    # Pick transaction date across two years
    # Add 1-20 mins
    start_date += datetime.timedelta(minutes=np.random.randint(1, 20))
    trans_date = start_date
    
    # Stop if we exceed 2025 (unlikely)
    if trans_date.year > 2025:
        # Reset date to continue
        pass
    
    # Compute quantity by season and rep performance
    month = trans_date.month
    day_of_week = trans_date.weekday()  # 0=Monday, 5=Friday
    base_qty = np.random.randint(3, 100)
    # Apply seasonal factor
    seasonal_qty = base_qty * month_factor.get(month, 1.0)
    # Apply day factor
    day_qty = seasonal_qty * day_factor.get(day_of_week, 1.0)
    # Apply rep performance
    final_qty = int(day_qty * rep["performance_factor"] * np.random.uniform(0.8, 1.2))
    final_qty = max(1, final_qty)  # At least 1
    
    # Payment method
    payment_method = np.random.choice(["Cash", "Credit Card", "Delayed Invoice"], p=[0.2, 0.25, 0.55])
    discount = np.random.choice([0.0, 0.05, 0.10, 0.15], p=[0.5, 0.2, 0.2, 0.1])
    
    sales_list.append({
        "transaction_id": f"TXN_{i:08d}",
        "transaction_date": trans_date.strftime("%Y/%m/%d %H:%M"),
        "customer_id": cust_id,
        "product_id": prod["product_id"],
        "rep_id": rep["rep_id"],
        "quantity_sold": final_qty,
        "payment_method": payment_method,
        "discount_applied": discount
    })

df_sales_raw = pd.DataFrame(sales_list)

print("تنظيف البيانات وحساب المؤشرات المالية ...")
# Merge data for revenue, cost, profit
df_merged = df_sales_raw.merge(df_products, on="product_id", how="left")

# Revenue after discount
base_revenue = df_sales_raw["quantity_sold"] * df_merged["our_price"]
df_sales_raw["total_sales_revenue"] = np.round(base_revenue * (1 - df_sales_raw["discount_applied"]), 2)
df_sales_raw["total_cost"] = np.round(df_sales_raw["quantity_sold"] * df_merged["cost_price"], 2)
df_sales_raw["profit_amount"] = np.round(df_sales_raw["total_sales_revenue"] - df_sales_raw["total_cost"], 2)
df_sales_raw["profit_margin_pct"] = np.round((df_sales_raw["profit_amount"] / df_sales_raw["total_sales_revenue"]) * 100, 2)

# Replace invalid values
df_sales_raw.replace([np.inf, -np.inf], 0, inplace=True)
df_sales_raw.fillna(0, inplace=True)

# Export clean files
df_products.to_csv("clean_products.csv", index=False)
df_customers.to_csv("clean_customers.csv", index=False)
df_reps_export.to_csv("clean_reps.csv", index=False)
df_sales_raw.to_csv("clean_sales.csv", index=False)

print("✅ تم توليد 100,000 معاملة (2024–2025) وحفظها في 4 ملفات CSV.")
print("نماذج من البيانات:")
print(df_sales_raw.head())