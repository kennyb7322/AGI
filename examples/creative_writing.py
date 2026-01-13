"""
AGI Framework - Creative Writing Example
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Example demonstrating creative writing capabilities
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine, ModelTrainer
from agi.core import TrainingConfig
from agi.utils import PromptEngineer


def main():
    """Main creative writing example."""
    print("=" * 60)
    print("AGI Framework - Creative Writing Example")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize model
    print("1. Initializing Creative Writing Model...")
    model = AGIModel(
        model_name="AGI-CreativeWriter",
        version="1.0.0",
        config={
            "max_length": 1024,
            "temperature": 0.9,  # Higher temperature for creativity
            "top_p": 0.95,
            "num_layers": 12,
            "hidden_size": 768,
        }
    )
    print(f"   {model}")
    print()
    
    # Train with creative writing data
    print("2. Training on Creative Writing Data...")
    training_config = TrainingConfig(
        learning_rate=0.0001,
        batch_size=16,
        epochs=8,
        validation_split=0.15
    )
    
    creative_training_data = [
        "Once upon a time in a magical kingdom...",
        "The stars whispered secrets to those who would listen...",
        "In the depths of the ocean, mysteries await...",
    ] * 20
    
    trainer = ModelTrainer(model, training_config)
    history = trainer.train(creative_training_data)
    print()
    print(trainer.get_training_summary())
    print()
    
    # Initialize components
    inference_engine = InferenceEngine(model)
    prompt_engineer = PromptEngineer()
    
    # Create writing prompts
    print("3. Setting up Creative Writing Prompts...")
    
    prompt_engineer.create_template(
        "story_opening",
        "Write an engaging opening for a {genre} story about {topic}. "
        "The tone should be {tone}."
    )
    
    prompt_engineer.create_template(
        "character_description",
        "Describe a {adjective} character who is a {profession}. "
        "Include their appearance, personality, and a unique quirk."
    )
    
    prompt_engineer.create_template(
        "scene_description",
        "Describe a {time_of_day} scene in {location}. "
        "Use vivid sensory details to bring the scene to life."
    )
    print("   Templates created")
    print()
    
    # Example 1: Story Opening
    print("4. Example 1: Story Opening Generation")
    print("-" * 60)
    
    template = prompt_engineer.get_template("story_opening")
    prompt = template.format(
        genre="science fiction",
        topic="first contact with aliens",
        tone="mysterious and awe-inspiring"
    )
    
    print(f"   Prompt: {prompt}")
    story_opening = inference_engine.generate(prompt, temperature=0.9, max_length=300)
    print(f"   Generated Opening:\n   {story_opening}")
    print()
    
    # Example 2: Character Description
    print("5. Example 2: Character Description")
    print("-" * 60)
    
    characters = [
        {"adjective": "mysterious", "profession": "detective"},
        {"adjective": "cheerful", "profession": "baker"},
        {"adjective": "cunning", "profession": "merchant"}
    ]
    
    template = prompt_engineer.get_template("character_description")
    
    for char_params in characters:
        prompt = template.format(**char_params)
        description = inference_engine.generate(prompt, temperature=0.85)
        print(f"   Character: {char_params['adjective']} {char_params['profession']}")
        print(f"   Description: {description}")
        print()
    
    # Example 3: Scene Description
    print("6. Example 3: Scene Description")
    print("-" * 60)
    
    scenes = [
        {"time_of_day": "dawn", "location": "a misty forest"},
        {"time_of_day": "midnight", "location": "an abandoned space station"},
        {"time_of_day": "sunset", "location": "a bustling marketplace"}
    ]
    
    template = prompt_engineer.get_template("scene_description")
    
    for scene_params in scenes:
        prompt = template.format(**scene_params)
        description = inference_engine.generate(prompt, temperature=0.9)
        print(f"   Scene: {scene_params['time_of_day']} at {scene_params['location']}")
        print(f"   Description: {description}")
        print()
    
    # Example 4: Persona-based Writing
    print("7. Example 4: Persona-based Creative Writing")
    print("-" * 60)
    
    personas = [
        ("romantic poet", "write a love poem about the moon"),
        ("noir detective", "describe discovering a mysterious clue"),
        ("enthusiastic scientist", "explain a fascinating discovery")
    ]
    
    for persona, task in personas:
        prompt = prompt_engineer.create_persona_prompt(
            persona=persona,
            task=task,
            tone="authentic"
        )
        
        result = inference_engine.generate(prompt, temperature=0.95)
        print(f"   Persona: {persona}")
        print(f"   Task: {task}")
        print(f"   Output: {result}")
        print()
    
    # Example 5: Multiple Creative Alternatives
    print("8. Example 5: Multiple Creative Alternatives")
    print("-" * 60)
    
    creative_prompt = "The ancient door slowly opened, revealing"
    print(f"   Starting prompt: {creative_prompt}")
    print()
    
    alternatives = inference_engine.generate_with_alternatives(
        creative_prompt,
        num_alternatives=4
    )
    
    for idx, alternative in enumerate(alternatives, 1):
        print(f"   Alternative {idx}: {alternative}")
        print()
    
    # Display statistics
    print("9. Creative Writing Statistics")
    print("-" * 60)
    stats = inference_engine.get_statistics()
    print(f"   Total creative pieces generated: {stats['total_requests']}")
    print(f"   Total tokens generated: {stats['total_tokens_generated']}")
    print(f"   Average generation time: {stats['average_latency']:.4f}s")
    print()
    
    # Save model
    print("10. Saving Creative Writer Model...")
    model.save("creative_writer_model.json")
    print()
    
    print("=" * 60)
    print("Creative Writing Example Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
