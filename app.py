import os
from dotenv import load_dotenv
from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
# --- CHANGE THIS LINE ---
from langchain_google_genai import ChatGoogleGenerativeAI # Import the Google Generative AI chat model
from langchain_core.output_parsers import StrOutputParser

# Load environment variables from .env file
load_dotenv()
# --- CHANGE THIS LINE ---
api_key = os.getenv("GOOGLE_API_KEY") # Now looking for GOOGLE_API_KEY

if not api_key:
    # --- CHANGE THIS MESSAGE ---
    raise ValueError("GOOGLE_API_KEY is not set in the environment variables.")

app = Flask(__name__)
CORS(app) # Enable CORS to allow the front-end to make requests

def get_code_feedback(code: str) -> str:
    """
    Analyzes code for authenticity, quality, and vulnerabilities and returns a report.
    """
    prompt = ChatPromptTemplate.from_messages([
        ("system", 
         "You are an expert AI code reviewer. Analyze the provided code for authenticity (is it common, standard code?), quality, potential bugs, and security vulnerabilities. "
         "Provide constructive feedback in a well-formatted, easy-to-read report. "
         "Start your response with a summary and then provide detailed bullet points."),
        ("user", "{code}")
    ])
    
    # --- CHANGE THIS LINE ---
    # Initialize the Gemini model with your API key
    # You can choose different Gemini models, e.g., "gemini-pro", "gemini-1.5-flash", etc.
    model = ChatGoogleGenerativeAI(model="gemini-1.5-flash", google_api_key=api_key)
    
    chain = {"code": RunnablePassthrough()} | prompt | model | StrOutputParser()
    
    response = chain.invoke(code)
    
    return response

@app.route('/analyze', methods=['POST'])
def analyze_code_endpoint():
    try:
        data = request.get_json()
        code_to_analyze = data.get('code', '')
        
        print(f"Received code: {code_to_analyze[:100]}...")  # Log first 100 chars

        if not code_to_analyze:
            return jsonify({"error": "No code provided"}), 400

        feedback_report = get_code_feedback(code_to_analyze)
        return jsonify({"report": feedback_report})

    except Exception as e:
        print(f"An error occurred: {e}")
        return jsonify({"error": str(e)}), 500

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)