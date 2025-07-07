import google.generativeai as genai
import os

genai.configure(api_key=os.getenv('AIzaSyCVTS3tvdEaheu0DJgUTKjoiE-H3sUakbQ'))

def query_gemini(question):
    response = genai.generate_text(prompt=question)
    return response.result
