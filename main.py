import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ohio RE: Unit 2 Master", layout="centered")

# 1. DATA INITIALIZATION
if 'cards' not in st.session_state:
    quiz = [
        {"q": "1. Real estate generally includes all the following EXCEPT:", "opts": "a. trees.\nb. air rights.\nc. annual crops.\nd. mineral rights.", "ans": "c. annual crops.", "exp": "Annual crops (emblements) are personal property."},
        {"q": "2. A woman rents space in a commercial building for a bookstore... Which BEST characterizes the contents?", "opts": "a. The shelves and tables are trade fixtures and will transfer when the owner sells.\nb. The shelves and tables are trade fixtures and may properly be removed by the woman before her lease expires.\nc. Because the woman is a tenant, the shelves and tables are fixtures and may not be removed.\nd. Because the shelves and tables are attached, they are treated the same as other fixtures.", "ans": "b. The shelves and tables are trade fixtures and may properly be removed...", "exp": "Trade fixtures belong to the tenant and are removable."},
        {"q": "3. The term nonhomogeneity refers to:", "opts": "a. scarcity.\nb. immobility.\nc. uniqueness.\nd. indestructibility.", "ans": "c. uniqueness.", "exp": "No two parcels of land are exactly the same."},
        {"q": "4. Another term for personal property is:", "opts": "a. realty.\nb. fixtures.\nc. chattels.\nd. fructus naturales.", "ans": "c. chattels.", "exp": "Chattel = Personal Property."},
        {"q": "5. A property owner wants to use water from a river... state relies on which rule of law?", "opts": "a. Riparian rights\nb. Littoral rights\nc. Doctrine of prior appropriation\nd. Doctrine of highest and best use", "ans": "c. Doctrine of prior appropriation", "exp": "Water use is controlled by the state via permits."},
        {"q": "6. A man inherited vacant land, removed topsoil, and died. Which is TRUE?", "opts": "a. Daughter inherits nothing.\nb. Daughter inherits the property as is.\nc. Daughter owns the topsoil wherever it is.\nd. Estate must restore property.", "ans": "b. The daughter inherits the property as is.", "exp": "She inherits the remaining interests in the land."},
        {"q": "7. A court would NOT consider which of the following for fixture status?", "opts": "a. The cost of the item\nb. Removal damage\nc. Adaptation to real estate\nd. Agreement of parties", "ans": "a. The cost of the item when it was purchased", "exp": "Cost is not part of the MARIA fixture test."},
        {"q": "8. Which is a physical characteristic of land?", "opts": "a. Indestructibility\nb. Improvements\nc. Area preference\nd. Scarcity", "ans": "a. Indestructibility", "exp": "Physical traits: Immobility, Indestructibility, Uniqueness."},
        {"q": "9. Act by which real property can be converted into personal property:", "opts": "a. Severance\nb. Accession\nc. Conversion\nd. Attachment", "ans": "a. Severance", "exp": "Severance involves detaching an item (e.g., cutting a tree)."},
        {"q": "10. Seller took a ceiling fan not addressed in the contract. Which is TRUE?", "opts": "a. Ceiling fans are usually considered real estate.\nb. The fan belongs to the seller.\nc. Fans are trade fixtures.\nd. Fans are personal property.", "ans": "a. Ceiling fans are usually considered real estate.", "exp": "Fixtures stay with the real property."},
        {"q": "11. Buyer sold mineral rights to an oil company. Buyer gave up:", "opts": "a. Air rights\nb. Surface rights\nc. Subsurface rights\nd. Occupancy rights", "ans": "c. Subsurface rights", "exp": "Mineral rights are beneath the surface."},
        {"q": "12. Lumber in the driveway for building a porch is:", "opts": "a. real property.\nb. personal property.\nc. a chattel that is real property.\nd. a trade fixture.", "ans": "b. personal property.", "exp": "Unattached building materials are personal property."},
        {"q": "13. Annexation, adaptation, and agreement are legal tests for:", "opts": "a. trade fixtures.\nb. real estate.\nc. a fixture or personal property.\nd. an improvement.", "ans": "c. a fixture or personal property.", "exp": "The MARIA test determines fixture status."},
        {"q": "14. Parking spaces and water rights are classified as:", "opts": "a. covenants.\nb. emblements.\nc. chattels.\nd. appurtenances.", "ans": "d. appurtenances.", "exp": "Appurtenances run with the land."},
        {"q": "15. A company builds tin shacks for turpentine storage. Which is TRUE?", "opts": "a. Action constitutes improvement.\nb. Chemicals are appurtenances.\nc. Shacks are trade fixtures.\nd. Use not in bundle of rights.", "ans": "a. The company's action constitutes improvement...", "exp": "Artificial attachments are improvements."},
        {"q": "16. Land located along the banks of a river. Water rights are:", "opts": "a. littoral rights.\nb. prior appropriation rights.\nc. riparian rights.\nd. hereditaments.", "ans": "c. riparian rights.", "exp": "Riparian = Flowing water (Rivers)."},
        {"q": "17. Bundle of rights entitles owner to all EXCEPT:", "opts": "a. sell property.\nb. exclude utility meter readers.\nc. erect No Trespassing signs.\nd. enjoy profits.", "ans": "b. exclude utility meter readers.", "exp": "Utility companies have access via easements."},
        {"q": "18. According to law, a trade fixture is usually treated as:", "opts": "a. a fixture.\nb. an easement.\nc. personalty.\nd. a license.", "ans": "c. personalty.", "exp": "Personalty is another term for personal property."},
        {"q": "19. House is located in a busy area. Concern is called:", "opts": "a. physical deterioration.\nb. area preference.\nc. permanence.\nd. immobility.", "ans": "b. area preference.", "exp": "Situs (location preference)."},
        {"q": "20. Which of the following is considered personal property?", "opts": "a. Fireplace\nb. Awnings\nc. Bathtub\nd. Patio furniture", "ans": "d. Patio furniture", "exp": "Patio furniture is movable (chattel)."}
    ]

    terms = [
        {"q": "Accession", "opts": "", "ans": "Acquiring title via annexation or accretion.", "exp": "Way to gain property through adding to it."},
        {"q": "Accretion", "opts": "", "ans": "Increase in land by soil deposit.", "exp": "The natural adding of land via water."},
        {"q": "Air Rights", "opts": "", "ans": "Right to use space above earth.", "exp": "Can be leased or sold separately."},
        {"q": "Annexation", "opts": "", "ans": "Converting personal property to real property.", "exp": "Example: Cement becoming a sidewalk."},
        {"q": "Appurtenance", "opts": "", "ans": "A right/privilege running with the land.", "exp": "Example: Parking spots or water rights."},
        {"q": "Area Preference (Situs)", "opts": "", "ans": "Location based on social/economic factors.", "exp": "Most important economic characteristic."},
        {"q": "Avulsion", "opts": "", "ans": "Sudden removal of soil by nature.", "exp": "Like a flood or landslide."},
        {"q": "Bundle of Legal Rights", "opts": "", "ans": "PCEED rights.", "exp": "Possession, Control, Enjoyment, Exclusion, Disposition."},
        {"q": "Chattel", "opts": "", "ans": "Movable personal property.", "exp": "Another name for personalty."},
        {"q": "Emblements", "opts": "", "ans": "Annual crops (Personal Property).", "exp": "Also known as fructus industriales."},
        {"q": "Erosion", "opts": "", "ans": "Gradual wearing away of land.", "exp": "Slow natural loss of soil."},
        {"q": "Fixture", "opts": "", "ans": "Attached personal property becoming real estate.", "exp": "Uses the MARIA legal test."},
        {"q": "Improvement", "opts": "", "ans": "Artificial attachment to land.", "exp": "Buildings, fences, utilities."},
        {"q": "Land", "opts": "", "ans": "Surface, subsurface, and air.", "exp": "The earth to the center and up to infinity."},
        {"q": "Littoral Rights", "opts": "", "ans": "Rights along non-flowing water.", "exp": "Lakes, oceans, seas."},
        {"q": "Manufactured Housing", "opts": "", "ans": "Built off-site.", "exp": "Personal property until permanently affixed."},
        {"q": "Nonhomogeneity", "opts": "", "ans": "Uniqueness of land.", "exp": "Physical characteristic of land."},
        {"q": "Personal Property", "opts": "", "ans": "Movable items (Chattels).", "exp": "Everything not real property."},
        {"q": "Prior Appropriation", "opts": "", "ans": "State-controlled water rights.", "exp": "Permit-based water law."},
        {"q": "Real Estate", "opts": "", "ans": "Land + Human-made improvements.", "exp": "The physical property."},
        {"q": "Real Property", "opts": "", "ans": "Real Estate + Bundle of Rights.", "exp": "The legal property definition."},
        {"q": "Riparian Rights", "opts": "", "ans": "Rights along flowing water.", "exp": "Rivers and streams."},
        {"q": "Severance", "opts": "", "ans": "Converting real property to personal property.", "exp": "Example: Cutting down a tree."},
        {"q": "Subsurface Rights", "opts": "", "ans": "Rights below the surface.", "exp": "Minerals, oil, and gas."},
        {"q": "Surface Rights", "opts": "", "ans": "Rights limited to the surface.", "exp": "Owner only owns the top layer."},
        {"q": "Trade Fixture", "opts": "", "ans": "Tenant business equipment.", "exp": "Removable by tenant before lease ends."},
        {"q": "Water Rights", "opts": "", "ans": "Rights to use water on/next to land.", "exp": "Riparian vs. Littoral."},
        {"q": "MARIA", "opts": "", "ans": "Fixture Test elements.", "exp": "Method, Adaptability, Relationship, Intention, Agreement."}
    ]
    
    st.session_state.cards = quiz + terms
    random.shuffle(st.session_state.cards)

# 2. STATE MANAGEMENT
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'reveal' not in st.session_state: st.session_state.reveal = False

# 3. SIDEBAR
st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.metric("Master Deck Size", len(st.session_state.cards))

# 4. TABS
tab1, tab2 = st.tabs(["🎴 Flashcards", "⚙️ Deck Management"])

with tab1:
    st.markdown(f"### Card {st.session_state.idx + 1} of {len(st.session_state.cards)}")
    curr = st.session_state.cards[st.session_state.idx]

    with st.container(border=True):
        st.markdown(f"#### {curr['q']}")
        if curr.get('opts'):
            st.info(curr['opts'])
        
        if st.session_state.reveal:
            st.divider()
            st.markdown(f"<h3 style='color: #d97706;'>{curr['ans']}</h3>", unsafe_allow_html=True)
            st.success(f"💡 {curr['exp']}")

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

with tab2:
    st.header("Deck Management")
    st.write("Review the full card list below:")
    st.dataframe(pd.DataFrame(st.session_state.cards), use_container_width=True)
    
    if st.button("🗑️ Reset & Reshuffle Deck"):
        random.shuffle(st.session_state.cards)
        st.session_state.idx = 0
        st.session_state.reveal = False
        st.rerun()
