import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI(
    base_url="https://integrate.api.nvidia.com/v1",
    api_key=os.getenv("NVIDIA_API_KEY")
)


def analyze_log_with_ai(log_text):

    prompt = f"""
You are a senior DevOps engineer.

Analyze the following structured log data.

1. Identify critical issues.
2. Detect possible attack patterns.
3. Suggest production-grade fixes.
4. Mention severity level (Low/Medium/High).

Log Data:
{log_text}
"""

    try:
        completion = client.chat.completions.create(
            model="nvidia/nvidia-nemotron-nano-9b-v2",
            messages=[
                {"role": "user", "content": prompt}
            ],
            temperature=0.3,
            top_p=0.9,
            max_tokens=800
        )

        return completion.choices[0].message.content

    except Exception as e:
        return f"Error connecting to NVIDIA AI: {str(e)}"
