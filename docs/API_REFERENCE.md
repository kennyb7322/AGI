# AGI Framework - API Reference

Copyright © 2026 kennyb7322  
Licensed under the MIT License

## Core Components

### agi.AGIModel

Main model class for generative AI.

#### Constructor

```python
AGIModel(
    model_name: str = "AGI-Base",
    version: str = "1.0.0",
    config: Optional[Dict[str, Any]] = None
)
```

**Parameters:**
- `model_name` (str): Name identifier for the model
- `version` (str): Version identifier
- `config` (Dict, optional): Configuration dictionary

**Returns:** AGIModel instance

**Example:**
```python
model = AGIModel(
    model_name="MyModel",
    version="1.0.0",
    config={"temperature": 0.7, "max_length": 512}
)
```

#### Methods

##### `train(training_data, epochs=10, **kwargs)`

Train the model on provided data.

**Parameters:**
- `training_data` (List[Any]): List of training examples
- `epochs` (int): Number of training epochs
- `**kwargs`: Additional training parameters

**Returns:** Dict[str, Any] - Training metrics

**Example:**
```python
metrics = model.train(
    training_data=["example 1", "example 2"],
    epochs=5
)
```

##### `generate(prompt, max_length=None, temperature=None, **kwargs)`

Generate text based on input prompt.

**Parameters:**
- `prompt` (str): Input text prompt
- `max_length` (int, optional): Maximum length of generated text
- `temperature` (float, optional): Sampling temperature
- `**kwargs`: Additional generation parameters

**Returns:** str - Generated text

**Example:**
```python
text = model.generate(
    prompt="Once upon a time",
    temperature=0.8,
    max_length=200
)
```

##### `evaluate(test_data)`

Evaluate model performance on test data.

**Parameters:**
- `test_data` (List[Any]): List of test examples

**Returns:** Dict[str, float] - Evaluation metrics

**Raises:** ValueError if model is not trained

**Example:**
```python
metrics = model.evaluate(test_data)
print(f"Accuracy: {metrics['accuracy']}")
```

##### `save(filepath)`

Save model to file.

**Parameters:**
- `filepath` (str): Path where model should be saved

**Returns:** None

**Example:**
```python
model.save("my_model.json")
```

##### `load(filepath)`

Load model from file.

**Parameters:**
- `filepath` (str): Path to saved model file

**Returns:** None

**Example:**
```python
model.load("my_model.json")
```

##### `get_info()`

Get model information.

**Returns:** Dict[str, Any] - Model information dictionary

**Example:**
```python
info = model.get_info()
print(info['model_name'])
```

---

### agi.core.NeuralNetwork

Neural network architecture for generative models.

#### Constructor

```python
NeuralNetwork(
    input_size: int = 768,
    hidden_sizes: Optional[List[int]] = None,
    output_size: int = 768,
    num_attention_heads: int = 12,
    dropout_rate: float = 0.1
)
```

**Parameters:**
- `input_size` (int): Input dimension
- `hidden_sizes` (List[int], optional): List of hidden layer sizes
- `output_size` (int): Output dimension
- `num_attention_heads` (int): Number of attention heads
- `dropout_rate` (float): Dropout rate for regularization

#### Methods

##### `forward(x)`

Forward pass through the network.

**Parameters:**
- `x` (List[float]): Input vector

**Returns:** List[float] - Output vector

**Raises:** ValueError if input size mismatch

##### `get_architecture()`

Get network architecture information.

**Returns:** Dict[str, Any] - Architecture description

##### `summary()`

Generate a summary of the network architecture.

**Returns:** str - Network summary

---

### agi.core.ModelTrainer

Training utilities for AGI models.

#### Constructor

```python
ModelTrainer(
    model: Any,
    config: Optional[TrainingConfig] = None
)
```

**Parameters:**
- `model`: Model instance to train
- `config` (TrainingConfig, optional): Training configuration

#### Methods

##### `train(training_data, validation_data=None, callbacks=None)`

Train the model.

**Parameters:**
- `training_data` (List[Any]): List of training examples
- `validation_data` (List[Any], optional): Validation data
- `callbacks` (List[Callable], optional): Callback functions

**Returns:** Dict[str, Any] - Training history

**Example:**
```python
history = trainer.train(
    training_data=train_set,
    validation_data=val_set
)
```

##### `get_training_summary()`

Get a summary of training progress.

**Returns:** str - Summary string

##### `plot_training_curves()`

Get training curves data for plotting.

**Returns:** Dict[str, List[float]] - Training metrics

---

### agi.core.TrainingConfig

Configuration for model training.

#### Constructor

```python
TrainingConfig(
    learning_rate: float = 0.001,
    batch_size: int = 32,
    epochs: int = 10,
    validation_split: float = 0.2,
    early_stopping_patience: int = 3,
    checkpoint_frequency: int = 1,
    log_frequency: int = 100
)
```

**Parameters:**
- `learning_rate` (float): Learning rate for optimization
- `batch_size` (int): Batch size for training
- `epochs` (int): Number of training epochs
- `validation_split` (float): Fraction of data for validation
- `early_stopping_patience` (int): Epochs to wait before early stopping
- `checkpoint_frequency` (int): Frequency of checkpoints (in epochs)
- `log_frequency` (int): Frequency of logging (in steps)

---

### agi.InferenceEngine

Inference engine for trained models.

#### Constructor

```python
InferenceEngine(
    model: Any,
    config: Optional[InferenceConfig] = None
)
```

**Parameters:**
- `model`: Trained model instance
- `config` (InferenceConfig, optional): Inference configuration

#### Methods

##### `generate(prompt, max_length=None, temperature=None, use_cache=True, **kwargs)`

Generate text from prompt.

**Parameters:**
- `prompt` (str): Input prompt text
- `max_length` (int, optional): Maximum length
- `temperature` (float, optional): Sampling temperature
- `use_cache` (bool): Whether to use response caching
- `**kwargs`: Additional parameters

**Returns:** str - Generated text

##### `batch_generate(prompts, max_length=None, temperature=None, **kwargs)`

Generate text for multiple prompts in batch.

**Parameters:**
- `prompts` (List[str]): List of input prompts
- `max_length` (int, optional): Maximum length
- `temperature` (float, optional): Sampling temperature
- `**kwargs`: Additional parameters

**Returns:** List[str] - List of generated texts

##### `generate_with_alternatives(prompt, num_alternatives=3, **kwargs)`

Generate multiple alternative responses.

**Parameters:**
- `prompt` (str): Input prompt text
- `num_alternatives` (int): Number of alternatives
- `**kwargs`: Additional parameters

**Returns:** List[str] - List of alternatives

##### `get_statistics()`

Get inference statistics.

**Returns:** Dict[str, Any] - Statistics dictionary

##### `clear_cache()`

Clear the response cache.

**Returns:** None

---

### agi.core.InferenceConfig

Configuration for model inference.

#### Constructor

```python
InferenceConfig(
    temperature: float = 0.7,
    top_p: float = 0.9,
    top_k: int = 50,
    max_length: int = 512,
    repetition_penalty: float = 1.0,
    num_return_sequences: int = 1,
    do_sample: bool = True
)
```

---

### agi.utils.PromptEngineer

Prompt engineering toolkit.

#### Constructor

```python
PromptEngineer()
```

#### Methods

##### `create_template(name, template)`

Create and register a prompt template.

**Parameters:**
- `name` (str): Template name
- `template` (str): Template string with {variable} placeholders

**Returns:** PromptTemplate instance

**Example:**
```python
engineer.create_template(
    "qa",
    "Question: {question}\nAnswer:"
)
```

##### `get_template(name)`

Get a registered template by name.

**Parameters:**
- `name` (str): Template name

**Returns:** PromptTemplate or None

##### `create_few_shot_prompt(task_description, examples, query)`

Create a few-shot learning prompt.

**Parameters:**
- `task_description` (str): Description of the task
- `examples` (List[Dict[str, str]]): List of example dictionaries
- `query` (str): The actual query to process

**Returns:** str - Formatted few-shot prompt

##### `create_chain_of_thought_prompt(problem, include_reasoning=True)`

Create a chain-of-thought prompt.

**Parameters:**
- `problem` (str): The problem to solve
- `include_reasoning` (bool): Whether to include reasoning instructions

**Returns:** str - Chain-of-thought prompt

##### `create_instruction_prompt(instruction, context=None, constraints=None)`

Create an instruction-following prompt.

**Parameters:**
- `instruction` (str): The main instruction
- `context` (str, optional): Context information
- `constraints` (List[str], optional): List of constraints

**Returns:** str - Formatted instruction prompt

##### `create_persona_prompt(persona, task, tone="professional")`

Create a prompt with a specific persona.

**Parameters:**
- `persona` (str): Description of the persona
- `task` (str): The task to perform
- `tone` (str): Desired tone of response

**Returns:** str - Persona-based prompt

---

### agi.utils.ContextManager

Context manager for conversation state.

#### Constructor

```python
ContextManager(
    max_context_length: int = 4096,
    max_turns: int = 50,
    summarization_threshold: int = 40
)
```

**Parameters:**
- `max_context_length` (int): Maximum context length in tokens
- `max_turns` (int): Maximum number of turns to keep
- `summarization_threshold` (int): Turns before summarization

#### Methods

##### `add_turn(role, content, metadata=None)`

Add a conversation turn.

**Parameters:**
- `role` (str): Speaker role (e.g., 'user', 'assistant')
- `content` (str): Message content
- `metadata` (Dict, optional): Optional metadata

**Returns:** None

##### `get_context(num_turns=None, include_summary=True)`

Get formatted context for model input.

**Parameters:**
- `num_turns` (int, optional): Number of recent turns to include
- `include_summary` (bool): Whether to include context summary

**Returns:** str - Formatted context string

##### `get_conversation_history()`

Get full conversation history.

**Returns:** List[Dict[str, Any]] - List of conversation turns

##### `clear_history()`

Clear conversation history.

**Returns:** None

##### `get_statistics()`

Get context statistics.

**Returns:** Dict[str, Any] - Statistics dictionary

##### `export_conversation(filepath)`

Export conversation to file.

**Parameters:**
- `filepath` (str): Path to export file

**Returns:** None

---

## Type Definitions

### Common Types

```python
# Configuration dictionary
Config = Dict[str, Any]

# Training data
TrainingData = List[Any]

# Metrics dictionary
Metrics = Dict[str, Union[float, int, List[float]]]

# Conversation turn
Turn = Dict[str, Any]  # {"role": str, "content": str, "timestamp": str}
```

---

## Error Handling

All methods include appropriate error handling:

- `ValueError`: Invalid input parameters
- `FileNotFoundError`: File operations on non-existent files
- `TypeError`: Type mismatches in parameters

Always wrap calls in try-except blocks for production use:

```python
try:
    result = model.generate(prompt)
except ValueError as e:
    print(f"Invalid input: {e}")
except Exception as e:
    print(f"Unexpected error: {e}")
```

---

For more examples, see the `examples/` and `use_cases/` directories.