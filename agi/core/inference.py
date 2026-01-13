"""
AGI Framework - Inference Engine
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Inference and generation utilities for trained models
"""

from typing import Dict, List, Optional, Any, Union
from datetime import datetime
import time


class InferenceConfig:
    """Configuration for model inference."""
    
    def __init__(
        self,
        temperature: float = 0.7,
        top_p: float = 0.9,
        top_k: int = 50,
        max_length: int = 512,
        repetition_penalty: float = 1.0,
        num_return_sequences: int = 1,
        do_sample: bool = True
    ):
        """
        Initialize inference configuration.
        
        Args:
            temperature: Sampling temperature (higher = more random)
            top_p: Nucleus sampling threshold
            top_k: Top-k sampling parameter
            max_length: Maximum generation length
            repetition_penalty: Penalty for repeating tokens
            num_return_sequences: Number of sequences to generate
            do_sample: Whether to use sampling or greedy decoding
        """
        self.temperature = temperature
        self.top_p = top_p
        self.top_k = top_k
        self.max_length = max_length
        self.repetition_penalty = repetition_penalty
        self.num_return_sequences = num_return_sequences
        self.do_sample = do_sample
    
    def to_dict(self) -> Dict[str, Any]:
        """Convert configuration to dictionary."""
        return {
            "temperature": self.temperature,
            "top_p": self.top_p,
            "top_k": self.top_k,
            "max_length": self.max_length,
            "repetition_penalty": self.repetition_penalty,
            "num_return_sequences": self.num_return_sequences,
            "do_sample": self.do_sample,
        }


class InferenceEngine:
    """
    Inference engine for AGI models.
    
    Provides optimized inference capabilities including:
    - Text generation
    - Batch processing
    - Multiple sampling strategies
    - Response caching
    - Performance monitoring
    """
    
    def __init__(
        self,
        model: Any,
        config: Optional[InferenceConfig] = None
    ):
        """
        Initialize inference engine.
        
        Args:
            model: Trained model instance
            config: Inference configuration
        """
        self.model = model
        self.config = config or InferenceConfig()
        self.inference_stats = {
            "total_requests": 0,
            "total_tokens_generated": 0,
            "average_latency": 0.0,
        }
        self._response_cache = {}
        
    def generate(
        self,
        prompt: str,
        max_length: Optional[int] = None,
        temperature: Optional[float] = None,
        use_cache: bool = True,
        **kwargs
    ) -> str:
        """
        Generate text from prompt.
        
        Args:
            prompt: Input prompt text
            max_length: Maximum length of generated text
            temperature: Sampling temperature
            use_cache: Whether to use response caching
            **kwargs: Additional generation parameters
            
        Returns:
            Generated text
        """
        # Check cache
        cache_key = f"{prompt}_{max_length}_{temperature}"
        if use_cache and cache_key in self._response_cache:
            return self._response_cache[cache_key]
        
        start_time = time.time()
        
        # Use config defaults if not specified
        max_length = max_length or self.config.max_length
        temperature = temperature or self.config.temperature
        
        # Generate text using the model
        generated_text = self.model.generate(
            prompt,
            max_length=max_length,
            temperature=temperature,
            **kwargs
        )
        
        # Update statistics
        latency = time.time() - start_time
        self._update_stats(generated_text, latency)
        
        # Cache response
        if use_cache:
            self._response_cache[cache_key] = generated_text
        
        return generated_text
    
    def batch_generate(
        self,
        prompts: List[str],
        max_length: Optional[int] = None,
        temperature: Optional[float] = None,
        **kwargs
    ) -> List[str]:
        """
        Generate text for multiple prompts in batch.
        
        Args:
            prompts: List of input prompts
            max_length: Maximum length of generated text
            temperature: Sampling temperature
            **kwargs: Additional generation parameters
            
        Returns:
            List of generated texts
        """
        print(f"Processing batch of {len(prompts)} prompts...")
        
        results = []
        for idx, prompt in enumerate(prompts):
            result = self.generate(
                prompt,
                max_length=max_length,
                temperature=temperature,
                **kwargs
            )
            results.append(result)
            
            if (idx + 1) % 10 == 0:
                print(f"  Processed {idx + 1}/{len(prompts)} prompts")
        
        print("Batch processing complete!")
        return results
    
    def generate_with_alternatives(
        self,
        prompt: str,
        num_alternatives: int = 3,
        **kwargs
    ) -> List[str]:
        """
        Generate multiple alternative responses.
        
        Args:
            prompt: Input prompt text
            num_alternatives: Number of alternatives to generate
            **kwargs: Additional generation parameters
            
        Returns:
            List of alternative generated texts
        """
        alternatives = []
        
        for i in range(num_alternatives):
            # Vary temperature for diversity
            temp = self.config.temperature + (i * 0.1)
            result = self.generate(
                prompt,
                temperature=temp,
                use_cache=False,
                **kwargs
            )
            alternatives.append(result)
        
        return alternatives
    
    def interactive_generate(
        self,
        initial_prompt: str,
        num_turns: int = 5,
        **kwargs
    ) -> List[Dict[str, str]]:
        """
        Generate interactive conversation turns.
        
        Args:
            initial_prompt: Initial conversation prompt
            num_turns: Number of conversation turns
            **kwargs: Additional generation parameters
            
        Returns:
            List of conversation turns
        """
        conversation = []
        current_context = initial_prompt
        
        for turn in range(num_turns):
            response = self.generate(current_context, **kwargs)
            
            conversation.append({
                "turn": turn + 1,
                "prompt": current_context,
                "response": response,
                "timestamp": datetime.now().isoformat(),
            })
            
            # Update context for next turn
            current_context = f"{current_context} {response}"
        
        return conversation
    
    def _update_stats(self, generated_text: str, latency: float) -> None:
        """Update inference statistics."""
        self.inference_stats["total_requests"] += 1
        self.inference_stats["total_tokens_generated"] += len(generated_text.split())
        
        # Update running average latency
        n = self.inference_stats["total_requests"]
        old_avg = self.inference_stats["average_latency"]
        self.inference_stats["average_latency"] = (old_avg * (n - 1) + latency) / n
    
    def get_statistics(self) -> Dict[str, Any]:
        """
        Get inference statistics.
        
        Returns:
            Dictionary with statistics
        """
        stats = self.inference_stats.copy()
        stats["cache_size"] = len(self._response_cache)
        stats["tokens_per_request"] = (
            stats["total_tokens_generated"] / stats["total_requests"]
            if stats["total_requests"] > 0 else 0
        )
        return stats
    
    def clear_cache(self) -> None:
        """Clear the response cache."""
        cache_size = len(self._response_cache)
        self._response_cache.clear()
        print(f"Cache cleared ({cache_size} entries removed)")
    
    def reset_statistics(self) -> None:
        """Reset inference statistics."""
        self.inference_stats = {
            "total_requests": 0,
            "total_tokens_generated": 0,
            "average_latency": 0.0,
        }
        print("Statistics reset")
    
    def __repr__(self) -> str:
        return f"InferenceEngine(requests={self.inference_stats['total_requests']}, cached={len(self._response_cache)})"
