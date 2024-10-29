from dotenv import load_dotenv
import google.generativeai as genai
import os

load_dotenv()


def get_car_AI_bio(brand, model, year):
    gemini_API_key = os.getenv('GEMINI_API_KEY')    
    genai.configure(api_key=gemini_API_key)
    
    gen_ai_model = genai.GenerativeModel("gemini-1.5-flash")
    
    prompt = f'Me mostre uma descrição de venda para o carro {brand} {model} {year} em apenas 250 caracteres. Fale coisas específicas desse modelo de carro.'
    response = gen_ai_model.generate_content(prompt)

    return response.text
