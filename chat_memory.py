class ChatMemory:
    def __init__(self, window_size=3):
        self.window_size = window_size * 2  # Store both user+bot messages
        self.history = []
    
    def add_exchange(self, user_input, bot_response):
        """Add new exchange with sliding window"""
        self.history.extend([
            {"role": "user", "content": user_input},
            {"role": "assistant", "content": bot_response}
        ])
        self.history = self.history[-self.window_size:]  # Enforce window size
    
    def get_context(self):
        """Return last N messages as HF API format"""
        return self.history.copy()
