import streamlit as st
import time
import os
import random

# Import your existing modules
from src.ingestion.google_search_client import live_google_search
from src.analysis.llm_handler import generate_ai_summary

# --- Glitch Protocol CSS and App Setup ---
st.set_page_config(page_title="Glitch Protocol", page_icon="👾", layout="centered")

def glitch_protocol_css():
    st.markdown("""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=VT323&display=swap');
            @import url('https://fonts.googleapis.com/css2?family=Space+Mono:wght@400;700&display=swap');
            
            html, body, [class*="st-"] {
                font-family: 'Space Mono', monospace;
            }
            .main {
                background-color: #0a0a0a;
            }
            h1 {
                font-family: 'VT323', monospace;
                font-size: 3rem;
                color: #ffffff;
                text-shadow: -2px -2px 0px #ff00c1, 2px 2px 0px #00fff9;
            }
            [data-testid="stChatMessage"] {
                border: 1px solid #333;
                background-color: #111;
                border-radius: 0;
            }
            .glitch-text {
                font-family: 'VT323', monospace;
                color: #00fff9;
                font-size: 1.2rem;
            }
            .st-emotion-cache-1s4r584, .st-emotion-cache-1pr3n0g, .st-emotion-cache-1outpf7 {
                color: #e1e1e1;
            }
        </style>
    """, unsafe_allow_html=True)

glitch_protocol_css()

if "messages" not in st.session_state:
    st.session_state.messages = [{"role": "assistant", "content": "SYSTEM ONLINE. I am DarkWeb Watcher. Feed me a query."}]

st.title("D_RKW_B W_TCHER")

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# --- Main Chat Logic with Streaming ---
if prompt := st.chat_input("Enter query..."):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    with st.chat_message("assistant"):
        spinner_placeholder = st.empty()
        glitch_texts = ["DECRYPTING DATA...", "ACCESSING MAINFRAME...", "QUERYING THE VOID...", "ANALYZING ANOMALIES...", "COMPILING REPORT..."]
        for _ in range(5):
            spinner_placeholder.markdown(f'<p class="glitch-text">{random.choice(glitch_texts)}</p>', unsafe_allow_html=True)
            time.sleep(0.3)
        spinner_placeholder.empty()

        # Search for information
        search_results = live_google_search(prompt)
        ai_prompt_data = {"user_question": prompt, "search_results": search_results}
        
        # Handle the response stream
        response_stream = generate_ai_summary(ai_prompt_data)
        
        # Use st.write_stream to display the response with a typing effect
        full_response = st.write_stream(response_stream)
        
        st.session_state.messages.append({"role": "assistant", "content": full_response})