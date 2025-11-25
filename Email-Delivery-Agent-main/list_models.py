from dotenv import load_dotenv
import os
import google.generativeai as genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
if not api_key:
    print("No GEMINI_API_KEY found")
    raise SystemExit(1)

genai.configure(api_key=api_key)
print("Fetching model list...")
models = []
for m in genai.list_models():
    methods = getattr(m, 'supported_generation_methods', [])
    if 'generateContent' in methods:
        models.append(m.name)
print("Models supporting generateContent:")
for name in models:
    print(" -", name)
