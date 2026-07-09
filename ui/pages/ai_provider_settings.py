import streamlit as st

from ai.providers.factory import get_ai_provider


def render():
    st.title("AI Provider Settings")

    provider_name = st.selectbox(
        "Select AI Provider",
        ["Manual Mode", "Ollama", "OpenAI"]
    )

    model = st.text_input(
        "Model",
        value="llama3.1:8b" if provider_name == "Ollama" else "gpt-4.1-mini"
    )

    prompt = st.text_area(
        "Test Prompt",
        value="Explain what ArkInsight is in one sentence."
    )

    if st.button("Test Provider"):
        provider = get_ai_provider(provider_name, model)
        response = provider.generate(prompt)

        st.subheader("Response")
        st.write(response)
