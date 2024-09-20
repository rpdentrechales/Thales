import streamlit as st

# --- PAGE SETUP ---
teste_page = st.Page(
    "views/teste.py",
    title="teste",
    icon=":material/thumb_up:",
    default=True,
)


# --- NAVIGATION SETUP [WITHOUT SECTIONS] ---
# pg = st.navigation(pages=[about_page, project_1_page, project_2_page])

# --- NAVIGATION SETUP [WITH SECTIONS]---
pg = st.navigation(
    {
        "Teste": [teste_page],
        
    }
)


# --- SHARED ON ALL PAGES ---
# st.logo("assets/codingisfun_logo.png")


# --- RUN NAVIGATION ---
pg.run()
