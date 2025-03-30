import streamlit as st
import json
import os
from langchain_groq import ChatGroq
from gtts import gTTS
import base64



# Load profile data from JSON file
with open('data.json') as f:
    data = json.load(f)

api_key= st.secrets['GROQ_API_KEY']
llm = ChatGroq(

    model='llama-3.1-8b-instant',
    api_key=api_key,
    verbose=True,
    max_tokens=None
  )

# Text-to-Speech Function
def text_to_speech(text, filename="response.mp3"):
    """Convert text to speech using gTTS and return the filename."""
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    return filename

def autoplay_audio(file_path: str):
    with open(file_path, "rb") as f:
        data = f.read()
    b64 = base64.b64encode(data).decode("utf-8")
    md = f"""
    <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
    </audio>
    """
    st.markdown(md, unsafe_allow_html=True)

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": f"You are Sonal Agnihotri. When an interviewer asks about Sonal Agnihotri, read the following biopic data and answer professionally: {data}"}
    ]

st.title(" AI Chatbot")
st.write("Ask about **Sonal Agnihotri**, and the AI will answer professionally!")

# Display chat history
for msg in st.session_state.messages:
    if msg["role"] == "human":
        st.chat_message("user").write(msg["content"])
    elif msg["role"] == "ai":
        st.chat_message("assistant").write(msg["content"])

# User input
user_input = st.chat_input("Type your question here...")
if user_input:
    # Add user message to session state
    st.session_state.messages.append({"role": "human", "content": user_input})

    # Prepare messages for LLM
    messages = [
        ("system", st.session_state.messages[0]["content"]),  # First system message
    ] + [("human" if m["role"] == "human" else "ai", m["content"]) for m in st.session_state.messages[1:]]

    # Get response from LLM
    with st.spinner("Thinking..."):
        response = llm.invoke(messages)
        response_text = response.content
        st.session_state.messages.append({"role": "ai", "content": response_text})

    # Display AI response
    st.chat_message("assistant").write(response_text)

    # Convert response to speech
    audio_file = text_to_speech(response_text)

    # Provide an audio player
    autoplay_audio(audio_file)

    # Provide a download button
    # with open(audio_file, "rb") as file:
    #     st.download_button(
    #         label="⬇️ Download Response",
    #         data=file,
    #         file_name="response.mp3",
    #         mime="audio/mp3"
    #     )

    # Cleanup
    os.remove(audio_file)