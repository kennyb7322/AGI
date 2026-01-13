"""
AGI Framework - Text Generation Example
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Example demonstrating text generation capabilities
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine
from agi.utils import PromptEngineer


def main():
    """Main text generation example."""
    print("=" * 60)
    print("AGI Framework - Text Generation Example")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize the model
    print("1. Initializing AGI Model...")
    model = AGIModel(
        model_name="AGI-TextGen",
        version="1.0.0"
    )
    
    # Display model info
    info = model.get_info()
    print(f"   Model: {info['model_name']}")
    print(f"   Version: {info['version']}")
    print(f"   Framework: {info['metadata']['framework']}")
    print()
    
    # Train the model (simulated)
    print("2. Training the model...")
    training_data = [
        "Example training text 1",
        "Example training text 2",
        "Example training text 3",
    ] * 10  # 30 training examples
    
    metrics = model.train(training_data, epochs=5)
    print(f"   Training complete!")
    print(f"   Final Loss: {metrics['loss'][-1]:.4f}")
    print(f"   Final Accuracy: {metrics['accuracy'][-1]:.4f}")
    print()
    
    # Initialize inference engine
    print("3. Setting up Inference Engine...")
    inference_engine = InferenceEngine(model)
    print(f"   {inference_engine}")
    print()
    
    # Initialize prompt engineer
    print("4. Setting up Prompt Engineer...")
    prompt_engineer = PromptEngineer()
    
    # Create some prompt templates
    prompt_engineer.create_template(
        "story_start",
        "Write a {genre} story that begins with: {opening}"
    )
    
    prompt_engineer.create_template(
        "explain",
        "Explain {topic} in simple terms for a {audience}"
    )
    print("   Prompt templates created")
    print()
    
    # Example 1: Basic text generation
    print("5. Example 1: Basic Text Generation")
    print("-" * 60)
    prompt1 = "Once upon a time in a distant galaxy"
    print(f"   Prompt: {prompt1}")
    result1 = inference_engine.generate(prompt1, temperature=0.7)
    print(f"   Generated: {result1}")
    print()
    
    # Example 2: Using prompt templates
    print("6. Example 2: Using Prompt Templates")
    print("-" * 60)
    template = prompt_engineer.get_template("story_start")
    prompt2 = template.format(genre="science fiction", opening="The stars aligned")
    print(f"   Prompt: {prompt2}")
    result2 = inference_engine.generate(prompt2, temperature=0.8)
    print(f"   Generated: {result2}")
    print()
    
    # Example 3: Multiple alternatives
    print("7. Example 3: Generating Multiple Alternatives")
    print("-" * 60)
    prompt3 = "The future of artificial intelligence is"
    print(f"   Prompt: {prompt3}")
    alternatives = inference_engine.generate_with_alternatives(prompt3, num_alternatives=3)
    for idx, alt in enumerate(alternatives, 1):
        print(f"   Alternative {idx}: {alt}")
    print()
    
    # Example 4: Batch generation
    print("8. Example 4: Batch Text Generation")
    print("-" * 60)
    prompts = [
        "Technology will",
        "In the year 2050",
        "The most important discovery"
    ]
    print(f"   Processing {len(prompts)} prompts...")
    batch_results = inference_engine.batch_generate(prompts)
    for prompt, result in zip(prompts, batch_results):
        print(f"   Prompt: {prompt}")
        print(f"   Result: {result}")
        print()
    
    # Display statistics
    print("9. Inference Statistics")
    print("-" * 60)
    stats = inference_engine.get_statistics()
    print(f"   Total requests: {stats['total_requests']}")
    print(f"   Total tokens generated: {stats['total_tokens_generated']}")
    print(f"   Average latency: {stats['average_latency']:.4f}s")
    print(f"   Cache size: {stats['cache_size']}")
    print()
    
    # Save the model
    print("10. Saving the model...")
    model.save("text_generation_model.json")
    print()
    
    print("=" * 60)
    print("Text Generation Example Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
