import streamlit as st

st.set_page_config(
    page_title='ArkInsight',
    page_icon='🛡️',
    layout='wide'
)

st.sidebar.title('ArkInsight')
page = st.sidebar.radio(
    'Navigation',
    ['Dashboard', 'AI Provider Settings', 'Repo Import', 'Assessment Workspace', 'Findings', 'Reports']
)

st.title('🛡️ ArkInsight')
st.subheader('AI Security Assessment Workbench')

st.info(f'Current page: {page}')

st.write('Phase 1 foundation is running successfully.')
