"""
AGI Framework - Context Manager
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Context management for maintaining conversation state and memory
"""

from typing import Dict, List, Optional, Any
from datetime import datetime
from collections import deque


class ConversationTurn:
    """Represents a single turn in a conversation."""
    
    def __init__(
        self,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ):
        """
        Initialize conversation turn.
        
        Args:
            role: Role of the speaker (e.g., 'user', 'assistant', 'system')
            content: Content of the message
            metadata: Optional metadata
        """
        self.role = role
        self.content = content
        self.metadata = metadata or {}
        self.timestamp = datetime.now().isoformat()
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert to dictionary."""
        return {
            "role": self.role,
            "content": self.content,
            "metadata": self.metadata,
            "timestamp": self.timestamp,
        }
    
    def __repr__(self) -> str:
        return f"ConversationTurn(role={self.role}, content_length={len(self.content)})"


class ContextManager:
    """
    Context manager for AGI models.
    
    Manages conversation history, context windows, and memory for
    maintaining coherent long-term interactions.
    
    Features:
    - Conversation history tracking
    - Context window management
    - Memory summarization
    - Multi-turn conversation support
    - Context pruning strategies
    """
    
    def __init__(
        self,
        max_context_length: int = 4096,
        max_turns: int = 50,
        summarization_threshold: int = 40
    ):
        """
        Initialize context manager.
        
        Args:
            max_context_length: Maximum length of context in tokens
            max_turns: Maximum number of conversation turns to keep
            summarization_threshold: Number of turns before summarization
        """
        self.max_context_length = max_context_length
        self.max_turns = max_turns
        self.summarization_threshold = summarization_threshold
        
        self.conversation_history: deque = deque(maxlen=max_turns)
        self.context_summary = ""
        self.metadata = {
            "created_at": datetime.now().isoformat(),
            "total_turns": 0,
            "summarization_count": 0,
        }
    
    def add_turn(
        self,
        role: str,
        content: str,
        metadata: Optional[Dict[str, Any]] = None
    ) -> None:
        """
        Add a conversation turn.
        
        Args:
            role: Speaker role
            content: Message content
            metadata: Optional metadata
        """
        turn = ConversationTurn(role, content, metadata)
        self.conversation_history.append(turn)
        self.metadata["total_turns"] += 1
        
        # Check if summarization is needed
        if len(self.conversation_history) >= self.summarization_threshold:
            self._summarize_context()
    
    def get_context(
        self,
        num_turns: Optional[int] = None,
        include_summary: bool = True
    ) -> str:
        """
        Get formatted context for model input.
        
        Args:
            num_turns: Number of recent turns to include (None for all)
            include_summary: Whether to include context summary
            
        Returns:
            Formatted context string
        """
        context_parts = []
        
        # Add summary if available
        if include_summary and self.context_summary:
            context_parts.append(f"[Previous Context Summary]\n{self.context_summary}\n")
        
        # Add recent turns
        turns_to_include = list(self.conversation_history)
        if num_turns is not None:
            turns_to_include = turns_to_include[-num_turns:]
        
        for turn in turns_to_include:
            context_parts.append(f"{turn.role}: {turn.content}")
        
        return "\n".join(context_parts)
    
    def get_conversation_history(self) -> List[Dict[str, Any]]:
        """
        Get full conversation history.
        
        Returns:
            List of conversation turn dictionaries
        """
        return [turn.to_dict() for turn in self.conversation_history]
    
    def clear_history(self) -> None:
        """Clear conversation history."""
        num_turns = len(self.conversation_history)
        self.conversation_history.clear()
        self.context_summary = ""
        print(f"Cleared {num_turns} conversation turns")
    
    def _summarize_context(self) -> None:
        """Summarize older context to save space."""
        if len(self.conversation_history) < self.summarization_threshold:
            return
        
        # Take first half of conversation for summarization
        num_to_summarize = len(self.conversation_history) // 2
        turns_to_summarize = list(self.conversation_history)[:num_to_summarize]
        
        # Create summary
        summary_parts = [
            f"Summary of {num_to_summarize} conversation turns:",
            "Key topics discussed:",
        ]
        
        # Extract key points (simplified)
        for turn in turns_to_summarize:
            if len(turn.content) > 50:
                summary_parts.append(f"- {turn.role}: {turn.content[:50]}...")
        
        self.context_summary = "\n".join(summary_parts)
        self.metadata["summarization_count"] += 1
        
        print(f"Context summarized ({num_to_summarize} turns)")
    
    def prune_context(self, strategy: str = "oldest") -> None:
        """
        Prune context using specified strategy.
        
        Args:
            strategy: Pruning strategy ('oldest', 'least_relevant')
        """
        if strategy == "oldest":
            if len(self.conversation_history) > 0:
                removed = self.conversation_history.popleft()
                print(f"Removed oldest turn: {removed.role}")
        
        elif strategy == "least_relevant":
            # Simplified: remove turns with shortest content
            if len(self.conversation_history) > 0:
                min_turn = min(self.conversation_history, key=lambda t: len(t.content))
                self.conversation_history.remove(min_turn)
                print(f"Removed least relevant turn: {min_turn.role}")
    
    def get_context_length(self) -> int:
        """
        Estimate current context length in tokens.
        
        Returns:
            Estimated token count
        """
        # Rough estimation: ~4 characters per token
        total_chars = sum(len(turn.content) for turn in self.conversation_history)
        return total_chars // 4
    
    def is_context_full(self) -> bool:
        """
        Check if context is approaching maximum length.
        
        Returns:
            True if context is > 90% full
        """
        current_length = self.get_context_length()
        return current_length > (self.max_context_length * 0.9)
    
    def add_system_message(self, message: str) -> None:
        """
        Add a system message to context.
        
        Args:
            message: System message content
        """
        self.add_turn("system", message, {"type": "system_instruction"})
    
    def get_last_turn(self, role: Optional[str] = None) -> Optional[ConversationTurn]:
        """
        Get the last conversation turn.
        
        Args:
            role: Optional role filter
            
        Returns:
            Last matching turn or None
        """
        if not self.conversation_history:
            return None
        
        if role is None:
            return self.conversation_history[-1]
        
        # Find last turn with matching role
        for turn in reversed(self.conversation_history):
            if turn.role == role:
                return turn
        
        return None
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get context statistics.
        
        Returns:
            Statistics dictionary
        """
        stats = {
            "total_turns": self.metadata["total_turns"],
            "current_turns": len(self.conversation_history),
            "context_length_tokens": self.get_context_length(),
            "context_length_percentage": (self.get_context_length() / self.max_context_length) * 100,
            "summarization_count": self.metadata["summarization_count"],
            "has_summary": bool(self.context_summary),
        }
        return stats
    
    def export_conversation(self, filepath: str) -> None:
        """
        Export conversation to file.
        
        Args:
            filepath: Path to export file
        """
        import json
        
        data = {
            "metadata": self.metadata,
            "context_summary": self.context_summary,
            "conversation": self.get_conversation_history(),
        }
        
        with open(filepath, 'w') as f:
            json.dump(data, f, indent=2)
        
        print(f"Conversation exported to {filepath}")
    
    def __repr__(self) -> str:
        return f"ContextManager(turns={len(self.conversation_history)}, length={self.get_context_length()})"
