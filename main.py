import streamlit as st
from google import genai
from typing import Generator
import time

# Page configuration
st.set_page_config(
    page_title="Gemini Chat Assistant",
    page_icon="✨",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for better UI
st.markdown("""
    <style>
    .main {
        padding: 0rem 1rem;
    }
    .stChatMessage {
        padding: 1rem;
        border-radius: 0.5rem;
        margin-bottom: 1rem;
    }
    .stChatInputContainer {
        padding: 1rem 0;
    }
    div[data-testid="stStatusWidget"] {
        display: none;
    }
    .chat-header {
        padding: 1rem 0;
        border-bottom: 1px solid #e0e0e0;
        margin-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar configuration
with st.sidebar:
    st.title("⚙️ Configuration")
    
    # API Key input
    api_key = st.text_input(
        "Google API Key",
        type="password",
        help="Enter your Google Gemini API key. Get one at https://makersuite.google.com/app/apikey"
    )
    
    st.divider()
    
    # Model selection
    model_choice = st.selectbox(
        "Model",
        ["gemini-1.5-pro", "gemini-1.5-flash", "gemini-1.0-pro"],
        index=1,
        help="Choose the Gemini model. Flash is faster, Pro is more capable."
    )
    
    # Temperature slider
    temperature = st.slider(
        "Temperature",
        min_value=0.0,
        max_value=2.0,
        value=0.7,
        step=0.1,
        help="Higher values make output more random, lower values more focused"
    )
    
    # Max tokens
    max_tokens = st.slider(
        "Max Output Tokens",
        min_value=256,
        max_value=8192,
        value=2048,
        step=256,
        help="Maximum length of generated response"
    )
    
    # Top P
    top_p = st.slider(
        "Top P",
        min_value=0.0,
        max_value=1.0,
        value=0.95,
        step=0.05,
        help="Nucleus sampling parameter"
    )
    
    st.divider()
    
    # System instruction
    system_instruction = st.text_area(
        "System Instructions",
        value="You are a helpful, friendly, and knowledgeable AI assistant. Provide clear, accurate, and concise responses.",
        height=150,
        help="Set the behavior and personality of the assistant"
    )
    
    st.divider()
    
    # Conversation controls
    col1, col2 = st.columns(2)
    with col1:
        if st.button("🗑️ Clear Chat", use_container_width=True):
            st.session_state.messages = []
            st.session_state.gemini_history = []
            st.rerun()
    
    with col2:
        if st.button("📥 Export Chat", use_container_width=True):
            if "messages" in st.session_state and st.session_state.messages:
                chat_text = "\n\n".join([
                    f"**{msg['role'].upper()}**: {msg['content']}"
                    for msg in st.session_state.messages
                ])
                st.download_button(
                    "Download",
                    chat_text,
                    file_name="chat_history.txt",
                    mime="text/plain",
                    use_container_width=True
                )
    
    st.divider()
    
    # Message counter
    if "messages" in st.session_state:
        st.metric("Messages", len(st.session_state.messages))
    
    # Info
    with st.expander("ℹ️ About"):
        st.markdown("""
        ### Gemini Chat Assistant
        
        A powerful chatbot powered by Google's Gemini AI models.
        
        **Features:**
        - 🚀 Real-time streaming responses
        - 🎨 Customizable model parameters
        - 💾 Conversation history
        - 📥 Export conversations
        - 🔒 Secure API key handling
        
        **Tips:**
        - Use Flash model for faster responses
        - Use Pro model for complex tasks
        - Adjust temperature for creativity
        - Lower temperature for factual answers
        """)

# Main chat interface
st.title("✨ Gemini Chat Assistant")
st.caption("Powered by Google Gemini AI")

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "gemini_history" not in st.session_state:
    st.session_state.gemini_history = []

# Configure Gemini
def configure_gemini(api_key: str, model: str, temp: float, max_tok: int, top_p_val: float, sys_inst: str):
    """Configure and return a Gemini model instance"""
    try:
        genai.configure(api_key=api_key)
        
        generation_config = {
            "temperature": temp,
            "top_p": top_p_val,
            "max_output_tokens": max_tok,
        }
        
        model_instance = genai.GenerativeModel(
            model_name=model,
            generation_config=generation_config,
            system_instruction=sys_inst
        )
        
        return model_instance
    except Exception as e:
        st.error(f"Error configuring Gemini: {str(e)}")
        return None

def stream_response(model, prompt: str, history: list) -> Generator[str, None, None]:
    """Generate streaming response from Gemini"""
    try:
        # Convert history to Gemini format
        gemini_history = []
        for msg in history:
            role = "user" if msg["role"] == "user" else "model"
            gemini_history.append({"role": role, "parts": [msg["content"]]})
        
        # Create chat session
        chat = model.start_chat(history=gemini_history)
        
        # Stream response
        response = chat.send_message(prompt, stream=True)
        
        for chunk in response:
            if chunk.text:
                yield chunk.text
                
    except Exception as e:
        yield f"⚠️ Error generating response: {str(e)}"

# Display chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Chat input
if prompt := st.chat_input("Ask me anything..."):
    
    # Check if API key is provided
    if not api_key:
        st.error("⚠️ Please enter your Google API Key in the sidebar to start chatting.")
        st.stop()
    
    # Add user message to chat
    st.session_state.messages.append({"role": "user", "content": prompt})
    
    with st.chat_message("user"):
        st.markdown(prompt)
    
    # Generate assistant response
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        full_response = ""
        
        # Configure model
        model = configure_gemini(
            api_key,
            model_choice,
            temperature,
            max_tokens,
            top_p,
            system_instruction
        )
        
        if model:
            try:
                # Stream the response
                with st.spinner("Thinking..."):
                    for chunk in stream_response(model, prompt, st.session_state.gemini_history):
                        full_response += chunk
                        message_placeholder.markdown(full_response + "▌")
                        time.sleep(0.01)  # Slight delay for visual effect
                    
                    message_placeholder.markdown(full_response)
                
                # Add to session state
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": full_response
                })
                st.session_state.gemini_history = st.session_state.messages.copy()
                
            except Exception as e:
                error_message = f"⚠️ An error occurred: {str(e)}"
                message_placeholder.markdown(error_message)
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": error_message
                })
        else:
            error_message = "⚠️ Failed to initialize Gemini model. Please check your API key."
            message_placeholder.markdown(error_message)

# Display welcome message if no messages
if len(st.session_state.messages) == 0:
    st.info("👋 Welcome! Enter your Google API key in the sidebar and start chatting!")
    
    with st.expander("💡 Example prompts"):
        st.markdown("""
        - Explain quantum computing in simple terms
        - Write a Python function to sort a list
        - What are the latest trends in AI?
        - Help me brainstorm ideas for a blog post
        - Analyze this code: `def factorial(n): return 1 if n == 0 else n * factorial(n-1)`
        """)
