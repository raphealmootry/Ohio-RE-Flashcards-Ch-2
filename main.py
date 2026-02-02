import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ohio RE: Unit 2 Master", layout="centered")

if 'cards' not in st.session_state:
    # 20 Quiz Questions from the uploaded images
    quiz_bank = [
        {"term": "1. Real estate generally includes all the following EXCEPT:\na. trees.\nb. air rights.\nc. annual crops.\nd. mineral rights.", 
         "def": "Answer: c. annual crops.", "explain": "Annual crops (emblements) are considered personal property, while trees and mineral rights are part of the real estate."},
        {"term": "2. A woman rents space in a commercial building for a bookstore. She has installed large reading tables fastened to the walls and bookshelves bolted to both the ceiling and the floor. Which BEST characterizes the contents?", 
         "def": "Answer: b. The shelves and tables are trade fixtures and may properly be removed by the woman before her lease expires...", "explain": "Trade fixtures are personal property of the tenant and removable before lease expiration."},
        {"term": "3. The term nonhomogeneity refers to:\na. scarcity.\nb. immobility.\nc. uniqueness.\nd. indestructibility.", 
         "def": "Answer: c. uniqueness.", "explain": "Nonhomogeneity means no two parcels of land are exactly the same."},
        {"term": "4. Another term for personal property is:\na. realty.\nb. fixtures.\nc. chattels.\nd. fructus naturales.", 
         "def": "Answer: c. chattels.", "explain": "Chattels is the legal term for personal property."},
        {"term": "5. A property owner wants to use water from a river that runs through the property... state relies on which rule of law?", 
         "def": "Answer: c. Doctrine of prior appropriation", "explain": "Prior appropriation is where water use is controlled by the state via permits."},
        {"term": "9. Which describes the act by which real property can be converted into personal property?\na. Severance\nb. Accession\nc. Conversion\nd. Attachment", 
         "def": "Answer: a. Severance", "explain": "Severance is the act of separating an item from the land (e.g., cutting down a tree)."},
        {"term": "10. While moving into a home, the buyer discovered the seller had taken the ceiling fan... Which statement is TRUE?", 
         "def": "Answer: a. Ceiling fans are usually considered real estate.", "explain": "Ceiling fans are fixtures; they are permanently attached and intended to remain."},
        {"term": "14. Parking spaces in multiunit buildings, water rights, and similar things of value that convey with property are classified as:\na. covenants.\nb. emblements.\nc. chattels.\nd. appurtenances.", 
         "def": "Answer: d. appurtenances.", "explain": "Appurtenances are rights or privileges that 'run with the land.'"},
        {"term": "19. A buyer is interested in a house... but it is located in a busy area... Her concern about location is called:\na. physical deterioration.\nb. area preference.\nc. permanence of investment.\nd. immobility.", 
         "def": "Answer: b. area preference.", "explain": "This is also known as 'Situs.'"}
    ]

    # Your custom 28-term list (simplified for the merge)
    terms = [
        {"term": "Accession", "def": "Acquiring title to additions/improvements via annexation.", "explain": "Title 47, Ch 4735 context."},
        {"term": "Annexation", "def": "Converting personal property into real property.", "explain": "Example: Mixing sand and gravel into concrete."},
        {"term": "Prior Appropriation", "def": "Water rights controlled by the state.", "explain": "Relates to Quiz Q#5."}
    ]
    
    st.session_state.cards = quiz_bank + terms
    random.shuffle(st.session_state.cards)

# State Management
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'reveal' not in st.session_state: st.session_state.reveal = False
if 'exp' not in st.session_state: st.session_state.exp = False

# Sidebar
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.metric("Master Deck", len(st.session_state.cards))

# Main UI
st.markdown(f"<h3 style='color: #1e3a8a;'>Card {st.session_state.idx + 1} of {len(st.session_state.cards)}</h3>", unsafe_allow_html=True)
curr = st.session_state.cards[st.session_state.idx]

with st.container(border=True):
    if not st.session_state.reveal:
        st.markdown(f"<div style='min-height: 250px;'><h4 style='color: #1e3a8a;'>{curr['term']}</h4></div>", unsafe_allow_html=True)
    else:
        st.markdown(f"<div style='min-height: 250px;'><h3 style='color: #d97706;'>{curr['def']}</h3></div>", unsafe_allow_html=True)
        if st.session_state.exp:
            st.info(f"💡 {curr['explain']}")

# Controls
c1, c2, c3 = st.columns(3)
with c1:
    if st.button("⬅️ Prev"):
        st.session_state.idx = (st.session_state.idx - 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.session_state.exp = False
        st.rerun()
with c2:
    if not st.session_state.reveal:
        if st.button("Flip to Answer", type="primary", use_container_width=True):
            st.session_state.reveal = True
            st.rerun()
    else:
        if st.button("Reveal Explanation", use_container_width=True):
            st.session_state.exp = True
            st.rerun()
with c3:
    if st.button("Next ➡️"):
        st.session_state.idx = (st.session_state.idx + 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.session_state.exp = False
        st.rerun()
