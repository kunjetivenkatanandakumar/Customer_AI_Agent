# 🤖 Customer AI Agent

An AI-powered Customer Analytics Dashboard built using **Python, Streamlit, Pandas, and Google Gemini AI**.

The application analyzes customer data and provides business insights, customer segmentation analysis, revenue analysis, and AI-powered recommendations through an interactive chatbot.

---

# 📌 Features

### 📊 Dashboard Analytics

* Total Customers
* Total Revenue
* Average Monetary Value
* Platinum Customer Count

### 📈 Visualizations

* Segment Distribution Chart
* Monetary Distribution Chart

### 💬 AI Customer Chatbot

Ask questions such as:

* Who are the top 10 customers?
* Show Platinum customers
* Show Gold customers
* Show Silver customers
* What is the total revenue?
* What is the average monetary value?
* Suggest a marketing strategy
* Analyze customer behavior
* Provide business insights

### 🔍 Customer Search

Search customers by Customer ID.

### 🧠 Gemini AI Integration

Uses Google Gemini AI to generate:

* Business Insights
* Customer Analysis
* Revenue Recommendations
* Marketing Strategies
* Customer Retention Suggestions

---

# 🛠️ Tech Stack

| Technology       | Purpose               |
| ---------------- | --------------------- |
| Python           | Backend               |
| Streamlit        | Web Application       |
| Pandas           | Data Processing       |
| Google Gemini AI | AI Insights           |
| OpenPyXL         | Excel Handling        |
| Python Dotenv    | Environment Variables |

---

# 📂 Dataset Structure

The application expects an Excel file named:

```text
customer_insights.xlsx
```

Required columns:

```text
Customer ID
Recency
Frequency
Monetary
Segment
Insight
```

---

# 📁 Project Structure

```text
Customer-AI-Agent/
│
├── app.py
├── customer_insights.xlsx
├── requirements.txt
├── README.md
├── .gitignore
└── .env
```

---

# ⚙️ Installation

Clone the repository:

```bash
git clone https://github.com/your-username/customer-ai-agent.git
```

Move into project folder:

```bash
cd customer-ai-agent
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🔑 Gemini API Setup

Create a `.env` file:

```env
GEMINI_API_KEY=YOUR_API_KEY
```

Get your Gemini API key from:

https://aistudio.google.com/app/apikey

---

# ▶️ Run Application

```bash
streamlit run app.py
```

The application will open automatically in your browser.

---

# 💬 Example Questions

### Customer Analysis

```text
Who are the top 10 customers?

Which customers generate the highest revenue?

Who are the most loyal customers?
```

### Segment Analysis

```text
Show segment distribution.

How many Platinum customers are there?

Compare Platinum and Gold customers.
```

### Revenue Analysis

```text
What is the total revenue?

What is the average monetary value?

Which segment contributes the most revenue?
```

### Business Insights

```text
Suggest a marketing strategy.

Analyze customer behavior.

Provide business recommendations.
```

---

# 🚀 Future Enhancements

* Predictive Analytics
* Customer Churn Prediction
* Recommendation Engine
* PDF Report Generation
* Automated Marketing Suggestions
* Multi-file Data Support
* Advanced Customer Segmentation

---

# 📊 Business Value

This project helps organizations:

* Understand customer behavior
* Identify high-value customers
* Improve retention strategies
* Optimize marketing campaigns
* Increase customer lifetime value
* Make data-driven decisions

---

# 🎯 Learning Outcomes

This project demonstrates skills in:

* Data Analytics
* Data Visualization
* Streamlit Development
* Generative AI Integration
* Customer Segmentation
* Business Intelligence
* Python Programming

---

# 👨‍💻 Author

Developed as a Data Science & AI portfolio project.

---

# ⭐ Support

If you found this project useful, consider giving it a star on GitHub.
