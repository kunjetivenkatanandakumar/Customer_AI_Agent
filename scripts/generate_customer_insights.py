import pandas as pd

df = pd.read_excel("data/rfm_customer_segments.xlsx")

def generate_insight(segment):

    if segment == "Platinum":
        return (
            "High-value customer. "
            "Offer VIP rewards and premium offers."
        )

    elif segment == "Gold":
        return (
            "Moderately engaged customer. "
            "Use targeted promotions."
        )

    else:
        return (
            "Low engagement customer. "
            "Run reactivation campaigns."
        )

df["Insight"] = df["Segment"].apply(generate_insight)

df.to_excel(
    "output/customer_insights.xlsx",
    index=False
)

print("Done")