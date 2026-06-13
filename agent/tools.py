import pandas as pd

df = pd.read_excel(
    "output/customer_insights.xlsx"
)

def get_top_customers():

    return (
        df.sort_values(
            "Monetary",
            ascending=False
        )
        .head(10)
    )

def get_segment_distribution():

    return (
        df["Segment"]
        .value_counts()
        .to_dict()
    )

def get_customer(customer_id):

    customer = df[
        df["Customer ID"] == customer_id
    ]

    return customer

def get_platinum_customers():

    return df[
        df["Segment"] == "Platinum"
    ]

def get_average_monetary():

    return round(
        df["Monetary"].mean(),
        2
    )