import streamlit as st
import pandas as pd

st.set_page_config(page_title="Ohio RE Exam Prep", layout="centered")

# 1. DATA PERSISTENCE (Management Logic)
if 'cards' not in st.session_state:
    st.session_state.cards = [
        {"term": "Land", "def": "Surface, subsurface, and air rights."},
        {"term": "Real Property", "def": "Real estate + Bundle of Rights (PUEEE)."},
        {"term": "Situs", "def": "Area preference (Economic characteristic)."},
        {"term": "Title 47, Ch 4735", "def": "Ohio Real Estate License Law."}
    ]

if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
if 'show_def' not in st.session_state:
    st.session_state.show_def = False

# 2. SIDEBAR - STUDY VIBES & STATS
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.write(f"**Total Cards in Deck:** {len(st.session_state.cards)}")

# 3. MAIN INTERFACE TABS
tab1, tab2 = st.tabs(["🎴 Flashcards", "⚙️ Manage Deck"])

with tab1:
    if len(st.session_state.cards) > 0:
        # Progress indicator (Forced dark color for visibility)
        st.markdown(f"<h3 style='color: #1e3a8a;'>Card {st.session_state.card_index + 1} of {len(st.session_state.cards)}</h3>", unsafe_allow_html=True)
        
        current_card = st.session_state.cards[st.session_state.card_index]

        # THE FLASHCARD OBJECT
        # High contrast: Blue border, White background, Dark Blue text
        with st.container(border=True):
            if not st.session_state.show_def:
                st.markdown(f"<h1 style='text-align: center; color: #1e3a8a; padding: 50px;'>{current_card['term']}</h1>", unsafe_allow_html=True)
            else:
                st.markdown(f"<h2 style='text-align: center; color: #d97706; padding: 50px;'>{current_card['def']}</h2>", unsafe_allow_html=True)

        # CONTROLS
        c1, c2, c3 = st.columns(3)
        with c1:
            if st.button("⬅️ Prev"):
                st.session_state.card_index = (st.session_state.card_index - 1) % len(st.session_state.cards)
                st.session_state.show_def = False
                st.rerun()
        with c2:
            if st.button("🔄 Flip", type="primary", use_container_width=True):
                st.session_state.show_def = not st.session_state.show_def
                st.rerun()
        with c3:
            if st.button("Next ➡️"):
                st.session_state.card_index = (st.session_state.card_index + 1) % len(st.session_state.cards)
                st.session_state.show_def = False
                st.rerun()
    else:
        st.warning("The deck is empty! Go to the 'Manage Deck' tab to add terms.")

with tab2:
    st.header("Deck Management")
    
    # ADD NEW CARD
    with st.expander("➕ Add New Term"):
        new_term = st.text_input("Term")
        new_def = st.text_area("Definition")
        if st.button("Add to Deck"):
            if new_term and new_def:
                st.session_state.cards.append({"term": new_term, "def": new_def})
                st.success(f"Added: {new_term}")
                st.rerun()

    # VIEW / DELETE CARDS
    st.write("---")
    st.write("### Current Deck")
    if len(st.session_state.cards) > 0:
        df_display = pd.DataFrame(st.session_state.cards)
        st.table(df_display)
        
        if st.button("🗑️ Clear Entire Deck"):
            st.session_state.cards = []
            st.session_state.card_index = 0
