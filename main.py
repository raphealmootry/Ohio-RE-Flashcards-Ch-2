import streamlit as st
import pandas as pd
import random

st.set_page_config(page_title="Ohio RE: Unit 2 COMPLETE", layout="centered")

if 'cards' not in st.session_state:
    # 1. THE 20 QUIZ QUESTIONS (From Photos & Key: CBCCCBAAAACBCDACBCBD)
    quiz_bank = [
        {"q": "1. Real estate generally includes all the following EXCEPT:", "opts": "a. trees.\nb. air rights.\nc. annual crops.\nd. mineral rights.", "ans": "c. annual crops.", "exp": "Emblements (annual crops) are personal property."},
        {"q": "2. A woman rents space for a bookstore. She bolts bookshelves to the floor and ceiling. These are:", "opts": "a. fixtures.\nb. trade fixtures.\nc. real property.\nd. part of the building.", "ans": "b. trade fixtures.", "exp": "Trade fixtures belong to the tenant and are removable."},
        {"q": "3. The term nonhomogeneity refers to:", "opts": "a. scarcity.\nb. immobility.\nc. uniqueness.\nd. indestructibility.", "ans": "c. uniqueness.", "exp": "No two parcels of land are exactly the same."},
        {"q": "4. Another term for personal property is:", "opts": "a. realty.\nb. fixtures.\nc. chattels.\nd. fructus naturales.", "ans": "c. chattels.", "exp": "Chattel is the legal name for personal property."},
        {"q": "5. A property owner wants to use water from a river... the state relies on:", "opts": "a. riparian rights.\nb. littoral rights.\nc. doctrine of prior appropriation.\nd. accession.", "ans": "c. doctrine of prior appropriation.", "exp": "Controlled by the state via permits."},
        {"q": "6. Which of the following is considered real property?", "opts": "a. emblems.\nb. a stud in the wall.\nc. a patio umbrella.\nd. a leasehold interest.", "ans": "b. a stud in the wall.", "exp": "It is a permanent part of the structure."},
        {"q": "7. Water rights for land abutting a river are:", "opts": "a. riparian rights.\nb. littoral rights.\nc. prior appropriation.\nd. erosion.", "ans": "a. riparian rights.", "exp": "Riparian = Rivers."},
        {"q": "8. The sudden removal of soil by an act of nature is:", "opts": "a. avulsion.\nb. erosion.\nc. accretion.\nd. accession.", "ans": "a. avulsion.", "exp": "Avulsion is sudden (flood/earthquake)."},
        {"q": "9. Annual crops are known as:", "opts": "a. emblements.\nb. fructus naturales.\nc. fixtures.\nd. appurtenances.", "ans": "a. emblements.", "exp": "Also called fructus industriales."},
        {"q": "10. The most important economic characteristic of land is:", "opts": "a. area preference.\nb. uniqueness.\nc. permanence.\nd. scarcity.", "ans": "a. area preference.", "exp": "Situs (location preference)."},
        {"q": "11. A ceiling fan is usually considered:", "opts": "a. a fixture.\nb. chattel.\nc. an emblement.\nd. an appurtenance.", "ans": "a. a fixture.", "exp": "It is permanently attached."},
        {"q": "12. The phrase 'bundle of legal rights' is properly included in:", "opts": "a. the definition of land.\nb. the definition of real estate.\nc. the definition of real property.\nd. the definition of personal property.", "ans": "c. the definition of real property.", "exp": "Real Property = Real Estate + Rights."},
        {"q": "13. A right, privilege, or improvement that passes with land is:", "opts": "a. an appurtenance.\nb. an emblement.\nc. a fixture.\nb. chattel.", "ans": "a. an appurtenance.", "exp": "Runs with the land."},
        {"q": "14. Parking spaces in multiunit buildings are classified as:", "opts": "a. covenants.\nb. emblements.\nc. chattels.\nd. appurtenances.", "ans": "d. appurtenances.", "exp": "They stay with the specific unit."},
        {"q": "15. A method by which real property can be converted to personal property is:", "opts": "a. severance.\nb. annexation.\nc. accretion.\nd. avulsion.", "ans": "a. severance.", "exp": "Severing/cutting it away."},
        {"q": "16. A farmer has a 20-year lease on a farm. The landlord dies. What happens?", "opts": "a. The lease terminates.\nb. The lease remains in effect.\nc. The lease must be renegotiated.\nd. The farmer is evicted.", "ans": "b. The lease remains in effect.", "exp": "Leases usually 'survive' the death of the landlord."},
        {"q": "17. Which is an example of an appurtenance?", "opts": "a. A custom mailbox.\nb. An easement.\nc. A tractor.\nd. A refrigerator.", "ans": "b. An easement.", "exp": "Easements are classic appurtenances."},
        {"q": "18. The process by which the government takes private land for public use:", "opts": "a. escheat.\nb. eminent domain.\nc. taxation.\nd. police power.", "ans": "b. eminent domain.", "exp": "Eminent Domain is the power; Condemnation is the act."},
        {"q": "19. A concern about location is called:", "opts": "a. physical deterioration.\nb. area preference.\nc. permanence of investment.\nd. immobility.", "ans": "b. area preference.", "exp": "Situs."},
        {"q": "20. Manufactured housing is personal property unless:", "opts": "a. it is painted.\nb. it is moved.\nc. it is permanently affixed to land.\nd. it is rented.", "ans": "c. it is permanently affixed to land.", "exp": "Once affixed, it becomes real estate."}
    ]

    # 2. THE 28 VOCAB TERMS
    terms_bank = [
        {"q": "Accession", "opts": "", "ans": "Acquiring title via annexation or accretion.", "exp": "Legal way property grows."},
        {"q": "Accretion", "opts": "", "ans": "Increase in land via water-borne soil.", "exp": "The opposite of erosion."},
        {"q": "Air Rights", "opts": "", "ans": "Rights to use space above earth.", "exp": "Can be leased or sold independently."},
        {"q": "Annexation", "opts": "", "ans": "Converting personal property to real property.", "exp": "Example: Mixing sand into concrete."},
        {"q": "Appurtenance", "opts": "", "ans": "A right that 'runs with the land.'", "exp": "Easements, parking spaces, etc."},
        {"q": "Avulsion", "opts": "", "ans": "Sudden removal of soil by nature.", "exp": "Like a flood or landslide."},
        {"q": "Bundle of Legal Rights", "opts": "", "ans": "PCEED rights.", "exp": "Possess, Control, Enjoy, Exclude, Dispose."},
        {"q": "Chattel", "opts": "", "ans": "Movable personal property.", "exp": "Think 'Cattle' = movable."},
        {"q": "Emblements", "ofpts": "", "ans": "Annual crops (Personal Property).", "exp": "Fructus industriales."},
        {"q": "Erosion", "opts": "", "ans": "Gradual wearing away of land.", "exp": "Slow natural process."},
        {"q": "Fixture", "opts": "", "ans": "Personal property now part of real estate.", "exp": "Uses the MARIA test."},
        {"q": "Improvement", "opts": "", "ans": "Artificial attachment to land.", "exp": "Buildings, fences, sewers."},
        {"q": "Land", "opts": "", "ans": "Surface, subsurface, and air.", "exp": "Natural definition."},
        {"q": "Littoral Rights", "opts": "", "ans": "Rights along non-flowing water.", "exp": "Lakes, seas, oceans."},
        {"q": "Manufactured Housing", "opts": "", "ans": "Off-site construction.", "exp": "Personal property until affixed."},
        {"q": "Nonhomogeneity", "opts": "", "ans": "Uniqueness.", "exp": "Physical characteristic of land."},
        {"q": "Prior Appropriation", "opts": "", "ans": "State-controlled water rights.", "exp": "Permit-based system."},
        {"q": "Real Estate", "ofpts": "", "ans": "Land + Improvements.", "exp": "Physical property."},
        {"q": "Real Property", "opts": "", "ans": "Real Estate + Bundle of Rights.", "exp": "Legal definition."},
        {"q": "Riparian Rights", "opts": "", "ans": "Rights along flowing water.", "exp": "Rivers and streams."},
        {"q": "Severance", "opts": "", "ans": "Real property to Personal property.", "exp": "Cutting down a tree."},
        {"q": "Situs", "opts": "", "ans": "Economic area preference.", "exp": "Location value."},
        {"q": "Subsurface Rights", "opts": "", "ans": "Rights beneath the surface.", "exp": "Minerals, oil, gas."},
        {"q": "Surface Rights", "opts": "", "ans": "Ownership of surface only.", "exp": "Limited rights."},
        {"q": "Trade Fixture", "opts": "", "ans": "Tenant business equipment.", "exp": "Removable by tenant."},
        {"q": "Water Rights", "opts": "", "ans": "Common law rights to water.", "exp": "Depends on location."},
        {"q": "MARIA", "opts": "", "ans": "Method, Adaptability, Relationship, Intention, Agreement.", "exp": "The fixture test."},
        {"q": "Ohio Title 47", "opts": "", "ans": "Ohio RE License Law.", "exp": "Chapter 4735."}
    ]
    
    st.session_state.cards = quiz_bank + terms_bank
    random.shuffle(st.session_state.cards)

# UI Logic
if 'idx' not in st.session_state: st.session_state.idx = 0
if 'reveal' not in st.session_state: st.session_state.reveal = False

st.sidebar.title("🎧 Study Vibe")
st.sidebar.video("https://www.youtube.com/watch?v=5yx6BWlEVcY")
st.sidebar.metric("Total Cards", len(st.session_state.cards))

st.markdown(f"### Card {st.session_state.idx + 1} of {len(st.session_state.cards)}")
curr = st.session_state.cards[st.session_state.idx]

with st.container(border=True):
    st.markdown(f"#### {curr['q']}")
    if curr['opts']:
        st.info(curr['opts'])
    
    if st.session_state.reveal:
        st.divider()
        st.success(f"**{curr['ans']}**")
        st.write(f"💡 {curr['exp']}")

c1, c2, c3 = st.columns(3)
with c1:
    if st.button("⬅️ Previous"):
        st.session_state.idx = (st.session_state.idx - 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.rerun()
with c2:
    if st.button("Reveal Answer", type="primary", use_container_width=True):
        st.session_state.reveal = not st.session_state.reveal
        st.rerun()
with c3:
    if st.button("Next ➡️"):
        st.session_state.idx = (st.session_state.idx + 1) % len(st.session_state.cards)
        st.session_state.reveal = False
        st.rerun()
