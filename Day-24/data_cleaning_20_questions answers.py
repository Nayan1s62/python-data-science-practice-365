import pandas as pd
import numpy as np

# Load dataset
df = pd.read_csv("33965eb5-e315-40da-91d3-14ca929c6786.csv")

# 1. Column Names
print(df.columns.tolist())

for col in df.columns:
    if col != col.strip():
        print("Leading/trailing space:", repr(col))

df.columns = (
    df.columns.str.strip()
    .str.lower()
    .str.replace(r"[^a-z0-9]+", "_", regex=True)
    .str.strip("_")
)

if "discount" in df.columns:
    df = df.rename(columns={"discount": "discount_pct"})

# 2. Duplicate Records
print("Duplicates before:", df.duplicated().sum())
df = df.drop_duplicates().reset_index(drop=True)
print("Duplicates after:", df.duplicated().sum())

# 3. Missing Values
missing_report = pd.DataFrame({
    "missing_count": df.isna().sum(),
    "missing_percentage": df.isna().mean() * 100
})
print(missing_report)

# 4. Missing Categorical Values
for col in ["city", "product_category", "payment_method"]:
    df[col] = df[col].fillna(df[col].mode()[0])

# 5. Missing Numerical Values
df["age"] = pd.to_numeric(df["age"], errors="coerce")
df["age"] = df["age"].fillna(df["age"].median())
df["customer_rating"] = df["customer_rating"].fillna(
    df["customer_rating"].median()
)
# Revenue = Cost + Profit
df.loc[df["revenue"].isna(), "revenue"] = (
    df["cost"] + df["profit"]
)

# 6. Date Cleaning
df["order_date"] = pd.to_datetime(
    df["order_date"], errors="coerce", format="mixed"
)
print("Invalid dates:", df["order_date"].isna().sum())
df = df.dropna(subset=["order_date"]).reset_index(drop=True)

# 7. Age Cleaning
df["age"] = (
    df["age"].astype("string")
    .str.extract(r"(\d+(?:\.\d+)?)", expand=False)
)
df["age"] = pd.to_numeric(df["age"], errors="coerce")

# 8. Age Outliers - IQR
Q1 = df["age"].quantile(.25)
Q3 = df["age"].quantile(.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

print("Age outliers:")
print(df.loc[(df["age"] < lower) | (df["age"] > upper), "age"])

df.loc[(df["age"] < 0) | (df["age"] > 100), "age"] = np.nan
df["age"] = df["age"].fillna(df["age"].median())

# 9. Unit Price Cleaning
def clean_price(x):
    if pd.isna(x):
        return np.nan
    x = str(x).strip().lower().replace(",", "")
    if x.endswith("k"):
        try:
            return float(x[:-1]) * 1000
        except:
            return np.nan
    x = x.replace("₹", "").replace("$", "").replace("inr", "").strip()
    return pd.to_numeric(x, errors="coerce")

df["unit_price"] = df["unit_price"].map(clean_price)

# 10. Unit Price Outliers
Q1 = df["unit_price"].quantile(.25)
Q3 = df["unit_price"].quantile(.75)
IQR = Q3 - Q1
lower = Q1 - 1.5 * IQR
upper = Q3 + 1.5 * IQR

before = ((df["unit_price"] < lower) |
          (df["unit_price"] > upper)).sum()
print("Unit price outliers before:", before)

df["unit_price"] = df["unit_price"].clip(lower, upper)

after = ((df["unit_price"] < lower) |
         (df["unit_price"] > upper)).sum()
print("Unit price outliers after:", after)

df["unit_price"] = df["unit_price"].fillna(
    df["unit_price"].median()
)

# 11. Units Sold Cleaning
words = {
    "zero":0, "one":1, "two":2, "three":3, "four":4,
    "five":5, "six":6, "seven":7, "eight":8, "nine":9,
    "ten":10, "eleven":11, "twelve":12, "thirteen":13,
    "fourteen":14, "fifteen":15, "sixteen":16,
    "seventeen":17, "eighteen":18, "nineteen":19, "twenty":20
}

s = df["units_sold"].astype("string").str.lower().str.strip()
s = s.map(lambda x: words.get(x, x) if pd.notna(x) else x)

df["units_sold"] = pd.to_numeric(
    s.astype("string").str.extract(r"(\d+)", expand=False),
    errors="coerce"
)
df["units_sold"] = df["units_sold"].fillna(
    df["units_sold"].median()
)

# 12. Discount Cleaning
df["discount_pct"] = (
    df["discount_pct"].astype("string")
    .str.lower().str.strip()
    .str.replace("%", "", regex=False)
    .str.replace("percent", "", regex=False)
)
df["discount_pct"] = pd.to_numeric(
    df["discount_pct"], errors="coerce"
)

# 13. Discount Outliers / Invalid Values
invalid = (
    (df["discount_pct"] < 0) |
    (df["discount_pct"] > 100)
)
print("Invalid discount values:")
print(df.loc[invalid, "discount_pct"])

df.loc[invalid, "discount_pct"] = np.nan
df["discount_pct"] = df["discount_pct"].fillna(
    df["discount_pct"].median()
)

# 14. City Standardization
df["city"] = (
    df["city"].astype("string").str.strip().str.lower()
)
df["city"] = df["city"].replace({
    "mumbai":"Mumbai",
    "bangalore":"Bangalore",
    "bengaluru":"Bangalore",
    "hyderbad":"Hyderabad",
    "hyderabad":"Hyderabad",
    "delhi":"Delhi",
    "chennai":"Chennai",
    "pune":"Pune"
})

# 15. Product Category
df["product_category"] = (
    df["product_category"].astype("string")
    .str.strip().str.lower()
)
df["product_category"] = df["product_category"].replace({
    "electronics":"Electronics",
    "home and kitchen":"Home & Kitchen",
    "home & kitchen":"Home & Kitchen",
    "beauty":"Beauty",
    "clothing":"Clothing",
    "sports":"Sports"
})

# 16. Gender
df["gender"] = (
    df["gender"].astype("string").str.strip().str.lower()
)
df["gender"] = df["gender"].replace({
    "male":"Male", "m":"Male",
    "female":"Female", "f":"Female",
    "other":"Other"
})

# 17. Customer Segment
df["customer_segment"] = (
    df["customer_segment"].astype("string")
    .str.strip().str.lower()
)
df["customer_segment"] = df["customer_segment"].replace({
    "prem":"Premium",
    "premium":"Premium",
    "reg":"Regular",
    "regular":"Regular",
    "budget":"Budget",
    "vip":"VIP"
})

# 18. Binary Columns
active_map = {
    "1":1, "0":0, "yes":1, "no":0,
    "y":1, "n":0, "active":1, "inactive":0
}
returned_map = {
    "1":1, "0":0, "yes":1, "no":0,
    "y":1, "n":0, "returned":1, "not returned":0
}

df["is_active"] = (
    df["is_active"].astype(str)
    .str.strip().str.lower().map(active_map)
)

df["returned"] = (
    df["returned"].astype(str)
    .str.strip().str.lower().map(returned_map)
)

# 19. Data-Type Validation
df.info()

assert pd.api.types.is_datetime64_any_dtype(df["order_date"])
assert pd.api.types.is_numeric_dtype(df["age"])
assert pd.api.types.is_numeric_dtype(df["unit_price"])
assert pd.api.types.is_numeric_dtype(df["units_sold"])
assert pd.api.types.is_numeric_dtype(df["discount_pct"])

assert set(df["is_active"].dropna().unique()).issubset({0, 1})
assert set(df["returned"].dropna().unique()).issubset({0, 1})

# 20. Final Audit
print("Duplicates:", df.duplicated().sum())
print("Missing values:")
print(df.isna().sum())
print("Invalid dates:", df["order_date"].isna().sum())

profit_check = np.isclose(
    df["profit"],
    df["revenue"] - df["cost"],
    atol=0.01
)

print("Revenue/Cost/Profit consistent:", profit_check.all())
print("Final shape:", df.shape)

# Save cleaned data
df.to_csv("cleaned_dataset.csv", index=False)
