import os
import google.generativeai as genai
from dotenv import load_dotenv

load_dotenv()

try:
    genai.configure(api_key=os.getenv("GEMINI_API_KEY"))
    model = genai.GenerativeModel('gemini-2.0-flash')
except Exception as e:
    model = None
    print(f"Error configuring Gemini API: {e}")

def generate_ai_summary(prompt_data):
    """
    Uses the Gemini LLM to generate a conversational summary of findings.
    This version returns a stream (generator) instead of a single string.
    """
    if not model:
        yield "The AI model is not configured correctly. Please check your API key."
        return

    prompt = f"""
    You are DarkWeb Watcher, an AI assistant with an edgy, digital persona.
    Your user has asked a question. Use the following search results to formulate a clear, concise, and conversational answer.
    Synthesize the information, don't just list the snippets.

    USER QUESTION: "{prompt_data['user_question']}"
    SEARCH RESULTS:
    {prompt_data['search_results']}
    """
    
    try:
        # Generate the content as a stream
        response_stream = model.generate_content(prompt, stream=True)
        for chunk in response_stream:
            yield chunk.text
            
    except Exception as e:
        yield f"Sorry, I encountered an error while analyzing the results: {e}"
