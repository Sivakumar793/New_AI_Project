AI Research & Content Generation Pipeline
📌 Overview

This project is an AI-powered research and content generation pipeline built using the CrewAI framework and Google Gemini API.
The system is designed to:

Research a given topic online

Summarize information

Generate structured and coherent content

📂 Project Structure
New_AI_Project/
│── .env               # API keys and environment variables  
│── requirements.txt   # Python dependencies  
│── crew.py            # Main orchestration file (entry point)  
│── agents.py          # Defines agents (AI workers)  
│── tasks.py           # Defines tasks for agents  
│── tools.py           # Helper tools (e.g., search, parsing)  

🚀 Workflow
The flow of the project:
[.env] -- API Keys --> [tools.py] -- Search Tool --> [agents.py] -- Agents -->
[tasks.py] -- Tasks --> [crew.py] -- Orchestration --> Output


⚙️ Setup & Installation

1) Clone the repository
   git clone https://github.com/Sivakumar793/New_AI_Project.git
   cd New_AI_Project
2) Create & activate virtual environment
   python -m venv venv
   source venv/bin/activate   # Mac/Linux
   venv\Scripts\activate      # Windows
3) Install dependencies
   pip install -r requirements.txt
4) Set up .env file
   Create a .env file in the project root and add your keys:
   GEMINI_API_KEY=your_gemini_api_key # you can your key
   SERPER_API_KEY=your_serper_api_key
5) ▶️ Run the Project
   python crew.py

🛠️ Technologies Used
Python 3.10+
CrewAI (multi-agent orchestration)
Google Gemini API (generative AI)
Serper API (search integration)



  
