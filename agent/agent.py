import os
try:
    # type: ignore - optional dependency may not be installed in all environments
    import google.generativeai as genai  # type: ignore
except Exception:  # pragma: no cover - graceful fallback when package is missing
    genai = None

from dotenv import load_dotenv

from agent.tools import (
    get_top_customers,
    get_segment_distribution,
    get_average_monetary
)

load_dotenv()

if genai is None:
    raise RuntimeError(
        "google.generativeai is not installed or could not be imported. "
        "Install the official package and ensure it's available in the environment: "
        "pip install google-generativeai"
    )

genai.configure(api_key=os.getenv("GEMINI_API_KEY"))

model = genai.GenerativeModel("gemini-2.5-flash")

def ask_agent(question):

    question = question.lower()

    # Tool 1

    if "top" in question and "customer" in question:

        result = get_top_customers()

        prompt = f"""
        Analyze these top customers:

        {result.to_string()}

        Explain in business language.
        """

        response = model.generate_content(
            prompt
        )

        return response.text

    # Tool 2

    elif "segment" in question:

        result = get_segment_distribution()

        prompt = f"""
        Analyze this segment distribution:

        {result}

        Give business insights.
        """

        response = model.generate_content(
            prompt
        )

        return response.text

    # Tool 3

    elif "average monetary" in question:

        result = get_average_monetary()

        return f"Average Monetary Value: {result}"

    else:

        return (
            "I do not understand the question."
        )