from model_loader import load_model
from chat_memory import ChatMemory
import os

class ChatbotInterface:
    def __init__(self):
        self.client, _ = load_model()
        self.memory = ChatMemory(window_size=3)  # Last 3 exchanges (6 messages)

    def generate_response(self, prompt):
        try:
            # Build context-aware prompt
            messages = self.memory.get_context()
            messages.append({"role": "user", "content": prompt})  # Add current user input


            response = self.client.chat_completion(
                model="mistralai/Mistral-7B-Instruct-v0.2",
                messages=messages,
                max_tokens=200,
                temperature=0.7
            )

            bot_reply = response.choices[0].message.content.strip()

            # Store the actual exchange in memory
            self.memory.add_exchange(prompt, bot_reply)

            return self.clean_response(bot_reply)
        
        except Exception as e:
            return f"Error: {str(e)}"

    def clean_response(self, response):
        """Ensure complete sentences and proper formatting"""
        if response and response[-1] not in {'.', '!', '?'}:
            last_punct = max(response.rfind('.'), response.rfind('!'), response.rfind('?'))
            if last_punct > 0:
                response = response[:last_punct+1]
        return response or "I didn't get that. Could you rephrase?"

    def run(self):
        print("Chatbot ready! Type '/exit' to quit.")
        while True:
            user_input = input("You: ").strip()
            if user_input.lower() == '/exit':
                print("Goodbye!")
                break
            if user_input:
                response = self.generate_response(user_input)
                print("Bot:", response)

if __name__ == "__main__":
    if not os.getenv("HF_TOKEN"):
        print("ERROR: Set HF_TOKEN environment variable first!")
        print("Run: set HF_TOKEN=your_api_token_here")
    else:
        ChatbotInterface().run()
