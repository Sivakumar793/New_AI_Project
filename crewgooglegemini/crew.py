import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)


from crewai import Crew, Process
import tasks     # ✅ import whole module
import agents    # ✅ import whole module

# Ask user for topic
topic = input("Enter the topic to Research: ")

# Forming the tech focused crew
crew = Crew(
    agents=[agents.news_researcher, agents.news_writer],
    tasks=[tasks.research_task, tasks.write_task],
    process=Process.sequential
)

# Starting the task execution process
# result = crew.kickoff(inputs={'topic': 'AI in healthcare'}) #static or fixed topic

result = crew.kickoff(inputs={'topic': topic})
print(result)