import streamlit as st
import os
from main import run_pipeline
from exporter import save_markdown

st.set_page_config(page_title="📄 Research Paper Analyzer", layout="wide")

st.title("📄 Research Paper Analyzer with CrewAI + Gemini")
st.markdown("Upload a PDF and get a structured AI-powered analysis.")

uploaded = st.file_uploader("Upload a research paper (PDF)", type="pdf")

if uploaded:
    with open("temp.pdf", "wb") as f:
        f.write(uploaded.read())

    try:
        with st.spinner("🔍 Analyzing your paper with AI agents..."):
            summary, topic, insights, citations = run_pipeline("temp.pdf")

        st.success("✅ Analysis complete!")

        # Display results
        st.subheader("📝 Summary")
        st.markdown(summary)

        st.subheader("🔍 Topic Classification")
        st.markdown(topic)

        st.subheader("💡 Key Insights")
        st.markdown(insights)

        st.subheader("📚 Citations")
        st.markdown(citations)

        # Download Markdown report
        with open("analysis_report.md", "r", encoding="utf-8") as f:
            md_content = f.read()

        st.download_button("📥 Download Report as Markdown", md_content, file_name="analysis_report.md")
    except Exception as e:
        error_text = str(e)
        if "RESOURCE_EXHAUSTED" in error_text or "429" in error_text or "quota" in error_text.lower():
            st.error(
                "❌ Gemini API quota exceeded (429). Add billing/upgrade quota in Google AI Studio, "
                "or use a different API key/project, then try again."
            )
        else:
            st.error(f"❌ Analysis failed: {error_text}")

else:
    st.info("📤 Please upload a PDF file to get started.")
