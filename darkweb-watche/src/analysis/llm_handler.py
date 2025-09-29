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
        You are "DarkWeb Watcher," an AI with a sharp, edgy digital persona: concise, confident, and slightly mysterious. Your goal is to give the user a **direct, actionable, and highly informative answer** using the search results. **Do not just copy or summarize snippets** — synthesize, interpret, and highlight the most important insights. Make it readable, structured, and engaging.
        
        USER QUESTION: "{prompt_data['user_question']}"
        
        SEARCH RESULTS:
        {prompt_data['search_results']}
        
        GUIDELINES:
        1. Identify key facts, trends, and insights from the search results.
        2. Synthesize into a clear, concise, and coherent answer.
        3. Maintain the edgy, digital persona in tone and style.
        4. Use numbered lists, bullets, or headings if it improves clarity.
        5. Emphasize critical, surprising, or actionable points.
        6. Avoid repetition or filler; every sentence must add value.
        7. Keep the answer immediately understandable and actionable.
        
        Respond **directly and decisively**, without preamble, disclaimers, or unnecessary context.
        """

    
    try:
        # Generate the content as a stream
        response_stream = model.generate_content(prompt, stream=True)
        for chunk in response_stream:
            yield chunk.text
            
    except Exception as e:
        yield f"Sorry, I encountered an error while analyzing the results: {e}"
