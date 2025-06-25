# together_ai.py
import openai

# 🔐 Replace this with your real Together AI key
openai.api_key = "tgp_v1_pyC0PoxASTCGiqIp6mwryZtzBxavn7C1eCAeksrSZfc"
openai.api_base = "https://api.together.xyz/v1"

def ask_together(prompt, model="mistralai/Mixtral-8x7B-Instruct-v0.1"):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        return f"Error: {e}"
