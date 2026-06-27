import streamlit as st 
from src.summary_manager import create_summary_bot, summarize_chat_history, get_session_history

st.set_page_config(page_title="Stateful Chatbot", page_icon="🤖")
st.title("🤖 Stateful Chatbot with Summary Memory")

if "current_summary" not in st.session_state:
    st.session_state.current_summary = "No conversation history yet."

if "messages" not in st.session_state:
    st.session_state.messages = []

bot_chain, summary_llm = create_summary_bot()
session_id = "streamlit_user_session"
config = {"configurable": {"session_id": session_id}}

for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if user_input := st.chat_input("What's on you mind?"):
    with st.chat_message("user"):
        st.markdown(user_input)
    st.session_state.messages.append({"role": "user", "content": user_input})

    with st.chat_message("assistant"):
        response = bot_chain.invoke(
            {"messages": user_input, "summary": st.session_state.current_summary},
            config=config
        )
        st.markdown(response.content)
    st.session_state.messages.append({"role": "assistant", "content": response.content})

    history = get_session_history(session_id)
    st.session_state.current_summary = summarize_chat_history(summary_llm, history, st.session_state.current_summary)