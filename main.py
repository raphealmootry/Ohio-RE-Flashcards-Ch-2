import streamlit as st
import random

st.set_page_config(page_title="Ohio RE: Unit 2 Master", layout="centered")

if 'cards' not in st.session_state:
    # 20 QUIZ QUESTIONS (Full Text Transcribed from Photos)
    quiz = [
        {"q": "1. Real estate generally includes all the following EXCEPT:", "opts": "a. trees.\nb. air rights.\nc. annual crops.\nd. mineral rights.", "ans": "c. annual crops.", "exp": "Annual crops (emblements) are personal property."},
        {"q": "2. A woman rents space in a commercial building for a bookstore. She has installed large reading tables fastened to the walls and bookshelves bolted to both the ceiling and the floor. Which BEST characterizes the contents?", "opts": "a. The shelves and tables are trade fixtures and will transfer when the property owner sells the building.\nb. The shelves and tables are trade fixtures and may properly be removed by the woman before her lease expires.\nc. Because the woman is a tenant, the shelves and tables are fixtures and may not be removed except with permission.\nd. Because the shelves and tables are attached to the building, they are treated the same as other fixtures.", "ans": "b. The shelves and tables are trade fixtures...", "exp": "Trade fixtures belong to the tenant and are removable."},
        {"q": "3. The term nonhomogeneity refers to:", "opts": "a. scarcity.\nb. immobility.\nc. uniqueness.\nd. indestructibility.", "ans": "c. uniqueness.", "exp": "No two parcels of land are exactly the same."},
        {"q": "4. Another term for personal property is:", "opts": "a. realty.\nb. fixtures.\nc. chattels.\nd. fructus naturales.", "ans": "c. chattels.", "exp": "Chattel is the legal name for personal property."},
        {"q": "5. A property owner wants to use water from a river that runs through the property... To do so, the owner is required by state law to submit an application... based on these facts, the state relies on which rule of law?", "opts": "a. Riparian rights\nb. Littoral rights\nc. Doctrine of prior appropriation\nd. Doctrine of highest and best use", "ans": "c. Doctrine of prior appropriation", "exp": "Water use is controlled by the state via permits."},
        {"q": "6. A man inherited a piece of vacant land, removed and sold all the topsoil, limestone, and gravel. At his death, he left the property to his daughter. Which is TRUE?", "opts": "a. The daughter inherits nothing.\nb. The daughter inherits the property as is.\nc. The daughter owns the gravel, limestone, and topsoil wherever it is.\nd. The man's estate must restore the property.", "ans": "b. The daughter inherits the property as is.", "exp": "The land remains, but the subsurface/surface resources were already severed."},
        {"q": "7. In determining whether an item is real or personal property, a court would NOT consider which of the following?", "opts": "a. The cost of the item when it was purchased\nb. Whether its removal would cause severe damage to the real estate\nc. Whether the item is clearly adapted to the real estate\nd. Any relevant agreement of the parties in their contract of sale", "ans": "a. The cost of the item when it was purchased", "exp": "Cost is not part of the MARIA fixture test."},
        {"q": "8. Which of the following is a physical characteristic of land?", "opts": "a. Indestructibility\nb. Improvements\nc. Area preference\nd. Scarcity", "ans": "a. Indestructibility", "exp": "Physical traits: Immobility, Indestructibility, Uniqueness."},
        {"q": "9. Which of the following describes the act by which real property can be converted into personal property?", "opts": "a. Severance\nb. Accession\nc. Conversion\nd. Attachment", "ans": "a. Severance", "exp": "Severance involves detaching an item (e.g., cutting a tree)."},
        {"q": "10. While moving into a newly purchased home, the buyer discovered that the seller had taken the ceiling fan... Which statement is TRUE?", "opts": "a. Ceiling fans are usually considered real estate.\nb. The ceiling fan belongs to the seller.\nc. Ceiling fans are considered trade fixtures.\nd. Ceiling fans are considered personal property.", "ans": "a. Ceiling fans are usually considered real estate.", "exp": "Fixtures stay with the real property."},
        {"q": "11. A buyer purchased a parcel of land and immediately sold the mineral rights to an oil company. The buyer gave up which of the following?", "opts": "a. Air rights\nb. Surface rights\nc. Subsurface rights\nd. Occupancy rights", "ans": "c. Subsurface rights", "exp": "Mineral rights are beneath the surface."},
        {"q": "12. A truckload of lumber that a homeowner purchased has been left in the driveway for use in building a porch. The lumber is considered:", "opts": "a. real property.\nb. personal property.\nc. a chattel that is real property.\nd. a trade or chattel fixture.", "ans": "b. personal property.", "exp": "Unattached building materials are personal property."},
        {"q": "13. Method of annexation, adaptation to real estate, and agreement between the parties are the legal tests for determining whether an item is:", "opts": "a. a trade fixture or personal property.\nb. real property or real estate.\nc. a fixture or personal property.\nd. an improvement.", "ans": "c. a fixture or personal property.", "exp": "The MARIA test determines fixture status."},
        {"q": "14. Parking spaces in multiunit buildings, water rights, and similar things of value that convey with property are classified as:", "opts": "a. covenants.\nb. emblements.\nc. chattels.\nd. appurtenances.", "ans": "d. appurtenances.", "exp": "Appurtenances run with the land."},
        {"q": "15. A paint company purchases a large tract of scenic forest land and builds several tin shacks there to store used turpentine... Which statement is TRUE?", "opts": "a. The company's action constitutes improvement of the property.\nb. The chemicals are considered appurtenances.\nc. The tin shacks are considered trade fixtures.\nd. Altering the property in order to store waste is not included in the bundle of rights.", "ans": "a. The company's action constitutes improvement...", "exp": "Artificial attachments are improvements."},
        {"q": "16. A property owner's land is located along the banks of a river. This owner's water rights are called:", "opts": "a. littoral rights.\nb. prior appropriation rights.\nc. riparian rights.\nd. hereditaments.", "ans": "c. riparian rights.", "exp": "Riparian = Flowing water (Rivers)."},
        {"q": "17. A property owner's bundle of legal rights entitles the owner to do all of the following EXCEPT:", "opts": "a. sell the property to a neighbor.\nb. exclude utility meter readers.\nc. erect No Trespassing signs.\nd. enjoy profits from its ownership.", "ans": "b. exclude utility meter readers.", "exp": "Utility companies have access via easements."},
        {"q": "18. According to law, a trade fixture is usually treated as:", "opts": "a. a fixture.\nb. an easement.\nc. personalty.\nd. a license.", "ans": "c. personalty.", "exp": "Personalty is another term for personal property."},
        {"q": "19. A buyer is interested in a house... but it is located in a busy area where she is not sure she wants to live. Her concern is called:", "opts": "a. physical deterioration.\nb. area preference.\nc. permanence of investment.\nd. immobility.", "ans": "b. area preference.", "exp": "Situs (location preference)."},
        {"q": "20. Which of the following is considered personal property?", "opts": "a. Wood-burning fireplace\nb. Awnings\nc. Bathtub\nd. Patio furniture", "ans": "d. Patio furniture", "exp": "Patio furniture is movable (chattel)."}
    ]

    # 28 VOCAB TERMS (No placeholders, all definitions included)
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

# State Management
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'reveal' not in st.session_state: st.session_state.reveal = False

st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.metric("Master Deck Size", len(st.session_state.cards))

st.markdown(f"### Card {st.session_state.idx + 1} of {len(st.session_state.cards)}")
curr = st.session_state.cards[st.session_state.idx]

with st.container(border=True):
    st.markdown(f"#### {curr['q']}")
    # Prevents KeyError: if 'opts' is empty, it doesn't try to render
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
    label = "Hide Answer" if st.session_state.reveal else "Reveal Answer / Flip"
    if st.button(label, type="primary", use_container_width=True):
        st.session_state.reveal = not st.session_state.reveal
        st.rerun()
with c3:
    if st.button("Next ➡️"):
        st.session_state.idx = (st.session_state.idx + 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.rerun()
