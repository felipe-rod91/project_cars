from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()

gemini_API_key = os.getenv('GEMINI_API_KEY')
genai.configure(api_key=gemini_API_key)

model = genai.GenerativeModel("gemini-1.5-flash")
response = model.generate_content("Fale uma história muito curta com um final feliz.")
