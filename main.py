import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.environ.get("GEMINI_API_KEY")
client = genai.Client(api_key=api_key)

response = client.models.generate_content(
    model='gemini-3.1-flash-lite-preview', contents="Why is Boot.dev such a great place to learn backend development? Use one paragraph maximum."
)
x = response.usage_metadata.prompt_token_count
y = response.usage_metadata.candidates_token_count 

print("Prompt tokens:", x) 
print("Response tokens:", y)

print(response.text)