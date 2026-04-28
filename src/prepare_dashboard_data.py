import sqlite3
import pandas as pd
import json
import os

def prepare_data():
    db_path = "data/nemo_stores.db"
    if not os.path.exists(db_path):
        print(f"Error: {db_path} not found.")
        return

    conn = sqlite3.connect(db_path)
    df = pd.read_sql_query("SELECT * FROM stores", conn)
    conn.close()

    # Basic KPIs
    kpis = {
        "total_stores": int(len(df)),
        "avg_rent": round(float(df['monthlyRent'].mean()), 1),
        "avg_deposit": round(float(df['deposit'].mean()), 1),
        "no_premium_pct": round(float((df['premium'] == 0).mean() * 100), 1)
    }

    # Rent Distribution (Histogram data)
    rent_bins = pd.cut(df['monthlyRent'], bins=10)
    rent_dist = rent_bins.value_counts().sort_index()
    rent_labels = [f"{int(b.left)}-{int(b.right)}만" for b in rent_dist.index]
    rent_values = rent_dist.values.tolist()

    # Deposit Distribution
    dep_bins = pd.cut(df['deposit'], bins=10)
    dep_dist = dep_bins.value_counts().sort_index()
    dep_labels = [f"{int(b.left/1000)}-{int(b.right/1000)}천만" for b in dep_dist.index]
    dep_values = dep_dist.values.tolist()

    # Category Breakdown
    cat_counts = df['businessLargeCodeName'].value_counts().head(10)
    cat_labels = cat_counts.index.tolist()
    cat_values = cat_counts.values.tolist()

    # Rent by Floor
    floor_rent = df.groupby('floor')['monthlyRent'].mean().sort_values(ascending=False).head(10)
    floor_labels = floor_rent.index.tolist()
    floor_values = [round(v, 1) for v in floor_rent.values]

    # Scatter data (Sampled for performance if too large)
    scatter_data = df[['size', 'monthlyRent']].sample(min(200, len(df))).to_dict(orient='records')

    dashboard_data = {
        "kpis": kpis,
        "rent_dist": {"labels": rent_labels, "values": rent_values},
        "dep_dist": {"labels": dep_labels, "values": dep_values},
        "categories": {"labels": cat_labels, "values": cat_values},
        "floor_rent": {"labels": floor_labels, "values": floor_values},
        "scatter_data": scatter_data
    }

    with open("dashboard_data.json", "w", encoding="utf-8") as f:
        json.dump(dashboard_data, f, ensure_ascii=False, indent=4)

    print("dashboard_data.json generated successfully.")

if __name__ == "__main__":
    prepare_data()
