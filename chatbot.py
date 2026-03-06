import streamlit as st
import random
import time

# Streamed response emulator
def response_generator():
    response = random.choice(
        [
            "Hello there! How can I assist you today?",
            "Hi, human! Is there anything I can help you with?",
            "Do you need help?",
            "Oh wow, I wasn’t expecting that!",
            "Haha, that actually made me smile.",
            "I get what you’re saying, totally makes sense.",
            "That’s a great question—let me think for a sec.",
            "I like that idea, it’s got some real potential.",
            "Wait, seriously? That’s wild!",
            "No problem at all, I’ve got you covered.",
            "That sounds like a good plan to me.",
            "I can see why you’d feel that way.",
            "Well, that took an unexpected turn!",
            "Thanks for sharing that—it’s actually really interesting.",
            "Haha, I see what you did there.",
            "That reminds me of something I read recently.",
            "Good point! You’ve got a sharp eye.",
            "That must’ve been quite an experience.",
            "I love the energy you’re bringing right now.",
            "Not gonna lie, that’s a solid take.",
            "You’ve got me curious now—tell me more.",
            "That’s one way to put it, and I kinda like it.",
            "You know what, that actually makes a lot of sense.",
            "A bold move! I respect it.",
            "Hang on, I’m processing that—it’s a lot to unpack!",
            "That’s a pretty creative way to think about it.",
            "Haha, you’re definitely keeping things interesting.",
            "Love that attitude—it’s contagious!"
        ]
    )
    for word in response.split():
        yield word + " "
        time.sleep(0.05)


st.title("Simple chat")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display chat messages from history on app rerun
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Accept user input
if prompt := st.chat_input("What is up?"):
    # Display user message in chat message container
    with st.chat_message("user"):
        st.markdown(prompt)
    # Add user message to chat history
    st.session_state.messages.append({"role": "user", "content": prompt})


# Display assistant response in chat message container
with st.chat_message("assistant"):
    response = st.write_stream(response_generator())

# Add assistant response to chat history
st.session_state.messages.append({"role": "assistant", "content": response})
