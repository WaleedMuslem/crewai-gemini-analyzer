from pdf_reader import extract_text_from_pdf
from gemini_client import gemini

# Import agents and task builder functions
from agents.summarizer import summarizer, get_summary_task
from agents.topic_classifier import topic_classifier, get_topic_task
from agents.insight_extractor import insight_extractor, get_insight_task
from agents.citation_extractor import citation_extractor, get_citation_task

from exporter import save_markdown
from crewai import Crew

def run_pipeline(pdf_path):
    # Extract text from the uploaded PDF
    text = extract_text_from_pdf(pdf_path)

    # Generate task objects using the paper text
    summary_task = get_summary_task(text)
    topic_task = get_topic_task(text)
    insight_task = get_insight_task(text)
    citation_task = get_citation_task(text)

    # Create Crew
    crew = Crew(
        agents=[summarizer, topic_classifier, insight_extractor, citation_extractor],
        tasks=[summary_task, topic_task, insight_task, citation_task],
        verbose=True
    )

    # Run all tasks
    result = crew.kickoff()
    print("\n✅ Final Output:\n", result)

    # Format and save Markdown report
    md_output = f"""
# 📄 Research Paper Analysis Report

## 📝 Summary
{summary_task.output}

## 🔍 Topic Classification
{topic_task.output}

## 💡 Key Insights
{insight_task.output}

## 📚 Citations
{citation_task.output}
"""
    save_markdown(md_output, "analysis_report.md")
    print("✅ Saved Markdown as: analysis_report.md")

    return (
        str(summary_task.output),
        str(topic_task.output),
        str(insight_task.output),
        str(citation_task.output),
    )

if __name__ == "__main__":
    run_pipeline("papers/sample_paper.pdf")
