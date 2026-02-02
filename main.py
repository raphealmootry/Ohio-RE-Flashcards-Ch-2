import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ohio RE: Ch 2 Final Master", layout="centered")

# 1. INTEGRATED MASTER DATA (Terms + Quiz Questions)
if 'cards' not in st.session_state:
    master_list = [
        {"term": "Accession", "def": "Acquiring title to additions via annexation or accretion."},
        {"term": "Accretion", "def": "Increase in land from soil deposits by water action."},
        {"term": "Air Rights", "def": "Rights to use space above a property; can be sold independently."},
        {"term": "Annexation", "def": "Converting personal property into real property (e.g., mixing cement)."},
        {"term": "Appurtenance", "def": "A right/improvement that 'runs with the land' (e.g., an easement)."},
        {"term": "Area Preference (Situs)", "def": "Economic characteristic: Location based on social factors."},
        {"term": "Avulsion", "def": "Sudden removal of land by nature (e.g., a flood)."},
        {"term": "Bundle of Legal Rights", "def": "PCEED: Possession, Control, Enjoyment, Exclusion, Disposition."},
        {"term": "Chattel", "def": "Movable personal property (e.g., furniture)."},
        {"term": "Emblements", "def": "Fructus industriales; annual crops (personal property)."},
        {"term": "Erosion", "def": "Gradual wearing away of land by natural forces."},
        {"term": "Fixture", "def": "Personal property permanently attached to become real property."},
        {"term": "Improvement", "def": "Any artificial, permanent attachment (e.g., a building or fence)."},
        {"term": "Land", "def": "Earth's surface, subsurface to center, and air to infinity."},
        {"term": "Littoral Rights", "def": "Rights bordering non-flowing water (lakes/oceans)."},
        {"term": "Manufactured Housing", "def": "Built off-site; personal property until permanently attached."},
        {"term": "Nonhomogeneity", "def": "Physical characteristic: No two parcels are exactly the same."},
        {"term": "Personal Property", "def": "Movable property; all property that is not real property."},
        {"term": "Prior Appropriation", "def": "Government-controlled water rights (mostly Western states)."},
        {"term": "Real Estate", "def": "Land plus all permanent human-made improvements."},
        {"term": "Real Property", "def": "Real estate plus the 'Bundle of Legal Rights'."},
        {"term": "Riparian Rights", "def": "Rights bordering flowing water (rivers/streams)."},
        {"term": "Severance", "def": "Changing real property to personal property by detaching it."},
        {"term": "Situs", "def": "Economic characteristic of land: Area preference."},
        {"term": "Subsurface Rights", "def": "Ownership rights to minerals/resources beneath the surface."},
        {"term": "Surface Rights", "def": "Ownership limited to the surface of the earth."},
        {"term": "Trade Fixture", "def": "Tenant business equipment; removable before lease ends."},
        {"term": "Water Rights", "def": "Common-law rights for land adjacent to water bodies."}
    ]

    # Integrated Quiz Questions based on your Key: cbcccbaaaacbcdacbcbd
    key = "CBCCCBAAAACBCDACBCBD"
    quiz_questions = [
        {"term": f"Quiz Question #{i+1}", "def": f"Answer Key: {key[i]}"} 
        for i in range(20)
    ]
    
    st.session_state.cards = master_list + quiz_questions
    random.shuffle(st.session_state.cards)

# 2. STATE MANAGEMENT
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'reveal' not in st.session_state: st.session_state.reveal = False

# 3. SIDEBAR (Vibe & Progress)
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.metric("Total Deck Size", len(st.session_state.cards))

# 4. MAIN INTERFACE
tab1, tab2 = st.tabs(["🎴 Master Deck", "⚙️ Deck Manager"])

with tab1:
    # High-contrast header (Deep Blue)
    st.markdown(f"<h3 style='color: #1e3a8a;'>Card {st.session_state.idx + 1} of {len(st.session_state.cards)}</h3>", unsafe_allow_html=True)
    
    curr = st.session_state.cards[st.session_state.idx]
    
    # THE FLASHCARD (Centering and Contrast)
    with st.container(border=True):
        if not st.session_state.reveal:
            st.markdown(f"<h1 style='text-align: center; color: #1e3a8a; padding: 50px;'>{curr['term']}</h1>", unsafe_allow_html=True)
        else:
            st.markdown(f"<h2 style='text-align: center; color: #d97706; padding: 50px;'>{curr['def']}</h2>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)
    with c1:
        if st.button("⬅️ Previous"):
            st.session_state.idx = (st.session_state.idx - 1) % len(st.session_state.cards)
            st.session_state.reveal = False
            st.rerun()
    with c2:
        btn_txt = "Hide Answer" if st.session_state.reveal else "Reveal / Flip"
        if st.button(btn_txt, type="primary", use_container_width=True):
            st.session_state.reveal = not st.session_state.reveal
            st.rerun()
    with c3:
        if st.button("Next ➡️"):
            st.session_state.idx = (st.session_state.idx + 1) % len(st.session_state.cards)
            st.session_state.reveal = False
            st.rerun()

with tab2:
    st.header("Deck Customization")
    st.dataframe(pd.DataFrame(st.session_state.cards), use_container_width=True)
    if st.button("🗑️ Reset and Reshuffle Deck"):
        random.shuffle(st.session_state.cards)
        st.session_state.idx = 0
        st.rerun()
