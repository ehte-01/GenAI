import streamlit as st
from dotenv import load_dotenv

from langchain_mistralai import ChatMistralAI
from langchain_core.messages import AIMessage, SystemMessage, HumanMessage

load_dotenv()

st.set_page_config(page_title="Mood AI Chatbot", page_icon="🤖", layout="centered")

# ---------- Mode definitions ----------
MODES = {
    "Angry Mode 😡": "You are an angry AI Agent. You respond aggressively and impatiently.",
    "Funny Mode 😂": "You are a very funny AI Agent. You respond with humour and jokes.",
    "Sad Mode 😢": "You are a very sad AI Agent. You respond in a depressed and emotional tone.",
}

# ---------- Sidebar: mode selection ----------
st.sidebar.title("⚙️ Settings")
selected_mode_label = st.sidebar.selectbox("Choose your AI mode:", list(MODES.keys()))
selected_system_prompt = MODES[selected_mode_label]

if st.sidebar.button("🔄 Reset Chat"):
    st.session_state.messages = [SystemMessage(content=selected_system_prompt)]
    st.session_state.current_mode = selected_mode_label
    st.rerun()

# ---------- Session state init ----------
if "messages" not in st.session_state:
    st.session_state.messages = [SystemMessage(content=selected_system_prompt)]
    st.session_state.current_mode = selected_mode_label

# If user changes mode mid-session, reset the conversation with new system prompt
if st.session_state.current_mode != selected_mode_label:
    st.session_state.messages = [SystemMessage(content=selected_system_prompt)]
    st.session_state.current_mode = selected_mode_label
    st.rerun()

# ---------- Model ----------
@st.cache_resource
def get_model():
    return ChatMistralAI(model="mistral-small-2506", temperature=0.9)

model = get_model()

# ---------- UI ----------
st.title("🤖 Mood-Based AI Chatbot")
st.caption(f"Currently in: **{selected_mode_label}**")

# Display chat history (skip the SystemMessage)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

# Chat input
prompt = st.chat_input("Type your message...")

if prompt:
    # Add user message
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    # Get bot response
    with st.chat_message("assistant"):
        with st.spinner("Thinking..."):
            response = model.invoke(st.session_state.messages)
            st.markdown(response.content)

    st.session_state.messages.append(AIMessage(content=response.content))