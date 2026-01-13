# AGI Framework Examples

This directory contains comprehensive examples demonstrating the capabilities of the AGI Framework.

## Examples Overview

### 1. Text Generation (`text_generation.py`)

Demonstrates core text generation capabilities:
- Basic text generation
- Using prompt templates
- Generating multiple alternatives
- Batch text generation
- Inference statistics

**Run:**
```bash
python examples/text_generation.py
```

### 2. Question Answering (`question_answering.py`)

Shows how to build Q&A systems:
- Factual question answering
- Contextual Q&A with document context
- Few-shot learning examples
- Chain-of-thought reasoning for complex questions
- Conversation history management

**Run:**
```bash
python examples/question_answering.py
```

### 3. Creative Writing (`creative_writing.py`)

Explores creative applications:
- Story opening generation
- Character descriptions
- Scene descriptions with sensory details
- Persona-based writing (poet, detective, scientist)
- Multiple creative alternatives

**Run:**
```bash
python examples/creative_writing.py
```

### 4. Code Generation (`code_generation.py`)

Demonstrates programming assistance:
- Python function generation
- Class generation with methods
- Code explanation
- Documentation generation
- Algorithm implementation with reasoning

**Run:**
```bash
python examples/code_generation.py
```

## Learning Path

We recommend exploring the examples in this order:

1. **Start with Text Generation** - Learn the basics of model initialization, training, and generation
2. **Move to Question Answering** - Understand context management and prompt engineering
3. **Explore Creative Writing** - See advanced prompt techniques and persona usage
4. **Try Code Generation** - Apply the framework to technical tasks

## Common Patterns

All examples follow similar patterns:

```python
# 1. Import components
from agi import AGIModel, InferenceEngine
from agi.utils import PromptEngineer

# 2. Initialize model
model = AGIModel(model_name="MyModel")

# 3. Train (if needed)
model.train(training_data, epochs=5)

# 4. Create inference engine
engine = InferenceEngine(model)

# 5. Generate output
result = engine.generate(prompt)
```

## Customization

Each example can be customized by:
- Adjusting model configuration parameters
- Modifying training data and epochs
- Changing inference parameters (temperature, max_length)
- Creating custom prompt templates
- Experimenting with different prompting strategies

## Output

Examples generate:
- Console output showing progress and results
- Optional saved models (`.json` files)
- Optional exported conversations

## Next Steps

After running the examples:
1. Review the source code to understand implementation
2. Modify examples to experiment with different parameters
3. Explore the use cases in `../use_cases/` for complete applications
4. Read the API reference in `../docs/API_REFERENCE.md`

## Support

For questions or issues:
- Check the main README.md
- Review API_REFERENCE.md
- Open an issue on GitHub
