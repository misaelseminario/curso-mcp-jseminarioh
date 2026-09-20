import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
client = genai.Client(api_key=os.environ["GEMINI_API_KEY"])

CANDIDATES = [
    "gemini-2.5-flash",
    "gemini-2.5-flash-lite",
    "gemini-3.1-flash-lite",
    "gemini-3.5-flash-lite",
    "gemini-3.6-flash",
]

for name in CANDIDATES:
    try:
        r = client.models.generate_content(model=name, contents="Di hola")
        print(f"OK    {name}: {r.text[:40]!r}")
    except Exception as exc:
        print(f"FALLA {name}: {str(exc)[:80]}")