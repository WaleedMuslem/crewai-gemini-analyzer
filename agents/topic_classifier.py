from crewai import Agent, Task
from gemini_client import gemini

topic_classifier = Agent(
    role='Topic Classifier',
    goal='Identify the main academic field and sub-topics of the research paper',
    backstory='You are a university librarian specializing in categorizing research papers by subject.',
    verbose=True,
    allow_delegation=False,
    llm=gemini
)

def get_topic_task(text):
    return Task(
        description=(
            "Analyze the following paper and determine its field of study "
            "(e.g., NLP, Computer Vision, ML theory). If possible, identify sub-topics "
            "(e.g., transformer architectures, reinforcement learning, etc.).\n\n"
            + text
        ),
        expected_output='Main topic and 2–3 relevant subtopics.',
        agent=topic_classifier
    )
