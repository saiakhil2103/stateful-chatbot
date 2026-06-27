from langchain_groq import ChatGroq
from langchain_core.chat_history import InMemoryChatMessageHistory
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import SystemMessage, HumanMessage
from src.config import GROQ_API_KEY 

sessions_db = {}

def get_session_history(session_id: str) -> InMemoryChatMessageHistory:
    if session_id not in sessions_db:
        sessions_db[session_id] = InMemoryChatMessageHistory()
    return sessions_db[session_id]

def create_summary_bot():
    """Initializes a chatbot that uses a running summary of past context"""
    llm = ChatGroq(model="llama-3.1-8b-instant", api_key=GROQ_API_KEY)
    prompt = ChatPromptTemplate.from_messages([
        ("system", (
            "You are a helpful assistant. Here is the summary of the conversation so far "
            "to help you maintain context.\n\n"
            "CRITICAL RULE: Do not mention, repeat, or quote this summary in your response."
            "Only use it as silent background knowledge to answer the user's latest message.\n\n"
            "Current Summary: {summary}"
        )),
        ("human", "{messages}")
    ])
    chain = prompt | llm 
    stateful_chain = RunnableWithMessageHistory(
        chain,
        get_session_history,
        input_messages_key="messages",
        history_messages_key="unused_history"
    )
    return stateful_chain, llm 

def summarize_chat_history(llm, history: InMemoryChatMessageHistory, current_summary: str) -> str:
    """Calls the LLM to generate a new summary combining old summary and a new messages."""
    messages = history.messages 
    if not messages:
        return current_summary 
    summary_prompt = (
        f"Current Summary: {current_summary}\n\n"
        f"New messages: {messages}\n\n"
        f"Distill the conversation into a concise updated summary, retaining crucial details."
    )
    response = llm.invoke([HumanMessage(content=summary_prompt)])
    return response.content 