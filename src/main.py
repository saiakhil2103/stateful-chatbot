from llm_manager import create_stateful_bot
from summary_manager import create_summary_bot, summarize_chat_history, get_session_history

def run_chatbot():
    print("🤖 Stateful Chatbot with Summary Memory Initialized!")
    print("Type 'exit' or 'quit' to end the conversation.\n")

    bot_chain, summary_llm = create_summary_bot()

    session_id = "local_summary_user"
    config = {"configurable": {"session_id": session_id}}

    current_summary = "No conversation history yet"

    while True:
        try:
            user_input = input("You: ")
            if user_input.lower() in ["exit", "quit"]:
                print("🤖 Goodbye!")
                break 
            if not user_input.strip():
                continue 

            response = bot_chain.invoke(
                {"messages": user_input, "summary": current_summary},
                config=config
            )

            print(f"Bot: {response.content}\n")

            history = get_session_history(session_id)
            current_summary = summarize_chat_history(summary_llm, history, current_summary)
        except KeyboardInterrupt:
            print("\n🤖 Session interrupted. Goodbye!")
            break 

if __name__ == "__main__":
    run_chatbot()
