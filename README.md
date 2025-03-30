# AI Interview Chatbot

An interactive AI-powered chatbot that simulates an interview conversation about yourself. The chatbot provides both text and voice responses to your questions.

## Features

- 💬 Interactive chat interface
- 🎯 Professional responses based on provided profile data
- 🔊 Text-to-Speech functionality (Note: There might be a brief delay before audio starts playing)
- 💾 Persistent chat history during the session
- 🤖 Powered by Groq's LLaMA 3.1 model

## Setup

1. Create a `.streamlit` directory in your project root:
```bash
mkdir .streamlit
```

2. Create a `secrets.toml` file inside `.streamlit` directory and add your Groq API key:
```toml
GROQ_API_KEY = "your-api-key-here"
```

3. Install the required dependencies:
```bash
pip install streamlit langchain-groq gtts playsound
```

## Running the Application

1. Start the Streamlit app:
```bash
streamlit run app.py
```

2. Open your browser and navigate to the provided local URL (typically http://localhost:8501)

## Usage

1. Type your question about yourself in the chat input
2. The bot will respond with text and automatically play an audio response
3. Wait a moment for the audio to begin playing (there might be a slight delay)
4. Continue the conversation by asking more questions

## Technical Stack

- Streamlit for the web interface
- Groq's LLaMA 3.1 for AI responses
- gTTS (Google Text-to-Speech) for voice generation
- LangChain for AI interaction

## Note

- The audio response may take a few seconds to start playing after the text appears
- Make sure your system's audio is enabled and at a comfortable volume
- Keep your API key secure and never commit it to version control

## Files

- `app.py`: Main Streamlit application
- `profile.json`: Contains professional profile data
- `.streamlit/secrets.toml`: Stores API key (not included in repo)

## Security

- Never commit your `secrets.toml` file to version control
- Keep your API keys private and secure
- The `.gitignore` file is configured to exclude sensitive files