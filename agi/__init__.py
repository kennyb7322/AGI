"""
AGI Framework - Artificial Generative Intelligence
Copyright (c) 2026 kennyb7322
Licensed under the MIT License (see LICENSE file)

Core AGI Framework Module
"""

__version__ = "1.0.0"
__author__ = "kennyb7322"
__license__ = "MIT"

from .core.model import AGIModel
from .core.neural_network import NeuralNetwork
from .core.trainer import ModelTrainer
from .core.inference import InferenceEngine
from .utils.prompt_engineering import PromptEngineer
from .utils.context_manager import ContextManager

__all__ = [
    'AGIModel',
    'NeuralNetwork',
    'ModelTrainer',
    'InferenceEngine',
    'PromptEngineer',
    'ContextManager',
]
