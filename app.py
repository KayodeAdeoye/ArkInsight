import streamlit as st

from ui.pages import (
    dashboard,
    ai_provider_settings,
    repo_import,
    assessment_workspace,
    findings,
    reports,
)

st.set_page_config(
    page_title="ArkInsight",
    page_icon="🛡️",
    layout="wide",
)

PAGES = {
    "Dashboard": dashboard.render,
    "AI Provider Settings": ai_provider_settings.render,
    "Repository Import": repo_import.render,
    "Assessment Workspace": assessment_workspace.render,
    "Findings": findings.render,
    "Reports": reports.render,
}

st.sidebar.title("ArkInsight")
selected_page = st.sidebar.radio("Navigation", list(PAGES.keys()))

PAGES[selected_page]()
