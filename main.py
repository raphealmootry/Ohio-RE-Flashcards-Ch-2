import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ohio RE: Ch 2 Master Deck", layout="centered")

# 1. INITIALIZE MASTER DECK (Terms + Quiz)
if 'cards' not in st.session_state:
    # Terms from your provided list (Duplicates removed)
    terms = [
        {"term": "Accession", "def": "Acquiring title to additions/improvements via annexation or accretion."},
        {"term": "Accretion", "def": "The increase of land by the deposit of soil by water action."},
        {"term": "Air Rights", "def": "The right to use the space above the earth; can be sold/leased independently."},
        {"term": "Annexation", "def": "Process of converting personal property into real property."},
        {"term": "Appurtenance", "def": "A right or privilege that 'runs with the land' (e.g., parking spaces)."},
        {"term": "Area Preference (Situs)", "def": "Location preference based on social/economic factors; 'Location, location, location.'"},
        {"term": "Avulsion", "def": "The sudden tearing away of land by an act of nature (e.g., a flood)."},
        {"term": "Bundle of Legal Rights", "def": "PCEED: Possession, Control, Enjoyment, Exclusion, Disposition."},
        {"term": "Chattel", "def": "Items of personal property; movable and not permanently attached."},
        {"term": "Emblements", "def": "Fructus industriales; annual crops considered personal property."},
        {"term": "Erosion", "def": "The gradual wearing away of land by natural forces."},
        {"term": "Fixture", "def": "Personal property permanently attached to become real property."},
        {"term": "Improvement", "def": "Any artificial, permanent attachment to land (buildings, fences, sewers)."},
        {"term": "Land", "def": "The earth's surface extending down to the center and up to infinity."},
        {"term": "Littoral Rights", "def": "Rights of owners bordering non-flowing water (lakes, oceans)."},
        {"term": "Manufactured Housing", "def": "Built off-site; personal property unless permanently affixed to land."},
        {"term": "Nonhomogeneity", "def": "Uniqueness; no two parcels of land are exactly the same."},
        {"term": "Personal Property", "def": "Property that is movable; all property that is not real property."},
        {"term": "Prior Appropriation", "def": "Government-controlled water rights (mostly Western states)."},
        {"term": "Real Estate", "def": "Land plus all human-made improvements permanently attached."},
        {"term": "Real Property", "def": "Real estate plus the bundle of legal rights."},
        {"term": "Riparian Rights", "def": "Rights of owners bordering flowing water (rivers, streams)."},
        {"term": "Severance", "def": "Converting real property to personal property by detaching it (e.g., cutting a tree)."},
        {"term": "Subsurface Rights", "def": "Ownership rights to minerals/resources beneath the surface."},
        {"term": "Surface Rights", "def": "Ownership limited to the surface of the earth."},
        {"term": "Trade Fixture", "def": "Tenant-owned business equipment; must be removed before lease ends."},
        {"term": "Water Rights", "def": "Common-law rights for owners of land adjacent to water."},
        {"term": "MARIA", "def": "Fixture Test: Method, Adaptability, Relationship, Intention, Agreement."}
    ]

    # Quiz Key: cbcccbaaaacbcdacbcbd (20 Questions)
    key = "CBCCCBAAAACBCDACBCBD"
    quiz = [{"term": f"Ch 2 Quiz Q#{i+1}", "def": f"Answer: {key[i]}"} for i in range(20)]
    
    # Combine and Shuffle
    st.session_state.cards = terms + quiz
    random.shuffle(st.session_state.cards)

# 2. STATE MANAGEMENT
if 'card_index' not in st.session_state: st.session_state.card_index = 0
if 'show_def' not in st.session_state: st.session_state.show_def = False

# 3. UI SIDEBAR
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.metric("Total Study Cards", len(st.session_state.cards))

# 4. MAIN TABS
t1, t2 = st.tabs(["🎴 Study Deck", "⚙️ Manage Deck"])

with t1:
    st.markdown(f"<h3 style='color: #1e3a8a;'>Card {st.session_state.card_index + 1} of {len(st.session_state.cards)}</h3>", unsafe_allow_html=True)
    
    curr = st.session_state.cards[st.session_state.card_index]
    
    with st.container(border=True):
        if not st.session_state.show_def:
            st.markdown(f"<h1 style='text-align: center; color: #1e3a8
