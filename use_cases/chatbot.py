"""
AGI Framework - Chatbot Use Case
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Complete use case: Building an intelligent chatbot
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine
from agi.utils import PromptEngineer, ContextManager


class AGIChatbot:
    """Intelligent chatbot using AGI Framework."""
    
    def __init__(self, name: str = "AGI Assistant"):
        """Initialize chatbot."""
        self.name = name
        
        # Initialize components
        self.model = AGIModel(
            model_name=f"AGI-Chatbot-{name}",
            version="1.0.0"
        )
        
        self.inference_engine = InferenceEngine(self.model)
        self.context_manager = ContextManager(max_context_length=2048)
        self.prompt_engineer = PromptEngineer()
        
        # Setup system prompt
        self._setup_system_prompt()
        
        # Train the model (simulated)
        self._train_chatbot()
    
    def _setup_system_prompt(self):
        """Setup system prompt for chatbot personality."""
        system_message = f"""You are {self.name}, a helpful and friendly AI assistant.
You provide accurate, informative, and engaging responses.
You maintain context across the conversation and ask clarifying questions when needed."""
        
        self.context_manager.add_system_message(system_message)
    
    def _train_chatbot(self):
        """Train the chatbot model."""
        training_data = [
            "Hello, how can I help you today?",
            "I understand your question. Let me explain...",
            "That's an interesting topic. Here's what I know...",
        ] * 10
        
        self.model.train(training_data, epochs=5)
    
    def chat(self, user_message: str) -> str:
        """
        Process user message and return response.
        
        Args:
            user_message: User's input message
            
        Returns:
            Chatbot response
        """
        # Add user message to context
        self.context_manager.add_turn("user", user_message)
        
        # Get conversation context
        context = self.context_manager.get_context(num_turns=10)
        
        # Create prompt with context
        prompt = f"{context}\nassistant:"
        
        # Generate response
        response = self.inference_engine.generate(
            prompt,
            temperature=0.7,
            max_length=256
        )
        
        # Add response to context
        self.context_manager.add_turn("assistant", response)
        
        return response
    
    def reset_conversation(self):
        """Reset conversation history."""
        self.context_manager.clear_history()
        self._setup_system_prompt()
    
    def get_conversation_stats(self):
        """Get conversation statistics."""
        return self.context_manager.get_statistics()


def main():
    """Main chatbot use case demonstration."""
    print("=" * 60)
    print("AGI Framework - Chatbot Use Case")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize chatbot
    print("Initializing AGI Chatbot...")
    chatbot = AGIChatbot(name="AGI Assistant")
    print(f"Chatbot '{chatbot.name}' is ready!")
    print()
    
    # Simulate conversation
    print("=" * 60)
    print("Starting Conversation Simulation")
    print("=" * 60)
    print()
    
    conversations = [
        "Hello! How are you today?",
        "Can you tell me about artificial intelligence?",
        "What are the main applications of AI?",
        "How does machine learning differ from traditional programming?",
        "Can you explain neural networks in simple terms?",
        "Thank you for the explanations!",
    ]
    
    for user_message in conversations:
        print(f"User: {user_message}")
        response = chatbot.chat(user_message)
        print(f"{chatbot.name}: {response}")
        print()
    
    # Display conversation statistics
    print("=" * 60)
    print("Conversation Statistics")
    print("=" * 60)
    stats = chatbot.get_conversation_stats()
    print(f"Total turns: {stats['total_turns']}")
    print(f"Current context: {stats['current_turns']} turns")
    print(f"Context length: {stats['context_length_tokens']} tokens")
    print(f"Context usage: {stats['context_length_percentage']:.1f}%")
    print()
    
    # Export conversation
    print("Exporting conversation history...")
    chatbot.context_manager.export_conversation("chatbot_conversation.json")
    print()
    
    # Test reset functionality
    print("=" * 60)
    print("Testing Conversation Reset")
    print("=" * 60)
    print()
    
    print("Resetting conversation...")
    chatbot.reset_conversation()
    
    new_message = "Hi, this is a fresh start!"
    print(f"User: {new_message}")
    response = chatbot.chat(new_message)
    print(f"{chatbot.name}: {response}")
    print()
    
    new_stats = chatbot.get_conversation_stats()
    print(f"New conversation turns: {new_stats['total_turns']}")
    print()
    
    print("=" * 60)
    print("Chatbot Use Case Complete!")
    print("=" * 60)
    print()
    print("Key Features Demonstrated:")
    print("  ✓ Context management across conversation")
    print("  ✓ System prompt for personality")
    print("  ✓ Conversation history tracking")
    print("  ✓ Statistics and monitoring")
    print("  ✓ Conversation export")
    print("  ✓ Reset functionality")


if __name__ == "__main__":
    main()
