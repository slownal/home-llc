import json
data = {
    "responses": {
        "life_story": "Curiosity and problem-solving have always been my driving forces. With a background in engineering and AI research, I thrive on tackling complex challenges that push me to learn and adapt. I’m passionate about building practical solutions—whether through automation, AI, or workflow optimization. Beyond work, I am dedicated to continuous learning and personal growth, always seeking new ways to expand my knowledge and skills.",
        "superpower": "I have a knack for breaking down complex problems into structured, actionable steps, ensuring clarity, efficiency, and meaningful results—whether in data analysis, technical troubleshooting, or process optimization.",
        "growth_areas": [
            "Expanding my expertise in AI and machine learning, with a focus on real-world applications.",
            "Strengthening my leadership and mentorship skills to guide teams effectively.",
            "Enhancing my ability to communicate technical concepts in a clear and accessible way to non-technical stakeholders."
        ],
        "misconception": "Some may assume that I am solely focused on technical details and less engaged in broader strategic discussions. In reality, I enjoy collaborating on high-level problem-solving and aligning solutions with business goals.",
        "pushing_boundaries": "I actively seek out challenging projects that push me to acquire new skills and think in innovative ways. I explore emerging technologies, take on responsibilities beyond my comfort zone, and continuously refine my approach based on feedback.",
        "experience": {
    "Megamind IT: Machine Learning Research Intern (Jan 2024 – Apr 2024)": [
        "Developed and optimized machine learning algorithms, achieving a 94% performance improvement over the baseline.",
        "Conducted 20+ literature reviews to stay updated on industry advancements.",
        "Collaborated with an interdisciplinary team of 10 members to design and implement machine learning models for various projects."
    ],
    "Safear Defense India: Python Developer Intern (Dec 2023 – Jan 2024)": [
        "Developed and maintained 10+ Python modules to enhance system functionality.",
        "Built multiple backend modules using Python and automated 50+ manual tasks.",
        "Handled script tasks for debugging and automation, coordinating with a team of 4 members on 10 integration tasks."
    ],
    "Alfido Tech: Data Analyst (Sept 2023 – Nov 2023)": [
        "Performed data cleaning, visualization, and analysis using tools like Excel and Power BI, leading to a 15% improvement in data comprehension and decision-making efficiency.",
        "Utilized Spark in Python to distribute data processing on large streaming datasets, improving data ingestion and processing efficiency by 65%."
    ],
    },

        "skills": {
            "Technical Stack": [
                "Data Science", "Machine Learning", "Deep Learning", "NLP", "Image Processing",
                "Generative AI", "LLMs", "RAG", "AI Agents", "MLOps"
            ],
            "Programming Languages": ["Python (OOP)", "Java", "HTML", "C++"],
            "Databases": ["MySQL", "MongoDB"],
            "Python Packages & Frameworks": [
                "Scikit-learn", "TensorFlow", "Keras", "Pandas", "NumPy", "Matplotlib",
                "Seaborn", "OpenCV", "Streamlit", "Heroku", "Flask", "FastAPI",
                "OpenAI", "LangChain", "LlamaIndex", "PyTorch"
            ],
            "API Development": ["REST API (FastAPI)"],
            "Cloud Platform": ["AWS", "GCP", "Azure"]
        }
    }
}


with open('data.json', 'w') as f:
    json.dump(data, f)

import json
import os
from langchain_groq import ChatGroq
from gtts import gTTS
import playsound
from dotenv import load_dotenv
load_dotenv()


# Load profile data from JSON file
with open('data.json') as f:
    data = json.load(f)


llm = ChatGroq(
    model='llama-3.1-8b-instant',
    
    verbose=True,
    max_tokens=None
)

# Text-to-Speech Function
def text_to_speech(text, filename="response.mp3"):
    """Converts text to speech using gTTS and saves to an audio file."""
    tts = gTTS(text=text, lang='en')
    tts.save(filename)
    
    return filename

# Get user input
user_input = input("Enter your question: ")

# Define messages
messages = [
    (
        "system",
        f"You are  Sonal Agnihotri. When an interviewer asks about Sonal Agnihotri, read the following biopic data and answer professionally: {data}"
    ),
    ("human", user_input),
]

# Get response from LLM
response = llm.invoke(messages)
response_text = response.content
print(response_text)

#Convert response to speech
audio_file = text_to_speech(response_text)

# Play the audio
playsound.playsound(audio_file)

# Remove the audio file
os.remove(audio_file)