
from crewai import Agent
from tools import tool
from dotenv import load_dotenv
load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI

import os

## Call the gemini model
llm=ChatGoogleGenerativeAI(
    model="gemini/gemini-2.0-flash", #gemini/gemini-2.0-flash
    verbose=True,
    temperature=0.5, 
    google_api_key=os.getenv("GEMINI_API_Key")
)

# patch fix:
if llm.model.startswith("models/"):
    llm.model = llm.model[len("models/"):]
    print("Patched model:", llm.model)

#Creating a senior researcher agent with memory and verbose mode
news_researcher=Agent(

    role="Senior Researcher",
    goal='Unccover ground breaking technologies in {topic}',
    verbose=True,
    memory=True,
    backstory=(
        "Driven by curiosity, you're at the forefront of"
        "innovation, eager to explore and share knowledge that could change"
        "the world."
    ),
    tools=[tool],
    llm=llm,
    allow_delegation=True
)

## creating write agent with custom tools responsible in writing news blog
news_writer = Agent(

    role='Writer', 
    goal='Narrate compelling tech stories about {topic}',
    verbose=True,
    memory=True,
    backstory=(

    "With a flair for simplifying complex topics, you craft"
    "engaging narratives that captivate and educate, bringing new"
    "discoveries to light in an accessible manner."

    ),
    tools=[],
    llm=llm,
    allow_delegation=False
)