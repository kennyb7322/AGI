"""
AGI Framework - Code Generation Example
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Example demonstrating code generation capabilities
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from agi import AGIModel, InferenceEngine
from agi.utils import PromptEngineer


def main():
    """Main code generation example."""
    print("=" * 60)
    print("AGI Framework - Code Generation Example")
    print("Copyright (c) 2026 kennyb7322")
    print("=" * 60)
    print()
    
    # Initialize model
    print("1. Initializing Code Generation Model...")
    model = AGIModel(
        model_name="AGI-CodeGen",
        version="1.0.0",
        config={
            "max_length": 2048,
            "temperature": 0.3,  # Lower temperature for more deterministic code
            "top_p": 0.85,
        }
    )
    print(f"   {model}")
    print()
    
    # Train model
    print("2. Training on Code Examples...")
    code_training_data = [
        "def function_name():",
        "class ClassName:",
        "import module_name",
    ] * 20
    
    model.train(code_training_data, epochs=5)
    print()
    
    # Initialize components
    inference_engine = InferenceEngine(model)
    prompt_engineer = PromptEngineer()
    
    # Create code generation templates
    print("3. Setting up Code Generation Templates...")
    
    prompt_engineer.create_template(
        "function_gen",
        "Write a Python function named '{name}' that {description}. "
        "Include docstring and type hints."
    )
    
    prompt_engineer.create_template(
        "class_gen",
        "Create a Python class '{name}' that {description}. "
        "Include __init__ method and docstring."
    )
    
    prompt_engineer.create_template(
        "code_explain",
        "Explain the following code:\n\n{code}\n\n"
        "Provide a clear explanation of what it does."
    )
    
    # Add code examples
    code_examples = [
        {
            "input": "Write a function to calculate factorial",
            "output": "def factorial(n: int) -> int:\n    if n <= 1:\n        return 1\n    return n * factorial(n - 1)"
        },
        {
            "input": "Write a function to check if a number is prime",
            "output": "def is_prime(n: int) -> bool:\n    if n < 2:\n        return False\n    for i in range(2, int(n**0.5) + 1):\n        if n % i == 0:\n            return False\n    return True"
        }
    ]
    prompt_engineer.add_few_shot_examples("code_examples", code_examples)
    print("   Templates and examples configured")
    print()
    
    # Example 1: Function Generation
    print("4. Example 1: Function Generation")
    print("-" * 60)
    
    functions_to_generate = [
        {"name": "calculate_average", "description": "calculates the average of a list of numbers"},
        {"name": "find_max", "description": "finds the maximum value in a list"},
        {"name": "reverse_string", "description": "reverses a given string"},
    ]
    
    template = prompt_engineer.get_template("function_gen")
    
    for func_spec in functions_to_generate:
        prompt = template.format(**func_spec)
        code = inference_engine.generate(prompt, temperature=0.2)
        
        print(f"   Function: {func_spec['name']}")
        print(f"   Description: {func_spec['description']}")
        print(f"   Generated Code:\n   {code}")
        print()
    
    # Example 2: Class Generation
    print("5. Example 2: Class Generation")
    print("-" * 60)
    
    classes_to_generate = [
        {"name": "BankAccount", "description": "manages a bank account with deposits and withdrawals"},
        {"name": "ShoppingCart", "description": "manages items in a shopping cart"},
    ]
    
    template = prompt_engineer.get_template("class_gen")
    
    for class_spec in classes_to_generate:
        prompt = template.format(**class_spec)
        code = inference_engine.generate(prompt, temperature=0.25)
        
        print(f"   Class: {class_spec['name']}")
        print(f"   Description: {class_spec['description']}")
        print(f"   Generated Code:\n   {code}")
        print()
    
    # Example 3: Few-Shot Code Generation
    print("6. Example 3: Few-Shot Code Generation")
    print("-" * 60)
    
    task_description = "Generate Python code based on the description."
    examples = prompt_engineer.get_few_shot_examples("code_examples")
    query = "Write a function to find the nth Fibonacci number"
    
    few_shot_prompt = prompt_engineer.create_few_shot_prompt(
        task_description,
        examples,
        query
    )
    
    code = inference_engine.generate(few_shot_prompt, temperature=0.2)
    print(f"   Query: {query}")
    print(f"   Generated Code:\n   {code}")
    print()
    
    # Example 4: Code Explanation
    print("7. Example 4: Code Explanation")
    print("-" * 60)
    
    code_to_explain = """
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1
"""
    
    template = prompt_engineer.get_template("code_explain")
    prompt = template.format(code=code_to_explain)
    
    explanation = inference_engine.generate(prompt, temperature=0.3)
    print(f"   Code:\n{code_to_explain}")
    print(f"   Explanation:\n   {explanation}")
    print()
    
    # Example 5: Code Documentation Generation
    print("8. Example 5: Code Documentation Generation")
    print("-" * 60)
    
    instruction_prompt = prompt_engineer.create_instruction_prompt(
        instruction="Add comprehensive docstrings to the following Python code",
        context="""
def process_data(data, filter_func=None):
    if filter_func:
        data = [x for x in data if filter_func(x)]
    return sorted(data)
""",
        constraints=[
            "Use Google-style docstrings",
            "Include parameter types and return type",
            "Provide usage examples"
        ]
    )
    
    documented_code = inference_engine.generate(instruction_prompt, temperature=0.2)
    print(f"   Task: Add documentation to code")
    print(f"   Result:\n   {documented_code}")
    print()
    
    # Example 6: Algorithm Implementation
    print("9. Example 6: Algorithm Implementation with Chain-of-Thought")
    print("-" * 60)
    
    algorithm_problem = """
Implement a function to find the longest common subsequence (LCS) 
between two strings using dynamic programming.
"""
    
    cot_prompt = prompt_engineer.create_chain_of_thought_prompt(
        algorithm_problem,
        include_reasoning=True
    )
    
    implementation = inference_engine.generate(cot_prompt, temperature=0.25, max_length=500)
    print(f"   Problem: {algorithm_problem.strip()}")
    print(f"   Implementation with reasoning:\n   {implementation}")
    print()
    
    # Display statistics
    print("10. Code Generation Statistics")
    print("-" * 60)
    stats = inference_engine.get_statistics()
    print(f"   Total code generations: {stats['total_requests']}")
    print(f"   Total tokens generated: {stats['total_tokens_generated']}")
    print(f"   Average generation time: {stats['average_latency']:.4f}s")
    print()
    
    print("=" * 60)
    print("Code Generation Example Complete!")
    print("=" * 60)


if __name__ == "__main__":
    main()
