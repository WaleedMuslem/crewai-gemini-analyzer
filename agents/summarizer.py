from crewai import Agent, Task
from gemini_client import gemini

summarizer = Agent(
    role='Summarizer',
    goal='Generate a concise, accurate summary of a research paper',
    backstory='You are an expert at reading and summarizing academic papers.',
    verbose=True,
    allow_delegation=False,
    llm=gemini
)

def get_summary_task(text):
    return Task(
        description=(
            'Summarize the following research paper text into major sections: '
            'Abstract, Introduction, Methods, Results, Conclusion.\n\n'
            + text
        ),
        expected_output='Structured summary with bullet points per section.',
        agent=summarizer
    )
