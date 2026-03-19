from crewai import Agent, Task
from gemini_client import gemini

insight_extractor = Agent(
    role='Insight Extractor',
    goal='Extract the novel contributions and key findings of the paper',
    backstory='You are an experienced data scientist who reads papers and summarizes what’s new or important.',
    verbose=True,
    allow_delegation=False,
    llm=gemini
)

def get_insight_task(text):
    return Task(
        description=(
            "From this paper, identify: 1) the new method or algorithm proposed, "
            "2) how it differs from previous work, and 3) its main experimental findings or conclusions.\n\n"
            + text
        ),
        expected_output='A bulleted list of contributions and a paragraph explaining their importance.',
        agent=insight_extractor
    )
