import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ohio RE Master: Dynamic Deck", layout="centered")

# 1. THE DATA (Synchronized with your Book Photos)
if 'cards' not in st.session_state:
    quiz_bank = [
        {"q": "1. Real estate generally includes all the following EXCEPT:", 
         "opts": "a. trees.\nb. air rights.\nc. annual crops.\nd. mineral rights.",
         "ans": "c. annual crops.", "exp": "Emblements (annual crops) are personal property."},
        {"q": "2. A woman rents space in a commercial building for a bookstore...", 
         "opts": "a. The shelves and tables are fixtures.\nb. The shelves and tables are trade fixtures...\nc. These are considered real estate.\nd. The landlord owns them now.",
         "ans": "b. trade fixtures", "exp": "Trade fixtures belong to the tenant and are removable."},
        # Add all 20 questions here following this 'q', 'opts', 'ans', 'exp' format
    ]
    
    # Merge with your 28 Terms
    terms = [{"q": "Accession", "opts": "", "ans": "Acquiring title via annexation.", "exp": "Legal principle of property growth."}]
    
    st.session_state.cards = quiz_bank + terms
    random.shuffle(st.session_state.cards)

# State Management
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'reveal' not in st.session_state: st.session_state.reveal = False

# Sidebar
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")

# Main Interface
st.markdown(f"<h3 style='color: #1e3a8a;'>Card {st.session_state.idx + 1} of {len(st.session_state.cards)}</h3>", unsafe_allow_html=True)
curr = st.session_state.cards[st.session_state.idx]

# THE DYNAMIC CARD CONTAINER
with st.container(border=True):
    # Front of Card: Question + Options
    st.markdown(f"### {curr['q']}")
    if curr['opts']:
        # Scrollable area for long multiple choice options
        st.info(curr['opts'])
    
    # Reveal Logic: Extra digital surface area for answers
    if st.session_state.reveal:
        st.divider()
        st.success(f"**{curr['ans']}**")
        with st.expander("Show Detailed Explanation"):
            st.write(curr['exp'])

# Controls
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("⬅️ Previous"):
        st.session_state.idx = (st.session_state.idx - 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.rerun()
with c2:
    label = "Hide Answer" if st.session_state.reveal else "Reveal Answer"
    if st.button(label, type="primary", use_container_width=True):
        st.session_state.reveal = not st.session_state.reveal
        st.rerun()
with c3:
    if st.button("Next ➡️"):
        st.session_state.idx = (st.session_state.idx + 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.rerun()
