from mailbox import Message
from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from config import GROQ_API_KEY

sessions_db = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    """Retrieves or creates a chat history for a specific session ID."""
    if session_id not in sessions_db:
        sessions_db[session_id] = InMemoryChatMessageHistory()
    return sessions_db[session_id]

def create_stateful_bot():
    """Initialize the LLM and chains it with message history management."""
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are a helpful assistant."),
        MessagesPlaceholder(variable_name="history"),
        ("human", "{messages}")
    ])
    chain = prompt | llm 
    stateful_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="messages",
        history_messages_key="history"
    )
    return stateful_chain 
