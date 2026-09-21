import streamlit as st

# 1. Initialize our card deck state
if "card_index" not in st.session_state:
    st.session_state.card_index = 0

# Sample flashcard data
flashcards = [
    {"proverb": "À chaque instant de notre vie, nous avons une main sur la porte de l'avenir", 
     "anglais": "At every moment of our life, we have a hand on the door of the future",
    "By": "Maeterlinck", "date": "9/20/2026"},
    {"proverb": "Un sourire coûte moins cher que l'électricité, mais donne autant de lumière", 
     "anglais": "A smile costs less than electricity but gives just as much light",
    "By": "Pierre", "date": "9/20/2026"},
    {"proverb": "Le monde est beau avant d'être vrai", 
     "anglais": "The world is beautiful before it is true",
    "By": "Whyte", "date": "9/20/2026"}
]

st.title("Francaise Flashcards 🗂️")
st.write("Click 'Know It' or 'Review Later' to sort through your deck.")

# Check if we have run out of cards
if st.session_state.card_index < len(flashcards):
    current_card = flashcards[st.session_state.card_index]
    
    # Render the card UI block
    with st.container(border=True):
        st.subheader(current_card["proverb"])
        
        # Simple toggle to simulate flipping a card over
        if st.button("👁️ Reveal translation"):
            st.info(current_card["anglais"])
            
    # Decision Buttons mimicking a Left/Right swipe
    col1, col2 = st.columns(2)
    with col1:
        if st.button("❌ Review Later", use_container_width=True):
            st.warning(f"Marked '{current_card['proverb']}' for review.")
            st.session_state.card_index += 1
            st.rerun()
            
    with col2:
        if st.button("✅ Know It!", use_container_width=True):
            st.success(f"Mastered '{current_card['proverb']}'!")
            st.session_state.card_index += 1
            st.rerun()
else:
    st.balloons()
    st.success("🎉 You've finished all the cards in this deck!")
    if st.button("🔄 Restart Deck"):
        st.session_state.card_index = 0
        st.rerun()
