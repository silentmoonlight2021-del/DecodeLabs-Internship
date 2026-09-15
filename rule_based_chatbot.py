import random

def enhanced_rule_based_chatbot():
    # Knowledge base with lists of responses for variety
    knowledge_base = {
        "greetings": {
            "keywords": ["hello", "hi", "hey", "greetings"],
            "responses": [
                "Hello! How can I assist you today?",
                "Hey there! What can I help you with?",
                "Hi! Ready to assist you."
            ]
        },
        "identity": {
            "keywords": ["who are you", "your name", "what are you"],
            "responses": [
                "I am an Enhanced Rule-Based AI Chatbot created for DecodeLabs Project 1.",
                "I'm a deterministic AI bot designed using Python dictionary logic!"
            ]
        },
        "capabilities": {
            "keywords": ["what can you do", "help", "features", "skills"],
            "responses": [
                "I can process text, perform keyword matching, and reply with dynamic responses!",
                "You can ask me about AI, Python, my identity, or type 'exit' to end the chat."
            ]
        },
        "python": {
            "keywords": ["python", "code", "programming"],
            "responses": [
                "Python is a clean, readable language perfect for building AI systems.",
                "Python makes logic design simple and fast with powerful dictionary data structures."
            ]
        },
        "ai": {
            "keywords": ["ai", "artificial intelligence", "ml"],
            "responses": [
                "Artificial Intelligence combines deterministic guardrails with probabilistic learning!",
                "AI systems start with explicit rules before moving into machine learning."
            ]
        }
    }

    print("==================================================")
    print("   DECODELABS - ENHANCED RULE-BASED AI ENGINE    ")
    print("==================================================")
    print("System Status: Active | Type 'exit' or 'bye' to quit.\n")

    while True:
        raw_input = input("You: ")
        clean_input = raw_input.lower().strip()

        # Exit Command
        if clean_input in ["exit", "bye", "quit"]:
            print("\nBot: Thank you for chatting! Goodbye.")
            break

        if not clean_input:
            continue

        matched_response = None

        # Keyword matching engine
        for intent, data in knowledge_base.items():
            if any(keyword in clean_input for keyword in data["keywords"]):
                matched_response = random.choice(data["responses"])
                break

        # Fallback Strategy
        if not matched_response:
            matched_response = "I don't have a rule for that phrase yet. Try asking about 'AI', 'Python', or type 'help'."

        print(f"Bot: {matched_response}\n")

if __name__ == "__main__":
    enhanced_rule_based_chatbot()