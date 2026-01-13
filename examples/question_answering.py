"""
AGI Framework - Question Answering Example
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Example demonstrating question answering capabilities
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine
from agi.utils import PromptEngineer, ContextManager


def main():
    """Main question answering example."""
    print("=" * 60)
    print("AGI Framework - Question Answering Example")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize components
    print("1. Initializing Components...")
    model = AGIModel(model_name="AGI-QA", version="1.0.0")
    inference_engine = InferenceEngine(model)
    prompt_engineer = PromptEngineer()
    context_manager = ContextManager()
    print("   All components initialized")
    print()
    
    # Train the model
    print("2. Training the model...")
    qa_training_data = [
        {"question": "What is AI?", "answer": "Artificial Intelligence"},
        {"question": "What is ML?", "answer": "Machine Learning"},
    ] * 15
    
    model.train(qa_training_data, epochs=5)
    print()
    
    # Create QA prompt templates
    print("3. Setting up QA Prompt Templates...")
    prompt_engineer.create_template(
        "factual_qa",
        "Question: {question}\nProvide a factual and accurate answer:\nAnswer:"
    )
    
    prompt_engineer.create_template(
        "contextual_qa",
        "Context: {context}\n\nQuestion: {question}\nAnswer based on the context:\nAnswer:"
    )
    
    # Add few-shot examples
    few_shot_examples = [
        {
            "input": "What is the capital of France?",
            "output": "The capital of France is Paris."
        },
        {
            "input": "What is photosynthesis?",
            "output": "Photosynthesis is the process by which plants convert sunlight into energy."
        }
    ]
    prompt_engineer.add_few_shot_examples("qa_examples", few_shot_examples)
    print("   Templates and examples configured")
    print()
    
    # Example 1: Basic Question Answering
    print("4. Example 1: Basic Question Answering")
    print("-" * 60)
    questions = [
        "What is artificial intelligence?",
        "How does machine learning work?",
        "What are neural networks?"
    ]
    
    for question in questions:
        template = prompt_engineer.get_template("factual_qa")
        prompt = template.format(question=question)
        
        answer = inference_engine.generate(prompt, max_length=200)
        
        # Add to context
        context_manager.add_turn("user", question)
        context_manager.add_turn("assistant", answer)
        
        print(f"   Q: {question}")
        print(f"   A: {answer}")
        print()
    
    # Example 2: Contextual Question Answering
    print("5. Example 2: Contextual Question Answering")
    print("-" * 60)
    
    context = """
    The AGI Framework is a comprehensive toolkit for building artificial 
    generative intelligence systems. It provides core components including 
    models, neural networks, training utilities, and inference engines.
    """
    
    contextual_questions = [
        "What is the AGI Framework?",
        "What components does it provide?"
    ]
    
    template = prompt_engineer.get_template("contextual_qa")
    
    for question in contextual_questions:
        prompt = template.format(context=context, question=question)
        answer = inference_engine.generate(prompt)
        
        print(f"   Q: {question}")
        print(f"   A: {answer}")
        print()
    
    # Example 3: Few-Shot Question Answering
    print("6. Example 3: Few-Shot Question Answering")
    print("-" * 60)
    
    task_description = "Answer the following questions accurately and concisely."
    examples = prompt_engineer.get_few_shot_examples("qa_examples")
    query = "What is deep learning?"
    
    few_shot_prompt = prompt_engineer.create_few_shot_prompt(
        task_description,
        examples,
        query
    )
    
    print("   Using few-shot prompt...")
    answer = inference_engine.generate(few_shot_prompt)
    print(f"   Q: {query}")
    print(f"   A: {answer}")
    print()
    
    # Example 4: Chain-of-Thought Reasoning
    print("7. Example 4: Chain-of-Thought Reasoning")
    print("-" * 60)
    
    complex_question = """
    If a model has 12 layers and each layer has 768 hidden units, 
    and each unit connects to all units in the next layer, 
    roughly how many parameters does it have?
    """
    
    cot_prompt = prompt_engineer.create_chain_of_thought_prompt(
        complex_question,
        include_reasoning=True
    )
    
    answer = inference_engine.generate(cot_prompt, max_length=300)
    print(f"   Complex Question:\n   {complex_question}")
    print(f"   Answer with Reasoning:\n   {answer}")
    print()
    
    # Display conversation history
    print("8. Conversation History")
    print("-" * 60)
    stats = context_manager.get_statistics()
    print(f"   Total turns: {stats['total_turns']}")
    print(f"   Current context length: {stats['context_length_tokens']} tokens")
    print(f"   Context usage: {stats['context_length_percentage']:.1f}%")
    print()
    
    # Export conversation
    print("9. Exporting conversation...")
    context_manager.export_conversation("qa_conversation.json")
    print()
    
    print("=" * 60)
    print("Question Answering Example Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
