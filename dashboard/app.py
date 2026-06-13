import streamlit as st
import pandas as pd
import importlib
from dotenv import load_dotenv
import os

try:
    genai = importlib.import_module("google.generativeai")
except Exception:
    genai = None

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Customer AI Agent",
    page_icon="🤖",
    layout="wide"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>
.main-title{
    text-align:center;
    font-size:45px;
    font-weight:bold;
}
.subtitle{
    text-align:center;
    color:gray;
}
.chat-box{
    padding:10px;
    border-radius:10px;
}
</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD ENVIRONMENT
# =====================================================

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    st.error("GEMINI_API_KEY not found in .env")
    st.stop()

# =====================================================
# GEMINI SETUP
# =====================================================

if genai is None:
    st.error("google-generative-ai package not found. Install with: pip install google-generative-ai")
    st.stop()

try:
    genai.configure(api_key=API_KEY)
    model = genai.GenerativeModel("gemini-1.5-flash")
except Exception as e:
    st.error(f"Gemini Error: {e}")
    st.stop()

# =====================================================
# LOAD DATASET
# =====================================================

try:
    df = pd.read_excel("customer_insights.xlsx")
except Exception as e:
    st.error(f"Error loading customer_insights.xlsx: {e}")
    st.stop()

# =====================================================
# REQUIRED COLUMNS
# =====================================================

required_columns = [
    "Customer ID",
    "Recency",
    "Frequency",
    "Monetary",
    "Segment",
    "Insight"
]

missing = [
    col for col in required_columns
    if col not in df.columns
]

if missing:
    st.error(f"Missing Columns: {missing}")
    st.stop()

# =====================================================
# HEADER
# =====================================================

st.markdown(
    "<div class='main-title'>🤖 Customer AI Agent</div>",
    unsafe_allow_html=True
)

st.markdown(
    "<div class='subtitle'>Customer Analytics Dashboard + AI Chatbot</div>",
    unsafe_allow_html=True
)

st.divider()

# =====================================================
# KPI SECTION
# =====================================================

total_customers = len(df)

total_revenue = round(
    df["Monetary"].sum(),
    2
)

avg_monetary = round(
    df["Monetary"].mean(),
    2
)

platinum_customers = len(
    df[df["Segment"] == "Platinum"]
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        "Customers",
        total_customers
    )

with col2:
    st.metric(
        "Revenue",
        f"₹{total_revenue:,.2f}"
    )

with col3:
    st.metric(
        "Avg Monetary",
        f"₹{avg_monetary:,.2f}"
    )

with col4:
    st.metric(
        "Platinum",
        platinum_customers
    )

st.divider()

# =====================================================
# CHARTS
# =====================================================

c1, c2 = st.columns(2)

with c1:
    st.subheader(
        "Segment Distribution"
    )

    st.bar_chart(
        df["Segment"].value_counts()
    )

with c2:
    st.subheader(
        "Monetary Distribution"
    )

    st.line_chart(
        df["Monetary"]
    )

st.divider()

# =====================================================
# DATA PREVIEW
# =====================================================

with st.expander("Preview Dataset"):
    st.dataframe(
        df.head(20),
        use_container_width=True
    )

# =====================================================
# AI CHATBOT
# =====================================================

st.header("💬 AI Customer Chatbot")

if "messages" not in st.session_state:
    st.session_state.messages = []

for msg in st.session_state.messages:
    with st.chat_message(msg["role"]):
        st.markdown(msg["content"])

user_question = st.chat_input(
    "Ask anything about your customers..."
)

if user_question:

    st.session_state.messages.append(
        {
            "role":"user",
            "content":user_question
        }
    )

    with st.chat_message("user"):
        st.markdown(user_question)

    try:

        # -----------------------------------
        # Built-in Analytics Commands
        # -----------------------------------

        question_lower = user_question.lower()

        if (
            "top" in question_lower
            and "customer" in question_lower
        ):

            result = (
                df.sort_values(
                    "Monetary",
                    ascending=False
                )
                .head(10)
            )

            answer = (
                "### Top 10 Customers\n\n"
                + result.to_markdown(index=False)
            )

        elif "platinum" in question_lower:

            result = df[
                df["Segment"]=="Platinum"
            ].head(20)

            answer = (
                f"Total Platinum Customers: {len(result)}\n\n"
                + result.to_markdown(index=False)
            )

        elif "gold" in question_lower:

            result = df[
                df["Segment"]=="Gold"
            ].head(20)

            answer = (
                f"Total Gold Customers: {len(result)}\n\n"
                + result.to_markdown(index=False)
            )

        elif "silver" in question_lower:

            result = df[
                df["Segment"]=="Silver"
            ].head(20)

            answer = (
                f"Total Silver Customers: {len(result)}\n\n"
                + result.to_markdown(index=False)
            )

        elif "revenue" in question_lower:

            answer = (
                f"Total Revenue = ₹{total_revenue:,.2f}"
            )

        elif "average" in question_lower:

            answer = (
                f"Average Monetary Value = ₹{avg_monetary:,.2f}"
            )

        elif "insight" in question_lower:

            answer = (
                df[
                    [
                        "Customer ID",
                        "Segment",
                        "Insight"
                    ]
                ]
                .head(50)
                .to_markdown(index=False)
            )

        else:

            dataset_summary = f"""
Dataset Columns:
{df.columns.tolist()}

Total Customers:
{len(df)}

Revenue:
{total_revenue}

Segment Distribution:
{df['Segment'].value_counts().to_dict()}

Sample Data:
{df.head(50).to_string()}
"""

            prompt = f"""
You are a Customer Analytics Expert.

Dataset Information:

{dataset_summary}

User Question:

{user_question}

Provide:
1. Direct Answer
2. Business Insights
3. Recommendations
"""

            response = model.generate_content(
                prompt
            )

            answer = response.text

    except Exception as e:

        answer = f"Error: {e}"

    st.session_state.messages.append(
        {
            "role":"assistant",
            "content":answer
        }
    )

    with st.chat_message("assistant"):
        st.markdown(answer)

# =====================================================
# CUSTOMER SEARCH
# =====================================================

st.divider()

st.subheader("🔍 Customer Search")

customer_id = st.text_input(
    "Enter Customer ID"
)

if customer_id:

    result = df[
        df["Customer ID"]
        .astype(str)
        .str.contains(
            customer_id,
            case=False,
            na=False
        )
    ]

    st.dataframe(
        result,
        use_container_width=True
    )

# =====================================================
# FOOTER
# =====================================================

st.divider()

st.caption(
    "Built with Streamlit + Gemini AI + Customer Analytics"
)
