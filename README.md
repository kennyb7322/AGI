# AGI Framework - Artificial Generative Intelligence

**Copyright © 2026 kennyb7322**  
**Licensed under the MIT License**

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)

A comprehensive, production-ready framework for building Artificial Generative Intelligence systems. The AGI Framework provides a complete toolkit with models, neural networks, training utilities, inference engines, and advanced prompt engineering capabilities.

## 🌟 Features

- **Complete Model Architecture**: Full-featured base models with training, inference, and evaluation
- **Neural Network Components**: Flexible neural network architecture with attention mechanisms
- **Advanced Training**: Comprehensive training utilities with validation, early stopping, and checkpointing
- **Optimized Inference**: High-performance inference engine with caching and batch processing
- **Prompt Engineering**: Sophisticated prompt engineering toolkit for optimal AI interactions
- **Context Management**: Intelligent conversation context and memory management
- **Production Ready**: Enterprise-grade code with comprehensive error handling and logging
- **Extensive Examples**: Complete examples for text generation, Q&A, creative writing, and code generation
- **Real-World Use Cases**: Full implementations of chatbots, content generation, and data analysis systems

## 📋 Table of Contents

- [Installation](#installation)
- [Quick Start](#quick-start)
- [Architecture](#architecture)
- [Core Components](#core-components)
- [Usage Guide](#usage-guide)
- [Examples](#examples)
- [Use Cases](#use-cases)
- [API Reference](#api-reference)
- [Contributing](#contributing)
- [License](#license)

## 🚀 Installation

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Basic Installation

```bash
# Clone the repository
git clone https://github.com/kennyb7322/AGI.git
cd AGI

# No additional dependencies required - pure Python implementation!
```

### For Development

```bash
# Install in development mode
pip install -e .
```

## ⚡ Quick Start

```python
from agi import AGIModel, InferenceEngine

# Initialize a model
model = AGIModel(model_name="MyAGI", version="1.0.0")

# Train the model
training_data = ["Example 1", "Example 2", "Example 3"]
model.train(training_data, epochs=5)

# Create inference engine
inference = InferenceEngine(model)

# Generate text
result = inference.generate("Your prompt here", temperature=0.7)
print(result)
```

## 🏗️ Architecture

The AGI Framework follows a modular, layered architecture:

```
┌─────────────────────────────────────────────────────────┐
│                   Application Layer                      │
│  (Examples, Use Cases, Custom Applications)             │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                   Utilities Layer                        │
│  • PromptEngineer  • ContextManager                     │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                   Core Framework Layer                   │
│  • AGIModel  • InferenceEngine  • ModelTrainer          │
└─────────────────────────────────────────────────────────┘
                          ↓
┌─────────────────────────────────────────────────────────┐
│                   Neural Network Layer                   │
│  • NeuralNetwork  • Layers  • Attention                 │
└─────────────────────────────────────────────────────────┘
```

### Design Principles

1. **Modularity**: Each component is independent and reusable
2. **Extensibility**: Easy to extend and customize for specific needs
3. **Simplicity**: Clean, intuitive API with sensible defaults
4. **Production-Ready**: Enterprise-grade code quality and error handling
5. **Documentation**: Comprehensive documentation and examples

## 🔧 Core Components

### 1. AGIModel

The base model class providing the foundation for all generative AI models.

**Key Features:**
- Standardized training interface
- Built-in text generation
- Model persistence (save/load)
- Comprehensive metadata tracking
- Evaluation metrics

**Example:**
```python
from agi import AGIModel

model = AGIModel(
    model_name="MyModel",
    version="1.0.0",
    config={
        "max_length": 512,
        "temperature": 0.7,
        "num_layers": 12,
        "hidden_size": 768
    }
)
```

### 2. NeuralNetwork

Flexible neural network architecture with support for various layer types.

**Key Features:**
- Dense layers with customizable dimensions
- Multi-head attention mechanisms
- Automatic weight initialization
- Layer-by-layer forward propagation
- Architecture summary and parameter counting

**Example:**
```python
from agi.core import NeuralNetwork

network = NeuralNetwork(
    input_size=768,
    hidden_sizes=[768, 768, 768],
    output_size=768,
    num_attention_heads=12
)

print(network.summary())
```

### 3. ModelTrainer

Comprehensive training utilities for model optimization.

**Key Features:**
- Configurable training parameters
- Validation and early stopping
- Checkpoint saving
- Training metrics tracking
- Progress monitoring

**Example:**
```python
from agi import ModelTrainer
from agi.core import TrainingConfig

config = TrainingConfig(
    learning_rate=0.001,
    batch_size=32,
    epochs=10,
    early_stopping_patience=3
)

trainer = ModelTrainer(model, config)
history = trainer.train(training_data, validation_data)
```

### 4. InferenceEngine

Optimized inference engine for text generation.

**Key Features:**
- Single and batch generation
- Response caching for efficiency
- Multiple sampling strategies
- Interactive conversation support
- Performance monitoring

**Example:**
```python
from agi import InferenceEngine

engine = InferenceEngine(model)

# Single generation
text = engine.generate("Your prompt", temperature=0.7)

# Batch generation
results = engine.batch_generate(["Prompt 1", "Prompt 2"])

# With alternatives
alternatives = engine.generate_with_alternatives("Prompt", num_alternatives=3)
```

### 5. PromptEngineer

Advanced prompt engineering toolkit.

**Key Features:**
- Reusable prompt templates
- Few-shot learning examples
- Chain-of-thought prompting
- Instruction-following prompts
- Persona-based prompts

**Example:**
```python
from agi.utils import PromptEngineer

engineer = PromptEngineer()

# Create template
engineer.create_template(
    "qa_template",
    "Question: {question}\nAnswer:"
)

# Use template
template = engineer.get_template("qa_template")
prompt = template.format(question="What is AI?")
```

### 6. ContextManager

Intelligent conversation context and memory management.

**Key Features:**
- Multi-turn conversation tracking
- Automatic context summarization
- Context window management
- Conversation export/import
- Statistics and monitoring

**Example:**
```python
from agi.utils import ContextManager

context = ContextManager(max_context_length=2048)

# Add conversation turns
context.add_turn("user", "Hello!")
context.add_turn("assistant", "Hi! How can I help?")

# Get formatted context
formatted = context.get_context(num_turns=10)
```

## 📖 Usage Guide

### Training a Model

```python
from agi import AGIModel

# Initialize model
model = AGIModel(model_name="CustomModel")

# Prepare training data
training_data = [
    "Training example 1",
    "Training example 2",
    # ... more examples
]

# Train
metrics = model.train(training_data, epochs=10)

# Save trained model
model.save("my_model.json")
```

### Generating Text

```python
from agi import AGIModel, InferenceEngine

# Load or create model
model = AGIModel.load("my_model.json")  # or create new

# Create inference engine
engine = InferenceEngine(model)

# Generate text
result = engine.generate(
    prompt="Once upon a time",
    temperature=0.8,
    max_length=200
)

print(result)
```

### Using Prompt Templates

```python
from agi.utils import PromptEngineer

engineer = PromptEngineer()

# Create template
engineer.create_template(
    "story",
    "Write a {genre} story about {topic}"
)

# Use template
template = engineer.get_template("story")
prompt = template.format(genre="sci-fi", topic="space exploration")
```

### Managing Conversation Context

```python
from agi.utils import ContextManager

context = ContextManager()

# Simulate conversation
context.add_turn("user", "What is machine learning?")
context.add_turn("assistant", "Machine learning is...")
context.add_turn("user", "Can you give an example?")

# Get context for next generation
conversation_context = context.get_context()

# Export conversation
context.export_conversation("conversation.json")
```

## 💡 Examples

The framework includes comprehensive examples:

### 1. Text Generation (`examples/text_generation.py`)

Demonstrates basic and advanced text generation capabilities including:
- Model initialization and training
- Template-based generation
- Multiple alternatives generation
- Batch processing

Run: `python examples/text_generation.py`

### 2. Question Answering (`examples/question_answering.py`)

Shows how to build Q&A systems with:
- Factual question answering
- Contextual Q&A
- Few-shot learning
- Chain-of-thought reasoning

Run: `python examples/question_answering.py`

### 3. Creative Writing (`examples/creative_writing.py`)

Explores creative applications including:
- Story opening generation
- Character descriptions
- Scene descriptions
- Persona-based writing

Run: `python examples/creative_writing.py`

### 4. Code Generation (`examples/code_generation.py`)

Demonstrates code generation features:
- Function generation
- Class generation
- Code explanation
- Documentation generation

Run: `python examples/code_generation.py`

## 🎯 Use Cases

### 1. Chatbot (`use_cases/chatbot.py`)

Complete chatbot implementation featuring:
- Context-aware conversations
- System prompt configuration
- Conversation history management
- Statistics tracking

Run: `python use_cases/chatbot.py`

### 2. Content Generation (`use_cases/content_generation.py`)

Automated content generation system for:
- Blog posts
- Social media content
- Product descriptions
- Email templates

Run: `python use_cases/content_generation.py`

### 3. Data Analysis (`use_cases/data_analysis.py`)

AI-powered data analysis system with:
- Dataset summarization
- Trend analysis
- Comparative analysis
- Insight generation

Run: `python use_cases/data_analysis.py`

## 📚 API Reference

### AGIModel

```python
AGIModel(model_name: str, version: str, config: Optional[Dict] = None)
```

**Methods:**
- `train(training_data, epochs, **kwargs)` - Train the model
- `generate(prompt, max_length, temperature, **kwargs)` - Generate text
- `evaluate(test_data)` - Evaluate model performance
- `save(filepath)` - Save model to file
- `load(filepath)` - Load model from file
- `get_info()` - Get model information

### InferenceEngine

```python
InferenceEngine(model, config: Optional[InferenceConfig] = None)
```

**Methods:**
- `generate(prompt, **kwargs)` - Generate single response
- `batch_generate(prompts, **kwargs)` - Generate multiple responses
- `generate_with_alternatives(prompt, num_alternatives)` - Generate alternatives
- `interactive_generate(prompt, num_turns)` - Interactive generation
- `get_statistics()` - Get inference statistics

### PromptEngineer

```python
PromptEngineer()
```

**Methods:**
- `create_template(name, template)` - Create prompt template
- `get_template(name)` - Retrieve template
- `create_few_shot_prompt(description, examples, query)` - Few-shot prompt
- `create_chain_of_thought_prompt(problem)` - CoT prompt
- `create_instruction_prompt(instruction, context, constraints)` - Instruction prompt
- `create_persona_prompt(persona, task, tone)` - Persona-based prompt

### ContextManager

```python
ContextManager(max_context_length: int, max_turns: int)
```

**Methods:**
- `add_turn(role, content, metadata)` - Add conversation turn
- `get_context(num_turns, include_summary)` - Get formatted context
- `get_conversation_history()` - Get full history
- `clear_history()` - Clear conversation
- `export_conversation(filepath)` - Export to file

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.

### Development Setup

```bash
git clone https://github.com/kennyb7322/AGI.git
cd AGI
```

### Guidelines

1. Follow PEP 8 style guidelines
2. Add tests for new features
3. Update documentation as needed
4. Ensure all tests pass before submitting PR

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

```
MIT License

Copyright (c) 2026 kennyb7322

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

## 📞 Contact

- **Author**: kennyb7322
- **Repository**: [https://github.com/kennyb7322/AGI](https://github.com/kennyb7322/AGI)
- **Issues**: [https://github.com/kennyb7322/AGI/issues](https://github.com/kennyb7322/AGI/issues)

## 🙏 Acknowledgments

This framework represents a comprehensive approach to building generative AI systems with a focus on:
- **Usability**: Easy to learn and use
- **Flexibility**: Adaptable to various use cases
- **Quality**: Production-ready code
- **Documentation**: Extensive guides and examples

---

**Built with ❤️ for the AI community**
