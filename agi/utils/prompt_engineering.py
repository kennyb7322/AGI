"""
AGI Framework - Prompt Engineering
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Tools and utilities for prompt engineering and optimization
"""

from typing import Dict, List, Optional, Any
import re


class PromptTemplate:
    """Template for structured prompts."""
    
    def __init__(self, template: str, variables: Optional[List[str]] = None):
        """
        Initialize prompt template.
        
        Args:
            template: Template string with placeholders (e.g., "Hello {name}")
            variables: List of variable names in the template
        """
        self.template = template
        self.variables = variables or self._extract_variables()
    
    def _extract_variables(self) -> List[str]:
        """Extract variable names from template."""
        return re.findall(r'\{(\w+)\}', self.template)
    
    def format(self, **kwargs) -> str:
        """
        Format template with provided variables.
        
        Args:
            **kwargs: Variable values
            
        Returns:
            Formatted prompt string
        """
        return self.template.format(**kwargs)
    
    def __repr__(self) -> str:
        return f"PromptTemplate(variables={self.variables})"


class PromptEngineer:
    """
    Prompt engineering toolkit for optimizing AI interactions.
    
    Provides utilities for:
    - Creating effective prompts
    - Prompt templates
    - Few-shot learning examples
    - Chain-of-thought prompting
    - Instruction tuning
    """
    
    def __init__(self):
        """Initialize prompt engineer."""
        self.templates = {}
        self.few_shot_examples = {}
        
    def create_template(self, name: str, template: str) -> PromptTemplate:
        """
        Create and register a prompt template.
        
        Args:
            name: Template name
            template: Template string
            
        Returns:
            PromptTemplate instance
        """
        prompt_template = PromptTemplate(template)
        self.templates[name] = prompt_template
        return prompt_template
    
    def get_template(self, name: str) -> Optional[PromptTemplate]:
        """
        Get a registered template by name.
        
        Args:
            name: Template name
            
        Returns:
            PromptTemplate or None
        """
        return self.templates.get(name)
    
    def create_few_shot_prompt(
        self,
        task_description: str,
        examples: List[Dict[str, str]],
        query: str
    ) -> str:
        """
        Create a few-shot learning prompt.
        
        Args:
            task_description: Description of the task
            examples: List of example dictionaries with 'input' and 'output'
            query: The actual query to process
            
        Returns:
            Formatted few-shot prompt
        """
        prompt_parts = [task_description, ""]
        
        # Add examples
        for idx, example in enumerate(examples, 1):
            prompt_parts.append(f"Example {idx}:")
            prompt_parts.append(f"Input: {example['input']}")
            prompt_parts.append(f"Output: {example['output']}")
            prompt_parts.append("")
        
        # Add query
        prompt_parts.append("Now, process this:")
        prompt_parts.append(f"Input: {query}")
        prompt_parts.append("Output:")
        
        return "\n".join(prompt_parts)
    
    def create_chain_of_thought_prompt(
        self,
        problem: str,
        include_reasoning: bool = True
    ) -> str:
        """
        Create a chain-of-thought prompt for complex reasoning.
        
        Args:
            problem: The problem to solve
            include_reasoning: Whether to include reasoning instructions
            
        Returns:
            Chain-of-thought prompt
        """
        prompt_parts = [problem]
        
        if include_reasoning:
            prompt_parts.append("")
            prompt_parts.append("Let's think through this step by step:")
            prompt_parts.append("1. First, identify the key information")
            prompt_parts.append("2. Then, break down the problem")
            prompt_parts.append("3. Finally, arrive at the solution")
            prompt_parts.append("")
            prompt_parts.append("Step-by-step reasoning:")
        
        return "\n".join(prompt_parts)
    
    def create_instruction_prompt(
        self,
        instruction: str,
        context: Optional[str] = None,
        constraints: Optional[List[str]] = None
    ) -> str:
        """
        Create an instruction-following prompt.
        
        Args:
            instruction: The main instruction
            context: Optional context information
            constraints: Optional list of constraints
            
        Returns:
            Formatted instruction prompt
        """
        prompt_parts = ["### Instruction", instruction]
        
        if context:
            prompt_parts.extend(["", "### Context", context])
        
        if constraints:
            prompt_parts.extend(["", "### Constraints"])
            for constraint in constraints:
                prompt_parts.append(f"- {constraint}")
        
        prompt_parts.extend(["", "### Response"])
        
        return "\n".join(prompt_parts)
    
    def optimize_prompt(self, prompt: str, optimization_type: str = "clarity") -> str:
        """
        Optimize a prompt for better results.
        
        Args:
            prompt: Original prompt
            optimization_type: Type of optimization ('clarity', 'specificity', 'structure')
            
        Returns:
            Optimized prompt
        """
        if optimization_type == "clarity":
            # Add clarity improvements
            return f"Please provide a clear and concise response to: {prompt}"
        
        elif optimization_type == "specificity":
            # Add specificity
            return f"Specifically address the following: {prompt}\n\nProvide detailed and specific information."
        
        elif optimization_type == "structure":
            # Add structure
            return f"Question: {prompt}\n\nPlease structure your response with:\n1. Main points\n2. Supporting details\n3. Conclusion"
        
        return prompt
    
    def add_few_shot_examples(self, name: str, examples: List[Dict[str, str]]) -> None:
        """
        Store few-shot examples for reuse.
        
        Args:
            name: Name for this set of examples
            examples: List of example dictionaries
        """
        self.few_shot_examples[name] = examples
    
    def get_few_shot_examples(self, name: str) -> Optional[List[Dict[str, str]]]:
        """
        Retrieve stored few-shot examples.
        
        Args:
            name: Name of the example set
            
        Returns:
            List of examples or None
        """
        return self.few_shot_examples.get(name)
    
    def create_persona_prompt(
        self,
        persona: str,
        task: str,
        tone: str = "professional"
    ) -> str:
        """
        Create a prompt with a specific persona.
        
        Args:
            persona: Description of the persona (e.g., "expert teacher", "creative writer")
            task: The task to perform
            tone: Desired tone of response
            
        Returns:
            Persona-based prompt
        """
        return f"""You are a {persona}. Your communication style is {tone}.

Task: {task}

Please respond in character, maintaining the persona throughout your response."""
    
    def list_templates(self) -> List[str]:
        """List all registered template names."""
        return list(self.templates.keys())
    
    def list_few_shot_examples(self) -> List[str]:
        """List all stored few-shot example sets."""
        return list(self.few_shot_examples.keys())
    
    def __repr__(self) -> str:
        return f"PromptEngineer(templates={len(self.templates)}, examples={len(self.few_shot_examples)})"
