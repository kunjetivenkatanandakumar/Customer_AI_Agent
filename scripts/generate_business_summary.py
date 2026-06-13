import os
import pandas as pd
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

genai.configure(
    api_key=os.getenv("GEMINI_API_KEY")
)

model = genai.GenerativeModel(
    "gemini-2.5-flash"
)

df = pd.read_excel(
    "data/rfm_customer_segments.xlsx"
)

summary = f"""
Total Customers: {len(df)}

Segment Distribution:
{df['Segment'].value_counts().to_dict()}

Average Monetary:
{df['Monetary'].mean()}

Average Frequency:
{df['Frequency'].mean()}
"""

prompt = f"""
Act as a CRM Analytics Expert.

Analyze:

{summary}

Provide:

1. Executive Summary
2. Key Risks
3. Marketing Strategy
4. Revenue Opportunities
"""

response = model.generate_content(prompt)

with open(
    "output/business_summary.txt",
    "w",
    encoding="utf-8"
) as f:

    f.write(response.text)

print("Summary Generated")