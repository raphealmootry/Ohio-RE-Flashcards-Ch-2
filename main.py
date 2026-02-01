import streamlit as st

st.set_page_config(page_title="Ohio RE Flashcards: Ch 2", layout="centered")

# 1. CUSTOMIZABLE TERM BANK (Easy to add/subtract here)
if 'cards' not in st.session_state:
    st.session_state.cards = [
        {"term": "Land", "def": "The earth's surface extending downward to the center of the earth and upward to infinity, including permanent natural objects."},
        {"term": "Real Estate", "def": "Land plus all human-made improvements to the land that are permanently attached to it."},
        {"term": "Real Property", "def": "Real estate plus the 'Bundle of Legal Rights' (PUEEE)."},
        {"term": "Bundle of Legal Rights", "def": "Possession, Use, Enjoyment, Exclusion, and Enclosure/Disposition."},
        {"term": "Situs", "def": "Economic characteristic: Area preference or location based on people's choices."},
        {"term": "Chattels / Personal Property", "def": "Items that do not fit the definition of real property; movable objects (e.g., furniture)."},
        {"term": "Fixtures", "def": "Personal property so attached to land or a building that it becomes part of the real property by law."},
        {"term": "Trade Fixtures", "def": "Items installed by a tenant for business use; removable by the tenant before the lease expires."},
        {"term": "Emblements", "def": "Annual crops (fructus industriales) such as corn or wheat, considered personal property."},
        {"term": "ORC Title 47, Ch 4735", "def": "Ohio's specific Real Estate License Law governing professional standards."}
    ]

# 2. STATE MANAGEMENT
if 'card_index' not in st.session_state:
    st.session_state.card_index = 0
if 'show_def' not in st.session_state:
    st.session_state.show_def = False

# 3. UI STYLING (Energizing Contrast)
st.markdown("""
    <style>
    .stApp { background-color: #f0f4f8; }
    .flashcard {
        background-color: #ffffff;
        border: 4px solid #3b82f6;
        border-radius: 15px;
        padding: 50px;
        text-align: center;
        box-shadow: 0 10px 25px rgba(0,0,0,0.1);
        min-height: 250px;
        display: flex;
        align-items: center;
        justify-content: center;
    }
    .term-text { color: #1e3a8a; font-size: 32px; font-weight: bold; }
    .def-text { color: #d97706; font-size: 24px; font-style: italic; }
    </style>
""", unsafe_allow_html=True)

# 4. YOUTUBE WIDGET (Chillhop Radio)
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.info("Keep the lofi beats running while you grind.")

# 5. FLASHCARD ENGINE
st.title("🧠 Chapter 2 Flashcards")
st.write(f"**Card {st.session_state.card_index + 1} of {len(st.session_state.cards)}**")

current_card = st.session_state.cards[st.session_state.card_index]

# Display Card
with st.container():
    st.markdown('<div class="flashcard">', unsafe_allow_html=True)
    if not st.session_state.show_def:
        st.markdown(f'<div class="term-text">{current_card["term"]}</div>', unsafe_allow_html=True)
    else:
        st.markdown(f'<div class="def-text">{current_card["def"]}</div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.write("---")

# Navigation Buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ Previous"):
        st.session_state.card_index = (st.session_state.card_index - 1) % len(st.session_state.cards)
        st.session_state.show_def = False
        st.rerun()

with col2:
    label = "Hide Definition" if st.session_state.show_def else "Reveal Definition"
    if st.button(label, type="primary"):
        st.session_state.show_def = not st.session_state.show_def
        st.rerun()

with col3:
    if st.button("Next ➡️"):
        st.session_state.card_index = (st.session_state.card_index + 1) % len(st.session_state.cards)
        st.session_state.show_def = False
        st.rerun()
