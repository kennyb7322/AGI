"""
AGI Framework - Core Module
Copyright (c) 2026 kennyb7322
Licensed under the MIT License

Core components for the AGI framework
"""

from .model import AGIModel
from .neural_network import NeuralNetwork
from .trainer import ModelTrainer
from .inference import InferenceEngine

__all__ = ['AGIModel', 'NeuralNetwork', 'ModelTrainer', 'InferenceEngine']
