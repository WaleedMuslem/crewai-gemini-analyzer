from crewai import Agent, Task
from gemini_client import gemini

citation_extractor = Agent(
    role='Citation Extractor',
    goal='Extract all cited papers and briefly describe their relevance',
    backstory='You are a reference expert who explains how previous works are connected to the current paper.',
    verbose=True,
    allow_delegation=False,
    llm=gemini
)

def get_citation_task(text):
    return Task(
        description=(
            "From the full text, list the most important referenced papers and briefly explain "
            "how they support, influence, or are extended by this paper.\n\n"
            + text
        ),
        expected_output='A numbered list of cited works with 1–2 sentence explanations.',
        agent=citation_extractor
    )
